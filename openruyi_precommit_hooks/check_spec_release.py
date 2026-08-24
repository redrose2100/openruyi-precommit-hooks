from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``Release`` field of an openRuyi spec file must follow the
# packaging guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines):
#
#   1. ``Release`` should use ``%autorelease``.
#   2. ``Release`` must not hardcode a distribution suffix or
#      override the value of ``%{dist}``.
#   3. When ``Version`` stays the same, the revision number in
#      ``Release`` must increase.
#   4. When ``Version`` changes, the revision number must be reset
#      to ``1``.
#
# The supplemental versioning spec
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/Versioning)
# adds that a plain ``Release`` value should be an integer starting at
# ``1`` (not ``0``).
#
# Statically checkable rules in this hook:
#   * the ``Release`` value should expand ``%autorelease`` (directly
#     or through ``%{autorelease}``); a literal integer revision is
#     reported as a suggestion;
#   * a literal ``0`` revision violates the "integer starting at 1"
#     rule;
#   * a non-digit tail such as ``.fc40`` hardcodes a dist suffix and
#     is forbidden, as is overriding ``dist`` via ``%global dist`` /
#     ``%define dist``;
#   * rules 3 and 4 (increment / reset on version change) need version
#     history and cannot be checked on a single file.
#
# Other macro-expanded values (e.g. ``%{release}`` or ``1%{?dist}``)
# cannot be judged statically, except for a literal ``0`` prefix, and
# are skipped.  Field presence is covered by ``check-spec-structure``,
# so a missing ``Release`` is not an error here.

_RE_RELEASE = re.compile(r'^Release\s*:\s*(\S+)')
# The numeric revision prefix of a Release value (e.g. ``1`` in
# ``1%{?dist}`` or ``1.fc40``).
_RE_NUM_PREFIX = re.compile(r'^[0-9]+')
# The ``dist`` macro redefined in the header (e.g. ``%global dist``).
_RE_DIST_OVERRIDE = re.compile(r'^\s*%(?:global|define)\s+dist\b')


def _check_spec_release(filename: str) -> list[str]:
    """Validate the ``Release`` field of ``filename``.

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

    release = None
    for line in lines:
        m = _RE_RELEASE.match(line.strip())
        if m:
            release = m.group(1)
            break
    if release is None:
        # Field presence is checked by ``check-spec-structure``.
        return errors

    if '%autorelease' in release or '%{autorelease}' in release:
        # Satisfies the recommendation; only the ``dist`` override
        # check below may still flag the file.
        pass
    elif '%' in release:
        # Macro-expanded values: check the literal prefix for a ``0``
        # revision or a hardcoded dist suffix before the macro part.
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
        # Literal value without macros.
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
            # A non-digit tail such as ``.fc40`` hardcodes a dist suffix.
            errors.append(
                f'{filename}: Release must not hardcode a dist suffix '
                f'(found "{release}")',
            )
        else:
            # A plain integer such as ``1`` works, but the guideline
            # recommends ``%autorelease``.
            errors.append(
                f'{filename}: Release should use "%autorelease" '
                f'instead of a fixed revision (found "{release}")',
            )

    # The ``dist`` macro must not be overridden (e.g. ``%global dist``).
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
