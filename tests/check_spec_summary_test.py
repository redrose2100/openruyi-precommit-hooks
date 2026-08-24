# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from pathlib import Path

from openruyi_precommit_hooks.check_spec_summary import main


def _write(tmp_path: Path, name: str, content: str) -> str:
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases -------------------------------------------------------

def test_ok_plain_ascii(tmp_path: Path) -> None:
    content = 'Summary:        A tool for building packages\n'
    retv = main([_write(tmp_path, 'good1.spec', content)])
    assert retv == 0


def test_ok_period_not_at_the_end(tmp_path: Path) -> None:
    # Dots inside the value (e.g. version numbers) are fine.
    content = 'Summary:        Version 1.5.7 of the example tool\n'
    retv = main([_write(tmp_path, 'good2.spec', content)])
    assert retv == 0


def test_ok_macro_expanded_summary(tmp_path: Path) -> None:
    # A macro-expanded value cannot be judged statically.
    content = 'Summary:        %{name} library\n'
    retv = main([_write(tmp_path, 'good3.spec', content)])
    assert retv == 0


def test_ok_missing_summary_not_reported(tmp_path: Path) -> None:
    # Field presence is covered by check-spec-structure.
    content = 'Name:           foo-bar\nVersion:        1.0\n'
    retv = main([_write(tmp_path, 'good4.spec', content)])
    assert retv == 0


def test_ok_trailing_whitespace_stripped(tmp_path: Path) -> None:
    content = 'Summary:        A tool for building packages   \n'
    retv = main([_write(tmp_path, 'good5.spec', content)])
    assert retv == 0


def test_ok_decorative_symbols_not_flagged(tmp_path: Path) -> None:
    # An en-dash is a decorative symbol, not a non-English language.
    content = 'Summary:        A fast tool \u2014 no fluff\n'
    retv = main([_write(tmp_path, 'good6.spec', content)])
    assert retv == 0


# --- failing cases -------------------------------------------------------

def test_trailing_period(tmp_path: Path) -> None:
    content = 'Summary:        A tool for building packages.\n'
    retv = main([_write(tmp_path, 'bad1.spec', content)])
    assert retv == 1


def test_cjk_chinese_summary(tmp_path: Path) -> None:
    content = 'Summary:        软件包功能描述\n'
    retv = main([_write(tmp_path, 'bad2.spec', content)])
    assert retv == 1


def test_fullwidth_period(tmp_path: Path) -> None:
    # A full-width period is not an English introduction.
    content = 'Summary:        软件包功能描述。\n'
    retv = main([_write(tmp_path, 'bad3.spec', content)])
    assert retv == 1


def test_both_violations(tmp_path: Path) -> None:
    content = 'Summary:        中文功能描述。\n'
    retv = main([_write(tmp_path, 'bad4.spec', content)])
    assert retv == 1
