# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_buildrequires import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_single_dependency_per_line(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  gcc\n'
        'BuildRequires:  make\n'
        'BuildRequires:  pkgconfig(zlib)\n',
    )
    assert main([f]) == 0


def test_ok_versioned_dependency(tmp_path):
    # a version comparison is still a single dependency
    f = _write(
        tmp_path,
        'good2.spec',
        'BuildSystem:    cmake\n'
        'BuildRequires:  cmake >= 3.4.3\n'
        'BuildRequires:  python3dist(hatchling) = 1.29\n',
    )
    assert main([f]) == 0


def test_ok_rich_dependency(tmp_path):
    # rich dependency expressions declare one dependency
    f = _write(
        tmp_path,
        'good3.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  (cmake(LLVM) >= 22 with cmake(LLVM) < 23)\n'
        'BuildRequires:  (llvm-static >= 22 with llvm-static < 23)\n',
    )
    assert main([f]) == 0


def test_ok_pkgconfig_virtual_dependency(tmp_path):
    # pkgconfig(xxx) is a single (virtual) dependency with a version
    f = _write(
        tmp_path,
        'good4.spec',
        'BuildSystem:    meson\n'
        'BuildRequires:  pkgconfig(glib-2.0) >= 2.6.0\n'
        'BuildRequires:  pkgconfig(libxml-2.0)\n',
    )
    assert main([f]) == 0


def test_ok_crate_dependency(tmp_path):
    # crate() dependencies carry a version comparison
    f = _write(
        tmp_path,
        'good5.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  crate(winapi-0.3/ws2def) >= 0.3.9\n'
        'BuildRequires:  crate(windows-sys-0.52/default) >= 0.52.0\n',
    )
    assert main([f]) == 0


def test_ok_macro_dependency(tmp_path):
    # a macro-expanded dependency is a single dependency
    f = _write(
        tmp_path,
        'good6.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  %{name}-devel = %{version}-%{release}\n'
        'BuildRequires:  pkgconfig(%{fpc_lib}) >= %{version}\n',
    )
    assert main([f]) == 0


def test_ok_missing_buildrequires_field(tmp_path):
    # BuildRequires is required; presence is covered by
    # check-spec-structure
    f = _write(
        tmp_path,
        'good7.spec',
        'Name:           foo\nVersion:        1.0\n'
        'BuildSystem:    autotools\n',
    )
    assert main([f]) == 0


def test_ok_buildrequires_in_subpackage_ignored(tmp_path):
    # BuildRequires inside a %package subpackage block is a different
    # field and is not covered by this rule
    f = _write(
        tmp_path,
        'good8.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  gcc\n'
        '\n'
        '%package        devel\n'
        'Summary:        Development files for %{name}\n'
        'BuildRequires:  libfoo-devel, libbar-devel\n',
    )
    assert main([f]) == 0


def test_ok_commented_out_buildrequires(tmp_path):
    f = _write(
        tmp_path,
        'good9.spec',
        '# BuildRequires:  libfoo-devel, libbar-devel\n'
        'BuildSystem:    autotools\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 0


def test_ok_no_buildrequires_lines(tmp_path):
    # a spec without any BuildRequires line passes (presence is covered
    # by check-spec-structure)
    f = _write(
        tmp_path,
        'good10.spec',
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


def test_ok_after_description_ignored(tmp_path):
    # %description cuts the header region; a later BuildRequires line
    # is outside the checked region and never reported
    f = _write(
        tmp_path,
        'good11.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  gcc\n'
        '\n'
        '%description\n'
        'A package.\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_bad_multiple_dependencies_on_one_line(tmp_path):
    # space separated packages violate "one dependency per line"
    f = _write(
        tmp_path,
        'bad1.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  automake autoconf\n',
    )
    assert main([f]) == 1


def test_bad_comma_separated_dependencies(tmp_path):
    # comma separated packages violate "one dependency per line"
    f = _write(
        tmp_path,
        'bad2.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  libXaw-devel, libXmu-devel\n',
    )
    assert main([f]) == 1


def test_bad_empty_value(tmp_path):
    # an empty BuildRequires cannot list a build-time dependency
    f = _write(
        tmp_path,
        'bad3.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:\n',
    )
    assert main([f]) == 1


def test_bad_multiple_errors_reported(tmp_path):
    f = _write(
        tmp_path,
        'bad4.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  automake autoconf\n'
        'BuildRequires:  libXaw-devel, libXmu-devel\n'
        'BuildRequires:\n',
    )
    assert main([f]) == 1


def test_bad_space_separated_in_middle(tmp_path):
    # multiple bare packages on one line in the middle of the list
    f = _write(
        tmp_path,
        'bad5.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  make\n'
        'BuildRequires:  autoconf automake libtool\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1
