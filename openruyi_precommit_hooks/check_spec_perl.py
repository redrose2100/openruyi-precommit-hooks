from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``BuildSystem: perlbuild`` / ``BuildSystem: perlmaker`` spec files
# of the openRuyi project must follow the perl build system guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems/perl):
#
#   A spec that uses the ``perlbuild`` or ``perlmaker`` build system
#   must declare these ``BuildRequires``:
#
#       BuildRequires:  perl-rpm-packaging
#       BuildRequires:  perl-rpm-macros
#       BuildRequires:  perl-macros
#
#   (Unlike the cmake/autotools guidelines, the perl page does not
#   mention a preinstalled-tool exemption, so all three requirements
#   must be declared.)
#
# Statically checkable rules in this hook:
#   * when ``BuildSystem`` is ``perlbuild`` or ``perlmaker``,
#     ``perl-rpm-packaging``, ``perl-rpm-macros`` and ``perl-macros``
#     must be declared in the header ``BuildRequires`` fields.
#   * ``Requires:``/``Provides:`` fields must not depend on a bare
#     ``perl-CPANDIST`` package name; the ``perl(MODULE)`` virtual
#     dependency format must be used instead.  A ``perl-X`` reference
#     is only allowed when the spec itself declares a ``%package perl-X``
#     subpackage (a split-off or bundled package).
#
# The other perl guidelines are not checked here:
#   * the ``perl(Module::Build)`` / ``perl(ExtUtils::MakeMaker)`` /
#     ``perl(Test::More)`` virtual dependencies are phrased as
#     "usually needed" (weak guideline) and depend on the upstream
#     build script, so they are not hard requirements;
#   * choosing between ``perlbuild`` (``Build.PL``) and ``perlmaker``
#     (``Makefile.PL``) depends on the upstream source tree and cannot
#     be judged from the spec alone;
#   * the ``BuildOption(build)``/``BuildOption(install)``/
#     ``BuildOption(check)`` examples are covered by
#     ``check-spec-buildoption``;
#   * the ``%files -f %{name}.files`` file list is phrased as "usually
#     used" (weak guideline) and is not a hard requirement.
#
# Field presence of ``BuildSystem`` is covered by ``check-spec-structure``;
# the general one-dependency-per-line formatting of ``BuildRequires`` is
# covered by ``check-spec-buildrequires``.

_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:\s*(.*)')
_RE_BUILDREQUIRES = re.compile(r'^BuildRequires\s*:\s*(.*)')

# ``Requires:`` / ``Provides:`` lines whose value starts with a bare
# ``perl-CPANDIST`` package name (e.g. ``perl-SGMLSpm``).  The CPAN
# distribution naming convention capitalises the first letter, so
# ``perl-XYZ`` identifies a distribution name whereas ``perl(xyz)`` is
# the virtual-dependency format that must be used instead.
_RE_REQ_PROV = re.compile(r'^(?:Requires|Provides)\s*:\s*(.*)')
_RE_PERL_PACKAGE = re.compile(r'^perl-[A-Z][A-Za-z0-9_-]*')

# ``%package perl-XYZ`` subpackage declarations.
_RE_PACKAGE_NAME = re.compile(
    r'^%package\s+(?:-n\s+)?([A-Za-z0-9_+.-]+)',
)

# The dependencies every perlbuild/perlmaker spec must declare.
_PERL_BUILDREQUIRES = frozenset({
    'perl-rpm-packaging',
    'perl-rpm-macros',
    'perl-macros',
})

# The ``BuildSystem`` values this hook applies to.
_PERL_BUILDSYSTEMS = frozenset({'perlbuild', 'perlmaker'})

# See check_spec_cmake._dependencies_in_values: ``-`` is a valid
# package-name character (e.g. ``perl-rpm-macros``), so it is kept, but
# a bare ``-suffix`` left over from a stripped macro must not count.
_TOKEN_RE = re.compile(r'^[A-Za-z0-9_.+/]+(?:-[A-Za-z0-9_.+/]+)*$')
_MACRO_RE = re.compile(r'%\{[^}]*\}')
_BARE_MACRO_RE = re.compile(
    r'(?<![A-Za-z0-9_.-])%[A-Za-z_][A-Za-z0-9_]*(?![A-Za-z0-9_.])',
)


def _subpackage_names(lines: list[str]) -> set[str]:
    """Collect the ``%package`` subpackage names declared by ``lines``.

    ``Requires: perl-X`` is allowed when the spec itself declares the
    ``perl-X`` package (e.g. a split-off subpackage), so those names are
    collected up front.  ``%package -n name`` overrides the prefix, and
    ``foo%{?bar}`` style macro names cannot be matched statically.
    """
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


def _check_spec_perl(filename: str) -> list[str]:
    """Validate the perl build requirements of ``filename``.

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

    # The ``perl(MODULE)`` virtual-dependency rule applies to every spec
    # (the perl guidelines describe the ``Requires``/``Provides`` format
    # in general), so it is checked before the build-system gate below.
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

    # Only the header region is inspected: ``BuildRequires`` inside a
    # ``%package`` subpackage block declares the subpackage build
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

    if buildsystem_value not in _PERL_BUILDSYSTEMS:
        # This hook only applies to perlbuild/perlmaker specs.
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
