from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_RELEASE = re.compile(r'^Release\s*:\s*(\S+)')
_RE_NUM_PREFIX = re.compile(r'^[0-9]+')
_RE_DIST_OVERRIDE = re.compile(r'^\s*%(?:global|define)\s+dist\b')


def _check_spec_release(filename: str) -> list[str]:
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

    release = None
    for line in lines:
        m = _RE_RELEASE.match(line.strip())
        if m:
            release = m.group(1)
            break
    if release is None:
        return errors

    if '%autorelease' in release or '%{autorelease}' in release:
        pass
    elif '%' in release:
        m = _RE_NUM_PREFIX.match(release)
        if m:
            num = m.group(0)
            rest = release[m.end():]
            if num == '0':
                errors.append(
                    f'{filename}: Release revision must start at 1 '
                    f'(found "{release}")',
                )
            elif rest and not rest.startswith('%'):
                errors.append(
                    f'{filename}: Release must not hardcode a dist '
                    f'suffix (found "{release}")',
                )
    else:
        m = _RE_NUM_PREFIX.match(release)
        if m is None:
            errors.append(
                f'{filename}: Release must be a plain integer starting '
                f'at 1 (found "{release}")',
            )
        elif m.group(0) == '0':
            errors.append(
                f'{filename}: Release revision must start at 1 '
                f'(found "{release}")',
            )
        elif release[m.end():]:
            errors.append(
                f'{filename}: Release must not hardcode a dist suffix '
                f'(found "{release}")',
            )
        else:
            errors.append(
                f'{filename}: Release should use "%autorelease" '
                f'instead of a fixed revision (found "{release}")',
            )

    for line in lines:
        if _RE_DIST_OVERRIDE.match(line):
            errors.append(
                f'{filename}: the "dist" macro must not be '
                f'overridden ({line.strip()})',
            )
            break
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_release(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
