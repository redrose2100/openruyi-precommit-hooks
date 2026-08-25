# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_buildoption import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_two_spaces_between_buildsystem_and_buildrequires(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'BuildSystem:    autotools\n'
        'BuildOption(conf):  --enable-foo\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 0


def test_ok_multiple_stages_in_order(tmp_path):
    # build -> install -> check order is respected
    f = _write(
        tmp_path,
        'good2.spec',
        'BuildSystem:    autotools\n'
        'BuildOption(build):  all info html\n'
        'BuildOption(install):  install.info\n'
        'BuildOption(check):  run-tests\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 0


def test_ok_repeated_same_stage(tmp_path):
    # the tag may appear any number of times for each section
    f = _write(
        tmp_path,
        'good3.spec',
        'BuildSystem:    autotools\n'
        'BuildOption(conf):  --enable-foo\n'
        'BuildOption(conf):  --enable-bar\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 0


def test_ok_other_stages_ignored_for_order(tmp_path):
    # conf/prep/generate_buildrequires are not part of the order check
    f = _write(
        tmp_path,
        'good4.spec',
        'BuildSystem:    autotools\n'
        'BuildOption(prep):  -n foo-%{version}\n'
        'BuildOption(conf):  --enable-foo\n'
        'BuildOption(build):  all\n'
        'BuildOption(install):  install\n'
        'BuildOption(check):  test\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 0


def test_ok_missing_buildoption_field(tmp_path):
    # BuildOption is optional; presence is covered by check-spec-structure
    f = _write(
        tmp_path,
        'good5.spec',
        'Name:           foo\nVersion:        1.0\n',
    )
    assert main([f]) == 0


def test_ok_buildoption_in_subpackage_ignored(tmp_path):
    # BuildOption inside a %package subpackage block is a different
    # field and is not covered by this rule
    f = _write(
        tmp_path,
        'good6.spec',
        'BuildSystem:    autotools\n'
        'BuildOption(conf):  --enable-foo\n'
        'BuildRequires:  gcc\n'
        '\n'
        '%package        devel\n'
        'Summary:        Development files for %{name}\n'
        'BuildOption(conf):  --enable-devel\n',
    )
    assert main([f]) == 0


def test_ok_commented_out_buildoption(tmp_path):
    f = _write(
        tmp_path,
        'good7.spec',
        '# BuildOption(conf):  --enable-foo\n'
        'BuildSystem:    autotools\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 0


def test_ok_without_buildsystem_anchor(tmp_path):
    # no BuildSystem: position cannot be judged, other rules still pass
    f = _write(
        tmp_path,
        'good8.spec',
        'BuildOption(conf):  --enable-foo\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 0


def test_ok_without_buildrequires_anchor(tmp_path):
    # no BuildRequires: position cannot be judged, other rules still pass
    f = _write(
        tmp_path,
        'good9.spec',
        'BuildSystem:    autotools\n'
        'BuildOption(conf):  --enable-foo\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_bad_single_space_separator(tmp_path):
    # BuildOption(<stage>): must be separated from its arguments by two
    # spaces
    f = _write(
        tmp_path,
        'bad1.spec',
        'BuildSystem:    autotools\n'
        'BuildOption(conf): --enable-foo\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1


def test_bad_no_stage_name(tmp_path):
    # the stage name may be omitted syntactically but the packager is
    # required to write it
    f = _write(
        tmp_path,
        'bad2.spec',
        'BuildSystem:    autotools\n'
        'BuildOption:  --enable-foo\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1


def test_bad_empty_stage_name(tmp_path):
    # BuildOption() with an empty stage name is reported
    f = _write(
        tmp_path,
        'bad3.spec',
        'BuildSystem:    autotools\n'
        'BuildOption():  --enable-foo\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1


def test_bad_before_buildsystem(tmp_path):
    # BuildOption before BuildSystem violates the position rule
    f = _write(
        tmp_path,
        'bad4.spec',
        'BuildOption(conf):  --enable-foo\n'
        'BuildSystem:    autotools\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1


def test_bad_after_buildrequires(tmp_path):
    # BuildOption after BuildRequires violates the position rule
    f = _write(
        tmp_path,
        'bad5.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  gcc\n'
        'BuildOption(conf):  --enable-foo\n',
    )
    assert main([f]) == 1


def test_bad_stage_order(tmp_path):
    # install before build violates the build -> install -> check order
    f = _write(
        tmp_path,
        'bad6.spec',
        'BuildSystem:    autotools\n'
        'BuildOption(install):  install.info\n'
        'BuildOption(build):  all\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1


def test_bad_check_before_install(tmp_path):
    # check before install violates the build -> install -> check order
    f = _write(
        tmp_path,
        'bad7.spec',
        'BuildSystem:    autotools\n'
        'BuildOption(check):  run-tests\n'
        'BuildOption(install):  install.info\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1


def test_bad_single_space_and_wrong_position(tmp_path):
    # both a wrong separator and a wrong position are reported
    f = _write(
        tmp_path,
        'bad8.spec',
        'BuildOption(conf): --enable-foo\n'
        'BuildSystem:    autotools\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1
