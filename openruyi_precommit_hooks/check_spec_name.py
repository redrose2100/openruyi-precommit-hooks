from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``Name`` field of an openRuyi spec file must follow the naming
# guidelines (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines):
#
#   1. ``Name`` must always be present.
#   2. The package name should be lowercase and prefer ``-`` over ``_``
#      as the separator.  Underscores are only allowed in the exceptions
#      defined by the supplemental spec (e.g. upstream names that
#      naturally contain an underscore like ``nss_wrapper``).
#   3. The package name must not encode an ABI (SONAME major) or the
#      upstream major version (e.g. a name like ``libfoo2``).
#
# The `perl-*` modules are exempt from the lowercase rule: the CPAN
# distribution groups must be capitalized per the supplemental spec.
# Names that expand a macro (e.g. ``python-%{pypi_name}``) cannot be
# statically checked, so they are skipped.

_RE_NAME = re.compile(r'^Name\s*:\s*(\S+)')
_RE_LIB_ABI = re.compile(r'^lib[a-z]+[0-9]+$')


def _check_spec_name(filename: str) -> list[str]:
    """Validate the ``Name`` field of ``filename``.

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

    name = None
    for line in lines:
        m = _RE_NAME.match(line.strip())
        if m:
            name = m.group(1)
            break
    if name is None:
        return [f'{filename}: missing required field "Name"']

    # A macro-expanded name (e.g. ``python-%{pypi_name}``) cannot be
    # checked statically.
    if '%' in name:
        return errors

    if not name.islower() and not name.startswith('perl-'):
        errors.append(
            f'{filename}: package name should be lowercase '
            f'(found "{name}")',
        )
    if '_' in name:
        errors.append(
            f'{filename}: prefer "-" over "_" in package name '
            f'(found "{name}")',
        )
    if _RE_LIB_ABI.match(name):
        errors.append(
            f'{filename}: package name should not encode an ABI or '
            f'major version (found "{name}")',
        )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_name(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
