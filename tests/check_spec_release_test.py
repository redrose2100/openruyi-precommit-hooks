# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from pathlib import Path

from openruyi_precommit_hooks.check_spec_release import main


def _write(tmp_path: Path, name: str, content: str) -> str:
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases -------------------------------------------------------

def test_ok_autorelease(tmp_path: Path) -> None:
    content = 'Name:           foo-bar\nRelease:        %autorelease\n'
    retv = main([_write(tmp_path, 'good1.spec', content)])
    assert retv == 0


def test_ok_bracket_autorelease(tmp_path: Path) -> None:
    content = 'Release:        %{autorelease}\n'
    retv = main([_write(tmp_path, 'good2.spec', content)])
    assert retv == 0


def test_ok_autorelease_with_other_macros(tmp_path: Path) -> None:
    # Kernel-style release combining macros with %autorelease.
    content = 'Release:        %{patchset_release}.%{config_version}_%autorelease\n'
    retv = main([_write(tmp_path, 'good3.spec', content)])
    assert retv == 0


def test_ok_macro_expanded_release(tmp_path: Path) -> None:
    # A macro-expanded value such as 1%{?dist} cannot be judged
    # statically.
    content = 'Release:        1%{?dist}\n'
    retv = main([_write(tmp_path, 'good4.spec', content)])
    assert retv == 0


def test_ok_missing_release_not_reported(tmp_path: Path) -> None:
    # Field presence is covered by check-spec-structure.
    content = 'Name:           foo-bar\nSummary:        x\n'
    retv = main([_write(tmp_path, 'good5.spec', content)])
    assert retv == 0


def test_ok_autorelease_with_other_global(tmp_path: Path) -> None:
    # A global macro that is not the dist macro passes.
    content = (
        'Release:        %autorelease\n'
        '%global myrelease 1\n'
    )
    retv = main([_write(tmp_path, 'good6.spec', content)])
    assert retv == 0


def test_ok_literal_dist_reference(tmp_path: Path) -> None:
    # Referencing %{dist} without overriding it is allowed.
    content = 'Release:        %autorelease\n%global mydist %{dist}\n'
    retv = main([_write(tmp_path, 'good7.spec', content)])
    assert retv == 0


# --- failing cases -------------------------------------------------------

def test_plain_integer_should_use_autorelease(tmp_path: Path) -> None:
    content = 'Release:        3\n'
    retv = main([_write(tmp_path, 'bad1.spec', content)])
    assert retv == 1


def test_zero_revision(tmp_path: Path) -> None:
    content = 'Release:        0\n'
    retv = main([_write(tmp_path, 'bad2.spec', content)])
    assert retv == 1


def test_hardcoded_dist_suffix(tmp_path: Path) -> None:
    content = 'Release:        1.fc40\n'
    retv = main([_write(tmp_path, 'bad3.spec', content)])
    assert retv == 1


def test_hardcoded_el_suffix(tmp_path: Path) -> None:
    content = 'Release:        2.el9\n'
    retv = main([_write(tmp_path, 'bad4.spec', content)])
    assert retv == 1


def test_non_numeric_tail_with_macro(tmp_path: Path) -> None:
    # 1.fc40%{?dist} hardcodes a suffix even though a macro is used.
    content = 'Release:        1.fc40%{?dist}\n'
    retv = main([_write(tmp_path, 'bad5.spec', content)])
    assert retv == 1


def test_literal_zero_with_macro(tmp_path: Path) -> None:
    content = 'Release:        0%{?dist}\n'
    retv = main([_write(tmp_path, 'bad6.spec', content)])
    assert retv == 1


def test_non_numeric_release(tmp_path: Path) -> None:
    content = 'Release:        rc1\n'
    retv = main([_write(tmp_path, 'bad7.spec', content)])
    assert retv == 1


def test_dist_global_override(tmp_path: Path) -> None:
    content = 'Release:        %autorelease\n%global dist foo\n'
    retv = main([_write(tmp_path, 'bad8.spec', content)])
    assert retv == 1


def test_dist_define_override(tmp_path: Path) -> None:
    content = 'Release:        %autorelease\n%define dist .fc40\n'
    retv = main([_write(tmp_path, 'bad9.spec', content)])
    assert retv == 1


def test_multiple_violations(tmp_path: Path) -> None:
    content = 'Release:        0.fc40\n'
    retv = main([_write(tmp_path, 'bad10.spec', content)])
    assert retv == 1