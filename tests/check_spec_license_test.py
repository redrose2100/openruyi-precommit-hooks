# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from pathlib import Path

from openruyi_precommit_hooks.check_spec_license import main


def _write(tmp_path: Path, name: str, content: str) -> str:
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases -------------------------------------------------------

def test_ok_single_identifier(tmp_path: Path) -> None:
    content = 'License:        MIT\n'
    retv = main([_write(tmp_path, 'good1.spec', content)])
    assert retv == 0


def test_ok_and_expression(tmp_path: Path) -> None:
    content = 'License:        GPL-3.0-or-later AND GPL-2.0-or-later AND CC0-1.0\n'
    retv = main([_write(tmp_path, 'good2.spec', content)])
    assert retv == 0


def test_ok_or_expression(tmp_path: Path) -> None:
    content = 'License:        GPL-1.0-or-later OR Artistic-1.0-Perl\n'
    retv = main([_write(tmp_path, 'good3.spec', content)])
    assert retv == 0


def test_ok_with_exception(tmp_path: Path) -> None:
    content = 'License:        GPL-3.0-only WITH Qt-GPL-exception-1.0\n'
    retv = main([_write(tmp_path, 'good4.spec', content)])
    assert retv == 0


def test_ok_later_suffix_not_flagged(tmp_path: Path) -> None:
    # The ``-or-later`` suffix contains ``or`` but is part of the SPDX
    # identifier and must never be treated as a lowercase operator.
    content = 'License:        GPL-3.0-or-later\n'
    retv = main([_write(tmp_path, 'good9.spec', content)])
    assert retv == 0


def test_ok_grouped_expression(tmp_path: Path) -> None:
    content = 'License:        (Apache-2.0 OR MIT) AND BSD-3-Clause\n'
    retv = main([_write(tmp_path, 'good5.spec', content)])
    assert retv == 0


def test_ok_license_ref(tmp_path: Path) -> None:
    content = 'License:        LicenseRef-openRuyi-Public-Domain\n'
    retv = main([_write(tmp_path, 'good6.spec', content)])
    assert retv == 0


def test_ok_macro_expanded_value(tmp_path: Path) -> None:
    # Values that expand at build time cannot be judged statically.
    content = 'License:        %{license}\n'
    retv = main([_write(tmp_path, 'good7.spec', content)])
    assert retv == 0


def test_ok_missing_field_covered_elsewhere(tmp_path: Path) -> None:
    # Field presence is covered by check-spec-structure, so a spec
    # without a License line passes here.
    content = 'Name:           example\n'
    retv = main([_write(tmp_path, 'good8.spec', content)])
    assert retv == 0


# --- failing cases -------------------------------------------------------

def test_bad_lowercase_and(tmp_path: Path) -> None:
    content = 'License:        BSD and MIT and zlib\n'
    retv = main([_write(tmp_path, 'bad1.spec', content)])
    assert retv == 1


def test_bad_lowercase_or_inside_group(tmp_path: Path) -> None:
    # Lowercase operators inside parentheses are flagged too.
    content = 'License:        (MIT or PSF-2.0)\n'
    retv = main([_write(tmp_path, 'bad5.spec', content)])
    assert retv == 1


def test_ok_uppercase_with_not_flagged(tmp_path: Path) -> None:
    # ``WITH`` is a valid uppercase SPDX operator.
    content = 'License:        Apache-2.0 WITH LLVM-exception\n'
    retv = main([_write(tmp_path, 'good10.spec', content)])
    assert retv == 0


def test_bad_lowercase_or_with_parens(tmp_path: Path) -> None:
    content = 'License:        BSD-3-Clause and (CDDL-1.0 or LGPL-2.1-only)\n'
    retv = main([_write(tmp_path, 'bad2.spec', content)])
    assert retv == 1


def test_bad_comma_separator(tmp_path: Path) -> None:
    content = 'License:        MIT, BSD-3-Clause\n'
    retv = main([_write(tmp_path, 'bad3.spec', content)])
    assert retv == 1


def test_bad_legacy_plus_suffix(tmp_path: Path) -> None:
    content = 'License:        GPLv3+\n'
    retv = main([_write(tmp_path, 'bad4.spec', content)])
    assert retv == 1


def test_bad_unbalanced_parentheses(tmp_path: Path) -> None:
    content = 'License:        (MIT OR Apache-2.0\n'
    retv = main([_write(tmp_path, 'bad6.spec', content)])
    assert retv == 1