from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_VERSION = re.compile(r'^Version\s*:\s*(\S+)')
_RE_PRERELEASE = re.compile(r'(alpha|beta|rc)(?=[0-9]|$)', re.IGNORECASE)
_RE_VCS_HASH = re.compile(r'^[0-9a-f]{40}$')
_RE_SNAPSHOT = re.compile(
    r'^[0-9]+(\.[0-9]+)*\+[a-z]+[0-9]{8}\.[0-9a-f]+$',
)


def _check_spec_version(filename: str) -> list[str]:
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
        return errors

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
