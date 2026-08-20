from __future__ import annotations

import argparse
from collections.abc import Sequence


def check_executables_have_shebangs(filenames: Sequence[str]) -> int:
    bad_files = []
    for filename in filenames:
        with open(filename, 'rb') as f:
            first_line = f.readline()
        shebang_present = first_line.startswith(b'#!')
        executable = _is_executable(filename)
        if executable and not shebang_present:
            bad_files.append(filename)
    if bad_files:
        print('Executable files without shebangs:')
        for filename in bad_files:
            print(f'  {filename}')
        return 1
    return 0


def _is_executable(filename: str) -> bool:
    import os
    return os.access(filename, os.X_OK)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)
    return check_executables_have_shebangs(args.filenames)


if __name__ == '__main__':
    raise SystemExit(main())