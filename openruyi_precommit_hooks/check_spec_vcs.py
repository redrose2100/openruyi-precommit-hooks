from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_VCS = re.compile(r'^#?\s*VCS\s*:\s*(.*)')
_RE_MACRO = re.compile(r'%\{[^}]*\}')
_RE_GIT_SCHEME = re.compile(r'^git:', re.IGNORECASE)
_RE_HTTP_SCHEME = re.compile(r'^https?://', re.IGNORECASE)
_NO_VCS_COMMENT = 'No VCS link available'
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
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _is_source_repo_link(value: str) -> bool:
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
            vcs_value = m.group(1).strip()
            vcs_is_comment = True
        else:
            vcs_value = m.group(1).strip()
            vcs_is_comment = False
        break

    if vcs_value is None:
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
