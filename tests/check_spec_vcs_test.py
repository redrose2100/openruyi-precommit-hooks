from __future__ import annotations

from openruyi_precommit_hooks.check_spec_vcs import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_url_points_to_repo(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'URL:            https://github.com/foo/bar\n',
    )
    assert main([f]) == 0


def test_ok_vcs_comment_no_link(tmp_path):
    f = _write(
        tmp_path,
        'good2.spec',
        '# VCS: No VCS link available\n',
    )
    assert main([f]) == 0


def test_ok_vcs_git_cloneable(tmp_path):
    f = _write(
        tmp_path,
        'good3.spec',
        'VCS:            git:https://git.example.org/project.git\n',
    )
    assert main([f]) == 0


def test_ok_skip_macro_expanded_vcs(tmp_path):
    f = _write(
        tmp_path,
        'good4.spec',
        'VCS:            %{-some-macro-}\n',
    )
    assert main([f]) == 0


# --- failing cases ---------------------------------------------------------

def test_missing_vcs_and_non_repo_url(tmp_path):
    f = _write(
        tmp_path,
        'bad1.spec',
        'URL:            https://example.org/project\n',
    )
    assert main([f]) == 1


def test_bad_git_prefix_not_cloneable(tmp_path):
    f = _write(
        tmp_path,
        'bad2.spec',
        'VCS:            git:example.org/project\n',
    )
    assert main([f]) == 1
