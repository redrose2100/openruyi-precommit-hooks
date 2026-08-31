from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# A subpackage that depends on the main package must depend on it at a
# strict version, so that header/link files and the runtime libraries
# stay in sync (openRuyi packaging guidelines, "Software package
# splitting" / SplitPackage):
#
#     https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/SplitPackage
#
# The guideline states (translated):
#
#   "A subpackage that needs the main package must depend on the main
#    package at a strict version, which avoids the headers/link files
#    and the runtime library going out of sync:
#
#        Requires: %{name}%{?_isa} = %{version}-%{release}
#
#    It is also recommended to append %{?_isa} after the main package
#    name so the dependency becomes architecture specific."
#
# Statically checkable rules in this hook:
#   * inside a ``%package`` subpackage block (other than the main
#     package itself), a plain ``Requires:`` value that references the
#     main package (via ``%{name}`` or the literal main-package name)
#     must carry a version comparison (``=``, ``>=``, ...).  A bare
#     ``Requires: %{name}`` or ``Requires: <mainname>`` is reported so
#     the packager writes the strict version dependency instead.
#
# Exemptions handled here:
#   * ``%{name}-<feature>`` references (a dependency on another
#     subpackage, not on the main package);
#   * references to virtual capabilities such as ``go(...)``,
#     ``pkgconfig(...)``, ``perl(...)``, ``python3dist(...)``;
#   * scriptlet ``Requires(pre):`` / ``Requires(post):`` ... variants
#     (they declare scriptlet or metadata roles, not the runtime
#     dependency on the main package, matching ``check-spec-requires``);
#   * a main-package name that expands a macro cannot be checked
#     statically and is skipped.
#
# ``Requires:`` field presence is covered by ``check-spec-structure``.

_RE_NAME = re.compile(r'^Name\s*:\s*(\S+)')
_RE_PACKAGE = re.compile(
    r'^%package\s+(?:-n\s+)?([A-Za-z0-9_+.-]+)',
)
# Plain ``Requires:`` (not the scriptlet variants).
_RE_REQUIRES = re.compile(r'^Requires\s*:\s*(.*)')
# A bare ``%{name}`` token (a reference to the main package).
_RE_NAME_MACRO = re.compile(r'(?<![\w%{])%\{name\}(?![\w-])')
# Templates compiled per-spec with the real main package name.
# A literal main-package-name token (word boundary on both sides; a
# following ``%`` means a macro continuation such as
# ``gcc%{gcc_version}-c++`` which expands to a *different* package, not
# a bare reference to the main package).
_RE_NAME_LITERAL_TMPL = r'(?<![\w.-]){name}(?![\w%-])'
# A reference to another subpackage such as ``%{name}-devel`` or
# ``<mainname>-client``.
_RE_SUBPKG_REF_TMPL = r'%\{name\}-|{name}-'
# A version comparison operator.
_RE_VERSION_OP = re.compile(r'(?:>=|<=|>|<|=)')
# A value that is a single virtual capability such as ``go(...)``,
# ``perl(...)`` or ``pkgconfig(...)`` never references the main package.
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
    """Validate the subpackage-to-main-package ``Requires`` of ``filename``.

    Returns a list of human readable error messages; empty on success.
    """
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
        # Field presence is checked by ``check-spec-structure``.
        return errors
    if '%' in name:
        # A macro-expanded main name cannot be checked statically.
        return errors

    literal = _RE_NAME_LITERAL_TMPL.format(name=re.escape(name))
    _RE_MAIN_LITERAL = re.compile(literal)
    # ``%{name}-`` (macro reference to the main package) is static;
    # ``<mainname>-`` must be escaped with the real package name.
    _RE_SUBPKG_REF = re.compile(
        r'%\{name\}-|' + re.escape(name) + r'-',
    )

    # Current ``%package`` subpackage name; ``None`` means the main
    # package block (top level).
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
            # Main package block: the rule is about subpackages that
            # depend on the main package, not the main package itself.
            continue
        m = _RE_REQUIRES.match(stripped)
        if not m:
            continue
        value = m.group(1).strip()
        if not value:
            continue
        # A value that is a single virtual capability such as
        # ``go(...)`` / ``perl(...)`` / ``pkgconfig(...)`` never
        # references the main package.
        if _RE_VIRTUAL.match(value):
            continue
        # A dependency on another subpackage (``%{name}-<feature>`` or
        # ``<mainname>-<feature>``) is not a dependency on the main
        # package; ``%{name}-devel``/``<mainname>-devel`` likewise.
        if _RE_SUBPKG_REF.search(value):
            continue
        # Does the value reference the main package?
        references_main = bool(
            _RE_NAME_MACRO.search(value) or _RE_MAIN_LITERAL.search(value),
        )
        if not references_main:
            continue
        if _RE_VERSION_OP.search(value):
            # Already pinned to a version (e.g. ``= %{version}``,
            # ``>= %{version}`` or the recommended
            # ``= %{version}-%{release}``).
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
