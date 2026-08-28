# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_rust import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_rust_app_deps_declared(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'BuildSystem:    rust\n'
        'BuildRequires:  rust\n'
        'BuildRequires:  rust-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_rustcrates_deps_declared(tmp_path):
    # a crate provider package only needs the macros, not the compiler
    f = _write(
        tmp_path,
        'good2.spec',
        'BuildSystem:    rustcrates\n'
        'BuildRequires:  rust-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_deps_with_version(tmp_path):
    f = _write(
        tmp_path,
        'good3.spec',
        'BuildSystem:    rust\n'
        'BuildRequires:  rust >= 1.70\n'
        'BuildRequires:  rust-rpm-macros >= 26\n',
    )
    assert main([f]) == 0


def test_ok_extra_deps_ignored(tmp_path):
    f = _write(
        tmp_path,
        'good4.spec',
        'BuildSystem:    rust\n'
        'BuildRequires:  rust\n'
        'BuildRequires:  rust-rpm-macros\n'
        'BuildRequires:  cargo\n'
        'BuildRequires:  pkgconfig(openssl)\n',
    )
    assert main([f]) == 0


def test_ok_not_rust_skipped(tmp_path):
    # the rule only applies to rust/rustcrates
    for bs in ('autotools', 'cmake', 'golang', 'meson', 'pyproject', 'perlbuild'):
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


def test_ok_rust_app_build_option(tmp_path):
    # a rust application may pass arguments to the cargo build stage
    f = _write(
        tmp_path,
        'good_build_option.spec',
        'BuildSystem:    rust\n'
        'BuildRequires:  rust\n'
        'BuildRequires:  rust-rpm-macros\n'
        'BuildOption(build):  --no-default-features --features "foo,bar"\n',
    )
    assert main([f]) == 0


def test_ok_rust_check_option_with_comment(tmp_path):
    f = _write(
        tmp_path,
        'good_check.spec',
        'BuildSystem:    rust\n'
        '# test_body requires network access unavailable in the build env\n'
        'BuildOption(check):  -- --skip test_body\n'
        'BuildRequires:  rust\n'
        'BuildRequires:  rust-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_rust_multi_line_check_comment_on_first(tmp_path):
    # consecutive BuildOption(check) lines form one block; only the
    # first line needs the comment above
    f = _write(
        tmp_path,
        'good_check_block.spec',
        'BuildSystem:    rust\n'
        '# These tests need a running display server\n'
        'BuildOption(check):  -- --skip gui\n'
        'BuildOption(check):  -- --skip egl\n'
        'BuildRequires:  rust\n'
        'BuildRequires:  rust-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_no_check_option(tmp_path):
    f = _write(
        tmp_path,
        'good_no_check.spec',
        'BuildSystem:    rust\n'
        'BuildRequires:  rust\n'
        'BuildRequires:  rust-rpm-macros\n',
    )
    assert main([f]) == 0


def test_ok_subpackage_buildrequires_ignored(tmp_path):
    # BuildRequires inside a %package subpackage block is a different
    # field, but the header one is what matters
    f = _write(
        tmp_path,
        'good_subpackage.spec',
        'BuildSystem:    rust\n'
        'BuildRequires:  rust\n'
        'BuildRequires:  rust-rpm-macros\n'
        '%package  devel\n'
        'BuildRequires:  cargo\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_fail_rust_app_missing_rust(tmp_path):
    f = _write(
        tmp_path,
        'bad1.spec',
        'BuildSystem:    rust\n'
        'BuildRequires:  rust-rpm-macros\n',
    )
    assert main([f]) == 1


def test_fail_rust_app_missing_macros(tmp_path):
    f = _write(
        tmp_path,
        'bad2.spec',
        'BuildSystem:    rust\n'
        'BuildRequires:  rust\n',
    )
    assert main([f]) == 1


def test_fail_rust_app_no_buildrequires(tmp_path):
    f = _write(
        tmp_path,
        'bad3.spec',
        'BuildSystem:    rust\n'
        'Name:  foo\n',
    )
    assert main([f]) == 1


def test_fail_rustcrates_missing_macros(tmp_path):
    f = _write(
        tmp_path,
        'bad4.spec',
        'BuildSystem:    rustcrates\n'
        'BuildRequires:  rust\n',
    )
    assert main([f]) == 1


def test_fail_comment_does_not_count(tmp_path):
    # a commented BuildRequires line is not a declaration
    f = _write(
        tmp_path,
        'bad5.spec',
        'BuildSystem:    rust\n'
        '# BuildRequires:  rust\n'
        '# BuildRequires:  rust-rpm-macros\n',
    )
    assert main([f]) == 1


def test_fail_macro_named_dependency_does_not_count(tmp_path):
    # a dependency whose name is a macro cannot be validated statically
    f = _write(
        tmp_path,
        'bad6.spec',
        'BuildSystem:    rust\n'
        'BuildRequires:  %{?something}\n',
    )
    assert main([f]) == 1


def test_fail_subpackage_br_does_not_count(tmp_path):
    # BuildRequires inside a %package subpackage block is a different
    # field and must not satisfy the header requirement
    f = _write(
        tmp_path,
        'bad7.spec',
        'BuildSystem:    rust\n'
        'Name:  foo\n'
        '%package  devel\n'
        'BuildRequires:  rust\n'
        'BuildRequires:  rust-rpm-macros\n',
    )
    assert main([f]) == 1


def test_fail_rustcrates_build_option(tmp_path):
    # the rustcrates build stage must not be overridden
    f = _write(
        tmp_path,
        'bad8.spec',
        'BuildSystem:    rustcrates\n'
        'BuildRequires:  rust-rpm-macros\n'
        'BuildOption(build):  --features "foo"\n',
    )
    assert main([f]) == 1


def test_fail_check_option_without_comment(tmp_path):
    # the previous non-blank line is not a comment, so the reason is missing
    f = _write(
        tmp_path,
        'bad9.spec',
        'BuildSystem:    rust\n'
        'BuildRequires:  rust\n'
        'BuildRequires:  rust-rpm-macros\n'
        'BuildOption(check):  -- --skip test_body\n',
    )
    assert main([f]) == 1


def test_fail_check_option_after_install_without_comment(tmp_path):
    # a single BuildOption(check) directly after BuildOption(build)
    # has no comment above and must fail
    f = _write(
        tmp_path,
        'bad10.spec',
        'BuildSystem:    rust\n'
        'BuildOption(build):  --no-default-features\n'
        'BuildOption(check):  -- --skip test_body\n'
        'BuildRequires:  rust\n'
        'BuildRequires:  rust-rpm-macros\n',
    )
    assert main([f]) == 1


def test_fail_combined_messages(tmp_path):
    import subprocess
    import sys

    f = _write(
        tmp_path,
        'bad_combined.spec',
        'BuildSystem:    rust\n'
        'BuildOption(check):  -- --skip test_body\n'
        'BuildRequires:  cargo\n',
    )
    res = subprocess.run(
        [sys.executable, '-m', 'openruyi_precommit_hooks.check_spec_rust', f],
        capture_output=True,
        text=True,
        check=False,
    )
    assert res.returncode == 1
    assert 'declare rust' in res.stdout
    assert 'BuildOption(check) must be preceded by a comment' in res.stdout


def test_fail_rustcrates_build_option_message(tmp_path):
    import subprocess
    import sys

    f = _write(
        tmp_path,
        'bad_rustcrates.spec',
        'BuildSystem:    rustcrates\n'
        'BuildRequires:  rust-rpm-macros\n'
        'BuildOption(build):  --features "foo"\n',
    )
    res = subprocess.run(
        [sys.executable, '-m', 'openruyi_precommit_hooks.check_spec_rust', f],
        capture_output=True,
        text=True,
        check=False,
    )
    assert res.returncode == 1
    assert 'BuildOption(build) must not be used' in res.stdout
