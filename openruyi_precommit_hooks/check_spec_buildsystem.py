from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``BuildSystem`` field of an openRuyi spec file must follow the
# packaging guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#buildsystem):
#
#   1. A spec must contain a ``BuildSystem`` field.
#   2. The ``BuildSystem`` value should be one of the following (or
#      another newly added value):
#
#          autotools
#          cmake
#          meson
#          golang
#          golangmodules
#          pyproject
#
#   3. When a package does not fit any of the above types or does not
#      need a configuration stage, ``BuildSystem`` may be empty, but
#      the reason must be explained in a comment.
#
# Field presence is covered by ``check-spec-structure`` (``BuildSystem``
# is a mandatory header field there), so a missing field is not reported
# here.  Statically checkable rules in this hook:
#   * a ``BuildSystem:`` field must not be empty unless the reason is
#     explained in a comment;
#   * the value must be a known build system (the ones listed in the
#     guidelines plus the additional values used by the openRuyi
#     repository).  An unknown value is reported so that a maintainer
#     can confirm whether it is a newly added build system.
#
# Whether a package really needs a configuration stage cannot be judged
# statically.

# The build systems listed in the packaging guidelines.
_GUIDELINE_BUILD_SYSTEMS = frozenset({
    'autotools',
    'cmake',
    'meson',
    'golang',
    'golangmodules',
    'pyproject',
})

# Additional build systems used by the openRuyi repository (the
# guidelines allow "other newly added values").
_REPO_BUILD_SYSTEMS = frozenset({
    'perlbuild',
    'perlmaker',
    'rust',
    'rustcrates',
})

_KNOWN_BUILD_SYSTEMS = _GUIDELINE_BUILD_SYSTEMS | _REPO_BUILD_SYSTEMS

_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:\s*(.*)')
# A comment that explains why ``BuildSystem`` is empty.  The comment
# must appear on the ``BuildSystem:`` line itself or on the line
# directly above it.
_RE_COMMENT = re.compile(r'^\s*#')
# Avoid echoing a very long value verbatim in an error message.
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _check_spec_buildsystem(filename: str) -> list[str]:
    """Validate the ``BuildSystem`` field of ``filename``.

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

    # Only the header region is inspected: ``BuildSystem`` inside a
    # ``%package`` subpackage block is a different field and is not
    # covered by this rule.
    cut = len(lines)
    for i, line in enumerate(lines):
        if re.match(r'^%(?:description|package)\b', line.strip()):
            cut = i
            break

    buildsystem_value = None
    buildsystem_idx = -1
    for i, line in enumerate(lines[:cut]):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        m = _RE_BUILDSYSTEM.match(stripped)
        if m:
            if buildsystem_idx == -1:
                buildsystem_idx = i
                buildsystem_value = m.group(1).strip()
            break

    if buildsystem_value is None:
        # ``BuildSystem`` is a mandatory header field; presence is
        # covered by ``check-spec-structure``.
        return errors

    if not buildsystem_value or buildsystem_value.startswith('#'):
        # An empty ``BuildSystem`` is allowed only when the reason is
        # explained in a comment (on the same line or the line above).
        if buildsystem_value.startswith('#'):
            return errors
        if (
            buildsystem_idx > 0 and
            _RE_COMMENT.match(lines[buildsystem_idx - 1])
        ):
            return errors
        errors.append(
            f'{filename}: BuildSystem is empty; the reason must be '
            f'explained in a comment',
        )
        return errors

    if buildsystem_value not in _KNOWN_BUILD_SYSTEMS:
        shown = _truncate(buildsystem_value)
        errors.append(
            f'{filename}: BuildSystem must be one of the known build '
            f'systems ({", ".join(sorted(_KNOWN_BUILD_SYSTEMS))}) or a '
            f'newly added value (found "{shown}")',
        )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_buildsystem(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
