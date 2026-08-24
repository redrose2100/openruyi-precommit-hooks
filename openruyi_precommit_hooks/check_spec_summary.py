from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``Summary`` field of an openRuyi spec file must follow the
# packaging guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines):
#
#   1. ``Summary`` must be a short description of what the package
#      does.
#   2. ``Summary`` should contain only the necessary English
#      introduction.
#   3. ``Summary`` must not end with an English period (``.``).
#
# Statically checkable rules in this hook:
#   * a literal value ending in ``.`` (after stripping whitespace)
#     violates rule 3;
#   * a value containing CJK or full-width characters (Han, Kana,
#     Hangul, full-width forms, CJK punctuation) is not an English
#     introduction and violates rule 2.  Decorative symbols such as
#     en-dashes or emoji are not flagged to avoid false positives.
#
# Rule 1 ("short description") is qualitative and cannot be checked
# on a single file.  Macro-expanded values (e.g. ``%{name} library``)
# are skipped, and a missing ``Summary`` is covered by
# ``check-spec-structure``.

_RE_SUMMARY = re.compile(r'^Summary\s*:\s*(.*)')
# Han ideographs, Kana, Hangul, full-width forms and CJK punctuation --
# clearly not an English introduction.
_RE_NON_ENGLISH = re.compile(
    r'[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af'
    r'\uff00-\uffef\u3000-\u303f]',
)
# Avoid echoing a very long Summary verbatim in an error message.
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _check_spec_summary(filename: str) -> list[str]:
    """Validate the ``Summary`` field of ``filename``.

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

    summary = None
    for line in lines:
        m = _RE_SUMMARY.match(line.strip())
        if m:
            summary = m.group(1).strip()
            break
    if summary is None or not summary:
        # Field presence is checked by ``check-spec-structure``.
        return errors

    # A macro-expanded summary (e.g. ``%{name} library``) cannot be
    # judged statically.
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
