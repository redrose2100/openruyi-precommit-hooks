from __future__ import annotations

import argparse
import re
from collections.abc import Sequence


_RE_SOURCE = re.compile(r'^Source([0-9]*)\s*:\s*(.*)')
_RE_MACRO_URL = re.compile(r'^%\{url\}')
_RE_SCHEME = re.compile(r'^https?://', re.IGNORECASE)
_RE_REMOTE_ASSET = re.compile(r'^#!RemoteAsset\s*:?\s*(.*)')
_RE_SHA256 = re.compile(r'^sha256\s*:\s*[0-9a-fA-F]{64}$')
_RE_SF_DOWNLOADS = re.compile(
    r'^https?://downloads\.sourceforge\.net/', re.IGNORECASE,
)
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _check_spec_source(filename: str) -> list[str]:
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

    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        m = _RE_SOURCE.match(stripped)
        if not m:
            continue
        value = m.group(2).strip()
        if not value:
            continue
        shown = _truncate(value)

        if 'sourceforge.net' in value and not _RE_SF_DOWNLOADS.match(value):
            errors.append(
                f'{filename}: Source with a sourceforge.net link must use '
                f'downloads.sourceforge.net (found "{shown}")',
            )

        prev = lines[i - 1].strip() if i > 0 else ''
        is_http = bool(_RE_SCHEME.match(value))
        is_network = is_http or bool(_RE_MACRO_URL.match(value))
        if not is_network:
            continue
        ra = _RE_REMOTE_ASSET.match(prev)
        if ra is None:
            errors.append(
                f'{filename}: Source obtained over the network must be '
                f'preceded by a #!RemoteAsset comment (found "{shown}")',
            )
            continue
        body = ra.group(1).strip()
        if not _RE_SHA256.match(body):
            errors.append(
                f'{filename}: #!RemoteAsset comment of an http(s) Source '
                f'must carry a sha256 checksum (found "{shown}")',
            )
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_source(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
