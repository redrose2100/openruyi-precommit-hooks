from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:\s*(.*)')
_RE_BUILDREQUIRES = re.compile(r'^BuildRequires\s*:\s*(.*)')

_CMAKE_BUILDREQUIRES = frozenset({'cmake'})


def _dependencies_in_values(values: list[str]) -> set[str]:
    deps: set[str] = set()
    for value in values:
        value = re.sub(r'%\{[^}]*\}', ' ', value)
        value = re.sub(
            r'(?<![A-Za-z0-9_.-])%[A-Za-z_][A-Za-z0-9_]*(?![A-Za-z0-9_.])',
            ' ',
            value,
        )
        for token in re.split(r'[\s,()]', value):
            token = token.strip()
            if re.match(r'^[A-Za-z0-9_.+/]+(?:-[A-Za-z0-9_.+/]+)*$', token):
                deps.add(token)
    return deps


def _check_spec_cmake(filename: str) -> list[str]:
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

    buildsystem_value: str | None = None
    buildrequires: list[str] = []
    for line in lines[:cut]:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        if buildsystem_value is None:
            m = _RE_BUILDSYSTEM.match(stripped)
            if m:
                buildsystem_value = m.group(1).strip()
        m = _RE_BUILDREQUIRES.match(stripped)
        if m:
            buildrequires.append(m.group(1).strip())

    if buildsystem_value != 'cmake':
        return errors

    deps = _dependencies_in_values(buildrequires)
    missing = sorted(_CMAKE_BUILDREQUIRES - deps)
    if missing:
        errors.append(
            f'{filename}: BuildSystem is cmake; BuildRequires must '
            f'declare {", ".join(missing)}',
        )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_cmake(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
