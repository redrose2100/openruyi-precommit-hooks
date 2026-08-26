"""Ensure the ``%files`` sections of an openRuyi spec file follow the
packaging guidelines
(https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#files):

   1. License text files must be marked with ``%license``; documentation
      files should be marked with ``%doc``.
   2. The ``%files`` list must not repeat the same file (except in the
      specific situations explicitly allowed).
   3. Packages must not contain ``.la`` (libtool archive) files; if the
      build produces them, the spec must remove them.
   4. Localized files must be handled in the ``%install`` section with
      the ``%find_lang`` mechanism; ``%files`` must not wildcard
      ``%{_datadir}/locale/*`` directly.

Statically checkable rules in this hook, evaluated per ``%files``
section:

   * license text tokens (``LICENSE``/``COPYING``/``LICENCE`` and
     variants, case-insensitive) listed under ``%doc`` or as bare file
     names must be marked with ``%license``;
   * documentation tokens (``README``/``NEWS``/``AUTHORS``/
     ``CHANGELOG``/``CHANGES``/``HISTORY``) listed as bare file names
     should be marked with ``%doc``;
   * the same plain file path must not be listed more than once in the
     same section (top level, outside conditional blocks);
   * ``.la`` files must not be listed (``%exclude`` entries are
     exclusions, not package contents, and are skipped);
   * ``%{_datadir}/locale/*`` wildcards must not be used.

Whether a translated file really comes from ``%find_lang`` during the
build cannot be judged statically; the hook reports the wildcard itself.
"""
from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# Section headers that end a ``%files`` block.
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
# Conditional block markers; entries inside are skipped by the
# duplicate check.
_CONDITIONALS = frozenset((
    'if',
    'ifarch',
    'ifnarch',
    'ifos',
    'ifnos',
    'else',
    'endif',
))
# File directives stripped from a line; ``doc``/``license``/``dir``/
# ``ghost`` alter the meaning of the path that follows them.
_FILE_DIRECTIVES = frozenset((
    'doc',
    'license',
    'config',
    'attr',
    'dir',
    'ghost',
    'verify',
    'lang',
    'exclude',
    'defattr',
    'caps',
    'artifact',
    'pubdate',
    'mark',
    'json',
    'yaml',
    'templatetag',
    'macro',
    'fileslist',
    'filesmultiline',
))

_RE_FILES = re.compile(r'^%files\b')
_RE_SECTION = re.compile(r'^%(\w+)')
# A complete directive token: ``%doc`` or ``%config(noreplace)``.
_RE_CMD_PAREN = re.compile(r'^%([a-z]+)\(([^)]*)\)$', re.I)
_RE_CMD_BARE = re.compile(r'^%([a-z]+)$', re.I)
# An unterminated directive argument spanning several tokens, e.g. the
# remainder of ``%verify(not md5 size mtime)`` or ``%attr(0750, ...)``.
_RE_CMD_OPEN = re.compile(r'^%([a-z]+)\([^)]*$', re.I)
_RE_LANG = re.compile(r'^%lang\([^)]*\)$')
# Pure parentheses fragments (directive arguments, possibly split on
# spaces): ``(noreplace)``, ``(0750, `` ...
_RE_PAREN_FRAGMENT = re.compile(r'^[^%]*(?:\(|\))[^%]*$')
# License text file tokens (with optional extension / glob).
_RE_LICENSE_TOKEN = re.compile(
    r'^(license|licence|copying)(\.[a-z0-9]+)?(\*)?$',
    re.I,
)
# Documentation file tokens (with optional extension / glob).
_RE_DOC_TOKEN = re.compile(
    r'^(readme|news|authors|changelog|changes|history)(\.[a-z0-9]+)?(\*)?$',
    re.I,
)
# The forbidden locale wildcard: ``%{_datadir}/locale/*``.
_RE_LOCALE_GLOB = re.compile(r'^%\{_datadir\}/locale/\*')


def _tokenize_file_line(line: str) -> list[tuple[frozenset[str], str]]:
    """Split a ``%files`` line into ``(kinds, path)`` pairs.

    ``kinds`` is the set of file directives accumulated before a path
    (``doc``/``license``/``dir``/``ghost``); the empty set means a bare
    file entry.  Directive arguments (``%attr(...)``, ``%verify(...)``,
    ``%caps(...)``, ``(noreplace)`` ...) are stripped.
    """
    out: list[tuple[frozenset[str], str]] = []
    kinds: set[str] = set()
    tokens = line.split()
    j = 0
    while j < len(tokens):
        tok = tokens[j]
        # Absorb an unterminated directive argument until its closing
        # parenthesis appears (e.g. ``%verify(not md5 size mtime)``).
        if _RE_CMD_OPEN.match(tok):
            buf = tok
            j += 1
            while j < len(tokens) and ')' not in tokens[j]:
                buf += ' ' + tokens[j]
                j += 1
            if j < len(tokens):
                buf += ' ' + tokens[j]
                j += 1
            m = re.match(r'^%([a-z]+)\(', buf, re.I)
            if m is not None and m.group(1).lower() in _FILE_DIRECTIVES:
                name = m.group(1).lower()
                if name in ('doc', 'license', 'dir', 'ghost'):
                    kinds.add(name)
            continue
        if tok.startswith('%{'):
            # A macro path such as ``%{_bindir}/file``; treat as a path.
            out.append((frozenset(kinds), tok))
        elif _RE_LANG.match(tok):
            pass
        elif _RE_PAREN_FRAGMENT.match(tok):
            pass
        else:
            m = _RE_CMD_PAREN.match(tok) or _RE_CMD_BARE.match(tok)
            if m is not None:
                name = m.group(1).lower()
                if name in _FILE_DIRECTIVES:
                    if name in ('doc', 'license', 'dir', 'ghost'):
                        kinds.add(name)
            else:
                out.append((frozenset(kinds), tok))
        j += 1
    return out


def _check_spec_files(filename: str) -> list[str]:
    """Validate the ``%files`` sections of ``filename``.

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
        if not _RE_FILES.match(stripped):
            i += 1
            continue
        header = stripped
        # (kinds, path, conditional depth) collected for the section.
        entries: list[tuple[frozenset[str], str, int]] = []
        cond_depth = 0
        i += 1
        while i < n:
            line = lines[i].strip()
            sm = _RE_SECTION.match(line)
            if sm is not None:
                name = sm.group(1)
                if name in _CONDITIONALS:
                    if line.startswith('%endif'):
                        cond_depth = max(0, cond_depth - 1)
                    elif not line.startswith('%else'):
                        cond_depth += 1
                    i += 1
                    continue
                if name in _SECTION_END:
                    break
            if not line or line.startswith('#'):
                i += 1
                continue
            if line == '}}':
                i += 1
                continue
            if line.startswith('%{expand:'):
                # ``%{expand: ... }}`` macro body; skip to the closing
                # ``}}`` line.
                i += 1
                while i < n and lines[i].strip() != '}}':
                    i += 1
                i += 1
                continue
            if line.startswith('%{!'):
                # Macro guard line such as
                # ``%{!?_licensedir:%global license %%doc}``.
                i += 1
                continue
            if re.match(r'^%(defattr|exclude|verify)\b', line, re.I):
                # ``%defattr``/``%exclude``/``%verify`` standalone lines
                # carry no package file entries.
                i += 1
                continue
            for kinds, path in _tokenize_file_line(line):
                entries.append((kinds, path, cond_depth))
            i += 1

        for kinds, path, _cd in entries:
            # Checkpoint 3: no ``.la`` (libtool archive) files.
            if path.endswith('.la') or re.search(r'\.la\.', path):
                errors.append(
                    f'{filename}: %files must not contain libtool '
                    f'archive ".la" files (found "{path}")',
                )
                continue
            # Checkpoint 4: no ``%{_datadir}/locale/*`` wildcards.
            if _RE_LOCALE_GLOB.match(path):
                errors.append(
                    f'{filename}: localized files must be handled with '
                    f'%find_lang in the %install section, not wildcarded '
                    f'as %{{_datadir}}/locale/* (found "{path}")',
                )
                continue
            base = path.split('/')[-1]
            # Checkpoint 1: license text files must use ``%license``.
            if _RE_LICENSE_TOKEN.match(base):
                if 'license' not in kinds:
                    if 'doc' in kinds:
                        errors.append(
                            f'{filename}: license file "{path}" in '
                            f'{header} must be marked with %license '
                            f'(found in %doc)',
                        )
                    elif (
                        'dir' not in kinds and
                        'ghost' not in kinds and
                        '/' not in path and
                        not path.startswith('%')
                    ):
                        errors.append(
                            f'{filename}: license file "{path}" in '
                            f'{header} must be marked with %license',
                        )
                continue
            # Checkpoint 2: documentation files should use ``%doc``.
            if _RE_DOC_TOKEN.match(base):
                if (
                    'doc' not in kinds and
                    'license' not in kinds and
                    'dir' not in kinds and
                    'ghost' not in kinds and
                    '/' not in path and
                    not path.startswith('%')
                ):
                    errors.append(
                        f'{filename}: documentation file "{path}" in '
                        f'{header} should be marked with %doc',
                    )

        # Checkpoint 2: the same plain file must not be listed twice at
        # the top level (outside conditional blocks).  ``%doc``/
        # ``%license`` entries install to their own directories and are
        # not duplicates; macro paths cannot be compared reliably.
        counted: dict[str, int] = {}
        dups: list[str] = []
        for kinds, path, cd in entries:
            if cd != 0:
                continue
            if (
                'dir' in kinds or 'ghost' in kinds or
                'doc' in kinds or 'license' in kinds
            ):
                continue
            if '*' in path or '?' in path:
                continue
            if path.startswith('%{'):
                continue
            counted[path] = counted.get(path, 0) + 1
            if counted[path] == 2:
                dups.append(path)
        for path in sorted(dups):
            errors.append(
                f'{filename}: %files must not list the same file twice '
                f'(found "{path}" {counted[path]} times in {header})',
            )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_files(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
