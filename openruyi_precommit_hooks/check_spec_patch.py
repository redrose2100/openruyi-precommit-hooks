from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``Patch`` and ``%patchlist`` fields of an openRuyi spec file must
# follow the packaging guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#patch-and-patchlist-%E5%8F%AF%E9%80%89):
#
#   1. Every patch referenced by a spec must have at least one comment
#      line above it explaining its purpose or giving an upstream link
#      (unless the purpose is already explained inside the patch).
#   2. Patch file names must start with a four digit number, and the
#      number range expresses the patch type:
#
#          0001-0999: upstream patches for the same version
#          1000-1999: CVE fixes or cross-version backports
#          2000-2999: openRuyi specific patches (not expected upstream)
#
#   3. When there are more than 3 patches, the spec should use
#      ``%patchlist``, and the list must be placed above
#      ``%description``.
#   4. Patch placement:
#        * when the spec has a ``BuildOption`` field, patches should be
#          located between ``BuildSystem`` and ``BuildOption``;
#        * when the spec has no ``BuildOption`` field, patches should be
#          located between ``BuildSystem`` and ``BuildRequires``.
#
# ``Patch`` and ``%patchlist`` are optional fields.  Statically
# checkable rules in this hook:
#   * every ``Patch:`` field must have a comment line directly above it;
#   * every ``%patchlist`` entry must have a comment line directly above
#     it;
#   * patch file names must start with a four digit number in one of the
#     documented ranges (0001-0999, 1000-1999, 2000-2999);
#   * when a spec has more than 3 patches it should use ``%patchlist``;
#   * ``%patchlist`` must be placed above ``%description``;
#   * ``Patch`` fields should be located between ``BuildSystem`` and
#     ``BuildOption`` (when present) or between ``BuildSystem`` and
#     ``BuildRequires`` (when ``BuildOption`` is absent).
#
# Whether a patch's purpose is really explained inside the patch file
# cannot be judged statically.

_RE_PATCH = re.compile(r'^Patch(\d*)\s*:\s*(.*)')
_RE_PATCHLIST = re.compile(r'^%patchlist\b')
_RE_COMMENT = re.compile(r'^\s*#')
_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:')
_RE_BUILDOPTION = re.compile(r'^BuildOption\s*\(')
_RE_BUILDREQUIRES = re.compile(r'^BuildRequires\s*:')
_RE_SECTION = re.compile(
    r'^%(?:description|package|prep|build|install|check|files|changelog)\b'
)
# A patch file name must start with a four digit number in one of the
# documented ranges.
_RE_PATCH_NAME = re.compile(r'^(\d{4})')
# The documented four digit prefix ranges.
_PREFIX_RANGES = ('0001-0999', '1000-1999', '2000-2999')
# Avoid echoing a very long value verbatim in an error message.
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _check_spec_patch(filename: str) -> list[str]:
    """Validate the ``Patch`` / ``%patchlist`` usage of ``filename``.

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

    # Only the header region is inspected: ``Patch`` / ``%patchlist``
    # inside a ``%package`` subpackage block is a different context and
    # is not covered by this rule.
    cut = len(lines)
    for i, line in enumerate(lines):
        if _RE_SECTION.match(line.strip()):
            cut = i
            break

    header = lines[:cut]

    # Collect ``Patch:`` fields and ``%patchlist`` blocks.
    patches: list[tuple[int, str]] = []  # (line_idx, patch file name)
    patchlist_idx = -1
    patchlist_entries: list[tuple[int, str]] = []  # (line_idx, name)
    in_patchlist = False
    for i, line in enumerate(header):
        stripped = line.strip()
        if not stripped:
            continue
        if _RE_PATCHLIST.match(stripped):
            patchlist_idx = i
            in_patchlist = True
            continue
        if in_patchlist:
            if stripped.startswith('%'):
                in_patchlist = False
            elif not stripped.startswith('#'):
                patchlist_entries.append((i, stripped))
            continue
        m = _RE_PATCH.match(stripped)
        if m:
            patches.append((i, m.group(2).strip()))

    # Checkpoint 1: every ``Patch:`` field must have a comment line
    # directly above it.
    for idx, name in patches:
        if idx > 0 and _RE_COMMENT.match(lines[idx - 1]):
            continue
        shown = _truncate(name)
        errors.append(
            f'{filename}: Patch "{shown}" must have a comment line above '
            f'it explaining its purpose or giving an upstream link',
        )

    # Checkpoint 1 (patchlist): every ``%patchlist`` entry must have a
    # comment line directly above it.
    for idx, name in patchlist_entries:
        if idx > 0 and _RE_COMMENT.match(lines[idx - 1]):
            continue
        shown = _truncate(name)
        errors.append(
            f'{filename}: patch "{shown}" in %patchlist must have a '
            f'comment line above it explaining its purpose or giving an '
            f'upstream link',
        )

    # Checkpoint 2: patch file names must start with a four digit number
    # in one of the documented ranges.
    all_names = [
        name for _, name in patches
    ] + [name for _, name in patchlist_entries]
    for name in all_names:
        m = _RE_PATCH_NAME.match(name)
        if not m:
            shown = _truncate(name)
            errors.append(
                f'{filename}: patch file name "{shown}" must start with '
                f'a four digit number ({", ".join(_PREFIX_RANGES)})',
            )
            continue
        prefix = int(m.group(1))
        if not (1 <= prefix <= 2999):
            shown = _truncate(name)
            errors.append(
                f'{filename}: patch file name "{shown}" must start with '
                f'a four digit number in one of the ranges '
                f'({", ".join(_PREFIX_RANGES)})',
            )

    # Checkpoint 3: when there are more than 3 patches the spec should
    # use ``%patchlist``.
    if len(patches) > 3 and patchlist_idx == -1:
        errors.append(
            f'{filename}: more than 3 patches should use %patchlist '
            f'(found {len(patches)} Patch fields)',
        )

    # Checkpoint 4: ``%patchlist`` must be placed above ``%description``.
    # The ``%patchlist`` block itself is searched in the whole file (it
    # may appear below ``%description``, which is exactly the violation
    # this checkpoint reports).
    patchlist_idx_full = -1
    for i, line in enumerate(lines):
        if _RE_PATCHLIST.match(line.strip()):
            patchlist_idx_full = i
            break
    if patchlist_idx_full != -1:
        description_idx = -1
        for i, line in enumerate(lines):
            if re.match(r'^%description\b', line.strip()):
                description_idx = i
                break
        if description_idx != -1 and patchlist_idx_full > description_idx:
            errors.append(
                f'{filename}: %patchlist must be placed above '
                f'%description',
            )

    # Checkpoint 5: ``Patch`` fields should be located between
    # ``BuildSystem`` and ``BuildOption`` (when present) or between
    # ``BuildSystem`` and ``BuildRequires`` (when ``BuildOption`` is
    # absent).
    if patches:
        buildsystem_idx = -1
        buildoption_idx = -1
        buildrequires_idx = -1
        for i, line in enumerate(header):
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            if _RE_BUILDSYSTEM.match(stripped):
                if buildsystem_idx == -1:
                    buildsystem_idx = i
            elif _RE_BUILDOPTION.match(stripped):
                if buildoption_idx == -1:
                    buildoption_idx = i
            elif _RE_BUILDREQUIRES.match(stripped):
                if buildrequires_idx == -1:
                    buildrequires_idx = i

        if buildsystem_idx != -1:
            if buildoption_idx != -1:
                anchor = buildoption_idx
                anchor_name = 'BuildOption'
            elif buildrequires_idx != -1:
                anchor = buildrequires_idx
                anchor_name = 'BuildRequires'
            else:
                anchor = -1
                anchor_name = ''
            if anchor != -1:
                for idx, _ in patches:
                    if not (buildsystem_idx < idx < anchor):
                        errors.append(
                            f'{filename}: Patch must be located between '
                            f'BuildSystem and {anchor_name}',
                        )
                        break
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_patch(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
