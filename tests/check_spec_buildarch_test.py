# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_buildarch import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_noarch_between_source_and_buildsystem(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'Source0:        https://example.com/foo-%{version}.tar.gz\n'
        'BuildArch:      noarch\n'
        'BuildSystem:    autotools\n',
    )
    assert main([f]) == 0


def test_ok_noarch_after_last_source(tmp_path):
    # multiple sources: BuildArch must come after the last one
    f = _write(
        tmp_path,
        'good2.spec',
        'Source0:        https://example.com/foo-%{version}.tar.gz\n'
        'Source1:        https://example.com/foo-%{version}-extra.tar.gz\n'
        'BuildArch:      noarch\n'
        'BuildSystem:    autotools\n',
    )
    assert main([f]) == 0


def test_ok_noarch_without_source(tmp_path):
    # no Source field: position cannot be judged, value is still valid
    f = _write(
        tmp_path,
        'good3.spec',
        'BuildArch:      noarch\n'
        'BuildSystem:    autotools\n',
    )
    assert main([f]) == 0


def test_ok_noarch_without_buildsystem(tmp_path):
    # no BuildSystem field: position cannot be judged, value is still valid
    f = _write(
        tmp_path,
        'good4.spec',
        'Source0:        https://example.com/foo-%{version}.tar.gz\n'
        'BuildArch:      noarch\n',
    )
    assert main([f]) == 0


def test_ok_missing_buildarch_field(tmp_path):
    # BuildArch is optional; presence is covered by check-spec-structure
    f = _write(
        tmp_path,
        'good5.spec',
        'Name:           foo\nVersion:        1.0\n',
    )
    assert main([f]) == 0


def test_ok_buildarch_in_subpackage_ignored(tmp_path):
    # BuildArch inside a %package subpackage block is a different field
    # and is not covered by this rule
    f = _write(
        tmp_path,
        'good6.spec',
        'Source0:        https://example.com/foo-%{version}.tar.gz\n'
        'BuildSystem:    autotools\n'
        '\n'
        '%package        devel\n'
        'Summary:        Development files for %{name}\n'
        'BuildArch:      noarch\n',
    )
    assert main([f]) == 0


def test_ok_commented_out_buildarch(tmp_path):
    f = _write(
        tmp_path,
        'good7.spec',
        '# BuildArch:     noarch\n'
        'Source0:        https://example.com/foo-%{version}.tar.gz\n'
        'BuildSystem:    autotools\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_bad_empty_value(tmp_path):
    f = _write(
        tmp_path,
        'bad1.spec',
        'Source0:        https://example.com/foo-%{version}.tar.gz\n'
        'BuildArch:\n'
        'BuildSystem:    autotools\n',
    )
    assert main([f]) == 1


def test_bad_before_source(tmp_path):
    # BuildArch before the last Source violates the position rule
    f = _write(
        tmp_path,
        'bad2.spec',
        'BuildArch:      noarch\n'
        'Source0:        https://example.com/foo-%{version}.tar.gz\n'
        'BuildSystem:    autotools\n',
    )
    assert main([f]) == 1


def test_bad_after_buildsystem(tmp_path):
    # BuildArch after BuildSystem violates the position rule
    f = _write(
        tmp_path,
        'bad3.spec',
        'Source0:        https://example.com/foo-%{version}.tar.gz\n'
        'BuildSystem:    autotools\n'
        'BuildArch:      noarch\n',
    )
    assert main([f]) == 1


def test_bad_non_noarch_value(tmp_path):
    # a value other than noarch is not used by the openRuyi repository
    f = _write(
        tmp_path,
        'bad4.spec',
        'Source0:        https://example.com/foo-%{version}.tar.gz\n'
        'BuildArch:      x86_64\n'
        'BuildSystem:    autotools\n',
    )
    assert main([f]) == 1


def test_bad_non_noarch_and_wrong_position(tmp_path):
    # both a wrong value and a wrong position are reported
    f = _write(
        tmp_path,
        'bad5.spec',
        'BuildArch:      aarch64\n'
        'Source0:        https://example.com/foo-%{version}.tar.gz\n'
        'BuildSystem:    autotools\n',
    )
    assert main([f]) == 1
