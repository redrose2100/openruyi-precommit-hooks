from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# The ``Source`` field of an openRuyi spec file must follow the
# packaging guidelines
# (https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#source):
#
#   1. ``Source`` must provide a location to obtain the upstream
#      source code (or an equivalent reproducible source archive).
#   2. When the ``URL`` field can be reused as a prefix of ``Source``,
#      ``Source`` may reuse ``%{url}``.
#   3. For ``Source`` obtained over the network, a ``#!RemoteAsset``
#      comment must be placed immediately above the ``Source`` line;
#      when there are multiple network sources, each one must carry
#      its own marker.
#   4. For ``Source`` obtained via HTTP(S), a ``sha256`` checksum must
#      be attached to the ``#!RemoteAsset`` comment so the downloaded
#      archive can be verified.
#
# Statically checkable rules in this hook:
#   * a network ``Source`` (starting with ``http://``, ``https://``
#     or ``%{url}``) must be preceded by a ``#!RemoteAsset`` comment;
#   * an HTTP(S) ``Source`` must carry ``sha256:`` inside its
#     ``#!RemoteAsset`` comment;
#   * SourceForge downloads must use the ``downloads.sourceforge.net``
#     host (``download.sourceforge.net`` / ``prdownloads...`` /
#     ``sourceforge.net/projects/...`` links are not reliable).
#
# Local files, ``git+``/``git:`` sources and the numbering rules are
# not judged here (git sources record a fixed commit inside
# ``#!RemoteAsset: git+...``).

_RE_SOURCE = re.compile(r'^Source([0-9]*)\s*:\s*(.*)')
# ``%{url}`` -- reuse of the ``URL`` field (allowed for network sources).
_RE_MACRO_URL = re.compile(r'^%\{url\}')
# Network sources obtained over HTTP(S).
_RE_SCHEME = re.compile(r'^https?://', re.IGNORECASE)
# The ``#!RemoteAsset`` marker line above a ``Source`` line.
_RE_REMOTE_ASSET = re.compile(r'^#!RemoteAsset\s*:?\s*(.*)')
# A sha256 checksum inside the marker (64 hex digits).
_RE_SHA256 = re.compile(r'^sha256\s*:\s*[0-9a-fA-F]{64}$')
# SourceForge download links must use the ``downloads`` host.
_RE_SF_DOWNLOADS = re.compile(
    r'^https?://downloads\.sourceforge\.net/', re.IGNORECASE,
)
# Avoid echoing a very long value verbatim in an error message.
_MAX_SHOWN = 60


def _truncate(value: str) -> str:
    if len(value) <= _MAX_SHOWN:
        return value
    return value[:_MAX_SHOWN - 3] + '...'


def _check_spec_source(filename: str) -> list[str]:
    """Validate the ``Source`` fields of ``filename``.

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

    for i, line in enumerate(lines):
        stripped = line.strip()
        # Skip commented-out ``# Source:`` lines.
        if not stripped or stripped.startswith('#'):
            continue
        m = _RE_SOURCE.match(stripped)
        if not m:
            continue
        value = m.group(2).strip()
        if not value:
            # Field presence is checked by ``check-spec-structure``.
            continue
        shown = _truncate(value)

        # SourceForge downloads must use the ``downloads`` host.
        if 'sourceforge.net' in value and not _RE_SF_DOWNLOADS.match(value):
            errors.append(
                f'{filename}: Source with a sourceforge.net link must use '
                f'downloads.sourceforge.net (found "{shown}")',
            )

        # A network source must be marked with ``#!RemoteAsset`` on the
        # line immediately before it.
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
        # HTTP(S) sources (and ``%{url}`` prefixes which expand to http(s)
        # links) must attach a sha256 checksum to the marker; a bare
        # ``#!RemoteAsset`` without a checksum, or one carrying any other
        # payload, is a violation.
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
