# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_files import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_license_and_doc(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        '%install\n'
        '%find_lang %{name}\n'
        '\n'
        '%files -f %{name}.lang\n'
        '%license COPYING\n'
        '%doc README.md\n'
        '%{_bindir}/foo\n',
    )
    assert main([f]) == 0


def test_ok_license_and_doc_coexist(tmp_path):
    # %license and %doc on different files coexist without errors.
    f = _write(
        tmp_path,
        'good2.spec',
        '%files\n'
        '%license LICENSE NOTICE\n'
        '%doc README\n',
    )
    assert main([f]) == 0


def test_fail_license_both_license_and_doc(tmp_path):
    # httpd tools pattern: the same license text installed both with
    # %license and inside %doc -- the %doc side is still reported.
    f = _write(
        tmp_path,
        'bad7.spec',
        '%files\n'
        '%license LICENSE NOTICE\n'
        '%doc LICENSE NOTICE\n',
    )
    assert main([f]) == 1


def test_ok_multiple_files_sections(tmp_path):
    f = _write(
        tmp_path,
        'good3.spec',
        '%files\n'
        '%license COPYING\n'
        '\n'
        '%files devel\n'
        '%doc README\n'
        '%{_libdir}/libfoo.so\n'
        '\n'
        '%files -n libfoo-data\n'
        '%license COPYING\n'
        '%{_datadir}/foo\n',
    )
    assert main([f]) == 0


def test_ok_config_defattr_verify(tmp_path):
    f = _write(
        tmp_path,
        'good4.spec',
        '%files\n'
        '%defattr (-,root,root,-)\n'
        '%config(noreplace) %{_sysconfdir}/foo.conf\n'
        '%verify(not md5 size mtime) %{_bindir}/foo\n'
        '%attr(0755, root, root) %{_bindir}/foo\n',
    )
    assert main([f]) == 0


def test_ok_exclude_and_glob(tmp_path):
    # expat-like: %exclude lines are exclusions, not package contents.
    # Globbing entries cannot be checked for duplicates statically.
    f = _write(
        tmp_path,
        'good5.spec',
        '%files\n'
        '%exclude %{_libdir}/libexpat.la\n'
        '%{_libdir}/*.so.*\n'
        '%doc %{_docdir}/foo/\n',
    )
    assert main([f]) == 0


def test_ok_macro_guard_and_expand(tmp_path):
    f = _write(
        tmp_path,
        'good6.spec',
        '%files\n'
        '%{!?_licensedir:%global license %%doc}\n'
        '%{expand:%%global _foo %%{_bindir}}\n'
        '}}\n'
        '%{_bindir}/foo\n',
    )
    assert main([f]) == 0


def test_ok_path_readme_lowercase_dir_ghost(tmp_path):
    # Paths with a directory component are data files, not docs.
    # %dir / %ghost do not install file content.
    f = _write(
        tmp_path,
        'good7.spec',
        '%files\n'
        '%{_sysconfdir}/ssl/README\n'
        '%dir %{_libexecdir}/foo\n'
        '%ghost %{_datadir}/foo/README\n',
    )
    assert main([f]) == 0


def test_ok_conditional_duplicates(tmp_path):
    # Same path in mutually exclusive %if branches is not a duplicate.
    f = _write(
        tmp_path,
        'good8.spec',
        '%files\n'
        '%if 0%{?rhel}\n'
        '%{_bindir}/foo\n'
        '%else\n'
        '%{_bindir}/foo\n'
        '%endif\n',
    )
    assert main([f]) == 0


def test_ok_lang_directive(tmp_path):
    f = _write(
        tmp_path,
        'good9.spec',
        '%files\n'
        '%lang(de) %{_datadir}/locale/de/LC_MESSAGES/foo.mo\n'
        '%lang(en) %{_datadir}/locale/en/LC_MESSAGES/foo.mo\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_fail_license_in_doc(tmp_path):
    f = _write(
        tmp_path,
        'bad1.spec',
        '%files\n'
        '%doc LICENSE\n'
        '%{_bindir}/foo\n',
    )
    assert main([f]) == 1


def test_fail_license_bare_plain(tmp_path):
    # A bare license-name token without %doc or %license.
    f = _write(
        tmp_path,
        'bad2.spec',
        '%files\n'
        'LICENSE\n',
    )
    assert main([f]) == 1


def test_fail_doc_bare(tmp_path):
    # A bare README-like token should be marked with %doc.
    f = _write(
        tmp_path,
        'bad3.spec',
        '%files\n'
        'README\n',
    )
    assert main([f]) == 1


def test_fail_duplicate(tmp_path):
    # Duplicate detection only applies to literal paths; macro paths
    # (%{...}) may expand differently and are not compared.
    f = _write(
        tmp_path,
        'bad4.spec',
        '%files\n'
        '/usr/share/foo/bar\n'
        '/usr/share/foo/bar\n',
    )
    assert main([f]) == 1


def test_ok_macro_duplicates(tmp_path):
    # The same macro path twice is not a violation: the macro may
    # expand to different paths in different contexts.
    f = _write(
        tmp_path,
        'ok10.spec',
        '%files\n'
        '%{_bindir}/foo\n'
        '%{_bindir}/foo\n',
    )
    assert main([f]) == 0


def test_fail_la_file(tmp_path):
    f = _write(
        tmp_path,
        'bad5.spec',
        '%files\n'
        '%{_libdir}/libfoo.la\n',
    )
    assert main([f]) == 1


def test_fail_locale_glob(tmp_path):
    f = _write(
        tmp_path,
        'bad6.spec',
        '%files\n'
        '%{_datadir}/locale/*\n',
    )
    assert main([f]) == 1


# --- error handling ---------------------------------------------------------

def test_error_missing_file(tmp_path):
    f = str(tmp_path / 'nope.spec')
    assert main([f]) == 1


def test_error_empty_file(tmp_path):
    f = _write(tmp_path, 'empty.spec', '')
    assert main([f]) == 1


def test_error_not_utf8(tmp_path):
    p = tmp_path / 'bad_enc.spec'
    p.write_bytes(b'%files\n\xff\xfe\n')
    assert main([str(p)]) == 1
