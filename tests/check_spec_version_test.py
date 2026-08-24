# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from pathlib import Path

from openruyi_precommit_hooks.check_spec_version import main


def _write(tmp_path: Path, name: str, content: str) -> str:
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases -------------------------------------------------------

def test_ok_digits_and_dots(tmp_path: Path) -> None:
    content = 'Name:           foo-bar\nVersion:        1.5.7\n'
    retv = main([_write(tmp_path, 'good1.spec', content)])
    assert retv == 0


def test_ok_date_version(tmp_path: Path) -> None:
    content = 'Version:        2025.07\n'
    retv = main([_write(tmp_path, 'good2.spec', content)])
    assert retv == 0


def test_ok_normalized_prerelease(tmp_path: Path) -> None:
    content = 'Version:        3.5.0~rc1\n'
    retv = main([_write(tmp_path, 'good3.spec', content)])
    assert retv == 0


def test_ok_plain_alpha_beta(tmp_path: Path) -> None:
    # Plain letters without the rc/alpha/beta markers are allowed.
    content = 'Version:        5.02c\n'
    retv = main([_write(tmp_path, 'good4.spec', content)])
    assert retv == 0


def test_ok_vcs_snapshot(tmp_path: Path) -> None:
    content = 'Version:        0+git20250808.ee5b7e3\n'
    retv = main([_write(tmp_path, 'good5.spec', content)])
    assert retv == 0


def test_ok_released_version_plus_snapshot(tmp_path: Path) -> None:
    # Upstream released before and now only publishes snapshots: keep
    # the last released version and append the snapshot info.
    content = 'Version:        4.3.1+git20260616.55a9409\n'
    retv = main([_write(tmp_path, 'good5b.spec', content)])
    assert retv == 0


def test_ok_macro_expanded_version(tmp_path: Path) -> None:
    content = 'Version:        %{version}\n'
    retv = main([_write(tmp_path, 'good6.spec', content)])
    assert retv == 0


def test_ok_missing_version_not_reported(tmp_path: Path) -> None:
    # Field presence is covered by check-spec-structure.
    content = 'Name:           foo-bar\nSummary:        x\n'
    retv = main([_write(tmp_path, 'good7.spec', content)])
    assert retv == 0


def test_ok_bare_version_only(tmp_path: Path) -> None:
    content = 'Version:        1.0\n'
    retv = main([_write(tmp_path, 'good8.spec', content)])
    assert retv == 0


# --- failing cases -------------------------------------------------------

def test_uppercase_prerelease(tmp_path: Path) -> None:
    content = 'Version:        3.5.0-RC1\n'
    retv = main([_write(tmp_path, 'bad1.spec', content)])
    assert retv == 1


def test_hyphen_in_version(tmp_path: Path) -> None:
    content = 'Version:        7.1.1-44\n'
    retv = main([_write(tmp_path, 'bad2.spec', content)])
    assert retv == 1


def test_underscore_in_version(tmp_path: Path) -> None:
    content = 'Version:        3_508\n'
    retv = main([_write(tmp_path, 'bad3.spec', content)])
    assert retv == 1


def test_vcs_commit_hash_version(tmp_path: Path) -> None:
    content = 'Version:        ee5b7e32b961a9da1933e9f46a018ba6cac8ef60\n'
    retv = main([_write(tmp_path, 'bad4.spec', content)])
    assert retv == 1


def test_uppercase_rc_matches_regex(tmp_path: Path) -> None:
    content = 'Version:        1.6RC1\n'
    retv = main([_write(tmp_path, 'bad5.spec', content)])
    assert retv == 1


def test_multiple_violations(tmp_path: Path) -> None:
    content = 'Version:        3.0_A9-1\n'
    retv = main([_write(tmp_path, 'bad6.spec', content)])
    assert retv == 1


def test_snapshot_missing_scm(tmp_path: Path) -> None:
    # ``+`` must be followed by an SCM name and date.
    content = 'Version:        10.2+2.0.2\n'
    retv = main([_write(tmp_path, 'bad7.spec', content)])
    assert retv == 1


def test_snapshot_bad_date_length(tmp_path: Path) -> None:
    # The date part must be exactly 8 digits (YYYYMMDD).
    content = 'Version:        0+git202608018.7828495\n'
    retv = main([_write(tmp_path, 'bad8.spec', content)])
    assert retv == 1
