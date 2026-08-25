from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``VCS`` field of an openRuyi spec file must follow the packaging
# guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#vcs):
#
#   1. ``VCS`` should be a source repository link used to locate the
#      source code.
#   2. When ``URL`` is already a source repository link, ``VCS`` may be
#      omitted.
#   3. When no usable source repository link exists, the following
#      comment must be written at the ``VCS`` field position (the
#      ``# VCS:`` prefix must be kept):
#
#          # VCS: No VCS link available
#
#   4. When the source is hosted in a Git repository, ``VCS`` should be
#      a cloneable link, e.g.:
#
#          VCS:            git:https://git.example.org/project.git
#
# Statically checkable rules in this hook:
#   * a ``VCS:`` field must be a cloneable source repository link
#     (``git:`` scheme, or a plain ``http(s)://`` link to a well-known
#     source-code hosting platform);
#   * a ``# VCS: No VCS link available`` comment is accepted in place of
#     a real link;
#   * a ``# VCS:`` comment with any other text is not a valid
#     declaration and is reported.
#
# Field presence is covered by ``check-spec-structure`` (which also
# allows ``VCS`` to be omitted when ``URL`` already points at a source
# repository).  Whether a link is really the canonical upstream
# repository cannot be judged statically.

_RE_VCS = re.compile(r'^#?\s*VCS\s*:\s*(.*)')
# ``%{name}``, ``%{srcname}`` ... -- any macro reference.
_RE_MACRO = re.compile(r'%\{[^}]*\}')
# A cloneable link uses the ``git:`` scheme or is an http(s) link.
_RE_GIT_SCHEME = re.compile(r'^git:', re.IGNORECASE)
_RE_HTTP_SCHEME = re.compile(r'^https?://', re.IGNORECASE)
# The exact comment that must be used when no VCS link is available.
_NO_VCS_COMMENT = 'No VCS link available'
# Well-known source-code hosting platforms.  A plain http(s) link to one
# of these is treated as a source repository link.
_SOURCE_REPO_HOSTS = frozenset({
    'github.com',
    'gitlab.com',
    'codeberg.org',
    'bitbucket.org',
    'hg.sr.ht',
    'invent.kde.org',
    'salsa.debian.org',
    'pagure.io',
    'code.videolan.org',
    'src.fedoraproject.org',
})
# Avoid echoing a very long value verbatim in an error message.
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _is_source_repo_link(value: str) -> bool:
    """Return True if ``value`` looks like a source repository link.

    A link is treated as a source repository when it uses the ``git:``
    scheme, or is an http(s) link hosted on a well-known source-code
    hosting platform (``github.com``, ``gitlab.*``, ``git.*``,
    ``codeberg.org``, …).
    """
    value = value.strip()
    if _RE_GIT_SCHEME.match(value):
        return True
    m = _RE_HTTP_SCHEME.match(value)
    if not m:
        return False
    host_match = re.match(r'^https?://([^/\s]+)', value, re.IGNORECASE)
    if not host_match:
        return False
    host = host_match.group(1).lower()
    if host in _SOURCE_REPO_HOSTS:
        return True
    if host.startswith('gitlab.') or host.startswith('git.'):
        return True
    return False


def _check_spec_vcs(filename: str) -> list[str]:
    """Validate the ``VCS`` field of ``filename``.

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

    vcs_value = None
    vcs_is_comment = False
    for line in lines:
        stripped = line.strip()
        m = _RE_VCS.match(stripped)
        if not m:
            continue
        if stripped.startswith('#'):
            # A commented-out ``# VCS:`` line is only meaningful when it
            # carries the exact "No VCS link available" text.
            vcs_value = m.group(1).strip()
            vcs_is_comment = True
        else:
            vcs_value = m.group(1).strip()
            vcs_is_comment = False
        break

    if vcs_value is None:
        # Field presence is checked by ``check-spec-structure``.
        return errors

    if vcs_is_comment:
        if vcs_value == _NO_VCS_COMMENT:
            return errors
        shown = _truncate(vcs_value)
        errors.append(
            f'{filename}: VCS comment must be exactly '
            f'"# VCS: {_NO_VCS_COMMENT}" (found "# VCS: {shown}")',
        )
        return errors

    if not vcs_value:
        # An empty ``VCS:`` value is not a usable declaration.
        errors.append(
            f'{filename}: VCS must be a source repository link or the '
            f'comment "# VCS: {_NO_VCS_COMMENT}" (found empty value)',
        )
        return errors

    shown = _truncate(vcs_value)
    if _RE_MACRO.search(vcs_value):
        errors.append(
            f'{filename}: VCS must not be built with macros such as '
            f'%{{name}} (found "{shown}")',
        )
    if not _is_source_repo_link(vcs_value):
        errors.append(
            f'{filename}: VCS must be a cloneable source repository link '
            f'(git: scheme or http(s) link to a source-code hosting '
            f'platform) (found "{shown}")',
        )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_vcs(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
