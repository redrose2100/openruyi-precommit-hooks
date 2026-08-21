from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The mandatory header fields of an openRuyi spec file and the order in
# which they must appear.  Every field must be present -- a package
# without a VCS checkout simply does not qualify.
_HEADER_FIELDS = (
    'Name',
    'Version',
    'Release',
    'Summary',
    'License',
    'URL',
    'VCS',
    'Source',
    'BuildSystem',
    'BuildRequires',
    'Requires',
)

# Sections that must be separated from the preceding content by a blank
# line (conditional blocks like `%if` are exempt).
_SECTIONS = (
    '%description',
    '%package',
    '%prep',
    '%build',
    '%install',
    '%check',
    '%files',
    '%changelog',
)


def _is_section_line(line: str) -> bool:
    """Return True if ``line`` opens one of the tracked sections.

    Section tags may carry parameters, e.g. ``%description devel`` or
    ``%files -f %{name}.lang``.
    """
    stripped = line.strip()
    for tag in _SECTIONS:
        if stripped == tag or stripped.startswith(tag + ' ') or \
                stripped.startswith(tag + '\t'):
            return True
    return False


def _field_name(stripped: str) -> str | None:
    """Return the header field name of ``stripped``, or None.

    ``Source`` also matches the numbered variants ``Source0`` …
    ``SourceN``; continuation lines (indented field bodies) return None.
    """
    for field in _HEADER_FIELDS:
        if field == 'Source':
            if re.match(r'^Source\d*:', stripped):
                return 'Source'
            continue
        if stripped.startswith(field + ':'):
            return field
    return None


def _header_seq(lines: list[str], cut: int) -> list[str]:
    """Extract header field order up to line ``cut``.

    Continuation lines and blank/comment/directive lines are ignored.
    """
    seq: list[str] = []
    for line in lines[:cut]:
        stripped = line.strip()
        if (
            not stripped or stripped.startswith('#') or
            stripped.startswith('%')
        ):
            continue
        field = _field_name(stripped)
        if field is not None:
            seq.append(field)
    return seq


def _check_header_order(lines: list[str], filename: str) -> list[str]:
    """Check that all header fields are present and in canonical order."""
    errors: list[str] = []
    cut = len(lines)
    for i, line in enumerate(lines):
        if line.strip().startswith('%description'):
            cut = i
            break
    seq = _header_seq(lines, cut)

    missing = [f for f in _HEADER_FIELDS if f not in seq]
    if missing:
        errors.append(
            f'{filename}: missing required header field(s): '
            f'{", ".join(missing)}',
        )
        # still report ordering problems below if any are present
    order = {field: idx for idx, field in enumerate(_HEADER_FIELDS)}
    positions: list[tuple[str, int]] = []
    for field in seq:
        positions.append((field, order[field]))
    # violations: a later field must never appear before an earlier one
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            if positions[i][1] > positions[j][1]:
                errors.append(
                    f'{filename}: header fields out of order: '
                    f'"{positions[j][0]}" appears after "{positions[i][0]}" '
                    f'(expected {_HEADER_FIELDS.index(positions[j][0]) + 1} '
                    f'< {_HEADER_FIELDS.index(positions[i][0]) + 1})',
                )
                return errors
    return errors


def _is_directive(line: str) -> bool:
    """Return True if ``line`` is a structural spec directive.

    Structural directives are the tracked section tags and the
    conditional/preprocessor keywords (``%if``, ``%ifarch``, ``%ifos``,
    ``%ifnarch``, ``%ifnos``, ``%else``, ``%endif``).  Bare macros such
    as ``%{_bindir}`` and macro invocations such as ``%find_lang`` or
    ``%make_install`` expand to content, so they are *not* structural.
    """
    stripped = line.strip()
    if not stripped.startswith('%'):
        return False
    if stripped.startswith('%{'):
        return False
    if _is_section_line(line):
        return True
    return re.match(
        r'^%(if|ifarch|ifos|ifnarch|ifnos|else|endif)\b', stripped,
    ) is not None


def _check_section_spacing(lines: list[str], filename: str) -> list[str]:
    """Check that sections are preceded by a blank line.

    Content lines (header fields, file lists, script lines) must be
    separated from a section tag by at least one blank line.  Other
    section tags and conditional directives (``%if``/``%else``/``%endif``)
    directly above the section do not require a blank line.
    """
    errors: list[str] = []
    for i, line in enumerate(lines):
        if not _is_section_line(line):
            continue
        j = i - 1
        while j >= 0 and lines[j].strip().startswith('#'):
            j -= 1
        if j >= 0 and lines[j].strip() != '' and not _is_directive(lines[j]):
            prev = lines[j].strip()
            errors.append(
                f'{filename}: section "{line.strip()}" must be preceded '
                f'by a blank line (found: "{prev[:40]}")',
            )
    return errors


def _check_spec_structure(filename: str) -> list[str]:
    """Validate the structure of ``filename``.

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

    errors.extend(_check_header_order(lines, filename))
    errors.extend(_check_section_spacing(lines, filename))
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_structure(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
