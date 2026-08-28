from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``BuildSystem: golang`` / ``BuildSystem: golangmodules`` spec files
# of the openRuyi project must follow the golang build system guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems/golang)
# and the golang language guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/languages/Golang):
#
#   A spec that uses the ``golang`` or ``golangmodules`` build system
#   must declare these ``BuildRequires``:
#
#       BuildRequires:  go
#       BuildRequires:  go-rpm-macros
#
#   (Unlike the cmake/autotools guidelines, the golang page does not
#   mention a preinstalled-tool exemption, so both requirements must be
#   declared.)
#
#   A library package ("仅包含库 (或二进制+库) 的软件包") must explicitly
#   write out the import paths and versions it provides:
#
#       Provides:       go(github.com/clipperhouse/uax29/v2) = %{version}
#
#   ("库软件包本身必须要显式在 RPM Spec 内写出自己提供的导入路径和版本")
#
# Statically checkable rules in this hook:
#   * when ``BuildSystem`` is ``golang`` or ``golangmodules``, ``go``
#     and ``go-rpm-macros`` must be declared in the header
#     ``BuildRequires`` fields;
#   * when ``BuildSystem`` is ``golangmodules`` (the build system used
#     for pure library packages), at least one ``Provides: go(...)``
#     must be declared for the package's own import path;
#   * every ``Provides: go(<import path>)`` must carry an explicit
#     version constraint (``= <version>``), matching the required
#     ``Provides: go(<import path>) = <version>`` form.
#
# The other golang guidelines are not checked here:
#   * defining the ``_name`` and ``go_import_path`` macros in the header
#     is phrased as "at least should" (weak guideline) and is not a
#     hard requirement;
#   * cross-build-system macro calls (``%go_common``,
#     ``%buildsystem_golangmodules_install``, ``%install -a``) depend on
#     whether binaries or libraries are shipped and cannot be judged
#     statically;
#   * ``BuildOption(prep)``/``BuildOption(check)`` examples are covered
#     by ``check-spec-buildoption``;
#   * binary-only package naming (no ``go-`` prefix), the
#     ``/usr/share/gocode`` install location and the ``Conflicts:``
#     mutual-exclusion rule for multiple library versions are either
#     non-mandatory or not statically decidable without external
#     knowledge of the upstream project.
#
# Field presence of ``BuildSystem`` is covered by ``check-spec-structure``;
# the general one-dependency-per-line formatting of ``BuildRequires`` is
# covered by ``check-spec-buildrequires``.

_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:\s*(.*)')
_RE_BUILDREQUIRES = re.compile(r'^BuildRequires\s*:\s*(.*)')
_RE_PROVIDES = re.compile(r'^Provides\s*:\s*(.*)')

# A ``Provides: go(<import path>)`` virtual provides entry.
_RE_GO_PROVIDES = re.compile(r'go\(([^)]+)\)')

# An explicit version constraint such as ``= %{version}`` or ``= 1.0.0``.
_RE_VERSION_EQ = re.compile(r'=\s*\S')

# rpm script sections in which ``Provides`` is never declared (prose and
# script bodies are not inspected).
_SKIP_SECTIONS = frozenset({
    'prep', 'generate_buildrequires', 'build', 'install', 'check',
    'files', 'files_devel', 'changelog', 'description',
    'pre', 'post', 'preun', 'postun', 'pretrans', 'posttrans',
    'filetriggerin', 'filetriggerun', 'filetriggerpostun',
    'transfiletriggerin', 'transfiletriggerun', 'transfiletriggerpostun',
    'verifyscript', 'sepolicy', 'lang',
})

# The dependencies every golang/golangmodules spec must declare.
_GO_BUILDREQUIRES = frozenset({'go', 'go-rpm-macros'})

# The ``BuildSystem`` values this hook applies to.
_GO_BUILDSYSTEMS = frozenset({'golang', 'golangmodules'})

# See check_spec_cmake._dependencies_in_values: ``-`` is a valid
# package-name character (e.g. ``go-rpm-macros``), so it is kept, but a
# bare ``-suffix`` left over from a stripped macro must not count.
_TOKEN_RE = re.compile(r'^[A-Za-z0-9_.+/]+(?:-[A-Za-z0-9_.+/]+)*$')
_MACRO_RE = re.compile(r'%\{[^}]*\}')
_BARE_MACRO_RE = re.compile(
    r'(?<![A-Za-z0-9_.-])%[A-Za-z_][A-Za-z0-9_]*(?![A-Za-z0-9_.])',
)


def _dependencies_in_values(values: list[str]) -> set[str]:
    """Extract the set of dependency names from ``BuildRequires`` values.

    Values are read from the raw ``BuildRequires:`` lines.  A value can
    declare several packages (the general rule of one dependency per
    line is enforced by ``check-spec-buildrequires``), so every token is
    collected here.
    """
    deps: set[str] = set()
    for value in values:
        # strip rpm macros so ``%{?foo}-devel`` does not pollute the set
        value = _MACRO_RE.sub(' ', value)
        value = _BARE_MACRO_RE.sub(' ', value)
        for token in re.split(r'[\s,()]', value):
            token = token.strip()
            if _TOKEN_RE.match(token):
                deps.add(token)
    return deps


def _check_spec_golang(filename: str) -> list[str]:
    """Validate the golang build requirements of ``filename``.

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

    # Only the header region is inspected for ``BuildRequires``: inside a
    # ``%package`` subpackage block it declares the subpackage build
    # dependencies and is not covered by this rule.
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
        # This hook only applies to golang/golangmodules specs.
        return errors

    deps = _dependencies_in_values(buildrequires)
    missing = sorted(_GO_BUILDREQUIRES - deps)
    if missing:
        errors.append(
            f'{filename}: BuildSystem is {buildsystem_value}; '
            f'BuildRequires must declare {", ".join(missing)}',
        )

    # The golang language guideline requires a library package to declare
    # the import paths it provides together with their versions:
    # ``Provides: go(<import path>) = <version>``.  ``Provides`` fields
    # are collected from the header region and from ``%package``
    # subpackage blocks (a second variant of the same library, e.g. a v2
    # module, may carry its own provide); prose sections
    # (``%description`` / ``%changelog``) and script sections (``%prep``,
    # ``%build``, ``%install``, ``%check``, ``%files``) are not
    # inspected.
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
            if (name.startswith('files') or name.startswith('description')
                    or name in _SKIP_SECTIONS):
                section = name
                continue
            # ``%if``/``%define``/``%{...}`` etc. do not change section.
        if section not in ('header', 'package'):
            continue
        if not stripped or stripped.startswith('#'):
            continue
        m = _RE_PROVIDES.match(stripped)
        if m:
            provides.append(m.group(1).strip())

    go_provides = [p for p in provides if _RE_GO_PROVIDES.search(p)]

    # ``golangmodules`` is the build system used for pure library
    # packages, so it must offer at least one ``go()`` virtual provide.
    if buildsystem_value == 'golangmodules' and not go_provides:
        errors.append(
            f'{filename}: BuildSystem is golangmodules; a library '
            'package must declare its own import path and version with '
            'Provides: go(<import path>) = <version>',
        )

    # Every ``Provides: go(...)`` must carry an explicit version
    # constraint (``= <version>``), as required by the guideline.
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
