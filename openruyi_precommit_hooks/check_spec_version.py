from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``Version`` field of an openRuyi spec file must be normalized per
# the packaging guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines):
#
#   1. A version consisting only of digits and dots may be used as-is
#      (e.g. ``1.5.7``), and so may a dot-formatted date (e.g.
#      ``2025.07``).
#   2. Prerelease markers (``alpha`` / ``beta`` / ``rc``) must be
#      lowercased and prefixed with ``~`` (e.g. ``3.5.0-rc1`` ->
#      ``3.5.0~rc1``).
#   3. A hyphen in the version is replaced with a dot (e.g.
#      ``7.1.1-44`` -> ``7.1.1.44``).
#   4. An underscore in the version is replaced with a dot (e.g.
#      ``17_6`` -> ``17.6``).
#   5. A version based on a VCS commit hash must use the snapshot
#      format ``0+<scm><YYYYMMDD>.<hash7>`` when the upstream has never
#      released (e.g. ``0+git20250808.ee5b7e3``); when the upstream has
#      released before and only publishes snapshots afterwards, the
#      ``Version`` keeps the last released version and appends
#      ``+<scm><YYYYMMDD>.<revision>`` (e.g. ``4.3.1+git20260616.55a9409``).
#
# Version components may contain ASCII letters (per the supplemental
# spec), so a plain alphanumeric version such as ``5.02c`` is not
# flagged.  Versions that expand a macro (e.g. ``%{version}``) cannot
# be checked statically and are skipped.  Field presence is covered by
# ``check-spec-structure``, so a missing ``Version`` is not an error
# here.

_RE_VERSION = re.compile(r'^Version\s*:\s*(\S+)')
# A prerelease marker is only treated as such when it is followed by a
# digit or ends the version (e.g. ``1.6rc1``, ``0.99.beta20``); plain
# letters like the ``c`` in ``5.02c`` are allowed.
_RE_PRERELEASE = re.compile(r'(alpha|beta|rc)(?=[0-9]|$)', re.IGNORECASE)
_RE_VCS_HASH = re.compile(r'^[0-9a-f]{40}$')
# A (released-)version followed by a snapshot info
# ``+<scm><YYYYMMDD>.<revision>`` (e.g. ``0+git20250808.ee5b7e3`` or
# ``4.3.1+git20260616.55a9409``).
_RE_SNAPSHOT = re.compile(
    r'^[0-9]+(\.[0-9]+)*\+[a-z]+[0-9]{8}\.[0-9a-f]+$',
)


def _check_spec_version(filename: str) -> list[str]:
    """Validate the ``Version`` field of ``filename``.

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

    version = None
    for line in lines:
        m = _RE_VERSION.match(line.strip())
        if m:
            version = m.group(1)
            break
    if version is None:
        # Field presence is checked by ``check-spec-structure``.
        return errors

    # A macro-expanded version (e.g. ``%{version}``) cannot be checked
    # statically.
    if '%' in version:
        return errors

    if _RE_VCS_HASH.match(version):
        errors.append(
            f'{filename}: VCS commit hash versions should use the '
            f'snapshot format "0+<scm><YYYYMMDD>.<hash7>" '
            f'(found "{version}")',
        )
        return errors

    prerelease = _RE_PRERELEASE.search(version)
    if prerelease:
        idx = prerelease.start()
        prev = version[idx - 1] if idx > 0 else ''
        marker = prerelease.group(0)
        if prev != '~' or marker != marker.lower():
            errors.append(
                f'{filename}: prerelease marker should be lowercased '
                f'and prefixed with "~" (found "{version}")',
            )
    elif '-' in version:
        errors.append(
            f'{filename}: "-" in version should be replaced with "." '
            f'(found "{version}")',
        )
    if '_' in version:
        errors.append(
            f'{filename}: "_" in version should be replaced with "." '
            f'(found "{version}")',
        )
    if '+' in version and not _RE_SNAPSHOT.match(version):
        errors.append(
            f'{filename}: snapshot versions should end with '
            f'"+<scm><YYYYMMDD>.<revision>" after the released '
            f'version (found "{version}")',
        )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_version(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
