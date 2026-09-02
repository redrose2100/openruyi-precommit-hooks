from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

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

_SOURCE_REPO_HOSTS = frozenset({
    'github.com',
    'gitlab.com',
    'codeberg.org',
    'bitbucket.org',
    'hg.sr.ht',
    'invent.kde.org',
    'salsa.debian.org',
    'pagure.io',
    'code.videolan.org',
    'src.fedoraproject.org',
})

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
    stripped = line.strip()
    for tag in _SECTIONS:
        if stripped == tag or stripped.startswith(tag + ' ') or \
                stripped.startswith(tag + '\t'):
            return True
    return False


def _field_name(stripped: str) -> str | None:
    for field in _HEADER_FIELDS:
        if field == 'Source':
            if re.match(r'^Source\d*:', stripped):
                return 'Source'
            continue
        if stripped.startswith(field + ':'):
            return field
    return None


def _header_seq(lines: list[str], cut: int) -> list[str]:
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


def _get_url_value(lines: list[str], cut: int) -> str | None:
    for line in lines[:cut]:
        stripped = line.strip()
        if stripped.startswith('URL:'):
            return stripped[len('URL:'):].strip()
    return None


def _is_source_repo_url(value: str) -> bool:
    value = value.strip()
    if value.startswith('git:'):
        return True
    if value.endswith('.git'):
        return True
    m = re.match(r'^https?://([^/\s]+)', value, re.IGNORECASE)
    if not m:
        return False
    host = m.group(1).lower()
    if host in _SOURCE_REPO_HOSTS:
        return True
    if host.startswith('gitlab.') or host.startswith('git.'):
        return True
    return False


def _check_header_order(lines: list[str], filename: str) -> list[str]:
    errors: list[str] = []
    cut = len(lines)
    for i, line in enumerate(lines):
        if line.strip().startswith('%description'):
            cut = i
            break
    seq = _header_seq(lines, cut)

    missing = [f for f in _HEADER_FIELDS if f not in seq]
    if 'VCS' in missing:
        url = _get_url_value(lines, cut)
        if url is not None and _is_source_repo_url(url):
            missing.remove('VCS')
    if missing:
        errors.append(
            f'{filename}: missing required header field(s): '
            f'{", ".join(missing)}',
        )
    order = {field: idx for idx, field in enumerate(_HEADER_FIELDS)}
    positions: list[tuple[str, int]] = []
    for field in seq:
        positions.append((field, order[field]))
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
