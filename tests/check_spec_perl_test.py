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


# --- virtual-dependency-format rule (checkpoint 2) --------------------------

def test_ok_perl_module_virtual_deps(tmp_path):
    # perl(MODULE) virtual dependencies are the preferred format
    f = _write(
        tmp_path,
        'good_virtual.spec',
        'BuildSystem:    perlbuild\n'
        'BuildRequires:  perl-rpm-packaging\n'
        'BuildRequires:  perl-rpm-macros\n'
        'BuildRequires:  perl-macros\n'
        'Requires:       perl(Archive::Zip)\n'
        'Provides:       perl(Archive::Zip)\n',
    )
    assert main([f]) == 0


def test_ok_perl_package_subpackage_declared(tmp_path):
    # perl-X is allowed when the spec declares the %package perl-X subpackage
    f = _write(
        tmp_path,
        'good_subpkg.spec',
        'Name:  git\n'
        'BuildSystem:    autotools\n'
        'Requires:       perl-Git = %{version}-%{release}\n'
        '%package        perl-Git\n'
        'Summary:        git perl bindings\n',
    )
    assert main([f]) == 0


def test_ok_no_reqprov_fields(tmp_path):
    # specs without Requires/Provides lines are unaffected
    f = _write(
        tmp_path,
        'good_plain.spec',
        'Name:  foo\n'
        'BuildSystem:    perlbuild\n'
        'BuildRequires:  perl-rpm-packaging\n'
        'BuildRequires:  perl-rpm-macros\n'
        'BuildRequires:  perl-macros\n',
    )
    assert main([f]) == 0


def test_fail_bare_perl_package_name(tmp_path):
    # docbook-utils style: Requires: perl-SGMLSpm must be perl(SGMLSpm)
    f = _write(
        tmp_path,
        'bad_virtual1.spec',
        'Name:  docbook-utils\n'
        'Requires:       perl-SGMLSpm\n',
    )
    assert main([f]) == 1


def test_fail_bare_perl_package_with_version(tmp_path):
    # help2man style: a version constraint does not change the violation
    f = _write(
        tmp_path,
        'bad_virtual2.spec',
        'Name:  help2man\n'
        'Requires:       perl-Locale-gettext >= 1.0\n',
    )
    assert main([f]) == 1


def test_fail_subpackage_not_declared(tmp_path):
    # a plain %package (not perl-*) does not exempt perl-X references
    f = _write(
        tmp_path,
        'bad_virtual3.spec',
        'Name:  foo\n'
        'Requires:       perl-Zip\n'
        '%package        devel\n'
        'Summary:        dev files\n',
    )
    assert main([f]) == 1


def test_fail_error_message_virtual_format(tmp_path):
    import subprocess
    import sys

    f = _write(
        tmp_path,
        'bad_virtual4.spec',
        'Name:  docbook-utils\n'
        'Requires:       perl-SGMLSpm\n'
        'Provides:       perl-SGMLSpm\n',
    )
    res = subprocess.run(
        [sys.executable, '-m', 'openruyi_precommit_hooks.check_spec_perl', f],
        capture_output=True,
        text=True,
        check=False,
    )
    assert res.returncode == 1
    assert 'perl(MODULE)' in res.stdout
    assert 'perl-SGMLSpm' in res.stdout


def test_fail_provides_bare_perl_package(tmp_path):
    f = _write(
        tmp_path,
        'bad_virtual5.spec',
        'Name:  foo\n'
        'Provides:       perl-Foo = %{version}\n',
    )
    assert main([f]) == 1
