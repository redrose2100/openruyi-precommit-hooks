# flake8: noqa: E501  -- spec file contents are reproduced verbatim
from __future__ import annotations

from openruyi_precommit_hooks.check_spec_patch import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_single_patch_with_comment(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        'BuildSystem:    autotools\n'
        '# Fix build with gcc 16\n'
        'Patch0:         0001-fix-build.patch\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 0


def test_ok_multiple_patches_with_comments(tmp_path):
    f = _write(
        tmp_path,
        'good2.spec',
        'BuildSystem:    autotools\n'
        '# Fix build with gcc 16\n'
        'Patch0:         0001-fix-build.patch\n'
        '# https://github.com/foo/foo/pull/123\n'
        'Patch1:         0002-upstream-fix.patch\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 0


def test_ok_patch_without_comment_but_inside_patch(tmp_path):
    # The guideline allows omitting the comment when the purpose is
    # already explained inside the patch; this cannot be judged
    # statically, so a missing comment is reported.  This test documents
    # that a comment is required.
    f = _write(
        tmp_path,
        'good3.spec',
        'BuildSystem:    autotools\n'
        'Patch0:         0001-fix-build.patch\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1


def test_ok_patchlist_above_description(tmp_path):
    f = _write(
        tmp_path,
        'good4.spec',
        'BuildSystem:    autotools\n'
        '%patchlist\n'
        '# Fix build with gcc 16\n'
        '0001-fix-build.patch\n'
        '# https://github.com/foo/foo/pull/123\n'
        '0002-upstream-fix.patch\n'
        '\n'
        '%description\n'
        'A test package.\n',
    )
    assert main([f]) == 0


def test_ok_patchlist_with_4_patches(tmp_path):
    # more than 3 patches should use %patchlist
    f = _write(
        tmp_path,
        'good5.spec',
        'BuildSystem:    autotools\n'
        '%patchlist\n'
        '# c1\n'
        '0001-a.patch\n'
        '# c2\n'
        '0002-b.patch\n'
        '# c3\n'
        '0003-c.patch\n'
        '# c4\n'
        '0004-d.patch\n'
        '\n'
        '%description\n'
        'A test package.\n',
    )
    assert main([f]) == 0


def test_ok_patch_between_buildsystem_and_buildoption(tmp_path):
    f = _write(
        tmp_path,
        'good6.spec',
        'BuildSystem:    autotools\n'
        '# Fix build\n'
        'Patch0:         0001-fix-build.patch\n'
        'BuildOption(build):  OPT="%{optflags}"\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 0


def test_ok_patch_between_buildsystem_and_buildrequires(tmp_path):
    f = _write(
        tmp_path,
        'good7.spec',
        'BuildSystem:    autotools\n'
        '# Fix build\n'
        'Patch0:         0001-fix-build.patch\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 0


def test_ok_no_patch(tmp_path):
    f = _write(
        tmp_path,
        'good8.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 0


def test_ok_patch_in_subpackage_ignored(tmp_path):
    # Patch inside a %package subpackage block is not covered
    f = _write(
        tmp_path,
        'good9.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  gcc\n'
        '\n'
        '%package        devel\n'
        'Summary:        Development files\n'
        'Patch0:         0001-fix-build.patch\n',
    )
    assert main([f]) == 0


def test_ok_patchlist_entries_with_comments(tmp_path):
    f = _write(
        tmp_path,
        'good10.spec',
        'BuildSystem:    autotools\n'
        '%patchlist\n'
        '# Fix build with gcc 16\n'
        '0001-fix-build.patch\n'
        '# https://github.com/foo/foo/pull/123\n'
        '0002-upstream-fix.patch\n'
        '\n'
        '%description\n'
        'A test package.\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_bad_patch_without_comment(tmp_path):
    f = _write(
        tmp_path,
        'bad1.spec',
        'BuildSystem:    autotools\n'
        'Patch0:         0001-fix-build.patch\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1


def test_bad_patch_name_not_4digit(tmp_path):
    f = _write(
        tmp_path,
        'bad2.spec',
        'BuildSystem:    autotools\n'
        '# Fix build\n'
        'Patch0:         fix-build.patch\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1


def test_bad_patch_name_prefix_out_of_range(tmp_path):
    f = _write(
        tmp_path,
        'bad3.spec',
        'BuildSystem:    autotools\n'
        '# Fix build\n'
        'Patch0:         3000-fix-build.patch\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1


def test_bad_more_than_3_patches_without_patchlist(tmp_path):
    f = _write(
        tmp_path,
        'bad4.spec',
        'BuildSystem:    autotools\n'
        '# c1\n'
        'Patch0:         0001-a.patch\n'
        '# c2\n'
        'Patch1:         0002-b.patch\n'
        '# c3\n'
        'Patch2:         0003-c.patch\n'
        '# c4\n'
        'Patch3:         0004-d.patch\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1


def test_bad_patchlist_below_description(tmp_path):
    f = _write(
        tmp_path,
        'bad5.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  gcc\n'
        '\n'
        '%description\n'
        'A test package.\n'
        '\n'
        '%patchlist\n'
        '# Fix build\n'
        '0001-fix-build.patch\n',
    )
    assert main([f]) == 1


def test_bad_patch_placement_after_buildoption(tmp_path):
    f = _write(
        tmp_path,
        'bad6.spec',
        'BuildSystem:    autotools\n'
        'BuildOption(build):  OPT="%{optflags}"\n'
        '# Fix build\n'
        'Patch0:         0001-fix-build.patch\n'
        'BuildRequires:  gcc\n',
    )
    assert main([f]) == 1


def test_bad_patch_placement_after_buildrequires(tmp_path):
    f = _write(
        tmp_path,
        'bad7.spec',
        'BuildSystem:    autotools\n'
        'BuildRequires:  gcc\n'
        '# Fix build\n'
        'Patch0:         0001-fix-build.patch\n',
    )
    assert main([f]) == 1


def test_bad_patchlist_entry_without_comment(tmp_path):
    f = _write(
        tmp_path,
        'bad8.spec',
        'BuildSystem:    autotools\n'
        '%patchlist\n'
        '0001-fix-build.patch\n'
        '\n'
        '%description\n'
        'A test package.\n',
    )
    assert main([f]) == 1
