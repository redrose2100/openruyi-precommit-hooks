from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``BuildSystem: meson`` spec files of the openRuyi project must
# follow the meson build system guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems/meson):
#
#   A spec that uses the ``meson`` build system must declare this
#   ``BuildRequires``:
#
#       BuildRequires:  meson
#
#   (Unlike the cmake/autotools guidelines, the meson page does not
#   mention a preinstalled-tool exemption, so the requirement must be
#   declared.)
#
# Statically checkable rules in this hook:
#   * when ``BuildSystem`` is ``meson``, ``meson`` must be declared in
#     the header ``BuildRequires`` fields.
#
# The other meson guidelines are not checked here:
#   * the ``BuildOption(conf)``/``BuildOption(build)`` examples
#     (``-Dman=enabled`` etc.) and the ``%build`` -> ``%conf`` /
#     ``%install -a`` migration are covered by
#     ``check-spec-buildoption`` and cannot be judged statically;
#   * ``ninja-build`` is meson's build backend but the guidelines never
#     ask specs to declare it, so it is not required here.
#
# Field presence of ``BuildSystem`` is covered by ``check-spec-structure``;
# the general one-dependency-per-line formatting of ``BuildRequires`` is
# covered by ``check-spec-buildrequires``.

_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:\s*(.*)')
_RE_BUILDREQUIRES = re.compile(r'^BuildRequires\s*:\s*(.*)')

# The dependency every meson spec must declare.
_MESON_BUILDREQUIRES = frozenset({'meson'})

# The ``BuildSystem`` values this hook applies to.
_MESON_BUILDSYSTEMS = frozenset({'meson'})

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


def _check_spec_meson(filename: str) -> list[str]:
    """Validate the meson build requirements of ``filename``.

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

    if buildsystem_value not in _MESON_BUILDSYSTEMS:
        # This hook only applies to meson specs.
        return errors

    deps = _dependencies_in_values(buildrequires)
    missing = sorted(_MESON_BUILDREQUIRES - deps)
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
        for err in _check_spec_meson(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
