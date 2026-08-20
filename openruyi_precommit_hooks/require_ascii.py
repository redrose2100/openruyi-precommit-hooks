from __future__ import annotations

import argparse
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dry-run', action='store_true',
        help='Only report files containing non-ASCII characters.',
    )
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        with open(filename, 'rb') as f:
            data = f.read()
        try:
            data.decode('ascii')
        except UnicodeDecodeError:
            retval = 1
            if args.dry_run:
                print(f'{filename}: contains non-ASCII characters')
        else:
            if not args.dry_run:
                # non-dry-run mode is a trivial passthrough example;
                # real fixers would rewrite the file here.
                pass
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
