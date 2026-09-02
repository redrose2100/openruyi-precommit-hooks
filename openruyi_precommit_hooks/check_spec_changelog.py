from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

_SECTION_END = frozenset((
    'changelog',
    'package',
    'prep',
    'build',
    'install',
    'check',
    'description',
    'pre',
    'post',
    'preun',
    'postun',
    'pretrans',
    'posttrans',
    'verifyscript',
    'triggerin',
    'triggerun',
    'triggerpostun',
    'triggerprein',
    'files',
))

_RE_CHANGELOG = re.compile(r'^%changelog\b')
_RE_SECTION = re.compile(r'^%(\w+)')
_RE_AUTOCHANGELOG = re.compile(r'^%\{(?:\?autochangelog|autochangelog)\}$')
_RE_AUTOCHANGELOG_PLAIN = re.compile(r'^%autochangelog\b')


def _check_spec_changelog(filename: str) -> list[str]:
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

    n = len(lines)
    i = 0
    while i < n:
        stripped = lines[i].strip()
        if not _RE_CHANGELOG.match(stripped):
            i += 1
            continue
        header = stripped
        body: list[str] = []
        i += 1
        while i < n:
            line = lines[i].strip()
            sm = _RE_SECTION.match(line)
            if sm is not None and sm.group(1) in _SECTION_END:
                break
            body.append(line)
            i += 1

        content = [line for line in body if line and not line.startswith('#')]
        has_autochangelog = any(
            _RE_AUTOCHANGELOG.match(line) or
            _RE_AUTOCHANGELOG_PLAIN.match(line)
            for line in content
        )
        handwritten = [
            line for line in content
            if not _RE_AUTOCHANGELOG.match(line) and
            not _RE_AUTOCHANGELOG_PLAIN.match(line)
        ]
        if handwritten:
            errors.append(
                f'{filename}: {header} must use %autochangelog '
                f'instead of handwritten changelog entries '
                f'(found "{handwritten[0]}")',
            )
        elif not has_autochangelog:
            errors.append(
                f'{filename}: {header} must use %autochangelog '
                f'(empty or comment-only section)',
            )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_changelog(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
