from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``BuildRequires`` field of an openRuyi spec file must follow the
# packaging guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#buildrequires):
#
#   1. ``BuildRequires`` must list the build-time dependencies.
#   2. The dependencies must be declared one per line.
#   3. ``gcc`` usually does not need to be declared explicitly for C
#      programs.
#   4. When a dependency is discovered through ``pkg-config``,
#      ``BuildRequires`` should declare ``pkgconfig(xxx)`` instead of
#      depending directly on ``xxx-devel``.
#   5. The spec must declare a complete set of build dependencies; it
#      must not omit required dependencies only because they happen to
#      be preinstalled in the build environment.
#
# The "typesetting and readability" section of the guidelines also
# requires that ``BuildRequires`` and ``Requires`` declare exactly one
# dependency per line
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#%E6%8E%92%E7%89%88%E4%B8%8E%E5%8F%AF%E8%AF%BB%E6%80%A7).
#
# The detailed policy on ``pkgconfig(xxx)`` is in the supplement
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/PkgConfigBuildRequires).
#
# ``BuildRequires`` is a required field.  Statically checkable rules in
# this hook:
#   * a ``BuildRequires:`` line must not be empty (an empty value cannot
#     declare a build-time dependency);
#   * a ``BuildRequires:`` line must declare exactly one dependency
#     (multiple packages on one line violate "one dependency per
#     line").
#
# Field presence is covered by ``check-spec-structure`` (``BuildRequires``
# is required, so a missing field is not reported here).  Whether the
# declared dependency set is really complete, whether ``gcc`` is needed,
# and whether ``pkgconfig(xxx)`` should be used instead of ``xxx-devel``
# cannot be judged statically.
#
# A ``BuildRequires`` line that carries several tokens is interpreted as
# a single dependency when it ends with a version comparison ("foo >=
# 1.2"), is a rich dependency ("(foo >= 1 with foo < 2)") or uses the
# ``with``/``without`` syntax; all other multi-token values are reported.

_RE_BUILDREQUIRES = re.compile(r'^BuildRequires\s*:\s*(.*)')
# A value that ends with a version comparison ("foo >= 1.2", "foo = 1.29").
_RE_VERSIONED = re.compile(r'^.+?\s+(?:[<>]=?|=)\s*\S+$')
# Rich dependency expression: "(foo >= 1 with foo < 2)".
_RE_RICH = re.compile(r'^\(.*\)$')
# Boolean "with/without" expression: "foo with bar".
_RE_WITH = re.compile(r'\s(?:with|without)\s')
# Avoid echoing a very long value verbatim in an error message.
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _is_single_dependency(value: str) -> bool:
    """Return True when ``value`` declares exactly one dependency."""
    if '%{' in value or _RE_WITH.search(value):
        return True
    if _RE_RICH.match(value) or _RE_VERSIONED.match(value):
        return True
    return len(value.split()) <= 1


def _check_spec_buildrequires(filename: str) -> list[str]:
    """Validate the ``BuildRequires`` fields of ``filename``.

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

    for i, line in enumerate(lines[:cut]):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        m = _RE_BUILDREQUIRES.match(stripped)
        if not m:
            continue
        value = m.group(1).strip()
        if not value:
            errors.append(
                f'{filename}: BuildRequires must list a build-time '
                f'dependency (found empty value)',
            )
            continue
        if not _is_single_dependency(value):
            shown = _truncate(value)
            errors.append(
                f'{filename}: BuildRequires must declare exactly one '
                f'dependency per line (found "{shown}")',
            )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_buildrequires(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
