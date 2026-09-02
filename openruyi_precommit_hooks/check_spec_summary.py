from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_SUMMARY = re.compile(r'^Summary\s*:\s*(.*)')
_RE_NON_ENGLISH = re.compile(
    r'[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af'
    r'\uff00-\uffef\u3000-\u303f]',
)
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _check_spec_summary(filename: str) -> list[str]:
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

    summary = None
    for line in lines:
        m = _RE_SUMMARY.match(line.strip())
        if m:
            summary = m.group(1).strip()
            break
    if summary is None or not summary:
        return errors

    if '%' in summary:
        return errors

    shown = _truncate(summary)
    if _RE_NON_ENGLISH.search(summary):
        errors.append(
            f'{filename}: Summary should contain only English text '
            f'(found "{shown}")',
        )
    if summary.endswith('.'):
        errors.append(
            f'{filename}: Summary must not end with a period '
            f'(found "{shown}")',
        )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_summary(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
