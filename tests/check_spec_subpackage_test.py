# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

import io
from contextlib import redirect_stdout

from openruyi_precommit_hooks.check_spec_subpackage import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


def _check(tmp_path, name, content):
    """Write a spec and run the hook, returning (returncode, output)."""
    f = _write(tmp_path, name, content)
    buf = io.StringIO()
    with redirect_stdout(buf):
        retv = main([f])
    return retv, buf.getvalue()


# --- passing cases ----------------------------------------------------------

def test_ok_subpackage_requires_main_with_strict_version(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'Name:           libfoo\n'
        'Version:        1.2.3\n'
        'BuildSystem:    autotools\n'
        '\n'
        '%description\n'
        'A foo library.\n'
        '\n'
        '%package        devel\n'
        'Summary:        Development files for libfoo\n'
        'Requires:       %{name}%{?_isa} = %{version}-%{release}\n',
    )
    assert main([f]) == 0


def test_ok_subpackage_requires_main_with_ge(tmp_path):
    f = _write(
        tmp_path,
        'good2.spec',
        'Name:           libbar\n'
        'Version:        2.0.0\n'
        'BuildSystem:    cmake\n'
        '\n'
        '%description\n'
        'A bar library.\n'
        '\n'
        '%package        -n libbar-tools\n'
        'Summary:        Tools for libbar\n'
        'Requires:       libbar >= %{version}\n',
    )
    assert main([f]) == 0


def test_ok_subpackage_requires_other_subpackage(tmp_path):
    # a reference to another subpackage (%{name}-devel) is not a
    # dependency on the main package
    f = _write(
        tmp_path,
        'good3.spec',
        'Name:           libbaz\n'
        'Version:        3.0.0\n'
        'BuildSystem:    meson\n'
        '\n'
        '%description\n'
        'A baz library.\n'
        '\n'
        '%package        devel\n'
        'Summary:        Development files for libbaz\n'
        'Requires:       %{name}-devel-static\n'
        'Requires:       %{name}-client\n',
    )
    assert main([f]) == 0


def test_ok_subpackage_requires_literal_other_subpackage(tmp_path):
    # a literal <mainname>-<feature> reference is to another subpackage
    f = _write(
        tmp_path,
        'good4.spec',
        'Name:           myapp\n'
        'Version:        4.0.0\n'
        'BuildSystem:    autotools\n'
        '\n'
        '%description\n'
        'An application.\n'
        '\n'
        '%package        -n myapp-plugins\n'
        'Summary:        Plugins for myapp\n'
        'Requires:       myapp-libs >= 1.0\n',
    )
    assert main([f]) == 0


def test_ok_virtual_dependency_values(tmp_path):
    # go(...)/pkgconfig(...)/perl(...) virtual capabilities never
    # reference the main package, even when the main package name is a
    # substring of the capability (moby, containerd, perl)
    f = _write(
        tmp_path,
        'good5.spec',
        'Name:           moby\n'
        'Version:        5.0.0\n'
        'BuildSystem:    golangmodules\n'
        '\n'
        '%description\n'
        'Moby.\n'
        '\n'
        '%package        -n go-github-moby-moby-api\n'
        'Summary:        API.\n'
        'Requires:       go(github.com/moby/docker-image-spec)\n',
    )
    assert main([f]) == 0


def test_ok_macro_continuation_is_not_main_reference(tmp_path):
    # gcc%{gcc_version}-c++ expands to a *different* package name,
    # not to the main package ``gcc``
    f = _write(
        tmp_path,
        'good6.spec',
        'Name:           gcc\n'
        'Version:        16.0.0\n'
        '%global         gcc_version 16\n'
        'BuildSystem:    autotools\n'
        '\n'
        '%description\n'
        'GCC.\n'
        '\n'
        '%package        -n gcc-c++\n'
        'Summary:        C++ frontend.\n'
        'Requires:       gcc%{gcc_version}-c++\n',
    )
    assert main([f]) == 0


def test_ok_main_package_block_requires(tmp_path):
    # the rule is about subpackages depending on the main package; the
    # main package block may depend on the subpackage
    f = _write(
        tmp_path,
        'good7.spec',
        'Name:           mainpkg\n'
        'Version:        7.0.0\n'
        'BuildSystem:    autotools\n'
        'Requires:       mainpkg-devel\n'
        '\n'
        '%description\n'
        'Main package.\n',
    )
    assert main([f]) == 0


def test_ok_scriptlet_requires_variant(tmp_path):
    # Requires(pre): etc. declare scriptlet roles, not the runtime
    # dependency on the main package (same as check-spec-requires)
    f = _write(
        tmp_path,
        'good8.spec',
        'Name:           scriptpkg\n'
        'Version:        8.0.0\n'
        'BuildSystem:    autotools\n'
        '\n'
        '%description\n'
        'Script.\n'
        '\n'
        '%package        devel\n'
        'Summary:        Devel files.\n'
        'Requires(pre):  scriptpkg\n',
    )
    assert main([f]) == 0


def test_ok_macro_expanded_main_name(tmp_path):
    # a Name that expands a macro cannot be checked statically
    f = _write(
        tmp_path,
        'good9.spec',
        'Name:           %{base_name}\n'
        'Version:        9.0.0\n'
        '\n'
        '%package        devel\n'
        'Summary:        Devel files.\n'
        'Requires:       foo\n',
    )
    assert main([f]) == 0


def test_ok_libperl_not_confused_with_main_perl(tmp_path):
    # a dependency on ``libperl`` is not a reference to the main
    # package ``perl`` (word-boundary literal match)
    f = _write(
        tmp_path,
        'good10.spec',
        'Name:           perl\n'
        'Version:        5.42.0\n'
        'BuildSystem:    autotools\n'
        '\n'
        '%description\n'
        'Perl.\n'
        '\n'
        '%package        devel\n'
        'Summary:        Devel files.\n'
        'Requires:       libperl\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_bad_subpackage_requires_main_bare(tmp_path):
    retv, out = _check(
        tmp_path,
        'bad1.spec',
        'Name:           e2fsprogs\n'
        'Version:        1.47.2\n'
        'BuildSystem:    autotools\n'
        '\n'
        '%description\n'
        'e2fsprogs.\n'
        '\n'
        '%package        -n e2fsprogs-scrub\n'
        'Summary:        Scrub tool.\n'
        'Requires:       e2fsprogs\n',
    )
    assert retv == 1
    assert 'bad1.spec:10: ' in out
    assert 'e2fsprogs-scrub' in out


def test_bad_subpackage_requires_main_bare_macro(tmp_path):
    retv, out = _check(
        tmp_path,
        'bad2.spec',
        'Name:           obs-build\n'
        'Version:        1.0.0\n'
        'BuildSystem:    autotools\n'
        '\n'
        '%description\n'
        'obs-build.\n'
        '\n'
        '%package        -n mkdrpms\n'
        'Summary:        mkdrpms.\n'
        'Requires:       %{name}\n',
    )
    assert retv == 1
    assert 'bad2.spec:10: ' in out
    assert 'mkdrpms' in out


def test_bad_devel_requires_main_bare(tmp_path):
    # the libmodulemd shape: a plain devel subpackage that needs the
    # main package at a strict version
    retv, out = _check(
        tmp_path,
        'bad3.spec',
        'Name:           libmodulemd\n'
        'Version:        2.15.0\n'
        'BuildSystem:    meson\n'
        '\n'
        '%description\n'
        'libmodulemd.\n'
        '\n'
        '%package        devel\n'
        'Summary:        Development files.\n'
        'Requires:       libmodulemd\n',
    )
    assert retv == 1
    assert 'bad3.spec:10: ' in out
    assert 'libmodulemd' in out


def test_bad_short_main_name_bare(tmp_path):
    # the perl shape: a bare ``Requires: perl`` in a %package macros
    # block with no version comparison
    retv, out = _check(
        tmp_path,
        'bad4.spec',
        'Name:           perl\n'
        'Version:        5.42.0\n'
        'BuildSystem:    autotools\n'
        '\n'
        '%description\n'
        'Perl.\n'
        '\n'
        '%package        macros\n'
        'Summary:        Macros.\n'
        'Requires:       perl\n',
    )
    assert retv == 1
    assert 'bad4.spec:10: ' in out
    assert 'macros' in out


def test_bad_subpackage_requires_main_bare_with_leading_lines(tmp_path):
    # the swig shape: a ``%package -n ccache-swig`` subpackage whose
    # ``Requires: swig`` sits further down the file; the reported line
    # number must point at the offending line, not at the block start
    retv, out = _check(
        tmp_path,
        'bad5.spec',
        'Name:           swig\n'
        'Version:        4.2.1\n'
        'BuildSystem:    autotools\n'
        '\n'
        '%description\n'
        'SWIG is a software development tool.\n'
        '\n'
        '%package        devel\n'
        'Summary:        Development files for swig.\n'
        'Requires:       swig%{?_isa} = %{version}-%{release}\n'
        '\n'
        '%package        -n ccache-swig\n'
        'Summary:        SWIG with ccache support.\n'
        'Requires:       swig\n',
    )
    assert retv == 1
    assert 'bad5.spec:14: ' in out
    assert 'ccache-swig' in out
