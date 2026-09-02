from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

_RE_BCOND = re.compile(r'^%bcond\s+(\S+)')
_RE_BCOND_WITH = re.compile(r'^%bcond_with\s+(\S+)')
_RE_BCOND_WITHOUT = re.compile(r'^%bcond_without\s+(\S+)')
_RE_REF = re.compile(r'%\{(with|without)\s+(\S+?)\}')


def _check_spec_bcond(filename: str) -> list[str]:
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

    declared: set[str] = set()
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#'):
            continue
        m = _RE_BCOND.match(stripped)
        if m is not None:
            declared.add(m.group(1))
            continue
        m = _RE_BCOND_WITH.match(stripped)
        if m is not None:
            declared.add(m.group(1))
            continue
        m = _RE_BCOND_WITHOUT.match(stripped)
        if m is not None:
            declared.add(m.group(1))

    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith('#'):
            continue
        m = _RE_BCOND_WITH.match(stripped)
        if m is not None:
            errors.append(
                f'{filename}:{lineno}: legacy %bcond_with must be replaced '
                f'with %bcond {m.group(1)} <0|1> '
                f'(found "{stripped}")',
            )
            continue
        m = _RE_BCOND_WITHOUT.match(stripped)
        if m is not None:
            errors.append(
                f'{filename}:{lineno}: legacy %bcond_without must be '
                f'replaced with %bcond {m.group(1)} <0|1> '
                f'(found "{stripped}")',
            )
            continue
        for rm in _RE_REF.finditer(stripped):
            name = rm.group(2)
            if name not in declared:
                errors.append(
                    f'{filename}:{lineno}: %{{{rm.group(1)} {name}}} '
                    f'references an undeclared switch; add '
                    f'%bcond {name} <0|1> (found "{stripped}")',
                )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_bcond(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
