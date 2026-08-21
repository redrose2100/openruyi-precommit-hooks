# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from pathlib import Path

from openruyi_precommit_hooks.check_spec_structure import main

GOOD_SPEC = '''\
# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           foo
Version:        1.0.0
Release:        %autorelease
Summary:        A test package
License:        MIT
URL:            https://example.com
VCS:            git:https://github.com/example/foo.git
Source0:        https://example.com/foo-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc

Requires:       glibc

%description
This is a test package.

%prep
%autosetup

%build
%make_build

%install
%make_install

%check
%make_build check

%files
%license LICENSE
%{_bindir}/foo

%changelog
%autochangelog
'''


def _write(tmp_path: Path, name: str, content: str) -> str:
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


def test_ok_spec(tmp_path: Path) -> None:
    retv = main([_write(tmp_path, 'good.spec', GOOD_SPEC)])
    assert retv == 0


def test_missing_vcs_fails(tmp_path: Path) -> None:
    # VCS is now mandatory; a package without it must fail the check.
    content = GOOD_SPEC.replace(
        'VCS:            git:https://github.com/example/foo.git\n', '',
    )
    retv = main([_write(tmp_path, 'bad1.spec', content)])
    assert retv == 1


def test_missing_requires_fails(tmp_path: Path) -> None:
    content = GOOD_SPEC.replace(
        'Requires:       glibc\n\n%description\n',
        '%description\n',
    )
    retv = main([_write(tmp_path, 'bad2.spec', content)])
    assert retv == 1


def test_fields_out_of_order(tmp_path: Path) -> None:
    # Summary before Version violates the canonical order.
    content = GOOD_SPEC.replace(
        'Summary:        A test package\n',
        'Summary:        A test package\nVersion:        1.0.0\n',
    ).replace(
        'Name:           foo\nVersion:        1.0.0\n',
        'Name:           foo\n',
    )
    retv = main([_write(tmp_path, 'bad3.spec', content)])
    assert retv == 1


def test_name_after_summary(tmp_path: Path) -> None:
    content = '''\
# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Summary:        A test package
Name:           foo
Version:        1.0.0
Release:        %autorelease
License:        MIT
URL:            https://example.com
BuildSystem:    autotools

BuildRequires:  gcc

Requires:       glibc

%description
Test.

%files
%{_bindir}/foo

%changelog
%autochangelog
'''
    retv = main([_write(tmp_path, 'bad4.spec', content)])
    assert retv == 1


def test_missing_blank_before_description(tmp_path: Path) -> None:
    # The %description section must be separated by a blank line.
    content = GOOD_SPEC.replace(
        'Requires:       glibc\n\n%description\n',
        'Requires:       glibc\n%description\n',
    )
    retv = main([_write(tmp_path, 'bad5.spec', content)])
    assert retv == 1


def test_missing_blank_before_changelog(tmp_path: Path) -> None:
    content = GOOD_SPEC.replace(
        '%{_bindir}/foo\n\n%changelog\n',
        '%{_bindir}/foo\n%changelog\n',
    )
    retv = main([_write(tmp_path, 'bad6.spec', content)])
    assert retv == 1


def test_if_block_exempt(tmp_path: Path) -> None:
    # A section directly after %if is legal and must not be flagged.
    content = GOOD_SPEC.replace(
        'BuildRequires:  gcc\n\nRequires:       glibc\n\n%description\n',
        'BuildRequires:  gcc\n%if %{with foo}\nBuildRequires:  foo\n%endif\n'
        'Requires:       glibc\n\n%description\n',
    )
    retv = main([_write(tmp_path, 'ok3.spec', content)])
    assert retv == 0


def test_comment_between_content_and_section(tmp_path: Path) -> None:
    # A comment line between the previous content and the section is the
    # same as having content before - blank line still required.
    content = GOOD_SPEC.replace(
        'Requires:       glibc\n\n%description\n',
        'Requires:       glibc\n# some comment\n%description\n',
    )
    retv = main([_write(tmp_path, 'bad7.spec', content)])
    assert retv == 1


def test_empty_file(tmp_path: Path) -> None:
    retv = main([_write(tmp_path, 'bad8.spec', '')])
    assert retv == 1


def test_multiple_files_all_bad(tmp_path: Path) -> None:
    bad = GOOD_SPEC.replace(
        'Requires:       glibc\n\n%description\n',
        'Requires:       glibc\n%description\n',
    )
    retv = main([
        _write(tmp_path, 'x1.spec', bad),
        _write(tmp_path, 'x2.spec', bad),
    ])
    assert retv == 1
