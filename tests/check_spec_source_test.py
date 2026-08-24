# flake8: noqa: E501  -- spec file contents are reproduced verbatim

from openruyi_precommit_hooks.check_spec_source import main


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding='utf-8')
    return str(p)


# --- passing cases ----------------------------------------------------------

def test_ok_http_source_with_sha256(tmp_path):
    f = _write(
        tmp_path,
        'good1.spec',
        '#!RemoteAsset:  sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\n'
        'Source:         https://www.apache.org/dist/apr/%{name}-%{version}.tar.bz2\n',
    )
    assert main([f]) == 0


def test_ok_https_source_with_sha256(tmp_path):
    f = _write(
        tmp_path,
        'good2.spec',
        '#!RemoteAsset:  sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\n'
        'Source:         https://github.com/P-H-C/phc-winner-argon2/archive/refs/tags/%{version}.tar.gz\n',
    )
    assert main([f]) == 0


def test_ok_local_source_no_marker(tmp_path):
    f = _write(
        tmp_path,
        'good3.spec',
        'Source:         %{name}-%{version}.tar.gz\n',
    )
    assert main([f]) == 0


def test_ok_git_source_uses_git_marker(tmp_path):
    # a git source records the ref in the #!RemoteAsset body; no sha256 needed
    f = _write(
        tmp_path,
        'good4.spec',
        '#!RemoteAsset:  git+https://aomedia.googlesource.com/aom#v%{version}\n'
        '#!CreateArchive\n'
        'Source:         %{name}-%{version}.tar.gz\n',
    )
    assert main([f]) == 0


def test_ok_multiple_sources_each_marked(tmp_path):
    f = _write(
        tmp_path,
        'good5.spec',
        '#!RemoteAsset:  sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\n'
        'Source0:        https://ftpmirror.gnu.org/gnu/autoconf/autoconf-%{version}.tar.xz\n'
        '#!RemoteAsset:  sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\n'
        'Source1:        https://ftpmirror.gnu.org/gnu/autoconf/autoconf-%{version}.tar.xz.sig\n',
    )
    assert main([f]) == 0


def test_ok_pcturl_reuse_with_sha256(tmp_path):
    # ``Source: %{url}/...`` must still carry the sha256 marker
    f = _write(
        tmp_path,
        'good6.spec',
        '#!RemoteAsset:  sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\n'
        'Source:         %{url}/archive/refs/tags/%{version}.tar.gz\n',
    )
    assert main([f]) == 0


def test_ok_missing_source_field(tmp_path):
    # presence is covered by check-spec-structure
    f = _write(
        tmp_path,
        'good7.spec',
        'Name:           foo\nVersion:        1.0\n',
    )
    assert main([f]) == 0


def test_ok_commented_out_source(tmp_path):
    f = _write(
        tmp_path,
        'good8.spec',
        '# Source:        https://example.org/foo.tar.gz\n',
    )
    assert main([f]) == 0


def test_ok_sourceforge_downloads_host(tmp_path):
    f = _write(
        tmp_path,
        'good9.spec',
        '#!RemoteAsset:  sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\n'
        'Source:         https://downloads.sourceforge.net/djvu/djvulibre-%{version}.tar.gz\n',
    )
    assert main([f]) == 0


# --- failing cases ----------------------------------------------------------

def test_bad_bare_remote_asset_without_sha256(tmp_path):
    f = _write(
        tmp_path,
        'bad1.spec',
        '#!RemoteAsset\n'
        'Source:         https://www.apache.org/dist/apr/%{name}-%{version}.tar.bz2\n',
    )
    assert main([f]) == 1


def test_bad_http_source_missing_remote_asset(tmp_path):
    f = _write(
        tmp_path,
        'bad2.spec',
        'Source:         http://audiofile.68k.org/audiofile-%{version}.tar.gz\n',
    )
    assert main([f]) == 1


def test_bad_remote_asset_without_colon(tmp_path):
    # ``#!RemoteAsset`` without a checksum payload is still a violation
    f = _write(
        tmp_path,
        'bad3.spec',
        '#!RemoteAsset\n'
        'Source:         https://ftpmirror.gnu.org/gnu/bc/bc-%{version}.tar.gz\n',
    )
    assert main([f]) == 1


def test_bad_remote_asset_wrong_sha256_length(tmp_path):
    f = _write(
        tmp_path,
        'bad4.spec',
        '#!RemoteAsset:  sha256:1234\n'
        'Source:         https://example.org/foo-%{version}.tar.gz\n',
    )
    assert main([f]) == 1


def test_bad_remote_asset_non_sha256_payload(tmp_path):
    # a non-sha256 payload (e.g. an unsupported marker) is a violation
    f = _write(
        tmp_path,
        'bad5.spec',
        '#!RemoteAsset:  some-other-payload\n'
        'Source:         https://example.org/foo-%{version}.tar.gz\n',
    )
    assert main([f]) == 1


def test_bad_sourceforge_wrong_host(tmp_path):
    f = _write(
        tmp_path,
        'bad6.spec',
        '#!RemoteAsset:  sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\n'
        'Source:         http://download.sourceforge.net/openjade/openjade-%{version}.tar.gz\n',
    )
    assert main([f]) == 1


def test_bad_sourceforge_projects_path(tmp_path):
    f = _write(
        tmp_path,
        'bad7.spec',
        '#!RemoteAsset:  sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\n'
        'Source:         https://sourceforge.net/projects/scons/files/scons/%{version}/SCons-%{version}.tar.gz\n',
    )
    assert main([f]) == 1


def test_bad_pcturl_source_without_sha256(tmp_path):
    f = _write(
        tmp_path,
        'bad8.spec',
        '#!RemoteAsset\n'
        'Source:         %{url}/archive/refs/tags/%{version}.tar.gz\n',
    )
    assert main([f]) == 1