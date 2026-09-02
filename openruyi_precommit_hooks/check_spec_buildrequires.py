from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_BUILDREQUIRES = re.compile(r'^BuildRequires\s*:\s*(.*)')
_RE_VERSIONED = re.compile(r'^.+?\s+(?:[<>]=?|=)\s*\S+$')
_RE_RICH = re.compile(r'^\(.*\)$')
_RE_WITH = re.compile(r'\s(?:with|without)\s')
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _is_single_dependency(value: str) -> bool:
    if '%{' in value or _RE_WITH.search(value):
        return True
    if _RE_RICH.match(value) or _RE_VERSIONED.match(value):
        return True
    return len(value.split()) <= 1


def _check_spec_buildrequires(filename: str) -> list[str]:
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

    cut = len(lines)
    for i, line in enumerate(lines):
        if re.match(r'^%(?:description|package)\b', line.strip()):
            cut = i
            break

    for i, line in enumerate(lines[:cut]):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        m = _RE_BUILDREQUIRES.match(stripped)
        if not m:
            continue
        value = m.group(1).strip()
        if not value:
            errors.append(
                f'{filename}: BuildRequires must list a build-time '
                f'dependency (found empty value)',
            )
            continue
        if not _is_single_dependency(value):
            shown = _truncate(value)
            errors.append(
                f'{filename}: BuildRequires must declare exactly one '
                f'dependency per line (found "{shown}")',
            )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_buildrequires(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
