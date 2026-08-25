from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``BuildArch`` field of an openRuyi spec file must follow the
# packaging guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#buildarch-%E5%8F%AF%E9%80%89):
#
#   1. ``BuildArch`` is used to declare the target architecture.
#   2. The ``BuildArch`` field should be located between the last
#      ``Source`` field and the ``BuildSystem`` field.
#   3. When ``BuildArch`` is ``noarch``, the package is independent of
#      the CPU architecture.
#
# ``BuildArch`` is an optional field.  Statically checkable rules in
# this hook:
#   * a ``BuildArch:`` field must not be empty (an empty value cannot
#     declare a target architecture);
#   * the ``BuildArch`` field must be located after the last ``Source``
#     field and before the ``BuildSystem`` field (when both are
#     present);
#   * the value must be ``noarch`` -- the only architecture value used
#     by the openRuyi repository (a package that is not architecture
#     independent simply omits the field).
#
# Field presence is covered by ``check-spec-structure`` (``BuildArch``
# is optional, so a missing field is not an error here).  Whether a
# package really is architecture independent cannot be judged
# statically.

_RE_BUILDARCH = re.compile(r'^BuildArch\s*:\s*(.*)')
# ``Source`` also matches the numbered variants ``Source0`` … ``SourceN``.
_RE_SOURCE = re.compile(r'^Source\d*\s*:')
_RE_BUILDSYSTEM = re.compile(r'^BuildSystem\s*:')
# The only architecture value used by the openRuyi repository.
_NOARCH = 'noarch'
# Avoid echoing a very long value verbatim in an error message.
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _check_spec_buildarch(filename: str) -> list[str]:
    """Validate the ``BuildArch`` field of ``filename``.

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

    # Only the header region is inspected: ``BuildArch`` inside a
    # ``%package`` subpackage block is a different field (it declares
    # the subpackage architecture) and is not covered by this rule.
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
        # ``BuildArch`` is optional; field presence is covered by
        # ``check-spec-structure``.
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

    # Position check: ``BuildArch`` should be located after the last
    # ``Source`` field and before the ``BuildSystem`` field.  When one
    # of the two anchors is missing the position cannot be judged.
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
