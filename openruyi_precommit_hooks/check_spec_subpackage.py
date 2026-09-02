from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_NAME = re.compile(r'^Name\s*:\s*(\S+)')
_RE_PACKAGE = re.compile(
    r'^%package\s+(?:-n\s+)?([A-Za-z0-9_+.-]+)',
)
_RE_REQUIRES = re.compile(r'^Requires\s*:\s*(.*)')
_RE_NAME_MACRO = re.compile(r'(?<![\w%{])%\{name\}(?![\w-])')
_RE_NAME_LITERAL_TMPL = r'(?<![\w.-]){name}(?![\w%-])'
_RE_SUBPKG_REF_TMPL = r'%\{name\}-|{name}-'
_RE_VERSION_OP = re.compile(r'(?:>=|<=|>|<|=)')
_RE_VIRTUAL = re.compile(
    r'^(?:go|pkgconfig|perl|python\d?dist|python\d|cmake|qmake|meson|'
    r'dlopen|config|rubygem|nodejs|crate|lib)\(',
)

_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _check_spec_subpackage(filename: str) -> list[str]:
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

    name = None
    for line in lines:
        m = _RE_NAME.match(line.strip())
        if m:
            name = m.group(1)
            break
    if name is None:
        return errors
    if '%' in name:
        return errors

    literal = _RE_NAME_LITERAL_TMPL.format(name=re.escape(name))
    _RE_MAIN_LITERAL = re.compile(literal)
    _RE_SUBPKG_REF = re.compile(
        r'%\{name\}-|' + re.escape(name) + r'-',
    )

    cur_subpkg: str | None = None
    for lineno, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if not stripped or stripped.startswith('#'):
            continue
        m = _RE_PACKAGE.match(stripped)
        if m:
            cur_subpkg = m.group(1)
            continue
        if cur_subpkg is None or cur_subpkg == name:
            continue
        m = _RE_REQUIRES.match(stripped)
        if not m:
            continue
        value = m.group(1).strip()
        if not value:
            continue
        if _RE_VIRTUAL.match(value):
            continue
        if _RE_SUBPKG_REF.search(value):
            continue
        references_main = bool(
            _RE_NAME_MACRO.search(value) or _RE_MAIN_LITERAL.search(value),
        )
        if not references_main:
            continue
        if _RE_VERSION_OP.search(value):
            continue
        shown = _truncate(value)
        errors.append(
            f'{filename}:{lineno}: subpackage "{cur_subpkg}" depends on '
            f'the main package "{name}" without a strict version; add a '
            f'version comparison such as "Requires: %{{name}}%{{?_isa}} = '
            f'%{{version}}-%{{release}}" (found "{shown}")',
        )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_subpackage(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
