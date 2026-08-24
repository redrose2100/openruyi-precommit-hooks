from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``URL`` field of an openRuyi spec file must follow the packaging
# guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#url):
#
#   1. ``URL`` must be the official website of the package; when there
#      is no official website, a source repository link may be used.
#   2. ``URL`` must not be built with macros such as ``%{name}``.
#
# Statically checkable rules in this hook:
#   * the value must start with an ``http://`` or ``https://`` scheme
#     (a placeholder like ``FIXME`` or a bare host is not a valid
#     website/repository link);
#   * the value must not contain any ``%{...}`` macro (the field is a
#     literal permanent link, not something assembled at build time).
#
# Field presence is covered by ``check-spec-structure``.  Whether a
# link really is the official upstream website or the canonical source
# repository cannot be judged statically.

_RE_URL = re.compile(r'^URL\s*:\s*(.*)')
# ``%{name}``, ``%{srcname}`` ... -- any macro reference.
_RE_MACRO = re.compile(r'%\{[^}]*\}')
# Official website or source repository links are http(s) links.
_RE_SCHEME = re.compile(r'^https?://', re.IGNORECASE)
# Avoid echoing a very long value verbatim in an error message.
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _check_spec_url(filename: str) -> list[str]:
    """Validate the ``URL`` field of ``filename``.

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

    url_value = None
    for line in lines:
        m = _RE_URL.match(line.strip())
        if m:
            # Skip commented-out ``# URL:`` lines.
            if not line.strip().startswith('#'):
                url_value = m.group(1).strip()
                break
    if url_value is None or not url_value:
        # Field presence is checked by ``check-spec-structure``.
        return errors

    shown = _truncate(url_value)
    if _RE_MACRO.search(url_value):
        errors.append(
            f'{filename}: URL must not be built with macros such as '
            f'%{{name}} (found "{shown}")',
        )
    if not _RE_SCHEME.match(url_value):
        errors.append(
            f'{filename}: URL must be a valid http(s) website or source '
            f'repository link (found "{shown}")',
        )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_url(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
