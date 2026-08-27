# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_perl import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_perlbuild_deps_declared(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'BuildSystem:    perlbuild\n'
        'BuildRequires:  perl-rpm-packaging\n'
        'BuildRequires:  perl-rpm-macros\n'
        'BuildRequires:  perl-macros\n',
    )
    assert main([f]) == 0


def test_ok_perlmaker_deps_declared(tmp_path):
    # the rule applies to perlmaker too, and all three dependency names
    # contain hyphens which must be recognised as valid package names
    f = _write(
        tmp_path,
        'good2.spec',
        'BuildSystem:    perlmaker\n'
        'BuildRequires:  perl-rpm-packaging\n'
        'BuildRequires:  perl-rpm-macros\n'
        'BuildRequires:  perl-macros\n',
    )
    assert main([f]) == 0


def test_ok_deps_with_version(tmp_path):
    f = _write(
        tmp_path,
        'good3.spec',
        'BuildSystem:    perlmaker\n'
        'BuildRequires:  perl-rpm-packaging >= 1\n'
        'BuildRequires:  perl-rpm-macros >= 2\n'
        'BuildRequires:  perl-macros >= 3\n',
    )
    assert main([f]) == 0


def test_ok_extra_deps_ignored(tmp_path):
    # perl(...) virtual dependencies and other extras do not affect the rule
    f = _write(
        tmp_path,
        'good4.spec',
        'BuildSystem:    perlbuild\n'
        'BuildRequires:  perl-rpm-packaging\n'
        'BuildRequires:  perl-rpm-macros\n'
        'BuildRequires:  perl-macros\n'
        'BuildRequires:  perl(Module::Build)\n'
        'BuildRequires:  perl(Test::More)\n',
    )
    assert main([f]) == 0


def test_ok_not_perl_skipped(tmp_path):
    # the rule only applies to perlbuild/perlmaker
    for bs in ('autotools', 'cmake', 'golang', 'meson', 'pyproject'):
        f = _write(
            tmp_path,
            f'good_{bs}.spec',
            f'BuildSystem:    {bs}\n'
            'BuildRequires:  zlib-devel\n',
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


def test_ok_ordered_deps_mixed(tmp_path):
    # dependency names may appear in any order
    f = _write(
        tmp_path,
        'good_mixed.spec',
        'BuildSystem:    perlmaker\n'
        'BuildRequires:  perl-macros\n'
        'BuildRequires:  zlib-devel\n'
        'BuildRequires:  perl-rpm-packaging\n'
        'BuildRequires:  perl-rpm-macros\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_fail_missing_one(tmp_path):
    f = _write(
        tmp_path,
        'bad1.spec',
        'BuildSystem:    perlbuild\n'
        'BuildRequires:  perl-rpm-packaging\n'
        'BuildRequires:  perl-rpm-macros\n',
    )
    assert main([f]) == 1


def test_fail_missing_two(tmp_path):
    f = _write(
        tmp_path,
        'bad2.spec',
        'BuildSystem:    perlmaker\n'
        'BuildRequires:  perl-macros\n',
    )
    assert main([f]) == 1


def test_fail_no_buildrequires(tmp_path):
    f = _write(
        tmp_path,
        'bad3.spec',
        'BuildSystem:    perlbuild\n'
        'Name:  foo\n',
    )
    assert main([f]) == 1


def test_fail_comment_does_not_count(tmp_path):
    # a commented BuildRequires line is not a declaration
    f = _write(
        tmp_path,
        'bad4.spec',
        'BuildSystem:    perlmaker\n'
        '# BuildRequires:  perl-rpm-macros\n',
    )
    assert main([f]) == 1


def test_fail_macro_named_dependency_does_not_count(tmp_path):
    # a dependency whose name is a macro cannot be validated statically
    f = _write(
        tmp_path,
        'bad5.spec',
        'BuildSystem:    perlbuild\n'
        'BuildRequires:  %{?something}\n',
    )
    assert main([f]) == 1


def test_fail_subpackage_br_does_not_count(tmp_path):
    # BuildRequires inside a %package subpackage block is a different
    # field and must not satisfy the header requirement
    f = _write(
        tmp_path,
        'bad6.spec',
        'BuildSystem:    perlmaker\n'
        'Name:  foo\n'
        '%package  devel\n'
        'BuildRequires:  perl-rpm-packaging\n'
        'BuildRequires:  perl-rpm-macros\n'
        'BuildRequires:  perl-macros\n',
    )
    assert main([f]) == 1


def test_fail_error_message_lists_missing(tmp_path):
    import subprocess
    import sys

    f = _write(
        tmp_path,
        'bad7.spec',
        'BuildSystem:    perlbuild\n'
        'BuildRequires:  perl-rpm-packaging\n'
        'BuildRequires:  perl-rpm-macros\n',
    )
    res = subprocess.run(
        [sys.executable, '-m', 'openruyi_precommit_hooks.check_spec_perl', f],
        capture_output=True,
        text=True,
        check=False,
    )
    assert res.returncode == 1
    assert 'declare perl-macros' in res.stdout


def test_fail_error_message_all_missing(tmp_path):
    import subprocess
    import sys

    f = _write(
        tmp_path,
        'bad8.spec',
        'BuildSystem:    perlmaker\n'
        'BuildRequires:  zlib-devel\n',
    )
    res = subprocess.run(
        [sys.executable, '-m', 'openruyi_precommit_hooks.check_spec_perl', f],
        capture_output=True,
        text=True,
        check=False,
    )
    assert res.returncode == 1
    assert 'declare perl-macros, perl-rpm-macros, perl-rpm-packaging' in res.stdout
