from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_GUIDELINE_BUILD_SYSTEMS = frozenset({
    'autotools',
    'cmake',
    'meson',
    'golang',
    'golangmodules',
    'pyproject',
})

_REPO_BUILD_SYSTEMS = frozenset({
    'perlbuild',
    'perlmaker',
    'rust',
    'rustcrates',
})

_KNOWN_BUILD_SYSTEMS = _GUIDELINE_BUILD_SYSTEMS | _REPO_BUILD_SYSTEMS

_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:\s*(.*)')
_RE_COMMENT = re.compile(r'^\s*#')
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _check_spec_buildsystem(filename: str) -> list[str]:
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

    buildsystem_value = None
    buildsystem_idx = -1
    for i, line in enumerate(lines[:cut]):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        m = _RE_BUILDSYSTEM.match(stripped)
        if m:
            if buildsystem_idx == -1:
                buildsystem_idx = i
                buildsystem_value = m.group(1).strip()
            break

    if buildsystem_value is None:
        return errors

    if not buildsystem_value or buildsystem_value.startswith('#'):
        if buildsystem_value.startswith('#'):
            return errors
        if (
            buildsystem_idx > 0 and
            _RE_COMMENT.match(lines[buildsystem_idx - 1])
        ):
            return errors
        errors.append(
            f'{filename}: BuildSystem is empty; the reason must be '
            f'explained in a comment',
        )
        return errors

    if buildsystem_value not in _KNOWN_BUILD_SYSTEMS:
        shown = _truncate(buildsystem_value)
        errors.append(
            f'{filename}: BuildSystem must be one of the known build '
            f'systems ({", ".join(sorted(_KNOWN_BUILD_SYSTEMS))}) or a '
            f'newly added value (found "{shown}")',
        )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_buildsystem(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
