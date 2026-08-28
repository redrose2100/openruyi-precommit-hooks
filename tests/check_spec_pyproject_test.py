# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_pyproject import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_pyproject_deps_declared(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'BuildSystem:    pyproject\n'
        'BuildRequires:  pyproject-rpm-macros\n'
        'BuildRequires:  pkgconfig(python3)\n',
    )
    assert main([f]) == 0


def test_ok_deps_with_version(tmp_path):
    f = _write(
        tmp_path,
        'good2.spec',
        'BuildSystem:    pyproject\n'
        'BuildRequires:  pyproject-rpm-macros >= 1\n',
    )
    assert main([f]) == 0


def test_ok_extra_deps_ignored(tmp_path):
    # python3dist(...) virtual dependencies and other extras do not affect the rule
    f = _write(
        tmp_path,
        'good3.spec',
        'BuildSystem:    pyproject\n'
        'BuildRequires:  pyproject-rpm-macros\n'
        'BuildRequires:  python3dist(setuptools)\n'
        'BuildRequires:  python3dist(wheel)\n',
    )
    assert main([f]) == 0


def test_ok_not_pyproject_skipped(tmp_path):
    # the rule only applies to pyproject
    for bs in ('autotools', 'cmake', 'golang', 'meson', 'perlbuild', 'perlmaker'):
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


def test_ok_install_option_with_module(tmp_path):
    f = _write(
        tmp_path,
        'good_install.spec',
        'BuildSystem:    pyproject\n'
        'BuildOption(install):  -l example_pkg\n'
        'BuildRequires:  pyproject-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_install_option_module_only(tmp_path):
    # the module name itself, without -l, is fine
    f = _write(
        tmp_path,
        'good_install_plain.spec',
        'BuildSystem:    pyproject\n'
        'BuildOption(install):  example_pkg\n'
        'BuildRequires:  pyproject-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_install_option_macro(tmp_path):
    f = _write(
        tmp_path,
        'good_install_macro.spec',
        'BuildSystem:    pyproject\n'
        'BuildOption(install):  -l %{srcname} +auto\n'
        'BuildRequires:  pyproject-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_no_install_option(tmp_path):
    f = _write(
        tmp_path,
        'good_no_install.spec',
        'BuildSystem:    pyproject\n'
        'BuildRequires:  pyproject-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_check_option_with_comment(tmp_path):
    f = _write(
        tmp_path,
        'good_check.spec',
        'BuildSystem:    pyproject\n'
        '# No module named pygments\n'
        'BuildOption(check):  -e example_pkg.support\n'
        'BuildRequires:  pyproject-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_check_option_multi_line_comment_on_first(tmp_path):
    # consecutive BuildOption(check) lines form one block; only the
    # first line needs the comment above
    f = _write(
        tmp_path,
        'good_check_block.spec',
        'BuildSystem:    pyproject\n'
        '# Build helper modules require the source tree as their cwd\n'
        'BuildOption(check):  -e a.b\n'
        'BuildOption(check):  -e a.c\n'
        'BuildRequires:  pyproject-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_header_with_extra_lines_before_comment(tmp_path):
    # the comment may be further above as long as no BuildOption line
    # separates it (blank/other lines are fine)
    f = _write(
        tmp_path,
        'good_check_comment_far.spec',
        'BuildSystem:    pyproject\n'
        'BuildOption(install):  -l example_pkg\n'
        '\n'
        '# No module named marray\n'
        'BuildOption(check):  -e example_pkg.tests*\n'
        'BuildRequires:  pyproject-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_subpackage_buildrequires_ignored_for_presence(tmp_path):
    # BuildRequires inside a %package subpackage block is a different
    # field, but the header one is what matters
    f = _write(
        tmp_path,
        'good_subpackage.spec',
        'BuildSystem:    pyproject\n'
        'BuildRequires:  pyproject-rpm-macros\n'
        '%package  devel\n'
        'BuildRequires:  python3-devel\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_fail_missing_pyproject_rpm_macros(tmp_path):
    f = _write(
        tmp_path,
        'bad1.spec',
        'BuildSystem:    pyproject\n'
        'BuildRequires:  pkgconfig(python3)\n',
    )
    assert main([f]) == 1


def test_fail_no_buildrequires(tmp_path):
    f = _write(
        tmp_path,
        'bad2.spec',
        'BuildSystem:    pyproject\n'
        'Name:  foo\n',
    )
    assert main([f]) == 1


def test_fail_comment_does_not_count(tmp_path):
    # a commented BuildRequires line is not a declaration
    f = _write(
        tmp_path,
        'bad3.spec',
        'BuildSystem:    pyproject\n'
        '# BuildRequires:  pyproject-rpm-macros\n',
    )
    assert main([f]) == 1


def test_fail_macro_named_dependency_does_not_count(tmp_path):
    # a dependency whose name is a macro cannot be validated statically
    f = _write(
        tmp_path,
        'bad4.spec',
        'BuildSystem:    pyproject\n'
        'BuildRequires:  %{?something}\n',
    )
    assert main([f]) == 1


def test_fail_subpackage_br_does_not_count(tmp_path):
    # BuildRequires inside a %package subpackage block is a different
    # field and must not satisfy the header requirement
    f = _write(
        tmp_path,
        'bad5.spec',
        'BuildSystem:    pyproject\n'
        'Name:  foo\n'
        '%package  devel\n'
        'BuildRequires:  pyproject-rpm-macros\n',
    )
    assert main([f]) == 1


def test_fail_install_option_empty(tmp_path):
    f = _write(
        tmp_path,
        'bad_install_empty.spec',
        'BuildSystem:    pyproject\n'
        'BuildOption(install):\n'
        'BuildRequires:  pyproject-rpm-macros\n',
    )
    assert main([f]) == 1


def test_fail_check_option_without_comment(tmp_path):
    # the previous non-blank line is not a comment, so the reason is missing
    f = _write(
        tmp_path,
        'bad_check.spec',
        'BuildSystem:    pyproject\n'
        'BuildRequires:  pyproject-rpm-macros\n'
        'BuildOption(check):  -e example_pkg.tests*\n',
    )
    assert main([f]) == 1


def test_fail_check_option_after_install_without_comment(tmp_path):
    # a single BuildOption(check) directly after BuildOption(install)
    # has no comment above and must fail
    f = _write(
        tmp_path,
        'bad_check_single.spec',
        'BuildSystem:    pyproject\n'
        'BuildOption(install):  -l example_pkg\n'
        'BuildOption(check):  -e example_pkg.tests*\n'
        'BuildRequires:  pyproject-rpm-macros\n',
    )
    assert main([f]) == 1


def test_fail_combined_messages(tmp_path):
    import subprocess
    import sys

    f = _write(
        tmp_path,
        'bad_combined.spec',
        'BuildSystem:    pyproject\n'
        'BuildOption(check):  -e x.y\n'
        'BuildRequires:  pkgconfig(python3)\n',
    )
    res = subprocess.run(
        [sys.executable, '-m', 'openruyi_precommit_hooks.check_spec_pyproject', f],
        capture_output=True,
        text=True,
        check=False,
    )
    assert res.returncode == 1
    assert 'declare pyproject-rpm-macros' in res.stdout
    assert 'BuildOption(check) must be preceded by a comment' in res.stdout
