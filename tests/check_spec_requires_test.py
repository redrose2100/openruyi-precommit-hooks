# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_requires import main


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
        'Requires:       gcc\n'
        'Requires:       make\n'
        'Requires:       pkgconfig(zlib)\n',
    )
    assert main([f]) == 0


def test_ok_versioned_dependency(tmp_path):
    # a version comparison is still a single dependency
    f = _write(
        tmp_path,
        'good2.spec',
        'BuildSystem:    cmake\n'
        'Requires:       cmake >= 3.4.3\n'
        'Requires:       python3dist(hatchling) = 1.29\n',
    )
    assert main([f]) == 0


def test_ok_rich_dependency(tmp_path):
    # rich dependency expressions declare one dependency
    f = _write(
        tmp_path,
        'good3.spec',
        'BuildSystem:    autotools\n'
        'Requires:       (cmake(LLVM) >= 22 with cmake(LLVM) < 23)\n'
        'Requires:       (llvm-static >= 22 with llvm-static < 23)\n',
    )
    assert main([f]) == 0


def test_ok_pkgconfig_virtual_dependency(tmp_path):
    # pkgconfig(xxx) is a single (virtual) dependency with a version
    f = _write(
        tmp_path,
        'good4.spec',
        'BuildSystem:    meson\n'
        'Requires:       pkgconfig(glib-2.0) >= 2.6.0\n'
        'Requires:       pkgconfig(libxml-2.0)\n',
    )
    assert main([f]) == 0


def test_ok_macro_dependency(tmp_path):
    # a macro-expanded dependency is a single dependency
    f = _write(
        tmp_path,
        'good5.spec',
        'BuildSystem:    autotools\n'
        'Requires:       %{name} = %{version}-%{release}\n'
        'Requires:       %{name}-devel = %{version}-%{release}\n',
    )
    assert main([f]) == 0


def test_ok_with_without_expression(tmp_path):
    # with/without boolean expressions declare a single dependency
    f = _write(
        tmp_path,
        'good6.spec',
        'BuildSystem:    autotools\n'
        'Requires:       foo with bar\n',
    )
    assert main([f]) == 0


def test_ok_no_requires_lines(tmp_path):
    # a spec without any Requires line passes (Requires is optional;
    # presence is covered by check-spec-structure)
    f = _write(
        tmp_path,
        'good7.spec',
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


def test_ok_requires_in_subpackage_checked(tmp_path):
    # Requires inside a %package subpackage block lists that subpackage's
    # runtime dependencies and is checked identically
    f = _write(
        tmp_path,
        'good8.spec',
        'BuildSystem:    autotools\n'
        'Requires:       gcc\n'
        '\n'
        '%package        devel\n'
        'Summary:        Development files for %{name}\n'
        'Requires:       libfoo-devel\n'
        'Requires:       libbar-devel\n',
    )
    assert main([f]) == 0


def test_ok_commented_out_requires(tmp_path):
    f = _write(
        tmp_path,
        'good9.spec',
        '# Requires:      libfoo-devel, libbar-devel\n'
        'BuildSystem:    autotools\n'
        'Requires:       gcc\n',
    )
    assert main([f]) == 0


def test_ok_scriptlet_variants_ignored(tmp_path):
    # Requires(pre): / Requires(post): etc. are different fields and are
    # not covered by this rule
    f = _write(
        tmp_path,
        'good10.spec',
        'BuildSystem:    autotools\n'
        'Requires(post): coreutils sed\n'
        'Requires(pre):  /usr/bin/mkdir /usr/bin/touch\n'
        'Requires:       gcc\n',
    )
    assert main([f]) == 0


def test_ok_requires_meta_variant_ignored(tmp_path):
    # Requires(meta): is a metadata dependency, not a runtime dependency
    f = _write(
        tmp_path,
        'good11.spec',
        'BuildSystem:    autotools\n'
        'Requires(meta): (%{name}-rpm-macros = %{version}-%{release} if rpm-build)\n'
        'Requires:       gcc\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_bad_multiple_dependencies_on_one_line(tmp_path):
    # space separated packages violate "one dependency per line"
    f = _write(
        tmp_path,
        'bad1.spec',
        'BuildSystem:    autotools\n'
        'Requires:       automake autoconf\n',
    )
    assert main([f]) == 1


def test_bad_comma_separated_dependencies(tmp_path):
    # comma separated packages violate "one dependency per line"
    f = _write(
        tmp_path,
        'bad2.spec',
        'BuildSystem:    autotools\n'
        'Requires:       libXaw-devel, libXmu-devel\n',
    )
    assert main([f]) == 1


def test_bad_empty_value(tmp_path):
    # an empty Requires cannot list a runtime dependency
    f = _write(
        tmp_path,
        'bad3.spec',
        'BuildSystem:    autotools\n'
        'Requires:\n',
    )
    assert main([f]) == 1


def test_bad_multiple_errors_reported(tmp_path):
    f = _write(
        tmp_path,
        'bad4.spec',
        'BuildSystem:    autotools\n'
        'Requires:       automake autoconf\n'
        'Requires:       libXaw-devel, libXmu-devel\n'
        'Requires:\n',
    )
    assert main([f]) == 1


def test_bad_subpackage_multiple_dependencies(tmp_path):
    # multiple packages on one line inside a %package subpackage block
    f = _write(
        tmp_path,
        'bad5.spec',
        'BuildSystem:    autotools\n'
        'Requires:       gcc\n'
        '\n'
        '%package        -tools\n'
        'Summary:        Tools package\n'
        'Requires:       file gzip e2fsprogs gawk tar\n',
    )
    assert main([f]) == 1