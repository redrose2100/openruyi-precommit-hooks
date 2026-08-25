# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_vcs import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_git_scheme_cloneable_link(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'VCS:            git:https://git.example.org/project.git\n',
    )
    assert main([f]) == 0


def test_ok_github_http_link(tmp_path):
    f = _write(
        tmp_path,
        'good2.spec',
        'VCS:            https://github.com/foo/bar\n',
    )
    assert main([f]) == 0


def test_ok_gitlab_http_link(tmp_path):
    f = _write(
        tmp_path,
        'good3.spec',
        'VCS:            https://gitlab.com/foo/bar\n',
    )
    assert main([f]) == 0


def test_ok_no_vcs_link_comment(tmp_path):
    f = _write(
        tmp_path,
        'good4.spec',
        '# VCS: No VCS link available\n',
    )
    assert main([f]) == 0


def test_ok_missing_vcs_field(tmp_path):
    # presence is covered by check-spec-structure
    f = _write(
        tmp_path,
        'good5.spec',
        'Name:           foo\nVersion:        1.0\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_bad_empty_value(tmp_path):
    f = _write(
        tmp_path,
        'bad1.spec',
        'VCS:\n',
    )
    assert main([f]) == 1


def test_bad_placeholder(tmp_path):
    f = _write(
        tmp_path,
        'bad2.spec',
        'VCS:            FIXME\n',
    )
    assert main([f]) == 1


def test_bad_bare_host_no_scheme(tmp_path):
    f = _write(
        tmp_path,
        'bad3.spec',
        'VCS:            git.example.org/project.git\n',
    )
    assert main([f]) == 1


def test_bad_macro_in_vcs(tmp_path):
    f = _write(
        tmp_path,
        'bad4.spec',
        'VCS:            git:https://git.example.org/%{name}.git\n',
    )
    assert main([f]) == 1


def test_bad_wrong_comment_text(tmp_path):
    f = _write(
        tmp_path,
        'bad5.spec',
        '# VCS: no repository available\n',
    )
    assert main([f]) == 1


def test_bad_commented_out_real_link(tmp_path):
    # a ``# VCS:`` comment must be exactly "No VCS link available";
    # any other text (even a real-looking link) is not a valid
    # declaration
    f = _write(
        tmp_path,
        'bad6.spec',
        '# VCS:            git:https://git.example.org/project.git\n',
    )
    assert main([f]) == 1


def test_bad_ftp_link(tmp_path):
    f = _write(
        tmp_path,
        'bad7.spec',
        'VCS:            ftp://ftp.example.org/project\n',
    )
    assert main([f]) == 1
