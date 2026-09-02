from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:\s*(.*)')
_RE_BUILDREQUIRES = re.compile(r'^BuildRequires\s*:\s*(.*)')
_RE_BUILDOPTION = re.compile(r'^BuildOption\s*\(([^)]*)\)\s*:(.*)')

_REQUIRED_BUILDREQUIRES = frozenset({'pyproject-rpm-macros'})

_PYPROJECT_BUILDSYSTEM = 'pyproject'

_TOKEN_RE = re.compile(r'^[A-Za-z0-9_.+/]+(?:-[A-Za-z0-9_.+/]+)*$')
_MACRO_RE = re.compile(r'%\{[^}]*\}')
_BARE_MACRO_RE = re.compile(
    r'(?<![A-Za-z0-9_.-])%[A-Za-z_][A-Za-z0-9_]*(?![A-Za-z0-9_.])',
)


def _dependencies_in_values(values: list[str]) -> set[str]:
    deps: set[str] = set()
    for value in values:
        value = _MACRO_RE.sub(' ', value)
        value = _BARE_MACRO_RE.sub(' ', value)
        for token in re.split(r'[\s,()]', value):
            token = token.strip()
            if _TOKEN_RE.match(token):
                deps.add(token)
    return deps


def _previous_nonblank(lines: list[str], index: int) -> int:
    j = index - 1
    while j >= 0 and not lines[j].strip():
        j -= 1
    return j


def _is_check_block_start(lines: list[str], index: int) -> bool:
    j = _previous_nonblank(lines, index)
    if j < 0:
        return True
    m = _RE_BUILDOPTION.match(lines[j].strip())
    if m and m.group(1).strip() == 'check':
        return False
    return True


def _has_comment_above(lines: list[str], index: int) -> bool:
    j = _previous_nonblank(lines, index)
    return j >= 0 and lines[j].strip().startswith('#')


def _check_spec_pyproject(filename: str) -> list[str]:
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
    install_options: list[tuple[int, str]] = []
    check_indices: list[int] = []
    for i, line in enumerate(lines[:cut]):
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
        m = _RE_BUILDOPTION.match(stripped)
        if m:
            stage = m.group(1).strip()
            value = m.group(2).strip()
            if stage == 'install':
                install_options.append((i + 1, value))
            elif stage == 'check':
                check_indices.append(i)

    if buildsystem_value != _PYPROJECT_BUILDSYSTEM:
        return errors

    deps = _dependencies_in_values(buildrequires)
    missing = sorted(_REQUIRED_BUILDREQUIRES - deps)
    if missing:
        errors.append(
            f'{filename}: BuildSystem is pyproject; BuildRequires must '
            f'declare {", ".join(missing)}',
        )

    for lineno, value in install_options:
        if not value:
            errors.append(
                f'{filename}:{lineno}: BuildOption(install) must carry '
                f'a module name (found an empty value)',
            )

    for index in check_indices:
        if (
            _is_check_block_start(lines, index) and
            not _has_comment_above(lines, index)
        ):
            errors.append(
                f'{filename}:{index + 1}: BuildOption(check) must be '
                f'preceded by a comment explaining why the modules are '
                f'skipped',
            )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_pyproject(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
