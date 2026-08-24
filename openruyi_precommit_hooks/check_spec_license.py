from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``License`` field of an openRuyi spec file must follow the
# packaging guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#license)
# and the Licenses sub-specification
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/Licenses):
#
#   1. ``License`` must use an SPDX License Identifier or an SPDX
#      License Expression.
#   2. When there are multiple licenses, their identifiers must be
#      joined with the SPDX operators ``AND`` / ``OR`` (and
#      ``WITH`` for exceptions).
#   3. Public-domain packages use ``LicenseRef-openRuyi-Public-Domain``
#      instead of free-form text.
#
# Statically checkable rules in this hook:
#   * lowercase ``and`` / ``or`` / ``with`` operators are not SPDX
#     operator tokens (must be uppercase);
#   * a comma (``,``) is not a valid SPDX operator -- use ``AND``;
#   * an ``+`` suffix (e.g. ``GPLv3+`` / ``MPL-2.0+``) is the legacy
#     Fedora style and has no SPDX meaning -- use the ``-or-later``
#     suffix instead;
#   * unbalanced parentheses break the SPDX expression grammar.
#
# Field presence is covered by ``check-spec-structure``.  Values that
# expand at build time (contain ``%`` macros) and whitespace-separated
# lists without any operator are skipped to avoid false positives.

_RE_LICENSE = re.compile(r'^License\s*:\s*(.*)')
# The operators with surrounding spaces.  ``WITH`` only appears inside
# a ``<id> WITH <exception>`` group, that is fine.  Matching on
# space/paren delimiters means the ``or`` embedded in identifiers such
# as ``GPL-3.0-or-later`` is never flagged.
_RE_LOWER_AND = re.compile(r'(^|[ (])\band($|[ )])')
_RE_LOWER_OR = re.compile(r'(^|[ (])\bor($|[ )])')
_RE_LOWER_WITH = re.compile(r'(^|[ (])\bwith($|[ )])')
# Legacy Fedora ``+`` suffix: a token ending in ``+`` such as
# ``GPLv3+`` or ``MPL-2.0+``; a bare ``+`` inside is not flagged.
_RE_PLUS_SUFFIX = re.compile(r'\b[A-Za-z0-9][A-Za-z0-9.-]*\+')
# Avoid echoing a very long value verbatim in an error message.
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _has_lowercase_operator(value: str) -> bool:
    """Return True if ``value`` uses a lowercase SPDX operator."""
    return bool(
        _RE_LOWER_AND.search(value)
        or _RE_LOWER_OR.search(value)
        or _RE_LOWER_WITH.search(value),
    )


def _check_spec_license(filename: str) -> list[str]:
    """Validate the ``License`` field of ``filename``.

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

    if not lines:
        return [f'{filename}: file is empty']

    license_value = None
    for line in lines:
        m = _RE_LICENSE.match(line.strip())
        if m:
            license_value = m.group(1).strip()
            break
    if license_value is None or not license_value:
        # Field presence is checked by ``check-spec-structure``.
        return errors

    # A macro-expanded value (e.g. ``%{license}``) cannot be judged
    # statically.
    if '%' in license_value:
        return errors

    shown = _truncate(license_value)
    if _has_lowercase_operator(license_value):
        errors.append(
            f'{filename}: License must use uppercase SPDX operators '
            f'AND/OR/WITH (found "{shown}")',
        )
    if ',' in license_value:
        errors.append(
            f'{filename}: License must not use a comma as a separator; '
            f'use AND (found "{shown}")',
        )
    if _RE_PLUS_SUFFIX.search(license_value):
        errors.append(
            f'{filename}: License must not use a legacy "+" suffix; '
            f'use the "-or-later" suffix (found "{shown}")',
        )
    if license_value.count('(') != license_value.count(')'):
        errors.append(
            f'{filename}: License expression has unbalanced parentheses '
            f'(found "{shown}")',
        )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_license(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())