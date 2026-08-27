from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``BuildSystem: cmake`` spec files of the openRuyi project must
# follow the cmake build system guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems/cmake):
#
#   A spec that uses the ``cmake`` build system must declare this
#   ``BuildRequires``:
#
#       BuildRequires:  cmake
#
#   ``gcc`` is preinstalled in the build environment and may be omitted.
#
# Statically checkable rules in this hook:
#   * when ``BuildSystem`` is ``cmake``, ``cmake`` must be declared in
#     the header ``BuildRequires`` fields.
#
# The other cmake guidelines (migrating ``%build``/``%install`` commands
# into ``BuildOption``/``%build -p``/``%install -a``, and the ``%conf``
# preset macros listed in the build system notes) are either covered by
# ``check-spec-buildoption`` or describe the build platform behaviour
# and cannot be judged statically.
#
# Field presence of ``BuildSystem`` is covered by ``check-spec-structure``;
# the general one-dependency-per-line formatting of ``BuildRequires`` is
# covered by ``check-spec-buildrequires``.

_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:\s*(.*)')
_RE_BUILDREQUIRES = re.compile(r'^BuildRequires\s*:\s*(.*)')

# The dependency every cmake spec must declare.
_CMAKE_BUILDREQUIRES = frozenset({'cmake'})


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
        value = re.sub(r'%\{[^}]*\}', ' ', value)
        value = re.sub(
            r'(?<![A-Za-z0-9_.-])%[A-Za-z_][A-Za-z0-9_]*(?![A-Za-z0-9_.])',
            ' ',
            value,
        )
        for token in re.split(r'[\s,()]', value):
            token = token.strip()
            if re.match(r'^[A-Za-z0-9_.+/]+$', token):
                deps.add(token)
    return deps


def _check_spec_cmake(filename: str) -> list[str]:
    """Validate the cmake build requirements of ``filename``.

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

    if buildsystem_value != 'cmake':
        # This hook only applies to ``BuildSystem: cmake`` specs.
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
