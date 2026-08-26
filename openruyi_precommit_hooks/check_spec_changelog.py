"""Ensure the ``%changelog`` section of an openRuyi spec file follows
the packaging guidelines
(https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#changelog):

   The content of the ``%changelog`` section must be ``%autochangelog``;
   handwritten changelog entries are not allowed.

Statically checkable rules in this hook, evaluated per ``%changelog``
section:

   * the section must contain the ``%autochangelog`` macro -- either the
     plain ``%autochangelog`` form or the conditional ``%{?autochangelog}``
     form is accepted;

   * the section must not contain any handwritten changelog entries
     (lines that are not comments and not the autochangelog macro).

A ``%changelog`` section that only contains comments (lines starting
with ``#``) or is empty is reported: the guidelines require the section
content to be ``%autochangelog`` and the ``%autochangelog`` macro
generates the changelog from VCS commit history, so an empty hand
maintained section cannot be right.
"""
from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# Section headers that end a ``%changelog`` block.  ``%changelog`` is
# traditionally the last section of a spec file, but a defensive list
# (mirroring the one in ``check_spec_files``) keeps the scan bounded if
# a spec places something after it.
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
# Both accepted forms of the autochangelog macro.
_RE_AUTOCHANGELOG = re.compile(r'^%\{(?:\?autochangelog|autochangelog)\}$')
_RE_AUTOCHANGELOG_PLAIN = re.compile(r'^%autochangelog\b')


def _check_spec_changelog(filename: str) -> list[str]:
    """Validate the ``%changelog`` section of ``filename``.

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

    n = len(lines)
    i = 0
    while i < n:
        stripped = lines[i].strip()
        if not _RE_CHANGELOG.match(stripped):
            i += 1
            continue
        header = stripped
        # ``%changelog`` may carry a subpackage selector such as
        # ``%changelog foo``; collect the body lines until the next
        # section.
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
