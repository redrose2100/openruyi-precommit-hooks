from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

# Check the `VCS` field according to openRuyi packaging guidelines
# (VCS section):
#   - `VCS` should point to a source repository link used to locate
#     source code.
#   - If `URL` already points to the source repository, `VCS` may be
#     omitted.
#   - If no VCS link is available, a comment line with the exact
#     prefix `# VCS:` must be present and contain
#     `No VCS link available`.
#   - For Git repositories, prefer a cloneable link such as
#     `VCS:            git:https://git.example.org/project.git`.

_RE_VCS = re.compile(r'^VCS\s*:\s*(.*)')
_RE_VCS_COMMENT = re.compile(r'^#\s*VCS\s*:\s*(.*)')
_RE_URL = re.compile(r'^URL\s*:\s*(.*)')

# heuristics for repository-like URLs
_RE_REPO_HINT = re.compile(r'(github\.com|gitlab\.com|bitbucket\.org|gitee\.com|codeberg\.org|\.git)')


def _is_repo_like(url: str) -> bool:
    if not url:
        return False
    return bool(_RE_REPO_HINT.search(url))


def _check_spec_vcs(filename: str) -> list[str]:
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

    vcs_value = None
    vcs_comment = None
    url_value = None

    for raw in lines:
        line = raw.strip()
        m = _RE_VCS.match(line)
        if m:
            vcs_value = m.group(1).strip()
            break
        mc = _RE_VCS_COMMENT.match(line)
        if mc and vcs_comment is None:
            vcs_comment = mc.group(1).strip()
        mu = _RE_URL.match(line)
        if mu and url_value is None:
            url_value = mu.group(1).strip()

    # If VCS is present
    if vcs_value:
        # Skip macro-expanded values
        if '%' in vcs_value:
            return errors
        # When using the git: prefix, ensure it contains a cloneable target
        if vcs_value.startswith('git:'):
            rest = vcs_value.split(':', 1)[1]
            if not rest or (not rest.startswith('http') and '@' not in rest and '.git' not in rest):
                errors.append(
                    f"{filename}: VCS uses 'git:' but the value after the prefix is not a recognizable clone URL (found '{vcs_value}')",
                )
    else:
        # No VCS field found. If URL points to a repo-like host, omission is allowed.
        if url_value and '%' not in url_value and _is_repo_like(url_value):
            return errors
        # If a VCS comment explicitly states no link is available, that's allowed
        if vcs_comment and 'No VCS link available' in vcs_comment:
            return errors
        errors.append(
            f"{filename}: missing VCS field; either provide a cloneable 'VCS:' value, set 'URL:' to the source repo, or add '# VCS: No VCS link available'",
        )

    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='spec files to check')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        for err in _check_spec_vcs(filename):
            print(err)
            retv = 1
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
