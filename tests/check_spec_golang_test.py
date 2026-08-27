# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_golang import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_golang_deps_declared(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'BuildSystem:    golang\n'
        'BuildRequires:  go\n'
        'BuildRequires:  go-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_golangmodules_deps_declared(tmp_path):
    # the rule applies to golangmodules too, and go-rpm-macros contains
    # a hyphen which must be recognised as a valid package name
    f = _write(
        tmp_path,
        'good2.spec',
        'BuildSystem:    golangmodules\n'
        'BuildRequires:  go\n'
        'BuildRequires:  go-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_deps_with_version(tmp_path):
    f = _write(
        tmp_path,
        'good3.spec',
        'BuildSystem:    golangmodules\n'
        'BuildRequires:  go >= 1.21\n'
        'BuildRequires:  go-rpm-macros >= 3\n',
    )
    assert main([f]) == 0


def test_ok_extra_deps_ignored(tmp_path):
    f = _write(
        tmp_path,
        'good4.spec',
        'BuildSystem:    golangmodules\n'
        'BuildRequires:  go\n'
        'BuildRequires:  go-rpm-macros\n'
        'BuildRequires:  go(github.com/stretchr/testify)\n'
        'BuildRequires:  pkgconfig(gflags)\n',
    )
    assert main([f]) == 0


def test_ok_not_golang_skipped(tmp_path):
    # the rule only applies to golang/golangmodules
    for bs in ('autotools', 'cmake', 'meson', 'pyproject', 'rustcrates'):
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
        'BuildSystem:    golangmodules\n'
        'BuildRequires:  go-rpm-macros\n'
        'BuildRequires:  zlib-devel\n'
        'BuildRequires:  go\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_fail_missing_go(tmp_path):
    f = _write(
        tmp_path,
        'bad1.spec',
        'BuildSystem:    golangmodules\n'
        'BuildRequires:  go-rpm-macros\n',
    )
    assert main([f]) == 1


def test_fail_missing_go_rpm_macros(tmp_path):
    f = _write(
        tmp_path,
        'bad2.spec',
        'BuildSystem:    golang\n'
        'BuildRequires:  go\n',
    )
    assert main([f]) == 1


def test_fail_no_buildrequires(tmp_path):
    f = _write(
        tmp_path,
        'bad3.spec',
        'BuildSystem:    golangmodules\n'
        'Name:  foo\n',
    )
    assert main([f]) == 1


def test_fail_comment_does_not_count(tmp_path):
    # a commented BuildRequires line is not a declaration
    f = _write(
        tmp_path,
        'bad4.spec',
        'BuildSystem:    golangmodules\n'
        '# BuildRequires:  go-rpm-macros\n',
    )
    assert main([f]) == 1


def test_fail_macro_named_dependency_does_not_count(tmp_path):
    # a dependency whose name is a macro cannot be validated statically
    f = _write(
        tmp_path,
        'bad5.spec',
        'BuildSystem:    golangmodules\n'
        'BuildRequires:  %{?something}\n',
    )
    assert main([f]) == 1


def test_fail_subpackage_br_does_not_count(tmp_path):
    # BuildRequires inside a %package subpackage block is a different
    # field and must not satisfy the header requirement
    f = _write(
        tmp_path,
        'bad6.spec',
        'BuildSystem:    golangmodules\n'
        'Name:  foo\n'
        '%package  devel\n'
        'BuildRequires:  go\n'
        'BuildRequires:  go-rpm-macros\n',
    )
    assert main([f]) == 1


def test_fail_error_message_lists_missing(tmp_path):
    import subprocess
    import sys

    f = _write(
        tmp_path,
        'bad7.spec',
        'BuildSystem:    golangmodules\n'
        'BuildRequires:  go\n',
    )
    res = subprocess.run(
        [sys.executable, '-m', 'openruyi_precommit_hooks.check_spec_golang', f],
        capture_output=True,
        text=True,
        check=False,
    )
    assert res.returncode == 1
    assert 'declare go-rpm-macros' in res.stdout


def test_fail_error_message_both_missing(tmp_path):
    import subprocess
    import sys

    f = _write(
        tmp_path,
        'bad8.spec',
        'BuildSystem:    golang\n'
        'BuildRequires:  zlib-devel\n',
    )
    res = subprocess.run(
        [sys.executable, '-m', 'openruyi_precommit_hooks.check_spec_golang', f],
        capture_output=True,
        text=True,
        check=False,
    )
    assert res.returncode == 1
    assert 'declare go, go-rpm-macros' in res.stdout
