# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_url import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_https_official_site(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'URL:            https://www.example.org/\n',
    )
    assert main([f]) == 0


def test_ok_repo_link_without_official_site(tmp_path):
    f = _write(
        tmp_path,
        'good2.spec',
        'URL:            https://github.com/foo/bar\n',
    )
    assert main([f]) == 0


def test_ok_http_link(tmp_path):
    f = _write(
        tmp_path,
        'good3.spec',
        'URL:            http://example.org/project\n',
    )
    assert main([f]) == 0


def test_ok_trailing_slash_and_path(tmp_path):
    f = _write(
        tmp_path,
        'good4.spec',
        'URL:            https://example.org/docs/project/\n',
    )
    assert main([f]) == 0


def test_ok_missing_url_field(tmp_path):
    # presence is covered by check-spec-structure
    f = _write(
        tmp_path,
        'good5.spec',
        'Name:           foo\nVersion:        1.0\n',
    )
    assert main([f]) == 0


def test_ok_empty_value_no_report(tmp_path):
    f = _write(
        tmp_path,
        'good6.spec',
        'URL:\n',
    )
    assert main([f]) == 0


def test_ok_commented_out_url(tmp_path):
    f = _write(
        tmp_path,
        'good7.spec',
        '# URL:            https://example.org\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_bad_macro_name_in_url(tmp_path):
    f = _write(
        tmp_path,
        'bad1.spec',
        'URL:            https://github.com/mreineck/%{name}\n',
    )
    assert main([f]) == 1


def test_bad_macro_srcname_in_url(tmp_path):
    f = _write(
        tmp_path,
        'bad2.spec',
        'URL:            https://pypi.org/project/%{srcname}/\n',
    )
    assert main([f]) == 1


def test_bad_fixme_placeholder(tmp_path):
    f = _write(
        tmp_path,
        'bad3.spec',
        'URL:            FIXME\n',
    )
    assert main([f]) == 1


def test_bad_bare_host_no_scheme(tmp_path):
    f = _write(
        tmp_path,
        'bad4.spec',
        'URL:            www.example.org\n',
    )
    assert main([f]) == 1


def test_bad_macro_and_no_scheme_both_reported(tmp_path):
    f = _write(
        tmp_path,
        'bad5.spec',
        'URL:            %{name}\n',
    )
    # both a macro and a missing scheme -> two errors, exit code 1
    assert main([f]) == 1
