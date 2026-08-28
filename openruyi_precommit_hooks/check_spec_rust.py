from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``BuildSystem: rust`` and ``BuildSystem: rustcrates`` spec files of
# the openRuyi project must follow the Rust build system guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems/rust):
#
#   Dependencies:
#     "When using the rust or rustcrates build system, these
#      BuildRequires are usually needed":
#
#         BuildRequires:    rust
#         BuildRequires:    rust-rpm-macros
#
#   Build stage (rustcrates):
#     "The rustcrates build stage does not run Cargo build ... therefore
#      please do not override this stage."
#
#   Testing (rust):
#     The ``rust`` build system provides a default test stage (Cargo
#     test) and arguments may be passed through ``BuildOption(check)``;
#     as in the pyproject guidelines, the reason for skipping parts of
#     the default tests must be written in a comment above.
#
# Statically checkable rules in this hook (applied only when
# ``BuildSystem`` is ``rust`` or ``rustcrates``):
#   * the header ``BuildRequires`` must declare ``rust-rpm-macros``
#     (both systems); a ``rust`` application package must also declare
#     ``rust`` (the compiler);
#   * a ``rustcrates`` spec must not use ``BuildOption(build)`` (the
#     build stage of the provider generation must not be overridden);
#   * each ``BuildOption(check)`` block of a ``rust`` spec must be
#     preceded by a comment that explains why the tests are skipped.
#
# Not checked here:
#   * ``crate(...)`` virtual dependencies: whether a package depends on
#     other crates cannot be decided from the spec alone (the upstream
#     Cargo.toml is not analysed), so no rule demands their presence;
#   * the three macros of a provider package (``crate_name``,
#     ``full_version``, ``pkgname``): "These macros usually do not need
#     to be modified manually" and all current specs declare them;
#   * ``%install`` of a ``rust`` application: "the rust build system
#     has no default install action" and ``%install -p/-a`` extensions
#     are legitimate, so a static presence rule cannot be phrased;
#   * the choice between ``rust`` and ``rustcrates``: it depends on the
#     upstream source tree and cannot be judged from the spec alone.
#
# Field presence of ``BuildSystem`` is covered by ``check-spec-structure``;
# the general two-space/order rules of ``BuildOption`` are covered by
# ``check-spec-buildoption``; ``BuildRequires: crate(...)`` dependency
# syntax is covered by ``check-spec-requires``.

_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:\s*(.*)')
_RE_BUILDREQUIRES = re.compile(r'^BuildRequires\s*:\s*(.*)')
_RE_BUILDOPTION = re.compile(r'^BuildOption\s*\(([^)]*)\)\s*:(.*)')

# The build systems this hook applies to.
_RUST_BUILDSYSTEMS = frozenset({'rust', 'rustcrates'})

# ``rust-rpm-macros`` provides the build-system macros for both
# systems.  ``rust`` (the compiler) is only needed by application
# packages that actually run Cargo build/test; crate provider packages
# never compile anything, so the guideline's second BuildRequire does
# not apply to them.
_RUSTCRATES_REQUIRED = frozenset({'rust-rpm-macros'})
_RUST_REQUIRED = frozenset({'rust', 'rust-rpm-macros'})

# See check_spec_perl._dependencies_in_values: ``-`` is a valid
# package-name character (e.g. ``rust-rpm-macros``), so it is kept, but
# a bare ``-suffix`` left over from a stripped macro must not count.
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


def _previous_nonblank(lines: list[str], index: int) -> int:
    """Return the index of the nearest non-blank line before ``index``.

    ``-1`` when no such line exists.
    """
    j = index - 1
    while j >= 0 and not lines[j].strip():
        j -= 1
    return j


def _is_check_block_start(lines: list[str], index: int) -> bool:
    """Whether ``lines[index]`` starts a ``BuildOption(check)`` block.

    Consecurive ``BuildOption(check)`` lines (no blank lines in
    between) form one block; only its first line needs the comment.
    """
    j = _previous_nonblank(lines, index)
    if j < 0:
        return True
    m = _RE_BUILDOPTION.match(lines[j].strip())
    if m and m.group(1).strip() == 'check':
        return False
    return True


def _has_comment_above(lines: list[str], index: int) -> bool:
    """Whether the nearest non-blank line above ``index`` is a comment."""
    j = _previous_nonblank(lines, index)
    return j >= 0 and lines[j].strip().startswith('#')


def _check_spec_rust(filename: str) -> list[str]:
    """Validate the Rust build requirements of ``filename``.

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
    build_option_lines: list[int] = []
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
            if stage == 'build':
                build_option_lines.append(i + 1)
            elif stage == 'check':
                check_indices.append(i)

    if buildsystem_value not in _RUST_BUILDSYSTEMS:
        # This hook only applies to rust/rustcrates specs.
        return errors

    deps = _dependencies_in_values(buildrequires)
    if buildsystem_value == 'rustcrates':
        missing = sorted(_RUSTCRATES_REQUIRED - deps)
        if missing:
            errors.append(
                f'{filename}: BuildSystem is rustcrates; BuildRequires '
                f'must declare {", ".join(missing)}',
            )
        for lineno in build_option_lines:
            # The rustcrates build stage runs a specpart generation
            # script and must not be overridden.
            errors.append(
                f'{filename}:{lineno}: BuildSystem is rustcrates; '
                f'BuildOption(build) must not be used (the build stage '
                f'cannot be overridden)',
            )
    else:
        missing = sorted(_RUST_REQUIRED - deps)
        if missing:
            errors.append(
                f'{filename}: BuildSystem is rust; BuildRequires must '
                f'declare {", ".join(missing)}',
            )
        for index in check_indices:
            if (
                _is_check_block_start(lines, index) and
                not _has_comment_above(lines, index)
            ):
                errors.append(
                    f'{filename}:{index + 1}: BuildOption(check) must be '
                    f'preceded by a comment explaining why the tests are '
                    f'skipped',
                )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_rust(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
