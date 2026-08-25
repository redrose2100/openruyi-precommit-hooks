# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_buildsystem import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_autotools(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'BuildSystem:    autotools\n',
    )
    assert main([f]) == 0


def test_ok_all_guideline_values(tmp_path):
    for value in (
        'autotools', 'cmake', 'meson', 'golang',
        'golangmodules', 'pyproject',
    ):
        f = _write(
            tmp_path,
            f'good_{value}.spec',
            f'BuildSystem:    {value}\n',
        )
        assert main([f]) == 0


def test_ok_repo_additional_values(tmp_path):
    # the guidelines allow "other newly added values"; the openRuyi
    # repository uses these additional build systems
    for value in ('perlbuild', 'perlmaker', 'rust', 'rustcrates'):
        f = _write(
            tmp_path,
            f'good_{value}.spec',
            f'BuildSystem:    {value}\n',
        )
        assert main([f]) == 0


def test_ok_empty_with_comment_above(tmp_path):
    # an empty BuildSystem is allowed when the reason is explained in a
    # comment on the line directly above
    f = _write(
        tmp_path,
        'good_comment_above.spec',
        '# no configuration stage needed\n'
        'BuildSystem:\n',
    )
    assert main([f]) == 0


def test_ok_empty_with_comment_same_line(tmp_path):
    # an empty BuildSystem is allowed when the reason is explained in a
    # comment on the same line
    f = _write(
        tmp_path,
        'good_comment_same_line.spec',
        'BuildSystem:    # no configuration stage needed\n',
    )
    assert main([f]) == 0


def test_ok_missing_buildsystem_field(tmp_path):
    # BuildSystem is a mandatory header field; presence is covered by
    # check-spec-structure
    f = _write(
        tmp_path,
        'good_missing.spec',
        'Name:           foo\nVersion:        1.0\n',
    )
    assert main([f]) == 0


def test_ok_buildsystem_in_subpackage_ignored(tmp_path):
    # BuildSystem inside a %package subpackage block is a different
    # field and is not covered by this rule
    f = _write(
        tmp_path,
        'good_subpackage.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%package        devel\n'
        'BuildSystem:    cmake\n',
    )
    assert main([f]) == 0


def test_ok_commented_out_buildsystem(tmp_path):
    # a commented-out BuildSystem line is not a real field
    f = _write(
        tmp_path,
        'good_commented.spec',
        '# BuildSystem:  autotools\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_bad_empty_without_comment(tmp_path):
    # an empty BuildSystem without an explanatory comment is a violation
    f = _write(
        tmp_path,
        'bad_empty.spec',
        'BuildSystem:\n',
    )
    assert main([f]) == 1


def test_bad_empty_comment_not_adjacent(tmp_path):
    # the explanatory comment must be on the same line or directly above
    f = _write(
        tmp_path,
        'bad_empty_far_comment.spec',
        '# no configuration stage needed\n'
        '\n'
        'BuildSystem:\n',
    )
    assert main([f]) == 1


def test_bad_unknown_value(tmp_path):
    # an unknown build system is reported so a maintainer can confirm
    # whether it is a newly added value
    f = _write(
        tmp_path,
        'bad_unknown.spec',
        'BuildSystem:    make\n',
    )
    assert main([f]) == 1


def test_bad_unknown_value_with_whitespace(tmp_path):
    f = _write(
        tmp_path,
        'bad_unknown_ws.spec',
        'BuildSystem:    custom-build\n',
    )
    assert main([f]) == 1
