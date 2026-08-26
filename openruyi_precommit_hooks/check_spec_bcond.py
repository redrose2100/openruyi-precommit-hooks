"""Ensure conditional-build switches in an openRuyi spec file follow
the packaging guidelines
(https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#条件构建):

   When a spec needs an optional build switch it should use ``%bcond``;
   the legacy ``%bcond_with`` / ``%bcond_without`` macros should be
   avoided.

Statically checkable rules in this hook:

   * ``%bcond_with`` / ``%bcond_without`` must not be used.  These
     legacy macros hard-code a default direction for the switch; declare
     the switch with ``%bcond <name> <default>`` instead.  ``%bcond``
     lets ``--with=`` / ``--without=`` override the default in either
     direction, which is the point of a *conditional* build switch.

   * every ``%{with <name>}`` / ``%{without <name>}`` reference must
     have a matching ``%bcond <name> <default>`` declaration somewhere
     in the file (the legacy ``%bcond_with`` / ``%bcond_without`` forms
     are also accepted as declarations, even though their own use is
     reported).  A reference to an undeclared switch hides the switch
     intent and typically evaluates to "disabled" at build time unless
     the builder passes ``--with=<name>`` by guess.

Builders may still override any declared switch from the command line
with ``--with=...`` / ``--without=...``; the check only requires the
switch to be *declared* in the spec.  Lines that are commented out
(starting with ``#``) are ignored.
"""
from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# Modern declaration form, e.g. ``%bcond bootstrap 0``.
_RE_BCOND = re.compile(r'^%bcond\s+(\S+)')
# Legacy declaration forms, e.g. ``%bcond_with openssl``.
_RE_BCOND_WITH = re.compile(r'^%bcond_with\s+(\S+)')
_RE_BCOND_WITHOUT = re.compile(r'^%bcond_without\s+(\S+)')
# Reference forms, e.g. ``%{with doc}`` / ``%{without bootstrap}``.
_RE_REF = re.compile(r'%\{(with|without)\s+(\S+?)\}')


def _check_spec_bcond(filename: str) -> list[str]:
    """Validate conditional-build switches in ``filename``.

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

    # Collect every declared switch name first so the reference check
    # is order independent (declarations usually live at the top of the
    # file, but that is not required).
    declared: set[str] = set()
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#'):
            continue
        m = _RE_BCOND.match(stripped)
        if m is not None:
            declared.add(m.group(1))
            continue
        m = _RE_BCOND_WITH.match(stripped)
        if m is not None:
            declared.add(m.group(1))
            continue
        m = _RE_BCOND_WITHOUT.match(stripped)
        if m is not None:
            declared.add(m.group(1))

    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith('#'):
            continue
        m = _RE_BCOND_WITH.match(stripped)
        if m is not None:
            errors.append(
                f'{filename}:{lineno}: legacy %bcond_with must be replaced '
                f'with %bcond {m.group(1)} <0|1> '
                f'(found "{stripped}")',
            )
            continue
        m = _RE_BCOND_WITHOUT.match(stripped)
        if m is not None:
            errors.append(
                f'{filename}:{lineno}: legacy %bcond_without must be '
                f'replaced with %bcond {m.group(1)} <0|1> '
                f'(found "{stripped}")',
            )
            continue
        for rm in _RE_REF.finditer(stripped):
            name = rm.group(2)
            if name not in declared:
                errors.append(
                    f'{filename}:{lineno}: %{{{rm.group(1)} {name}}} '
                    f'references an undeclared switch; add '
                    f'%bcond {name} <0|1> (found "{stripped}")',
                )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_bcond(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
