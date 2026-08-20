from __future__ import annotations

import argparse
from collections.abc import Generator
from collections.abc import Sequence
from typing import Any

import yaml


def _exhaust(gen: Generator) -> None:
    for _ in gen:
        pass


def _parse_unsafe(stream: Any) -> None:
    """Syntax-only check: parse tokens without constructing objects."""
    _exhaust(yaml.parse(stream))


def _load_all(stream: Any) -> None:
    _exhaust(yaml.load_all(stream, Loader=yaml.SafeLoader))


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
        if args.unsafe:
            _parse_unsafe(stream)
        elif args.multi:
            _load_all(stream)
        else:
            yaml.load(stream, Loader=yaml.SafeLoader)

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
