# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_autotools import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_all_deps_declared(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  autoconf\n'
        'BuildRequires:  automake\n'
        'BuildRequires:  libtool\n'
        'BuildRequires:  make\n',
    )
    assert main([f]) == 0


def test_ok_all_deps_one_line(tmp_path):
    # declaring several packages on one line is a formatting violation
    # (handled by check-spec-buildrequires) but the names are still found
    f = _write(
        tmp_path,
        'good2.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  autoconf automake libtool make\n',
    )
    assert main([f]) == 0


def test_ok_deps_with_version(tmp_path):
    f = _write(
        tmp_path,
        'good3.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  autoconf >= 2.69\n'
        'BuildRequires:  automake\n'
        'BuildRequires:  libtool\n'
        'BuildRequires:  make >= 4.0\n',
    )
    assert main([f]) == 0


def test_ok_extra_deps_ignored(tmp_path):
    f = _write(
        tmp_path,
        'good4.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  autoconf\n'
        'BuildRequires:  automake\n'
        'BuildRequires:  libtool\n'
        'BuildRequires:  make\n'
        'BuildRequires:  pkgconfig(zlib)\n'
        'BuildRequires:  gettext-devel\n',
    )
    assert main([f]) == 0


def test_ok_not_autotools_skipped(tmp_path):
    # the rule only applies to BuildSystem: autotools
    for bs in ('cmake', 'meson', 'golang', 'pyproject', 'rustcrates'):
        f = _write(
            tmp_path,
            f'good_{bs}.spec',
            f'BuildSystem:    {bs}\n'
            'BuildRequires:  cmake\n',
        )
        assert main([f]) == 0


def test_ok_empty_buildsystem(tmp_path):
    # empty BuildSystem falls outside the rule (structure hook owns it)
    f = _write(
        tmp_path,
        'good_empty_bs.spec',
        'BuildSystem:\n',
    )
    assert main([f]) == 0


def test_ok_no_buildrequires(tmp_path):
    # a non-autotools spec without BuildRequires is fine
    f = _write(
        tmp_path,
        'good_nobr.spec',
        'BuildSystem:    golang\n'
        'Name:  foo\n',
    )
    assert main([f]) == 0


def test_fail_subpackage_br_does_not_count(tmp_path):
    # BuildRequires inside a %package subpackage block is a different
    # field and must not satisfy the header requirement
    f = _write(
        tmp_path,
        'bad_subpkg.spec',
        'BuildSystem:    autotools\n'
        'Name:  foo\n'
        '%package  devel\n'
        'BuildRequires:  autoconf\n'
        'BuildRequires:  automake\n'
        'BuildRequires:  libtool\n'
        'BuildRequires:  make\n',
    )
    assert main([f]) == 1


def test_ok_ordered_deps_mixed(tmp_path):
    # dependency names may appear in any order
    f = _write(
        tmp_path,
        'good_mixed.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  make\n'
        'BuildRequires:  zlib-devel\n'
        'BuildRequires:  libtool\n'
        'BuildRequires:  automake\n'
        'BuildRequires:  autoconf\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_fail_missing_all(tmp_path):
    f = _write(
        tmp_path,
        'bad1.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  zlib-devel\n',
    )
    assert main([f]) == 1


def test_fail_missing_make_only(tmp_path):
    f = _write(
        tmp_path,
        'bad2.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  autoconf\n'
        'BuildRequires:  automake\n'
        'BuildRequires:  libtool\n',
    )
    assert main([f]) == 1


def test_fail_missing_autoconf_automake(tmp_path):
    f = _write(
        tmp_path,
        'bad3.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  libtool\n'
        'BuildRequires:  make\n',
    )
    assert main([f]) == 1


def test_fail_missing_libtool(tmp_path):
    f = _write(
        tmp_path,
        'bad4.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  autoconf\n'
        'BuildRequires:  automake\n'
        'BuildRequires:  make\n',
    )
    assert main([f]) == 1


def test_fail_comment_does_not_count(tmp_path):
    # a commented BuildRequires line is not a declaration
    f = _write(
        tmp_path,
        'bad5.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  autoconf\n'
        '# BuildRequires:  automake\n'
        'BuildRequires:  libtool\n'
        'BuildRequires:  make\n',
    )
    assert main([f]) == 1


def test_fail_macro_named_dependency_does_not_count(tmp_path):
    # a dependency whose name is a macro (e.g. a metapackage named after
    # a macro) cannot be validated statically and does not satisfy the
    # requirement
    f = _write(
        tmp_path,
        'bad6.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  autoconf\n'
        'BuildRequires:  automake\n'
        'BuildRequires:  libtool\n'
        'BuildRequires:  %{?something}\n',
    )
    assert main([f]) == 1


def test_fail_error_message_lists_missing(tmp_path):
    import subprocess
    import sys

    f = _write(
        tmp_path,
        'bad7.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  libtool\n'
        'BuildRequires:  make\n',
    )
    res = subprocess.run(
        [sys.executable, '-m', 'openruyi_precommit_hooks.check_spec_autotools', f],
        capture_output=True,
        text=True,
        check=False,
    )
    assert res.returncode == 1
    assert 'declare autoconf, automake' in res.stdout
    assert ', libtool' not in res.stdout
    assert ', make' not in res.stdout
