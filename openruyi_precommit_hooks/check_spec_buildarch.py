from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_BUILDARCH = re.compile(r'^BuildArch\s*:\s*(.*)')
_RE_SOURCE = re.compile(r'^Source\d*\s*:')
_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:')
_NOARCH = 'noarch'
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _check_spec_buildarch(filename: str) -> list[str]:
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

    cut = len(lines)
    for i, line in enumerate(lines):
        if re.match(r'^%(?:description|package)\b', line.strip()):
            cut = i
            break

    buildarch_value = None
    buildarch_idx = -1
    last_source_idx = -1
    buildsystem_idx = -1
    for i, line in enumerate(lines[:cut]):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        m = _RE_BUILDARCH.match(stripped)
        if m:
            if buildarch_idx == -1:
                buildarch_idx = i
                buildarch_value = m.group(1).strip()
        elif _RE_SOURCE.match(stripped):
            last_source_idx = i
        elif _RE_BUILDSYSTEM.match(stripped):
            if buildsystem_idx == -1:
                buildsystem_idx = i

    if buildarch_value is None:
        return errors

    if not buildarch_value:
        errors.append(
            f'{filename}: BuildArch must declare a target architecture '
            f'(found empty value)',
        )
        return errors

    shown = _truncate(buildarch_value)
    if buildarch_value != _NOARCH:
        errors.append(
            f'{filename}: BuildArch must be "{_NOARCH}" (the only '
            f'architecture value used by the openRuyi repository) '
            f'(found "{shown}")',
        )

    if last_source_idx != -1 and buildsystem_idx != -1:
        if not (last_source_idx < buildarch_idx < buildsystem_idx):
            errors.append(
                f'{filename}: BuildArch must be located between the last '
                f'Source field and the BuildSystem field',
            )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_buildarch(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
