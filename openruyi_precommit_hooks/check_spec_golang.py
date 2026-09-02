from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:\s*(.*)')
_RE_BUILDREQUIRES = re.compile(r'^BuildRequires\s*:\s*(.*)')
_RE_PROVIDES = re.compile(r'^Provides\s*:\s*(.*)')

_RE_GO_PROVIDES = re.compile(r'go\(([^)]+)\)')

_RE_VERSION_EQ = re.compile(r'=\s*\S')

_SKIP_SECTIONS = frozenset({
    'prep', 'generate_buildrequires', 'build', 'install', 'check',
    'files', 'files_devel', 'changelog', 'description',
    'pre', 'post', 'preun', 'postun', 'pretrans', 'posttrans',
    'filetriggerin', 'filetriggerun', 'filetriggerpostun',
    'transfiletriggerin', 'transfiletriggerun', 'transfiletriggerpostun',
    'verifyscript', 'sepolicy', 'lang',
})

_GO_BUILDREQUIRES = frozenset({'go', 'go-rpm-macros'})

_GO_BUILDSYSTEMS = frozenset({'golang', 'golangmodules'})

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


def _check_spec_golang(filename: str) -> list[str]:
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

    if buildsystem_value not in _GO_BUILDSYSTEMS:
        return errors

    deps = _dependencies_in_values(buildrequires)
    missing = sorted(_GO_BUILDREQUIRES - deps)
    if missing:
        errors.append(
            f'{filename}: BuildSystem is {buildsystem_value}; '
            f'BuildRequires must declare {", ".join(missing)}',
        )

    provides: list[str] = []
    section = 'header'
    for line in lines:
        stripped = line.strip()
        m_sect = re.match(r'^%([a-z][a-z0-9_]*)', stripped)
        if m_sect:
            name = m_sect.group(1)
            if name.startswith('package'):
                section = 'package'
                continue
            if (
                name.startswith('files') or name.startswith('description') or
                name in _SKIP_SECTIONS
            ):
                section = name
                continue
        if section not in ('header', 'package'):
            continue
        if not stripped or stripped.startswith('#'):
            continue
        m = _RE_PROVIDES.match(stripped)
        if m:
            provides.append(m.group(1).strip())

    go_provides = [p for p in provides if _RE_GO_PROVIDES.search(p)]

    if buildsystem_value == 'golangmodules' and not go_provides:
        errors.append(
            f'{filename}: BuildSystem is golangmodules; a library '
            'package must declare its own import path and version with '
            'Provides: go(<import path>) = <version>',
        )

    for value in go_provides:
        if not _RE_VERSION_EQ.search(value):
            errors.append(
                f'{filename}: Provides: go(...) must carry an explicit '
                f'version constraint such as "= %{{version}}"; '
                f'got "{value}"',
            )

    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_golang(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
