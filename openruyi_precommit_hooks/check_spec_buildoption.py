from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``BuildOption`` field of an openRuyi spec file must follow the
# packaging guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#buildoption-%E5%8F%AF%E9%80%89)
# and the declarative build systems supplement
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems):
#
#   1. When extra arguments are needed for a specific build stage, a
#      spec may use the ``BuildOption(<stage>):`` field.
#   2. ``BuildOption(<stage>):`` must be separated from its arguments by
#      two spaces.
#   3. Multiple arguments must be declared one per line.
#   4. When ``BuildOption`` is used, it should be located between
#      ``BuildSystem`` and ``BuildRequires``.
#   5. The ``BuildOption`` lines should be written in the same order as
#      the RPM build process, i.e. ``%build``, ``%install``, ``%check``.
#
# The supplement adds:
#   * the tag may appear any number of times for each section;
#   * although the build stage name may be omitted syntactically, the
#     packager is required to write it.
#
# ``BuildOption`` is an optional field.  Statically checkable rules in
# this hook:
#   * a ``BuildOption`` line must carry a stage name (``BuildOption``
#     without ``(<stage>)`` is reported);
#   * ``BuildOption(<stage>):`` must be separated from its arguments by
#     two spaces;
#   * the ``BuildOption`` lines should be located between ``BuildSystem``
#     and ``BuildRequires`` (when both anchors are present);
#   * the ``BuildOption`` lines should be written in the order
#     ``build`` -> ``install`` -> ``check`` (only the relative order of
#     these three stages is judged; other stages such as ``conf``,
#     ``prep`` or ``generate_buildrequires`` are ignored).
#
# Field presence is covered by ``check-spec-structure`` (``BuildOption``
# is optional, so a missing field is not an error here).  Whether the
# arguments are really needed for a stage cannot be judged statically.

_RE_BUILDOPTION = re.compile(r'^BuildOption\s*\(([^)]*)\)\s*:(.*)')
# A ``BuildOption`` line without a stage name (the stage name may be
# omitted syntactically but the packager is required to write it).
_RE_BUILDOPTION_NO_STAGE = re.compile(r'^BuildOption\s*:\s*(.*)')
_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:')
_RE_BUILDREQUIRES = re.compile(r'^BuildRequires\s*:')
# The stages whose relative order must follow the RPM build process.
_ORDERED_STAGES = ('build', 'install', 'check')
# Avoid echoing a very long value verbatim in an error message.
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _check_spec_buildoption(filename: str) -> list[str]:
    """Validate the ``BuildOption`` fields of ``filename``.

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

    # Only the header region is inspected: ``BuildOption`` inside a
    # ``%package`` subpackage block is a different field and is not
    # covered by this rule.
    cut = len(lines)
    for i, line in enumerate(lines):
        if re.match(r'^%(?:description|package)\b', line.strip()):
            cut = i
            break

    buildoption_idx = -1
    buildsystem_idx = -1
    buildrequires_idx = -1
    stages: list[str] = []
    for i, line in enumerate(lines[:cut]):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        m = _RE_BUILDOPTION.match(stripped)
        if m:
            if buildoption_idx == -1:
                buildoption_idx = i
            stage = m.group(1).strip()
            value = m.group(2)
            if not stage:
                errors.append(
                    f'{filename}: BuildOption must carry a build stage '
                    f'name (found "BuildOption: ..." without '
                    f'"(<stage>)")',
                )
            # ``BuildOption(<stage>):`` must be separated from its
            # arguments by two spaces.  An empty value is allowed.
            if value and not value.startswith('  '):
                shown = _truncate(value.strip())
                errors.append(
                    f'{filename}: BuildOption({stage}) must be separated '
                    f'from its arguments by two spaces (found '
                    f'"{shown}")',
                )
            stages.append(stage)
        elif _RE_BUILDOPTION_NO_STAGE.match(stripped):
            if buildoption_idx == -1:
                buildoption_idx = i
            errors.append(
                f'{filename}: BuildOption must carry a build stage name '
                f'(found "BuildOption: ..." without "(<stage>)")',
            )
        elif _RE_BUILDSYSTEM.match(stripped):
            if buildsystem_idx == -1:
                buildsystem_idx = i
        elif _RE_BUILDREQUIRES.match(stripped):
            if buildrequires_idx == -1:
                buildrequires_idx = i

    if buildoption_idx == -1:
        # ``BuildOption`` is optional; field presence is covered by
        # ``check-spec-structure``.
        return errors

    # Position check: ``BuildOption`` should be located between
    # ``BuildSystem`` and ``BuildRequires``.  When one of the two
    # anchors is missing the position cannot be judged.
    if buildsystem_idx != -1 and buildrequires_idx != -1:
        if not (buildsystem_idx < buildoption_idx < buildrequires_idx):
            errors.append(
                f'{filename}: BuildOption must be located between '
                f'BuildSystem and BuildRequires',
            )

    # Order check: the ``BuildOption`` lines should be written in the
    # order ``build`` -> ``install`` -> ``check``.  Only the relative
    # order of these three stages is judged; other stages are ignored.
    ordered = [s for s in stages if s in _ORDERED_STAGES]
    seen: list[str] = []
    for s in ordered:
        if s not in seen:
            seen.append(s)
    if len(seen) > 1:
        it = iter(_ORDERED_STAGES)
        if not all(any(s == y for y in it) for s in seen):
            errors.append(
                f'{filename}: BuildOption stages should be written in '
                f'the order build, install, check (found '
                f'{", ".join(seen)})',
            )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_buildoption(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
