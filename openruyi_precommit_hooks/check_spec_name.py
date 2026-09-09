from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_NAME = re.compile(r'^Name\s*:\s*(\S+)')
_RE_UPSTREAM_FIELD = re.compile(r'^(?:URL|VCS|Source\d*)\s*:\s*(\S+)')
_RE_LIB_ABI = re.compile(r'^lib[a-z]+[0-9]+$')


def _upstream_tokens(lines: list[str]) -> set[str]:
    """Collect identifier tokens from upstream metadata fields.

    ``URL``/``VCS``/``Source`` values usually point at the upstream
    project, so a ``lib<name><number>`` package whose name matches one
    of these identifiers is the actual upstream name (e.g. ``libxml2``,
    ``libssh2``) rather than an encoded ABI or major version.
    """
    tokens: set[str] = set()
    for line in lines:
        m = _RE_UPSTREAM_FIELD.match(line.strip())
        if not m:
            continue
        value = re.sub(r'%\{[^}]*\}', '', m.group(1))
        tokens.update(re.findall(r'[A-Za-z0-9]+', value.lower()))
    return tokens


def _check_spec_name(filename: str) -> list[str]:
    errors: list[str] = []
    try:
        with open(filename, encoding='utf-8') as f:
            lines = f.read().splitlines()
    except UnicodeDecodeError:
        return [f'{filename}: file is not valid UTF-8']
    except OSError as exc:
        return [f'{filename}: {exc}']

    if not lines:
        return [f'{filename}: file is empty']

    name = None
    for line in lines:
        m = _RE_NAME.match(line.strip())
        if m:
            name = m.group(1)
            break
    if name is None:
        return [f'{filename}: missing required field "Name"']

    if '%' in name:
        return errors

    if not name.islower() and not name.startswith('perl-'):
        errors.append(
            f'{filename}: package name should be lowercase '
            f'(found "{name}")',
        )
    if '_' in name:
        errors.append(
            f'{filename}: prefer "-" over "_" in package name '
            f'(found "{name}")',
        )
    if _RE_LIB_ABI.match(name):
        tokens = _upstream_tokens(lines)
        if name.lower() not in tokens:
            errors.append(
                f'{filename}: package name should not encode an ABI or '
                f'major version (found "{name}")',
            )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_name(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
