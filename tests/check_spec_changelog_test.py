# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_changelog import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_plain_autochangelog(tmp_path):
    # %autochangelog directly; the canonical form
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
        'BuildSystem:    autotools\n'
        '\n'
        '%changelog\n'
        '%autochangelog\n',
    )
    assert main([f]) == 0


def test_ok_conditional_autochangelog(tmp_path):
    # %{?autochangelog} expands only when %autochangelog is defined; the
    # openRuyi repository uses this form in many packages
    f = _write(
        tmp_path,
        'good2.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%changelog\n'
        '%{?autochangelog}\n',
    )
    assert main([f]) == 0


def test_ok_comments_around_autochangelog(tmp_path):
    # comments inside the section are allowed as long as the section
    # still contains the autochangelog macro
    f = _write(
        tmp_path,
        'good3.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%changelog\n'
        '# generated from git history\n'
        '%autochangelog\n',
    )
    assert main([f]) == 0


def test_ok_autochangelog_with_whitespace(tmp_path):
    # the macro may be indented
    f = _write(
        tmp_path,
        'good4.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%changelog\n'
        '  %autochangelog\n',
    )
    assert main([f]) == 0


def test_ok_no_changelog_section(tmp_path):
    # a spec without a %changelog section passes; presence is a
    # structure concern covered by check-spec-structure
    f = _write(
        tmp_path,
        'good5.spec',
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


# --- failing cases ----------------------------------------------------------

def test_bad_handwritten_changelog(tmp_path):
    # traditional handwritten entries violate the rule
    f = _write(
        tmp_path,
        'bad1.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%changelog\n'
        '* Mon Aug 26 2026 Jane Doe <jane@example.org> - 1.0-1\n'
        '- initial package\n',
    )
    assert main([f]) == 1


def test_bad_empty_changelog(tmp_path):
    # %changelog alone without %autochangelog is reported
    f = _write(
        tmp_path,
        'bad2.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%changelog\n',
    )
    assert main([f]) == 1


def test_bad_comment_only_changelog(tmp_path):
    # comments alone do not satisfy "%changelog must be %autochangelog"
    f = _write(
        tmp_path,
        'bad3.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%changelog\n'
        '# TODO: add changelog\n',
    )
    assert main([f]) == 1


def test_bad_partial_autochangelog_typo(tmp_path):
    # a close-but-not-quite macro is still handwritten content
    f = _write(
        tmp_path,
        'bad4.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%changelog\n'
        '%autochangelg\n',
    )
    assert main([f]) == 1


def test_bad_mixed_section(tmp_path):
    # handwritten entries plus %autochangelog: the handwritten entries
    # must be removed
    f = _write(
        tmp_path,
        'bad5.spec',
        'BuildSystem:    autotools\n'
        '\n'
        '%changelog\n'
        '* Mon Aug 26 2026 Jane Doe <jane@example.org> - 1.0-1\n'
        '- initial package\n'
        '%autochangelog\n',
    )
    assert main([f]) == 1
