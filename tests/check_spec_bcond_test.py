# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_bcond import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_no_conditional_build(tmp_path):
    # a spec without any conditional-build switch passes
    f = _write(
        tmp_path,
        'good1.spec',
        'Name:           foo\n'
        'Version:        1.0\n'
        'Release:        %autorelease\n'
        'Summary:        Foo package\n'
        'License:        MIT\n'
        'URL:            https://example.org/foo\n'
        'VCS:            git:https://example.org/foo.git\n'
        'Source:         https://example.org/foo-%{version}.tar.gz\n'
        'BuildSystem:    autotools\n',
    )
    assert main([f]) == 0


def test_ok_modern_bcond_with_ref(tmp_path):
    # %bcond declaration plus %{with} reference: the canonical form
    f = _write(
        tmp_path,
        'good2.spec',
        'Name:           foo\n'
        'Version:        1.0\n'
        'Release:        %autorelease\n'
        'Summary:        Foo package\n'
        'License:        MIT\n'
        'BuildSystem:    autotools\n'
        '\n'
        '%bcond bootstrap 0\n'
        '\n'
        '%package devel\n'
        'Summary:        Development files\n'
        '\n'
        '%if %{with bootstrap}\n'
        '# skip tests during bootstrap\n'
        '%endif\n',
    )
    assert main([f]) == 0


def test_ok_bcond_after_ref(tmp_path):
    # declaration order does not matter; the reference may precede it
    f = _write(
        tmp_path,
        'good3.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%if %{with doc}\n'
        'BuildRequires:  doxygen\n'
        '%endif\n'
        '\n'
        '%bcond doc 0\n',
    )
    assert main([f]) == 0


def test_ok_without_reference(tmp_path):
    # %{without x} needs the same declaration as %{with x}
    f = _write(
        tmp_path,
        'good4.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%bcond bootstrap 1\n'
        '\n'
        '%if %{without bootstrap}\n'
        'BuildRequires:  gcc\n'
        '%endif\n',
    )
    assert main([f]) == 0


def test_ok_mixed_defaults(tmp_path):
    # several switches, some defaulted on, some off
    f = _write(
        tmp_path,
        'good5.spec',
        'BuildSystem:    cmake\n'
        '\n'
        '%bcond tests 0\n'
        '%bcond docs 1\n'
        '%bcond systemd 0\n'
        '\n'
        '%if %{with tests}\n'
        'BuildRequires:  pytest\n'
        '%endif\n'
        '\n'
        '%if %{without docs}\n'
        '# docs forced off\n'
        '%endif\n',
    )
    assert main([f]) == 0


def test_ok_commented_legacy_macro(tmp_path):
    # commented-out lines are ignored, even when they carry the legacy
    # macro name or references
    f = _write(
        tmp_path,
        'good6.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '# %bcond_with openssl (replaced upstream by %bcond openssl 0)\n'
        '# %if %{with openssl}\n'
        '# %endif\n',
    )
    assert main([f]) == 0


def test_legacy_macro_counts_as_declaration(tmp_path):
    # even though %bcond_with is reported (rule 1), its switch name
    # still counts as declared, so the %{with openssl} reference does
    # not additionally trigger the undeclared-switch error: only the
    # legacy-macro error is reported
    f = _write(
        tmp_path,
        'good7.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%bcond_with openssl\n'
        '%if %{with openssl}\n'
        'BuildRequires:  openssl-devel\n'
        '%endif\n',
    )
    out = _run(f)
    assert 'legacy %bcond_with must be replaced' in out
    assert 'undeclared switch' not in out


# --- failing cases ----------------------------------------------------------

def test_bad_legacy_bcond_with(tmp_path):
    f = _write(
        tmp_path,
        'bad1.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%bcond_with openssl\n'
        '\n'
        '%if %{with openssl}\n'
        'BuildRequires:  openssl-devel\n'
        '%endif\n',
    )
    out = _run(f)
    assert 'legacy %bcond_with must be replaced' in out


def test_bad_legacy_bcond_without(tmp_path):
    f = _write(
        tmp_path,
        'bad2.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%bcond_without pkgconfig_compat\n',
    )
    out = _run(f)
    assert 'legacy %bcond_without must be replaced' in out


def test_bad_undeclared_reference(tmp_path):
    f = _write(
        tmp_path,
        'bad3.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%if %{with static}\n'
        'BuildRequires:  glibc-static\n'
        '%endif\n',
    )
    out = _run(f)
    assert '%{with static} references an undeclared switch' in out


def test_bad_undeclared_without_reference(tmp_path):
    f = _write(
        tmp_path,
        'bad4.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%if %{without bootstrap}\n'
        '# nothing\n'
        '%endif\n',
    )
    out = _run(f)
    assert '%{without bootstrap} references an undeclared switch' in out


def test_bad_both_rules_same_file(tmp_path):
    # one legacy macro and one undeclared reference in the same file:
    # both are reported
    f = _write(
        tmp_path,
        'bad5.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%bcond_with guile\n'
        '\n'
        '%if %{with guile}\n'
        'BuildRequires:  guile-devel\n'
        '%endif\n'
        '\n'
        '%if %{with extra}\n'
        '# undeclared\n'
        '%endif\n',
    )
    out = _run(f)
    assert 'legacy %bcond_with must be replaced' in out
    assert '%{with extra} references an undeclared switch' in out


def test_bad_reports_line_numbers(tmp_path):
    f = _write(
        tmp_path,
        'bad6.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%if %{with doc}\n'
        '%endif\n',
    )
    out = _run(f)
    assert ':3:' in out


def test_bad_duplicate_references_reported_once_per_line(tmp_path):
    # the same undeclared switch referenced twice on one line yields
    # two messages (one per reference), while two lines each referencing
    # it once also yield two messages total
    f = _write(
        tmp_path,
        'bad7.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%if %{with doc} || %{with doc}\n'
        '%endif\n'
        '%if %{with doc}\n'
        '%endif\n',
    )
    out = _run(f)
    assert out.count('%{with doc} references an undeclared switch') == 3


def _run(filename):
    import subprocess
    import sys
    proc = subprocess.run(
        [sys.executable, '-m', 'openruyi_precommit_hooks.check_spec_bcond',
         filename],
        capture_output=True, text=True,
    )
    return proc.stdout + proc.stderr


if __name__ == '__main__':
    # allow a quick manual run: python tests/check_spec_bcond_test.py f.spec
    import sys
    if len(sys.argv) > 1:
        print(_run(sys.argv[1]))