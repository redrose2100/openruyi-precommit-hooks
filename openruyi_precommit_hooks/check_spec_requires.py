from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_REQUIRES = re.compile(r'^Requires\s*:\s*(.*)')
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


def _check_spec_requires(filename: str) -> list[str]:
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

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        m = _RE_REQUIRES.match(stripped)
        if not m:
            continue
        value = m.group(1).strip()
        if not value:
            errors.append(
                f'{filename}: Requires must list a runtime dependency '
                f'(found empty value)',
            )
            continue
        if not _is_single_dependency(value):
            shown = _truncate(value)
            errors.append(
                f'{filename}: Requires must declare exactly one '
                f'dependency per line (found "{shown}")',
            )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_requires(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
