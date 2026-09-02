from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_LICENSE = re.compile(r'^License\s*:\s*(.*)')
_RE_LOWER_AND = re.compile(r'(^|[ (])\band($|[ )])')
_RE_LOWER_OR = re.compile(r'(^|[ (])\bor($|[ )])')
_RE_LOWER_WITH = re.compile(r'(^|[ (])\bwith($|[ )])')
_RE_PLUS_SUFFIX = re.compile(r'\b[A-Za-z0-9][A-Za-z0-9.-]*\+')
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _has_lowercase_operator(value: str) -> bool:
    return bool(
        _RE_LOWER_AND.search(value) or
        _RE_LOWER_OR.search(value) or
        _RE_LOWER_WITH.search(value),
    )


def _check_spec_license(filename: str) -> list[str]:
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
        return errors

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
