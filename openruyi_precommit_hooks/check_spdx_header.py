from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# Every spec file in the openRuyi distribution must start with an SPDX
# header block declaring copyright and license information, e.g.:
#
#     # SPDX-FileCopyrightText: (C) 2026 Institute of Software,
#     #                         Chinese Academy of Sciences (ISCAS)
#     # SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#     # SPDX-FileContributor: Your Name <your.email@example.com>
#     #
#     # SPDX-License-Identifier: MulanPSL-2.0
#
# The mandatory lines are the two `SPDX-FileCopyrightText` lines and the
# final `SPDX-License-Identifier: MulanPSL-2.0` line, and they must
# appear in this order at the *start* of the file (only leading blank
# lines may precede the block). `SPDX-FileContributor` lines are
# optional.

_RE_COPYRIGHT_ISCAS = re.compile(
    r'^#\s*SPDX-FileCopyrightText:\s*\(C\)\s*'
    r'\d{4}(?:\s*,\s*\d{4}|\s*-\s*\d{4})*\s+'
    r'Institute\s+of\s+Software,\s+Chinese\s+Academy\s+of\s+'
    r'Sciences\s+\(ISCAS\)\s*$',
)
_RE_COPYRIGHT_RUYI = re.compile(
    r'^#\s*SPDX-FileCopyrightText:\s*\(C\)\s*'
    r'\d{4}(?:\s*,\s*\d{4}|\s*-\s*\d{4})*\s+'
    r'openRuyi\s+Project\s+Contributors\s*$',
)
_RE_CONTRIBUTOR = re.compile(r'^#\s*SPDX-FileContributor:\s*.+\s*$')
_RE_BLANK_COMMENT = re.compile(r'^#\s*$')
_RE_LICENSE = re.compile(
    r'^#\s*SPDX-License-Identifier:\s*MulanPSL-2\.0\s*$',
)


def _header_block(lines: list[str]) -> list[str]:
    """Return the stripped consecutive comment lines at the top of the file."""
    i = 0
    # allow a few leading blank lines before the header
    while i < len(lines) and not lines[i].strip():
        i += 1
    block: list[str] = []
    while i < len(lines) and lines[i].lstrip().startswith('#'):
        block.append(lines[i].strip())
        i += 1
    return block


def _is_spdx_line(line: str) -> bool:
    return (
        line.startswith('# SPDX-FileCopyrightText:') or
        line.startswith('# SPDX-FileContributor:') or
        line.startswith('# SPDX-License-Identifier:')
    )


def _dedup(errors: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for err in errors:
        if err not in seen:
            seen.add(err)
            out.append(err)
    return out


def _check_spdx_header(filename: str) -> list[str]:
    """Validate the SPDX header of ``filename``.

    Returns a list of human readable error messages; empty on success.
    """
    errors: list[str] = []
    try:
        with open(filename, encoding='utf-8') as f:
            lines = f.read().splitlines()
    except UnicodeDecodeError:
        return [f'{filename}: file is not valid UTF-8']
    except OSError as exc:
        return [f'{filename}: {exc}']

    block = _header_block(lines)
    if not block:
        return [f'{filename}: file is empty or does not start with comments']

    has_iscas = any(_RE_COPYRIGHT_ISCAS.match(line) for line in block)
    has_ruyi = any(_RE_COPYRIGHT_RUYI.match(line) for line in block)
    has_license = any(_RE_LICENSE.match(line) for line in block)

    if not has_iscas:
        errors.append(
            f'{filename}: missing required header line '
            '"# SPDX-FileCopyrightText: (C) <year> '
            'Institute of Software, Chinese Academy of '
            'Sciences (ISCAS)"',
        )
    if not has_ruyi:
        errors.append(
            f'{filename}: missing required header line '
            '"# SPDX-FileCopyrightText: (C) <year> '
            'openRuyi Project Contributors"',
        )
    if not has_license:
        errors.append(
            f'{filename}: missing required header line '
            '"# SPDX-License-Identifier: MulanPSL-2.0"',
        )

    # order check: ISCAS -> ruyi -> (contributors) -> blank "#" -> license
    ordered = [line for line in block if _is_spdx_line(line)]
    required_seq = [
        _RE_COPYRIGHT_ISCAS,
        _RE_COPYRIGHT_RUYI,
        _RE_LICENSE,
    ]
    pos = 0
    for pat in required_seq:
        found = False
        while pos < len(ordered):
            if pat.match(ordered[pos]):
                found = True
                pos += 1
                break
            pos += 1
        if not found:
            break
    return _dedup(errors)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spdx_header(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
