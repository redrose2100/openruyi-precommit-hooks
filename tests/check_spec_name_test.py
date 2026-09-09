# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from pathlib import Path

from openruyi_precommit_hooks.check_spec_name import main


def _write(tmp_path: Path, name: str, content: str) -> str:
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases -------------------------------------------------------

def test_ok_lowercase_hyphen(tmp_path: Path) -> None:
    content = 'Name:           my-package\nVersion:        1.0\n'
    retv = main([_write(tmp_path, 'good1.spec', content)])
    assert retv == 0


def test_underscore_reported_but_exemptible(tmp_path: Path) -> None:
    # Upstream names that naturally contain an underscore (e.g.
    # ``nss_wrapper``) are exempt per the supplemental spec, but the
    # hook cannot know the upstream name -- it always reports the
    # underscore and leaves the final decision to the packager.
    content = 'Name:           wpa_supplicant\n'
    retv = main([_write(tmp_path, 'ok2.spec', content)])
    assert retv == 1


def test_ok_perl_module_uppercase(tmp_path: Path) -> None:
    # perl-* modules keep the CPAN distribution capitalization.
    content = 'Name:           perl-Archive-Tar\n'
    retv = main([_write(tmp_path, 'good3.spec', content)])
    assert retv == 0


def test_ok_macro_expanded_name(tmp_path: Path) -> None:
    # ``python-%{pypi_name}`` expands at build time; skip static checks.
    content = 'Name:           python-%{pypi_name}\n'
    retv = main([_write(tmp_path, 'good4.spec', content)])
    assert retv == 0


# --- failing cases -------------------------------------------------------

def test_missing_name_field(tmp_path: Path) -> None:
    content = 'Version:        1.0\nSummary:        x\n'
    retv = main([_write(tmp_path, 'bad1.spec', content)])
    assert retv == 1


def test_uppercase_name(tmp_path: Path) -> None:
    content = 'Name:           Catch2\n'
    retv = main([_write(tmp_path, 'bad2.spec', content)])
    assert retv == 1


def test_mixed_case_name(tmp_path: Path) -> None:
    content = 'Name:           NetworkManager\n'
    retv = main([_write(tmp_path, 'bad3.spec', content)])
    assert retv == 1


def test_underscore_separator(tmp_path: Path) -> None:
    content = 'Name:           createrepo_c\n'
    retv = main([_write(tmp_path, 'bad4.spec', content)])
    assert retv == 1


def test_abi_version_encoded(tmp_path: Path) -> None:
    # ``libfoo2`` encodes the major version into the name.
    content = 'Name:           libfoo2\n'
    retv = main([_write(tmp_path, 'bad5.spec', content)])
    assert retv == 1


def test_abi_name_is_upstream_project(tmp_path: Path) -> None:
    # ``libxml2`` is the upstream project name (matches the URL), not
    # an encoded major version -- see openRuyi-Project/openRuyi#1232.
    content = (
        'Name:           libxml2\n'
        'URL:            https://gitlab.gnome.org/GNOME/libxml2\n'
    )
    retv = main([_write(tmp_path, 'good5.spec', content)])
    assert retv == 0


def test_abi_name_upstream_from_vcs(tmp_path: Path) -> None:
    # Upstream name may also appear in the ``VCS`` field.
    content = (
        'Name:           libssh2\n'
        'VCS:            git:https://github.com/libssh2/libssh2\n'
    )
    retv = main([_write(tmp_path, 'good6.spec', content)])
    assert retv == 0


def test_abi_name_upstream_from_source(tmp_path: Path) -> None:
    # ``Source`` pointing at the upstream tarball also counts.
    content = (
        'Name:           libp11\n'
        'Source:         https://github.com/OpenSC/libp11/archive/'
        'refs/tags/libp11-%{version}.tar.gz\n'
    )
    retv = main([_write(tmp_path, 'good7.spec', content)])
    assert retv == 0


def test_abi_name_macro_stripped_in_url(tmp_path: Path) -> None:
    # ``%{name}``-style macros are stripped before token comparison.
    content = (
        'Name:           libfoo2\n'
        'URL:            https://example.org/libfoo2/\n'
    )
    retv = main([_write(tmp_path, 'good8.spec', content)])
    assert retv == 0


def test_multiple_violations(tmp_path: Path) -> None:
    content = 'Name:           LibFoo_2\n'
    retv = main([_write(tmp_path, 'bad6.spec', content)])
    assert retv == 1


def test_empty_file(tmp_path: Path) -> None:
    retv = main([_write(tmp_path, 'bad7.spec', '')])
    assert retv == 1


def test_multiple_files_one_bad(tmp_path: Path) -> None:
    retv = main([
        _write(tmp_path, 'x1.spec', 'Name:           foo\n'),
        _write(tmp_path, 'x2.spec', 'Name:           Catch2\n'),
    ])
    assert retv == 1
