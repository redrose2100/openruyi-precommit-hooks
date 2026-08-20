from __future__ import annotations

import argparse
from collections.abc import Sequence
from typing import Any

import yaml


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m', '--multi', '--allow-multiple-documents', action='store_true',
    )
    parser.add_argument(
        '--unsafe', action='store_true',
        help=(
            'Instead of loading the files, simply parse them for syntax.  '
            'A syntax-only check enables extensions and unsafe constructs '
            'which would otherwise be forbidden.  Using this option removes '
            'all guarantees of portability to other yaml implementations.  '
            'Implies --allow-multiple-documents'
        ),
    )
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    def _load(stream: Any) -> None:
        loader = yaml.SafeLoader
        if args.unsafe:
            loader = yaml.Loader  # syntax-only: allow unsafe constructs
        if args.multi or args.unsafe:
            for _ in yaml.load_all(stream, Loader=loader):
                pass
        else:
            yaml.load(stream, Loader=loader)

    retval = 0
    for filename in args.filenames:
        try:
            with open(filename, encoding='UTF-8') as f:
                _load(f)
        except yaml.YAMLError as exc:
            print(exc)
            retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())