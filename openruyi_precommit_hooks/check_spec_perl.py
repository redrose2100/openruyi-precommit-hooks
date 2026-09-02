from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:\s*(.*)')
_RE_BUILDREQUIRES = re.compile(r'^BuildRequires\s*:\s*(.*)')

_RE_REQ_PROV = re.compile(r'^(?:Requires|Provides)\s*:\s*(.*)')
_RE_PERL_PACKAGE = re.compile(r'^perl-[A-Z][A-Za-z0-9_-]*')

_RE_PACKAGE_NAME = re.compile(
    r'^%package\s+(?:-n\s+)?([A-Za-z0-9_+.-]+)',
)

_PERL_BUILDREQUIRES = frozenset({
    'perl-rpm-packaging',
    'perl-rpm-macros',
    'perl-macros',
})

_PERL_BUILDSYSTEMS = frozenset({'perlbuild', 'perlmaker'})

_TOKEN_RE = re.compile(r'^[A-Za-z0-9_.+/]+(?:-[A-Za-z0-9_.+/]+)*$')
_MACRO_RE = re.compile(r'%\{[^}]*\}')
_BARE_MACRO_RE = re.compile(
    r'(?<![A-Za-z0-9_.-])%[A-Za-z_][A-Za-z0-9_]*(?![A-Za-z0-9_.])',
)


def _subpackage_names(lines: list[str]) -> set[str]:
    names: set[str] = set()
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith('%package'):
            continue
        m = _RE_PACKAGE_NAME.match(stripped)
        if m and '%' not in m.group(1):
            name = m.group(1)
            if name.startswith('perl-'):
                names.add(name)
    return names


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


def _check_spec_perl(filename: str) -> list[str]:
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

    subpackages = _subpackage_names(lines)
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        m = _RE_REQ_PROV.match(stripped)
        if not m:
            continue
        value = m.group(1).strip()
        for token in re.split(r'[\s,]+', value):
            token = token.rstrip('=<>~')
            pkg_m = _RE_PERL_PACKAGE.match(token)
            if not pkg_m:
                continue
            pkg = pkg_m.group(0)
            if pkg not in subpackages:
                errors.append(
                    f'{filename}: requires/provides must use the '
                    f'perl(MODULE) virtual dependency format, not the '
                    f'package name "{pkg}"',
                )

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

    if buildsystem_value not in _PERL_BUILDSYSTEMS:
        return errors

    deps = _dependencies_in_values(buildrequires)
    missing = sorted(_PERL_BUILDREQUIRES - deps)
    if missing:
        errors.append(
            f'{filename}: BuildSystem is {buildsystem_value}; '
            f'BuildRequires must declare {", ".join(missing)}',
        )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_perl(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
