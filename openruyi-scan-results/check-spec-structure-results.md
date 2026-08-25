# check-spec-structure 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库的 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-structure` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 违规 |
| --- | ---: | ---: |
| 5337 | 1863 | 3474 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| 缺少必填字段 | 3462 |
| 头部字段乱序 | 56 |
| 段落前缺少空行 | 11 |

## 问题清单

### 1. 缺少必填字段

主包头部（第一个 `%description` 之前）**必须**包含以下全部字段，且按顺序出现：

```spec
Name:
Version:
Release:
Summary:
License:
URL:
VCS:
Source:
BuildSystem:
BuildRequires:
Requires:
```

> **`VCS` 豁免**：若 `URL` 已为源代码仓库链接（如 `github.com`、`gitlab.*`、`git.*`、`codeberg.org`、`bitbucket.org` 等源码托管平台，或以 `git:` 开头、以 `.git` 结尾），则 `VCS` 可以省略。

各字段缺失文件数：

| 字段 | 缺失文件数 |
| --- | --- |
| `Name` | 0 |
| `Version` | 0 |
| `Release` | 0 |
| `Summary` | 0 |
| `License` | 0 |
| `URL` | 17 |
| `VCS` | 772 |
| `Source` | 7 |
| `BuildSystem` | 120 |
| `BuildRequires` | 49 |
| `Requires` | 2971 |

按缺失字段组合统计：

| 缺失字段组合 | 文件数 |
| --- | --- |
| `Requires` | 2583 |
| `VCS` | 425 |
| `VCS, Requires` | 308 |
| `BuildSystem` | 37 |
| `BuildSystem, Requires` | 29 |
| `BuildRequires, Requires` | 13 |
| `BuildSystem, BuildRequires, Requires` | 12 |
| `VCS, BuildSystem, Requires` | 12 |
| `VCS, BuildSystem` | 9 |
| `BuildSystem, BuildRequires` | 6 |
| `URL, VCS, Requires` | 5 |
| `Source, BuildSystem, BuildRequires` | 3 |
| `URL, VCS, BuildSystem, BuildRequires` | 3 |
| `VCS, BuildSystem, BuildRequires, Requires` | 3 |
| `BuildRequires` | 2 |
| `URL` | 2 |
| `URL, Requires` | 2 |
| `URL, BuildSystem, BuildRequires` | 1 |
| `URL, VCS` | 1 |
| `URL, VCS, BuildSystem, BuildRequires, Requires` | 1 |
| `URL, VCS, Source, BuildSystem, BuildRequires` | 1 |
| `URL, VCS, Source, BuildSystem, BuildRequires, Requires` | 1 |
| `VCS, BuildRequires, Requires` | 1 |
| `VCS, Source, BuildSystem, BuildRequires` | 1 |
| `VCS, Source, BuildSystem, BuildRequires, Requires` | 1 |

缺失文件清单（链接指向 openRuyi 仓库 `main` 分支）：

| # | spec 文件 | 字段值 | 问题类型 |
| --- | --- | --- | --- |
| 1 | [aardvark-dns/aardvark-dns.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aardvark-dns/aardvark-dns.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2 | [abseil-cpp/abseil-cpp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/abseil-cpp/abseil-cpp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 3 | [accounts-qml-module/accounts-qml-module.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/accounts-qml-module/accounts-qml-module.spec) | `Requires` | 缺少必填字段：`Requires` |
| 4 | [acl/acl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/acl/acl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 5 | [acpica/acpica.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/acpica/acpica.spec) | `Requires` | 缺少必填字段：`Requires` |
| 6 | [adwaita-icon-theme/adwaita-icon-theme.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/adwaita-icon-theme/adwaita-icon-theme.spec) | `Requires` | 缺少必填字段：`Requires` |
| 7 | [aflplusplus/aflplusplus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aflplusplus/aflplusplus.spec) | `Requires` | 缺少必填字段：`Requires` |
| 8 | [agg/agg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/agg/agg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 9 | [aha/aha.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aha/aha.spec) | `Requires` | 缺少必填字段：`Requires` |
| 10 | [aide/aide.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aide/aide.spec) | `Requires` | 缺少必填字段：`Requires` |
| 11 | [angelscript/angelscript.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/angelscript/angelscript.spec) | `Requires` | 缺少必填字段：`Requires` |
| 12 | [aom/aom.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aom/aom.spec) | `Requires` | 缺少必填字段：`Requires` |
| 13 | [appstream/appstream.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/appstream/appstream.spec) | `Requires` | 缺少必填字段：`Requires` |
| 14 | [appstream-glib/appstream-glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/appstream-glib/appstream-glib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 15 | [apr/apr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/apr/apr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 16 | [apr-util/apr-util.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/apr-util/apr-util.spec) | `Requires` | 缺少必填字段：`Requires` |
| 17 | [argon2/argon2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/argon2/argon2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 18 | [arrow/arrow.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/arrow/arrow.spec) | `Requires` | 缺少必填字段：`Requires` |
| 19 | [asciinema/asciinema.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/asciinema/asciinema.spec) | `Requires` | 缺少必填字段：`Requires` |
| 20 | [asmjit/asmjit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/asmjit/asmjit.spec) | `Requires` | 缺少必填字段：`Requires` |
| 21 | [asn1c/asn1c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/asn1c/asn1c.spec) | `Requires` | 缺少必填字段：`Requires` |
| 22 | [aspell/aspell.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aspell/aspell.spec) | `Requires` | 缺少必填字段：`Requires` |
| 23 | [atf/atf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/atf/atf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 24 | [atkmm/atkmm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/atkmm/atkmm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 25 | [attr/attr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/attr/attr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 26 | [audiofile/audiofile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/audiofile/audiofile.spec) | `Requires` | 缺少必填字段：`Requires` |
| 27 | [augeas/augeas.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/augeas/augeas.spec) | `Requires` | 缺少必填字段：`Requires` |
| 28 | [avahi/avahi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/avahi/avahi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 29 | [babeltrace/babeltrace.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/babeltrace/babeltrace.spec) | `Requires` | 缺少必填字段：`Requires` |
| 30 | [babl/babl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/babl/babl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 31 | [baloo-widgets/baloo-widgets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/baloo-widgets/baloo-widgets.spec) | `Requires` | 缺少必填字段：`Requires` |
| 32 | [bdftopcf/bdftopcf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bdftopcf/bdftopcf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 33 | [benchmark/benchmark.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/benchmark/benchmark.spec) | `Requires` | 缺少必填字段：`Requires` |
| 34 | [bind/bind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bind/bind.spec) | `Requires` | 缺少必填字段：`Requires` |
| 35 | [binutils/binutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/binutils/binutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 36 | [black-hole-solver/black-hole-solver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/black-hole-solver/black-hole-solver.spec) | `Requires` | 缺少必填字段：`Requires` |
| 37 | [blake3/blake3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/blake3/blake3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 38 | [bolt/bolt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bolt/bolt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 39 | [boost/boost.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/boost/boost.spec) | `Requires` | 缺少必填字段：`Requires` |
| 40 | [bpftool/bpftool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bpftool/bpftool.spec) | `Requires` | 缺少必填字段：`Requires` |
| 41 | [bpftrace/bpftrace.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bpftrace/bpftrace.spec) | `Requires` | 缺少必填字段：`Requires` |
| 42 | [brotli/brotli.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/brotli/brotli.spec) | `Requires` | 缺少必填字段：`Requires` |
| 43 | [btrfs-progs/btrfs-progs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/btrfs-progs/btrfs-progs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 44 | [bubblewrap/bubblewrap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bubblewrap/bubblewrap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 45 | [c-ares/c-ares.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/c-ares/c-ares.spec) | `Requires` | 缺少必填字段：`Requires` |
| 46 | [cairo/cairo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cairo/cairo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 47 | [cairomm1.0/cairomm1.0.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cairomm1.0/cairomm1.0.spec) | `Requires` | 缺少必填字段：`Requires` |
| 48 | [capstone/capstone.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/capstone/capstone.spec) | `Requires` | 缺少必填字段：`Requires` |
| 49 | [cargo-c/cargo-c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cargo-c/cargo-c.spec) | `Requires` | 缺少必填字段：`Requires` |
| 50 | [Catch2/Catch2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/Catch2/Catch2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 51 | [cbindgen/cbindgen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cbindgen/cbindgen.spec) | `Requires` | 缺少必填字段：`Requires` |
| 52 | [cc-switch-cli/cc-switch-cli.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cc-switch-cli/cc-switch-cli.spec) | `Requires` | 缺少必填字段：`Requires` |
| 53 | [ccache/ccache.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ccache/ccache.spec) | `Requires` | 缺少必填字段：`Requires` |
| 54 | [cdson/cdson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cdson/cdson.spec) | `Requires` | 缺少必填字段：`Requires` |
| 55 | [cereal/cereal.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cereal/cereal.spec) | `Requires` | 缺少必填字段：`Requires` |
| 56 | [cfitsio/cfitsio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cfitsio/cfitsio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 57 | [cfortran/cfortran.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cfortran/cfortran.spec) | `Requires` | 缺少必填字段：`Requires` |
| 58 | [cgctl/cgctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cgctl/cgctl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 59 | [chafa/chafa.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/chafa/chafa.spec) | `Requires` | 缺少必填字段：`Requires` |
| 60 | [check/check.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/check/check.spec) | `Requires` | 缺少必填字段：`Requires` |
| 61 | [checkpolicy/checkpolicy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/checkpolicy/checkpolicy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 62 | [chkconfig/chkconfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/chkconfig/chkconfig.spec) | `Requires` | 缺少必填字段：`Requires` |
| 63 | [chrpath/chrpath.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/chrpath/chrpath.spec) | `Requires` | 缺少必填字段：`Requires` |
| 64 | [ck/ck.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ck/ck.spec) | `Requires` | 缺少必填字段：`Requires` |
| 65 | [clamav/clamav.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/clamav/clamav.spec) | `Requires` | 缺少必填字段：`Requires` |
| 66 | [clang-wrap/clang-wrap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/clang-wrap/clang-wrap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 67 | [cli11/cli11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cli11/cli11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 68 | [cmocka/cmocka.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cmocka/cmocka.spec) | `Requires` | 缺少必填字段：`Requires` |
| 69 | [colord-gtk/colord-gtk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/colord-gtk/colord-gtk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 70 | [composefs/composefs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/composefs/composefs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 71 | [compsize/compsize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/compsize/compsize.spec) | `Requires` | 缺少必填字段：`Requires` |
| 72 | [concurrentqueue/concurrentqueue.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/concurrentqueue/concurrentqueue.spec) | `Requires` | 缺少必填字段：`Requires` |
| 73 | [conntrack-tools/conntrack-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/conntrack-tools/conntrack-tools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 74 | [continuity/continuity.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/continuity/continuity.spec) | `Requires` | 缺少必填字段：`Requires` |
| 75 | [convmv/convmv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/convmv/convmv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 76 | [coreutils/coreutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/coreutils/coreutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 77 | [cpio/cpio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cpio/cpio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 78 | [cpp-httplib/cpp-httplib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cpp-httplib/cpp-httplib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 79 | [cpp-threadpool/cpp-threadpool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cpp-threadpool/cpp-threadpool.spec) | `Requires` | 缺少必填字段：`Requires` |
| 80 | [cppunit/cppunit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cppunit/cppunit.spec) | `Requires` | 缺少必填字段：`Requires` |
| 81 | [cpuinfo/cpuinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cpuinfo/cpuinfo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 82 | [crc32c/crc32c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crc32c/crc32c.spec) | `Requires` | 缺少必填字段：`Requires` |
| 83 | [createrepo_c/createrepo_c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/createrepo_c/createrepo_c.spec) | `Requires` | 缺少必填字段：`Requires` |
| 84 | [crun/crun.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crun/crun.spec) | `Requires` | 缺少必填字段：`Requires` |
| 85 | [cryptopp/cryptopp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cryptopp/cryptopp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 86 | [csmith/csmith.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/csmith/csmith.spec) | `Requires` | 缺少必填字段：`Requires` |
| 87 | [curl/curl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/curl/curl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 88 | [cyrus-sasl/cyrus-sasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cyrus-sasl/cyrus-sasl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 89 | [dash/dash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dash/dash.spec) | `Requires` | 缺少必填字段：`Requires` |
| 90 | [date/date.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/date/date.spec) | `Requires` | 缺少必填字段：`Requires` |
| 91 | [dav1d/dav1d.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dav1d/dav1d.spec) | `Requires` | 缺少必填字段：`Requires` |
| 92 | [dbus-broker/dbus-broker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dbus-broker/dbus-broker.spec) | `Requires` | 缺少必填字段：`Requires` |
| 93 | [dbus-glib/dbus-glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dbus-glib/dbus-glib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 94 | [deltarpm/deltarpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/deltarpm/deltarpm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 95 | [desktop-file-utils/desktop-file-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/desktop-file-utils/desktop-file-utils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 96 | [dhcpcd/dhcpcd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dhcpcd/dhcpcd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 97 | [dialog/dialog.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dialog/dialog.spec) | `Requires` | 缺少必填字段：`Requires` |
| 98 | [ding-libs/ding-libs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ding-libs/ding-libs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 99 | [djvulibre/djvulibre.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/djvulibre/djvulibre.spec) | `Requires` | 缺少必填字段：`Requires` |
| 100 | [dlpack/dlpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dlpack/dlpack.spec) | `Requires` | 缺少必填字段：`Requires` |
| 101 | [dmidecode/dmidecode.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dmidecode/dmidecode.spec) | `Requires` | 缺少必填字段：`Requires` |
| 102 | [doctest/doctest.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/doctest/doctest.spec) | `Requires` | 缺少必填字段：`Requires` |
| 103 | [dolphin-plugins/dolphin-plugins.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dolphin-plugins/dolphin-plugins.spec) | `Requires` | 缺少必填字段：`Requires` |
| 104 | [dosfstools/dosfstools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dosfstools/dosfstools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 105 | [dotconf/dotconf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dotconf/dotconf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 106 | [double-conversion/double-conversion.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/double-conversion/double-conversion.spec) | `Requires` | 缺少必填字段：`Requires` |
| 107 | [dpdk/dpdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dpdk/dpdk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 108 | [draco/draco.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/draco/draco.spec) | `Requires` | 缺少必填字段：`Requires` |
| 109 | [dropbear/dropbear.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dropbear/dropbear.spec) | `Requires` | 缺少必填字段：`Requires` |
| 110 | [drpm/drpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/drpm/drpm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 111 | [dtc/dtc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dtc/dtc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 112 | [duktape/duktape.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/duktape/duktape.spec) | `Requires` | 缺少必填字段：`Requires` |
| 113 | [dwarfs/dwarfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dwarfs/dwarfs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 114 | [dwarves/dwarves.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dwarves/dwarves.spec) | `Requires` | 缺少必填字段：`Requires` |
| 115 | [dwz/dwz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dwz/dwz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 116 | [ebook-tools/ebook-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ebook-tools/ebook-tools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 117 | [ecbuild/ecbuild.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ecbuild/ecbuild.spec) | `Requires` | 缺少必填字段：`Requires` |
| 118 | [eccodes/eccodes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/eccodes/eccodes.spec) | `Requires` | 缺少必填字段：`Requires` |
| 119 | [editorconfig-core-c/editorconfig-core-c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/editorconfig-core-c/editorconfig-core-c.spec) | `Requires` | 缺少必填字段：`Requires` |
| 120 | [efi-rpm-macros/efi-rpm-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/efi-rpm-macros/efi-rpm-macros.spec) | `Requires` | 缺少必填字段：`Requires` |
| 121 | [efibootmgr/efibootmgr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/efibootmgr/efibootmgr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 122 | [efitools/efitools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/efitools/efitools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 123 | [efivar/efivar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/efivar/efivar.spec) | `Requires` | 缺少必填字段：`Requires` |
| 124 | [eigen3/eigen3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/eigen3/eigen3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 125 | [elfutils/elfutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/elfutils/elfutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 126 | [ell/ell.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ell/ell.spec) | `Requires` | 缺少必填字段：`Requires` |
| 127 | [emacs/emacs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/emacs/emacs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 128 | [enchant/enchant.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/enchant/enchant.spec) | `Requires` | 缺少必填字段：`Requires` |
| 129 | [enet/enet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/enet/enet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 130 | [erofs-utils/erofs-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/erofs-utils/erofs-utils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 131 | [ethtool/ethtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ethtool/ethtool.spec) | `Requires` | 缺少必填字段：`Requires` |
| 132 | [exempi/exempi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/exempi/exempi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 133 | [exfatprogs/exfatprogs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/exfatprogs/exfatprogs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 134 | [exiv2/exiv2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/exiv2/exiv2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 135 | [expat/expat.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expat/expat.spec) | `Requires` | 缺少必填字段：`Requires` |
| 136 | [f2fs-tools/f2fs-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/f2fs-tools/f2fs-tools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 137 | [fakeroot/fakeroot.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fakeroot/fakeroot.spec) | `Requires` | 缺少必填字段：`Requires` |
| 138 | [fastfetch/fastfetch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fastfetch/fastfetch.spec) | `Requires` | 缺少必填字段：`Requires` |
| 139 | [fast_float/fast_float.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fast_float/fast_float.spec) | `Requires` | 缺少必填字段：`Requires` |
| 140 | [fcft/fcft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fcft/fcft.spec) | `Requires` | 缺少必填字段：`Requires` |
| 141 | [fcitx5/fcitx5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fcitx5/fcitx5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 142 | [fcitx5-gtk/fcitx5-gtk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fcitx5-gtk/fcitx5-gtk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 143 | [fcitx5-qt/fcitx5-qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fcitx5-qt/fcitx5-qt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 144 | [fdk-aac/fdk-aac.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fdk-aac/fdk-aac.spec) | `Requires` | 缺少必填字段：`Requires` |
| 145 | [fdupes/fdupes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fdupes/fdupes.spec) | `Requires` | 缺少必填字段：`Requires` |
| 146 | [ffmpeg/ffmpeg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ffmpeg/ffmpeg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 147 | [ffnvcodec/ffnvcodec.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ffnvcodec/ffnvcodec.spec) | `Requires` | 缺少必填字段：`Requires` |
| 148 | [fftw/fftw.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fftw/fftw.spec) | `Requires` | 缺少必填字段：`Requires` |
| 149 | [file/file.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/file/file.spec) | `Requires` | 缺少必填字段：`Requires` |
| 150 | [findutils/findutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/findutils/findutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 151 | [fio/fio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fio/fio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 152 | [flac/flac.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/flac/flac.spec) | `Requires` | 缺少必填字段：`Requires` |
| 153 | [flatbuffers/flatbuffers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/flatbuffers/flatbuffers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 154 | [flite/flite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/flite/flite.spec) | `Requires` | 缺少必填字段：`Requires` |
| 155 | [fltk/fltk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fltk/fltk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 156 | [fmt/fmt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fmt/fmt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 157 | [font-util/font-util.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/font-util/font-util.spec) | `Requires` | 缺少必填字段：`Requires` |
| 158 | [fontconfig/fontconfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fontconfig/fontconfig.spec) | `Requires` | 缺少必填字段：`Requires` |
| 159 | [fontforge/fontforge.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fontforge/fontforge.spec) | `Requires` | 缺少必填字段：`Requires` |
| 160 | [foxi/foxi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/foxi/foxi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 161 | [fp16/fp16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fp16/fp16.spec) | `Requires` | 缺少必填字段：`Requires` |
| 162 | [freecell-solver/freecell-solver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freecell-solver/freecell-solver.spec) | `Requires` | 缺少必填字段：`Requires` |
| 163 | [freeglut/freeglut.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freeglut/freeglut.spec) | `Requires` | 缺少必填字段：`Requires` |
| 164 | [freerdp/freerdp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freerdp/freerdp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 165 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `Requires` | 缺少必填字段：`Requires` |
| 166 | [fribidi/fribidi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fribidi/fribidi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 167 | [fscryptctl/fscryptctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fscryptctl/fscryptctl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 168 | [fxdiv/fxdiv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fxdiv/fxdiv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 169 | [gawk/gawk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gawk/gawk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 170 | [gc/gc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gc/gc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 171 | [gcr/gcr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcr/gcr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 172 | [gd/gd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gd/gd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 173 | [gdal/gdal.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gdal/gdal.spec) | `Requires` | 缺少必填字段：`Requires` |
| 174 | [gdb/gdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gdb/gdb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 175 | [gdbm/gdbm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gdbm/gdbm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 176 | [gdk-pixbuf/gdk-pixbuf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gdk-pixbuf/gdk-pixbuf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 177 | [gegl/gegl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gegl/gegl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 178 | [gemmlowp/gemmlowp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gemmlowp/gemmlowp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 179 | [genext2fs/genext2fs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/genext2fs/genext2fs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 180 | [genimage/genimage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/genimage/genimage.spec) | `Requires` | 缺少必填字段：`Requires` |
| 181 | [gexiv2/gexiv2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gexiv2/gexiv2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 182 | [gflags/gflags.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gflags/gflags.spec) | `Requires` | 缺少必填字段：`Requires` |
| 183 | [glew/glew.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glew/glew.spec) | `Requires` | 缺少必填字段：`Requires` |
| 184 | [glfw/glfw.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glfw/glfw.spec) | `Requires` | 缺少必填字段：`Requires` |
| 185 | [glib/glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glib/glib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 186 | [glibmm/glibmm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glibmm/glibmm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 187 | [glibmm2.4/glibmm2.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glibmm2.4/glibmm2.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 188 | [glog/glog.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glog/glog.spec) | `Requires` | 缺少必填字段：`Requires` |
| 189 | [glslang/glslang.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glslang/glslang.spec) | `Requires` | 缺少必填字段：`Requires` |
| 190 | [glu/glu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glu/glu.spec) | `Requires` | 缺少必填字段：`Requires` |
| 191 | [glusterfs/glusterfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glusterfs/glusterfs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 192 | [gmp/gmp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gmp/gmp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 193 | [gnu-efi/gnu-efi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gnu-efi/gnu-efi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 194 | [gnutls/gnutls.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gnutls/gnutls.spec) | `Requires` | 缺少必填字段：`Requires` |
| 195 | [go-aead-dev-mem/go-aead-dev-mem.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-aead-dev-mem/go-aead-dev-mem.spec) | `Requires` | 缺少必填字段：`Requires` |
| 196 | [go-aead-dev-minisign/go-aead-dev-minisign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-aead-dev-minisign/go-aead-dev-minisign.spec) | `Requires` | 缺少必填字段：`Requires` |
| 197 | [go-aead-dev-mtls/go-aead-dev-mtls.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-aead-dev-mtls/go-aead-dev-mtls.spec) | `Requires` | 缺少必填字段：`Requires` |
| 198 | [go-bindata-assetfs/go-bindata-assetfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-bindata-assetfs/go-bindata-assetfs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 199 | [go-dario-mergo/go-dario-mergo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-dario-mergo/go-dario-mergo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 200 | [go-etcd-io-gofail/go-etcd-io-gofail.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-etcd-io-gofail/go-etcd-io-gofail.spec) | `Requires` | 缺少必填字段：`Requires` |
| 201 | [go-filippo-edwards25519/go-filippo-edwards25519.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-filippo-edwards25519/go-filippo-edwards25519.spec) | `Requires` | 缺少必填字段：`Requires` |
| 202 | [go-github-adalogics-go-fuzz-headers/go-github-adalogics-go-fuzz-headers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-adalogics-go-fuzz-headers/go-github-adalogics-go-fuzz-headers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 203 | [go-github-agext-levenshtein/go-github-agext-levenshtein.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-agext-levenshtein/go-github-agext-levenshtein.spec) | `Requires` | 缺少必填字段：`Requires` |
| 204 | [go-github-agnivade-levenshtein/go-github-agnivade-levenshtein.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-agnivade-levenshtein/go-github-agnivade-levenshtein.spec) | `Requires` | 缺少必填字段：`Requires` |
| 205 | [go-github-ajg-form/go-github-ajg-form.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-ajg-form/go-github-ajg-form.spec) | `Requires` | 缺少必填字段：`Requires` |
| 206 | [go-github-ajstarks-svgo/go-github-ajstarks-svgo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-ajstarks-svgo/go-github-ajstarks-svgo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 207 | [go-github-akamensky-argparse/go-github-akamensky-argparse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-akamensky-argparse/go-github-akamensky-argparse.spec) | `Requires` | 缺少必填字段：`Requires` |
| 208 | [go-github-alecthomas-participle-v2/go-github-alecthomas-participle-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-alecthomas-participle-v2/go-github-alecthomas-participle-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 209 | [go-github-alecthomas-repr/go-github-alecthomas-repr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-alecthomas-repr/go-github-alecthomas-repr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 210 | [go-github-aliyun-aliyun-oss-go-sdk/go-github-aliyun-aliyun-oss-go-sdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-aliyun-aliyun-oss-go-sdk/go-github-aliyun-aliyun-oss-go-sdk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 211 | [go-github-anishathalye-porcupine/go-github-anishathalye-porcupine.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-anishathalye-porcupine/go-github-anishathalye-porcupine.spec) | `Requires` | 缺少必填字段：`Requires` |
| 212 | [go-github-anmitsu-go-shlex/go-github-anmitsu-go-shlex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-anmitsu-go-shlex/go-github-anmitsu-go-shlex.spec) | `Requires` | 缺少必填字段：`Requires` |
| 213 | [go-github-antihax-optional/go-github-antihax-optional.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-antihax-optional/go-github-antihax-optional.spec) | `Requires` | 缺少必填字段：`Requires` |
| 214 | [go-github-apache-arrow-go-v18/go-github-apache-arrow-go-v18.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-apache-arrow-go-v18/go-github-apache-arrow-go-v18.spec) | `Requires` | 缺少必填字段：`Requires` |
| 215 | [go-github-apache-beam/go-github-apache-beam.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-apache-beam/go-github-apache-beam.spec) | `Requires` | 缺少必填字段：`Requires` |
| 216 | [go-github-apache-thrift/go-github-apache-thrift.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-apache-thrift/go-github-apache-thrift.spec) | `Requires` | 缺少必填字段：`Requires` |
| 217 | [go-github-aperturerobotics-json-iterator-lite/go-github-aperturerobotics-json-iterator-lite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-aperturerobotics-json-iterator-lite/go-github-aperturerobotics-json-iterator-lite.spec) | `Requires` | 缺少必填字段：`Requires` |
| 218 | [go-github-apparentlymart-go-cidr/go-github-apparentlymart-go-cidr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-apparentlymart-go-cidr/go-github-apparentlymart-go-cidr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 219 | [go-github-apparentlymart-go-textseg/go-github-apparentlymart-go-textseg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-apparentlymart-go-textseg/go-github-apparentlymart-go-textseg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 220 | [go-github-apparentlymart-go-textseg-v15/go-github-apparentlymart-go-textseg-v15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-apparentlymart-go-textseg-v15/go-github-apparentlymart-go-textseg-v15.spec) | `Requires` | 缺少必填字段：`Requires` |
| 221 | [go-github-apparentlymart-go-textseg-v17/go-github-apparentlymart-go-textseg-v17.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-apparentlymart-go-textseg-v17/go-github-apparentlymart-go-textseg-v17.spec) | `Requires` | 缺少必填字段：`Requires` |
| 222 | [go-github-arbovm-levenshtein/go-github-arbovm-levenshtein.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-arbovm-levenshtein/go-github-arbovm-levenshtein.spec) | `Requires` | 缺少必填字段：`Requires` |
| 223 | [go-github-armon-circbuf/go-github-armon-circbuf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-armon-circbuf/go-github-armon-circbuf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 224 | [go-github-armon-go-radix/go-github-armon-go-radix.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-armon-go-radix/go-github-armon-go-radix.spec) | `Requires` | 缺少必填字段：`Requires` |
| 225 | [go-github-armon-go-socks5/go-github-armon-go-socks5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-armon-go-socks5/go-github-armon-go-socks5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 226 | [go-github-asaskevich-govalidator/go-github-asaskevich-govalidator.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-asaskevich-govalidator/go-github-asaskevich-govalidator.spec) | `Requires` | 缺少必填字段：`Requires` |
| 227 | [go-github-aws-smithy-go/go-github-aws-smithy-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-aws-smithy-go/go-github-aws-smithy-go.spec) | `Requires` | 缺少必填字段：`Requires` |
| 228 | [go-github-aymanbagabas-go-osc52/go-github-aymanbagabas-go-osc52.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-aymanbagabas-go-osc52/go-github-aymanbagabas-go-osc52.spec) | `Requires` | 缺少必填字段：`Requires` |
| 229 | [go-github-aymanbagabas-go-osc52-v2/go-github-aymanbagabas-go-osc52-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-aymanbagabas-go-osc52-v2/go-github-aymanbagabas-go-osc52-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 230 | [go-github-aymanbagabas-go-udiff/go-github-aymanbagabas-go-udiff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-aymanbagabas-go-udiff/go-github-aymanbagabas-go-udiff.spec) | `Requires` | 缺少必填字段：`Requires` |
| 231 | [go-github-aymerick-douceur/go-github-aymerick-douceur.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-aymerick-douceur/go-github-aymerick-douceur.spec) | `Requires` | 缺少必填字段：`Requires` |
| 232 | [go-github-bahlo-generic-list-go/go-github-bahlo-generic-list-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-bahlo-generic-list-go/go-github-bahlo-generic-list-go.spec) | `Requires` | 缺少必填字段：`Requires` |
| 233 | [go-github-benmathews-bench/go-github-benmathews-bench.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-benmathews-bench/go-github-benmathews-bench.spec) | `Requires` | 缺少必填字段：`Requires` |
| 234 | [go-github-beorn7-perks/go-github-beorn7-perks.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-beorn7-perks/go-github-beorn7-perks.spec) | `Requires` | 缺少必填字段：`Requires` |
| 235 | [go-github-bgentry-speakeasy/go-github-bgentry-speakeasy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-bgentry-speakeasy/go-github-bgentry-speakeasy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 236 | [go-github-bitly-go-simplejson/go-github-bitly-go-simplejson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-bitly-go-simplejson/go-github-bitly-go-simplejson.spec) | `Requires` | 缺少必填字段：`Requires` |
| 237 | [go-github-bits-and-blooms-bitset/go-github-bits-and-blooms-bitset.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-bits-and-blooms-bitset/go-github-bits-and-blooms-bitset.spec) | `Requires` | 缺少必填字段：`Requires` |
| 238 | [go-github-blang-semver-v4/go-github-blang-semver-v4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-blang-semver-v4/go-github-blang-semver-v4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 239 | [go-github-blevesearch-segment/go-github-blevesearch-segment.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-blevesearch-segment/go-github-blevesearch-segment.spec) | `Requires` | 缺少必填字段：`Requires` |
| 240 | [go-github-bmatcuk-doublestar/go-github-bmatcuk-doublestar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-bmatcuk-doublestar/go-github-bmatcuk-doublestar.spec) | `Requires` | 缺少必填字段：`Requires` |
| 241 | [go-github-boltdb-bolt/go-github-boltdb-bolt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-boltdb-bolt/go-github-boltdb-bolt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 242 | [go-github-boombuler-barcode/go-github-boombuler-barcode.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-boombuler-barcode/go-github-boombuler-barcode.spec) | `Requires` | 缺少必填字段：`Requires` |
| 243 | [go-github-bradfitz-gomemcache-memcache/go-github-bradfitz-gomemcache-memcache.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-bradfitz-gomemcache-memcache/go-github-bradfitz-gomemcache-memcache.spec) | `Requires` | 缺少必填字段：`Requires` |
| 244 | [go-github-brianvoe-gofakeit-v7/go-github-brianvoe-gofakeit-v7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-brianvoe-gofakeit-v7/go-github-brianvoe-gofakeit-v7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 245 | [go-github-bsm-gomega/go-github-bsm-gomega.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-bsm-gomega/go-github-bsm-gomega.spec) | `Requires` | 缺少必填字段：`Requires` |
| 246 | [go-github-buger-jsonparser/go-github-buger-jsonparser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-buger-jsonparser/go-github-buger-jsonparser.spec) | `Requires` | 缺少必填字段：`Requires` |
| 247 | [go-github-burntsushi-toml/go-github-burntsushi-toml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-burntsushi-toml/go-github-burntsushi-toml.spec) | `Requires` | 缺少必填字段：`Requires` |
| 248 | [go-github-bwesterb-go-ristretto/go-github-bwesterb-go-ristretto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-bwesterb-go-ristretto/go-github-bwesterb-go-ristretto.spec) | `Requires` | 缺少必填字段：`Requires` |
| 249 | [go-github-cenkalti-backoff/go-github-cenkalti-backoff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-cenkalti-backoff/go-github-cenkalti-backoff.spec) | `Requires` | 缺少必填字段：`Requires` |
| 250 | [go-github-cenkalti-backoff-v4/go-github-cenkalti-backoff-v4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-cenkalti-backoff-v4/go-github-cenkalti-backoff-v4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 251 | [go-github-cenkalti-backoff-v5/go-github-cenkalti-backoff-v5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-cenkalti-backoff-v5/go-github-cenkalti-backoff-v5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 252 | [go-github-cespare-xxhash-v2/go-github-cespare-xxhash-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-cespare-xxhash-v2/go-github-cespare-xxhash-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 253 | [go-github-charlievieth-fastwalk/go-github-charlievieth-fastwalk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-charlievieth-fastwalk/go-github-charlievieth-fastwalk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 254 | [go-github-charmbracelet-x/go-github-charmbracelet-x.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-charmbracelet-x/go-github-charmbracelet-x.spec) | `Requires` | 缺少必填字段：`Requires` |
| 255 | [go-github-chewxy-math32/go-github-chewxy-math32.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-chewxy-math32/go-github-chewxy-math32.spec) | `Requires` | 缺少必填字段：`Requires` |
| 256 | [go-github-chzyer-logex/go-github-chzyer-logex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-chzyer-logex/go-github-chzyer-logex.spec) | `Requires` | 缺少必填字段：`Requires` |
| 257 | [go-github-circonus-labs-circonusllhist/go-github-circonus-labs-circonusllhist.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-circonus-labs-circonusllhist/go-github-circonus-labs-circonusllhist.spec) | `Requires` | 缺少必填字段：`Requires` |
| 258 | [go-github-clipperhouse-stringish/go-github-clipperhouse-stringish.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-clipperhouse-stringish/go-github-clipperhouse-stringish.spec) | `Requires` | 缺少必填字段：`Requires` |
| 259 | [go-github-cloudykit-fastprinter/go-github-cloudykit-fastprinter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-cloudykit-fastprinter/go-github-cloudykit-fastprinter.spec) | `Requires` | 缺少必填字段：`Requires` |
| 260 | [go-github-cloudykit-jet/go-github-cloudykit-jet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-cloudykit-jet/go-github-cloudykit-jet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 261 | [go-github-cockroachdb-datadriven/go-github-cockroachdb-datadriven.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-cockroachdb-datadriven/go-github-cockroachdb-datadriven.spec) | `Requires` | 缺少必填字段：`Requires` |
| 262 | [go-github-codahale-rfc6979/go-github-codahale-rfc6979.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-codahale-rfc6979/go-github-codahale-rfc6979.spec) | `Requires` | 缺少必填字段：`Requires` |
| 263 | [go-github-code-hex-go-generics-cache/go-github-code-hex-go-generics-cache.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-code-hex-go-generics-cache/go-github-code-hex-go-generics-cache.spec) | `Requires` | 缺少必填字段：`Requires` |
| 264 | [go-github-codegangsta-inject/go-github-codegangsta-inject.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-codegangsta-inject/go-github-codegangsta-inject.spec) | `Requires` | 缺少必填字段：`Requires` |
| 265 | [go-github-coder-quartz/go-github-coder-quartz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-coder-quartz/go-github-coder-quartz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 266 | [go-github-coder-websocket/go-github-coder-websocket.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-coder-websocket/go-github-coder-websocket.spec) | `Requires` | 缺少必填字段：`Requires` |
| 267 | [go-github-containernetworking-cni/go-github-containernetworking-cni.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-containernetworking-cni/go-github-containernetworking-cni.spec) | `Requires` | 缺少必填字段：`Requires` |
| 268 | [go-github-coreos-go-iptables/go-github-coreos-go-iptables.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-coreos-go-iptables/go-github-coreos-go-iptables.spec) | `Requires` | 缺少必填字段：`Requires` |
| 269 | [go-github-cosiner-argv/go-github-cosiner-argv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-cosiner-argv/go-github-cosiner-argv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 270 | [go-github-cpuguy83-dockercfg/go-github-cpuguy83-dockercfg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-cpuguy83-dockercfg/go-github-cpuguy83-dockercfg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 271 | [go-github-cpuguy83-tar2go/go-github-cpuguy83-tar2go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-cpuguy83-tar2go/go-github-cpuguy83-tar2go.spec) | `Requires` | 缺少必填字段：`Requires` |
| 272 | [go-github-creack-pty/go-github-creack-pty.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-creack-pty/go-github-creack-pty.spec) | `Requires` | 缺少必填字段：`Requires` |
| 273 | [go-github-d4l3k-go-bfloat16/go-github-d4l3k-go-bfloat16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-d4l3k-go-bfloat16/go-github-d4l3k-go-bfloat16.spec) | `Requires` | 缺少必填字段：`Requires` |
| 274 | [go-github-datadog-datadog-go/go-github-datadog-datadog-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-datadog-datadog-go/go-github-datadog-datadog-go.spec) | `Requires` | 缺少必填字段：`Requires` |
| 275 | [go-github-datadog-zstd/go-github-datadog-zstd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-datadog-zstd/go-github-datadog-zstd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 276 | [go-github-davecgh-go-spew/go-github-davecgh-go-spew.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-davecgh-go-spew/go-github-davecgh-go-spew.spec) | `Requires` | 缺少必填字段：`Requires` |
| 277 | [go-github-dchest-siphash/go-github-dchest-siphash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-dchest-siphash/go-github-dchest-siphash.spec) | `Requires` | 缺少必填字段：`Requires` |
| 278 | [go-github-dennwc-varint/go-github-dennwc-varint.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-dennwc-varint/go-github-dennwc-varint.spec) | `Requires` | 缺少必填字段：`Requires` |
| 279 | [go-github-dlclark-regexp2/go-github-dlclark-regexp2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-dlclark-regexp2/go-github-dlclark-regexp2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 280 | [go-github-docker-go-connections/go-github-docker-go-connections.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-docker-go-connections/go-github-docker-go-connections.spec) | `Requires` | 缺少必填字段：`Requires` |
| 281 | [go-github-docker-go-units/go-github-docker-go-units.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-docker-go-units/go-github-docker-go-units.spec) | `Requires` | 缺少必填字段：`Requires` |
| 282 | [go-github-dougm-pretty/go-github-dougm-pretty.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-dougm-pretty/go-github-dougm-pretty.spec) | `Requires` | 缺少必填字段：`Requires` |
| 283 | [go-github-dustin-go-humanize/go-github-dustin-go-humanize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-dustin-go-humanize/go-github-dustin-go-humanize.spec) | `Requires` | 缺少必填字段：`Requires` |
| 284 | [go-github-emersion-go-sasl/go-github-emersion-go-sasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-emersion-go-sasl/go-github-emersion-go-sasl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 285 | [go-github-emicklei-go-restful-v3/go-github-emicklei-go-restful-v3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-emicklei-go-restful-v3/go-github-emicklei-go-restful-v3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 286 | [go-github-emirpasic-gods/go-github-emirpasic-gods.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-emirpasic-gods/go-github-emirpasic-gods.spec) | `Requires` | 缺少必填字段：`Requires` |
| 287 | [go-github-emirpasic-gods-v2/go-github-emirpasic-gods-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-emirpasic-gods-v2/go-github-emirpasic-gods-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 288 | [go-github-erofs-go-erofs/go-github-erofs-go-erofs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-erofs-go-erofs/go-github-erofs-go-erofs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 289 | [go-github-etcd-io-bbolt/go-github-etcd-io-bbolt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-etcd-io-bbolt/go-github-etcd-io-bbolt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 290 | [go-github-facette-natsort/go-github-facette-natsort.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-facette-natsort/go-github-facette-natsort.spec) | `Requires` | 缺少必填字段：`Requires` |
| 291 | [go-github-fatih-set/go-github-fatih-set.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-fatih-set/go-github-fatih-set.spec) | `Requires` | 缺少必填字段：`Requires` |
| 292 | [go-github-fatih-structs/go-github-fatih-structs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-fatih-structs/go-github-fatih-structs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 293 | [go-github-felixge-httpsnoop/go-github-felixge-httpsnoop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-felixge-httpsnoop/go-github-felixge-httpsnoop.spec) | `Requires` | 缺少必填字段：`Requires` |
| 294 | [go-github-flopp-go-findfont/go-github-flopp-go-findfont.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-flopp-go-findfont/go-github-flopp-go-findfont.spec) | `Requires` | 缺少必填字段：`Requires` |
| 295 | [go-github-gabriel-vasile-mimetype/go-github-gabriel-vasile-mimetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-gabriel-vasile-mimetype/go-github-gabriel-vasile-mimetype.spec) | `Requires` | 缺少必填字段：`Requires` |
| 296 | [go-github-gkampitakis-ciinfo/go-github-gkampitakis-ciinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-gkampitakis-ciinfo/go-github-gkampitakis-ciinfo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 297 | [go-github-gkampitakis-go-diff/go-github-gkampitakis-go-diff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-gkampitakis-go-diff/go-github-gkampitakis-go-diff.spec) | `Requires` | 缺少必填字段：`Requires` |
| 298 | [go-github-go-errors-errors/go-github-go-errors-errors.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-errors-errors/go-github-go-errors-errors.spec) | `Requires` | 缺少必填字段：`Requires` |
| 299 | [go-github-go-git-gcfg/go-github-go-git-gcfg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-git-gcfg/go-github-go-git-gcfg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 300 | [go-github-go-jose-go-jose-v4/go-github-go-jose-go-jose-v4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-jose-go-jose-v4/go-github-go-jose-go-jose-v4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 301 | [go-github-go-ldap-ldap/go-github-go-ldap-ldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-ldap-ldap/go-github-go-ldap-ldap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 302 | [go-github-go-loger-logr/go-github-go-loger-logr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-loger-logr/go-github-go-loger-logr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 303 | [go-github-go-martini-martini/go-github-go-martini-martini.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-martini-martini/go-github-go-martini-martini.spec) | `Requires` | 缺少必填字段：`Requires` |
| 304 | [go-github-go-openapi-errors/go-github-go-openapi-errors.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-openapi-errors/go-github-go-openapi-errors.spec) | `Requires` | 缺少必填字段：`Requires` |
| 305 | [go-github-go-openapi-testify/go-github-go-openapi-testify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-openapi-testify/go-github-go-openapi-testify.spec) | `Requires` | 缺少必填字段：`Requires` |
| 306 | [go-github-go-openapi-testify-v2/go-github-go-openapi-testify-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-openapi-testify-v2/go-github-go-openapi-testify-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 307 | [go-github-go-playground-assert-v2/go-github-go-playground-assert-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-playground-assert-v2/go-github-go-playground-assert-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 308 | [go-github-go-redis-redis/go-github-go-redis-redis.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-redis-redis/go-github-go-redis-redis.spec) | `Requires` | 缺少必填字段：`Requires` |
| 309 | [go-github-go-task-slim-sprig/go-github-go-task-slim-sprig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-task-slim-sprig/go-github-go-task-slim-sprig.spec) | `Requires` | 缺少必填字段：`Requires` |
| 310 | [go-github-go-task-slim-sprig-v3/go-github-go-task-slim-sprig-v3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-task-slim-sprig-v3/go-github-go-task-slim-sprig-v3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 311 | [go-github-go-test-deep/go-github-go-test-deep.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-test-deep/go-github-go-test-deep.spec) | `Requires` | 缺少必填字段：`Requires` |
| 312 | [go-github-go-viper-mapstructure-v2/go-github-go-viper-mapstructure-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-viper-mapstructure-v2/go-github-go-viper-mapstructure-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 313 | [go-github-go-zookeeper-zk/go-github-go-zookeeper-zk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-go-zookeeper-zk/go-github-go-zookeeper-zk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 314 | [go-github-gobwas-glob/go-github-gobwas-glob.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-gobwas-glob/go-github-gobwas-glob.spec) | `Requires` | 缺少必填字段：`Requires` |
| 315 | [go-github-gobwas-httphead/go-github-gobwas-httphead.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-gobwas-httphead/go-github-gobwas-httphead.spec) | `Requires` | 缺少必填字段：`Requires` |
| 316 | [go-github-gobwas-pool/go-github-gobwas-pool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-gobwas-pool/go-github-gobwas-pool.spec) | `Requires` | 缺少必填字段：`Requires` |
| 317 | [go-github-gobwas-ws/go-github-gobwas-ws.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-gobwas-ws/go-github-gobwas-ws.spec) | `Requires` | 缺少必填字段：`Requires` |
| 318 | [go-github-godbus-dbus/go-github-godbus-dbus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-godbus-dbus/go-github-godbus-dbus.spec) | `Requires` | 缺少必填字段：`Requires` |
| 319 | [go-github-gogo-protobuf/go-github-gogo-protobuf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-gogo-protobuf/go-github-gogo-protobuf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 320 | [go-github-gohugoio-hashstructure/go-github-gohugoio-hashstructure.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-gohugoio-hashstructure/go-github-gohugoio-hashstructure.spec) | `Requires` | 缺少必填字段：`Requires` |
| 321 | [go-github-golang-jwt-jwt-v5/go-github-golang-jwt-jwt-v5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-golang-jwt-jwt-v5/go-github-golang-jwt-jwt-v5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 322 | [go-github-golang-snappy/go-github-golang-snappy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-golang-snappy/go-github-golang-snappy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 323 | [go-github-google-btree/go-github-google-btree.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-google-btree/go-github-google-btree.spec) | `Requires` | 缺少必填字段：`Requires` |
| 324 | [go-github-google-flatbuffers/go-github-google-flatbuffers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-google-flatbuffers/go-github-google-flatbuffers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 325 | [go-github-google-go-cmp/go-github-google-go-cmp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-google-go-cmp/go-github-google-go-cmp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 326 | [go-github-google-go-intervals/go-github-google-go-intervals.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-google-go-intervals/go-github-google-go-intervals.spec) | `Requires` | 缺少必填字段：`Requires` |
| 327 | [go-github-google-go-pkcs11/go-github-google-go-pkcs11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-google-go-pkcs11/go-github-google-go-pkcs11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 328 | [go-github-google-go-querystring/go-github-google-go-querystring.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-google-go-querystring/go-github-google-go-querystring.spec) | `Requires` | 缺少必填字段：`Requires` |
| 329 | [go-github-google-gofuzz/go-github-google-gofuzz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-google-gofuzz/go-github-google-gofuzz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 330 | [go-github-google-jsonschema-go/go-github-google-jsonschema-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-google-jsonschema-go/go-github-google-jsonschema-go.spec) | `Requires` | 缺少必填字段：`Requires` |
| 331 | [go-github-google-licensecheck/go-github-google-licensecheck.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-google-licensecheck/go-github-google-licensecheck.spec) | `Requires` | 缺少必填字段：`Requires` |
| 332 | [go-github-google-renameio/go-github-google-renameio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-google-renameio/go-github-google-renameio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 333 | [go-github-google-uuid/go-github-google-uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-google-uuid/go-github-google-uuid.spec) | `Requires` | 缺少必填字段：`Requires` |
| 334 | [go-github-gookit-assert/go-github-gookit-assert.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-gookit-assert/go-github-gookit-assert.spec) | `Requires` | 缺少必填字段：`Requires` |
| 335 | [go-github-gorilla-mux/go-github-gorilla-mux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-gorilla-mux/go-github-gorilla-mux.spec) | `Requires` | 缺少必填字段：`Requires` |
| 336 | [go-github-grafana-regexp/go-github-grafana-regexp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-grafana-regexp/go-github-grafana-regexp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 337 | [go-github-grpc-ecosystem-grpc-gateway/go-github-grpc-ecosystem-grpc-gateway.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-grpc-ecosystem-grpc-gateway/go-github-grpc-ecosystem-grpc-gateway.spec) | `Requires` | 缺少必填字段：`Requires` |
| 338 | [go-github-hashicorp-cronexpr/go-github-hashicorp-cronexpr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-cronexpr/go-github-hashicorp-cronexpr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 339 | [go-github-hashicorp-errwrap/go-github-hashicorp-errwrap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-errwrap/go-github-hashicorp-errwrap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 340 | [go-github-hashicorp-go-cleanhttp/go-github-hashicorp-go-cleanhttp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-go-cleanhttp/go-github-hashicorp-go-cleanhttp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 341 | [go-github-hashicorp-go-gatedio/go-github-hashicorp-go-gatedio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-go-gatedio/go-github-hashicorp-go-gatedio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 342 | [go-github-hashicorp-go-msgpack/go-github-hashicorp-go-msgpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-go-msgpack/go-github-hashicorp-go-msgpack.spec) | `Requires` | 缺少必填字段：`Requires` |
| 343 | [go-github-hashicorp-go-msgpack-v2/go-github-hashicorp-go-msgpack-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-go-msgpack-v2/go-github-hashicorp-go-msgpack-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 344 | [go-github-hashicorp-go-multierror/go-github-hashicorp-go-multierror.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-go-multierror/go-github-hashicorp-go-multierror.spec) | `Requires` | 缺少必填字段：`Requires` |
| 345 | [go-github-hashicorp-go-rootcerts/go-github-hashicorp-go-rootcerts.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-go-rootcerts/go-github-hashicorp-go-rootcerts.spec) | `Requires` | 缺少必填字段：`Requires` |
| 346 | [go-github-hashicorp-go-secure-stdlib/go-github-hashicorp-go-secure-stdlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-go-secure-stdlib/go-github-hashicorp-go-secure-stdlib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 347 | [go-github-hashicorp-go-syslog/go-github-hashicorp-go-syslog.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-go-syslog/go-github-hashicorp-go-syslog.spec) | `Requires` | 缺少必填字段：`Requires` |
| 348 | [go-github-hashicorp-go-uuid/go-github-hashicorp-go-uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-go-uuid/go-github-hashicorp-go-uuid.spec) | `Requires` | 缺少必填字段：`Requires` |
| 349 | [go-github-hashicorp-go-version/go-github-hashicorp-go-version.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-go-version/go-github-hashicorp-go-version.spec) | `Requires` | 缺少必填字段：`Requires` |
| 350 | [go-github-hashicorp-golang-lru/go-github-hashicorp-golang-lru.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-golang-lru/go-github-hashicorp-golang-lru.spec) | `Requires` | 缺少必填字段：`Requires` |
| 351 | [go-github-hashicorp-golang-lru-v2/go-github-hashicorp-golang-lru-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-golang-lru-v2/go-github-hashicorp-golang-lru-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 352 | [go-github-hashicorp-logutils/go-github-hashicorp-logutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-logutils/go-github-hashicorp-logutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 353 | [go-github-hashicorp-vic/go-github-hashicorp-vic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-vic/go-github-hashicorp-vic.spec) | `Requires` | 缺少必填字段：`Requires` |
| 354 | [go-github-hashicorp-yamux/go-github-hashicorp-yamux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hashicorp-yamux/go-github-hashicorp-yamux.spec) | `Requires` | 缺少必填字段：`Requires` |
| 355 | [go-github-henvic-httpretty/go-github-henvic-httpretty.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-henvic-httpretty/go-github-henvic-httpretty.spec) | `Requires` | 缺少必填字段：`Requires` |
| 356 | [go-github-hexops-gotextdiff/go-github-hexops-gotextdiff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hexops-gotextdiff/go-github-hexops-gotextdiff.spec) | `Requires` | 缺少必填字段：`Requires` |
| 357 | [go-github-hpcloud-tail/go-github-hpcloud-tail.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-hpcloud-tail/go-github-hpcloud-tail.spec) | `Requires` | 缺少必填字段：`Requires` |
| 358 | [go-github-huandu-xstrings/go-github-huandu-xstrings.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-huandu-xstrings/go-github-huandu-xstrings.spec) | `Requires` | 缺少必填字段：`Requires` |
| 359 | [go-github-iancoleman-strcase/go-github-iancoleman-strcase.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-iancoleman-strcase/go-github-iancoleman-strcase.spec) | `Requires` | 缺少必填字段：`Requires` |
| 360 | [go-github-ianlancetaylor-demangle/go-github-ianlancetaylor-demangle.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-ianlancetaylor-demangle/go-github-ianlancetaylor-demangle.spec) | `Requires` | 缺少必填字段：`Requires` |
| 361 | [go-github-icza-backscanner/go-github-icza-backscanner.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-icza-backscanner/go-github-icza-backscanner.spec) | `Requires` | 缺少必填字段：`Requires` |
| 362 | [go-github-icza-mighty/go-github-icza-mighty.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-icza-mighty/go-github-icza-mighty.spec) | `Requires` | 缺少必填字段：`Requires` |
| 363 | [go-github-igrmk-treemap-v2/go-github-igrmk-treemap-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-igrmk-treemap-v2/go-github-igrmk-treemap-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 364 | [go-github-inconshreveable-mousetrap/go-github-inconshreveable-mousetrap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-inconshreveable-mousetrap/go-github-inconshreveable-mousetrap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 365 | [go-github-influxdata-line-protocol/go-github-influxdata-line-protocol.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-influxdata-line-protocol/go-github-influxdata-line-protocol.spec) | `Requires` | 缺少必填字段：`Requires` |
| 366 | [go-github-influxdata-line-protocol-v2/go-github-influxdata-line-protocol-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-influxdata-line-protocol-v2/go-github-influxdata-line-protocol-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 367 | [go-github-jinzhu-copier/go-github-jinzhu-copier.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-jinzhu-copier/go-github-jinzhu-copier.spec) | `Requires` | 缺少必填字段：`Requires` |
| 368 | [go-github-jinzhu-now/go-github-jinzhu-now.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-jinzhu-now/go-github-jinzhu-now.spec) | `Requires` | 缺少必填字段：`Requires` |
| 369 | [go-github-johncgriffin-overflow/go-github-johncgriffin-overflow.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-johncgriffin-overflow/go-github-johncgriffin-overflow.spec) | `Requires` | 缺少必填字段：`Requires` |
| 370 | [go-github-josharian-intern/go-github-josharian-intern.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-josharian-intern/go-github-josharian-intern.spec) | `Requires` | 缺少必填字段：`Requires` |
| 371 | [go-github-joshdk-go-junit/go-github-joshdk-go-junit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-joshdk-go-junit/go-github-joshdk-go-junit.spec) | `Requires` | 缺少必填字段：`Requires` |
| 372 | [go-github-jpillora-backoff/go-github-jpillora-backoff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-jpillora-backoff/go-github-jpillora-backoff.spec) | `Requires` | 缺少必填字段：`Requires` |
| 373 | [go-github-jstemmer-go-junit-report/go-github-jstemmer-go-junit-report.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-jstemmer-go-junit-report/go-github-jstemmer-go-junit-report.spec) | `Requires` | 缺少必填字段：`Requires` |
| 374 | [go-github-juju-gnuflag/go-github-juju-gnuflag.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-juju-gnuflag/go-github-juju-gnuflag.spec) | `Requires` | 缺少必填字段：`Requires` |
| 375 | [go-github-julienschmidt-httprouter/go-github-julienschmidt-httprouter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-julienschmidt-httprouter/go-github-julienschmidt-httprouter.spec) | `Requires` | 缺少必填字段：`Requires` |
| 376 | [go-github-junegunn-go-shellwords/go-github-junegunn-go-shellwords.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-junegunn-go-shellwords/go-github-junegunn-go-shellwords.spec) | `Requires` | 缺少必填字段：`Requires` |
| 377 | [go-github-kataras-golog/go-github-kataras-golog.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-kataras-golog/go-github-kataras-golog.spec) | `Requires` | 缺少必填字段：`Requires` |
| 378 | [go-github-kataras-jwt/go-github-kataras-jwt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-kataras-jwt/go-github-kataras-jwt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 379 | [go-github-kevinburke-ssh-config/go-github-kevinburke-ssh-config.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-kevinburke-ssh-config/go-github-kevinburke-ssh-config.spec) | `Requires` | 缺少必填字段：`Requires` |
| 380 | [go-github-klauspost-asmfmt/go-github-klauspost-asmfmt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-klauspost-asmfmt/go-github-klauspost-asmfmt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 381 | [go-github-klauspost-compress/go-github-klauspost-compress.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-klauspost-compress/go-github-klauspost-compress.spec) | `Requires` | 缺少必填字段：`Requires` |
| 382 | [go-github-klauspost-cpuid-v2/go-github-klauspost-cpuid-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-klauspost-cpuid-v2/go-github-klauspost-cpuid-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 383 | [go-github-klauspost-filepathx/go-github-klauspost-filepathx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-klauspost-filepathx/go-github-klauspost-filepathx.spec) | `Requires` | 缺少必填字段：`Requires` |
| 384 | [go-github-klauspost-readahead/go-github-klauspost-readahead.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-klauspost-readahead/go-github-klauspost-readahead.spec) | `Requires` | 缺少必填字段：`Requires` |
| 385 | [go-github-klauspost-reedsolomon/go-github-klauspost-reedsolomon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-klauspost-reedsolomon/go-github-klauspost-reedsolomon.spec) | `Requires` | 缺少必填字段：`Requires` |
| 386 | [go-github-kolo-xmlrpc/go-github-kolo-xmlrpc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-kolo-xmlrpc/go-github-kolo-xmlrpc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 387 | [go-github-kr-fs/go-github-kr-fs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-kr-fs/go-github-kr-fs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 388 | [go-github-kylelemons-godebug/go-github-kylelemons-godebug.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-kylelemons-godebug/go-github-kylelemons-godebug.spec) | `Requires` | 缺少必填字段：`Requires` |
| 389 | [go-github-lesismal-nbio/go-github-lesismal-nbio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-lesismal-nbio/go-github-lesismal-nbio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 390 | [go-github-lib-pq/go-github-lib-pq.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-lib-pq/go-github-lib-pq.spec) | `Requires` | 缺少必填字段：`Requires` |
| 391 | [go-github-lucasb-eyer-go-colorful/go-github-lucasb-eyer-go-colorful.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-lucasb-eyer-go-colorful/go-github-lucasb-eyer-go-colorful.spec) | `Requires` | 缺少必填字段：`Requires` |
| 392 | [go-github-lucasjones-reggen/go-github-lucasjones-reggen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-lucasjones-reggen/go-github-lucasjones-reggen.spec) | `Requires` | 缺少必填字段：`Requires` |
| 393 | [go-github-lunixbochs-vtclean/go-github-lunixbochs-vtclean.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-lunixbochs-vtclean/go-github-lunixbochs-vtclean.spec) | `Requires` | 缺少必填字段：`Requires` |
| 394 | [go-github-magiconair-properties/go-github-magiconair-properties.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-magiconair-properties/go-github-magiconair-properties.spec) | `Requires` | 缺少必填字段：`Requires` |
| 395 | [go-github-mailru-easyjson/go-github-mailru-easyjson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-mailru-easyjson/go-github-mailru-easyjson.spec) | `Requires` | 缺少必填字段：`Requires` |
| 396 | [go-github-maruel-natural/go-github-maruel-natural.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-maruel-natural/go-github-maruel-natural.spec) | `Requires` | 缺少必填字段：`Requires` |
| 397 | [go-github-masterminds-goutils/go-github-masterminds-goutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-masterminds-goutils/go-github-masterminds-goutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 398 | [go-github-masterminds-semver-v3/go-github-masterminds-semver-v3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-masterminds-semver-v3/go-github-masterminds-semver-v3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 399 | [go-github-mattn-go-shellwords/go-github-mattn-go-shellwords.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-mattn-go-shellwords/go-github-mattn-go-shellwords.spec) | `Requires` | 缺少必填字段：`Requires` |
| 400 | [go-github-maxatome-go-testdeep/go-github-maxatome-go-testdeep.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-maxatome-go-testdeep/go-github-maxatome-go-testdeep.spec) | `Requires` | 缺少必填字段：`Requires` |
| 401 | [go-github-microsoft-go-winio/go-github-microsoft-go-winio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-microsoft-go-winio/go-github-microsoft-go-winio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 402 | [go-github-miekg-dns/go-github-miekg-dns.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-miekg-dns/go-github-miekg-dns.spec) | `Requires` | 缺少必填字段：`Requires` |
| 403 | [go-github-miekg-pkcs11/go-github-miekg-pkcs11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-miekg-pkcs11/go-github-miekg-pkcs11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 404 | [go-github-mikelolasagasti-xz/go-github-mikelolasagasti-xz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-mikelolasagasti-xz/go-github-mikelolasagasti-xz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 405 | [go-github-minio-asm2plan9s/go-github-minio-asm2plan9s.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-minio-asm2plan9s/go-github-minio-asm2plan9s.spec) | `Requires` | 缺少必填字段：`Requires` |
| 406 | [go-github-minio-c2goasm/go-github-minio-c2goasm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-minio-c2goasm/go-github-minio-c2goasm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 407 | [go-github-minio-csvparser/go-github-minio-csvparser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-minio-csvparser/go-github-minio-csvparser.spec) | `Requires` | 缺少必填字段：`Requires` |
| 408 | [go-github-minio-kes-go/go-github-minio-kes-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-minio-kes-go/go-github-minio-kes-go.spec) | `Requires` | 缺少必填字段：`Requires` |
| 409 | [go-github-minio-simdjson-go/go-github-minio-simdjson-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-minio-simdjson-go/go-github-minio-simdjson-go.spec) | `Requires` | 缺少必填字段：`Requires` |
| 410 | [go-github-minio-sio/go-github-minio-sio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-minio-sio/go-github-minio-sio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 411 | [go-github-minio-websocket/go-github-minio-websocket.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-minio-websocket/go-github-minio-websocket.spec) | `Requires` | 缺少必填字段：`Requires` |
| 412 | [go-github-minio-xxml/go-github-minio-xxml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-minio-xxml/go-github-minio-xxml.spec) | `Requires` | 缺少必填字段：`Requires` |
| 413 | [go-github-mitchellh-colorstring/go-github-mitchellh-colorstring.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-mitchellh-colorstring/go-github-mitchellh-colorstring.spec) | `Requires` | 缺少必填字段：`Requires` |
| 414 | [go-github-mitchellh-go-homedir/go-github-mitchellh-go-homedir.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-mitchellh-go-homedir/go-github-mitchellh-go-homedir.spec) | `Requires` | 缺少必填字段：`Requires` |
| 415 | [go-github-mitchellh-go-ps/go-github-mitchellh-go-ps.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-mitchellh-go-ps/go-github-mitchellh-go-ps.spec) | `Requires` | 缺少必填字段：`Requires` |
| 416 | [go-github-mitchellh-go-testing-interface/go-github-mitchellh-go-testing-interface.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-mitchellh-go-testing-interface/go-github-mitchellh-go-testing-interface.spec) | `Requires` | 缺少必填字段：`Requires` |
| 417 | [go-github-mitchellh-go-wordwrap/go-github-mitchellh-go-wordwrap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-mitchellh-go-wordwrap/go-github-mitchellh-go-wordwrap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 418 | [go-github-mitchellh-hashstructure/go-github-mitchellh-hashstructure.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-mitchellh-hashstructure/go-github-mitchellh-hashstructure.spec) | `Requires` | 缺少必填字段：`Requires` |
| 419 | [go-github-mitchellh-mapstructure/go-github-mitchellh-mapstructure.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-mitchellh-mapstructure/go-github-mitchellh-mapstructure.spec) | `Requires` | 缺少必填字段：`Requires` |
| 420 | [go-github-mitchellh-reflectwalk/go-github-mitchellh-reflectwalk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-mitchellh-reflectwalk/go-github-mitchellh-reflectwalk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 421 | [go-github-moby-locker/go-github-moby-locker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-moby-locker/go-github-moby-locker.spec) | `Requires` | 缺少必填字段：`Requires` |
| 422 | [go-github-moby-patternmatcher/go-github-moby-patternmatcher.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-moby-patternmatcher/go-github-moby-patternmatcher.spec) | `Requires` | 缺少必填字段：`Requires` |
| 423 | [go-github-moby-pubsub/go-github-moby-pubsub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-moby-pubsub/go-github-moby-pubsub.spec) | `Requires` | 缺少必填字段：`Requires` |
| 424 | [go-github-moby-spdystream/go-github-moby-spdystream.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-moby-spdystream/go-github-moby-spdystream.spec) | `Requires` | 缺少必填字段：`Requires` |
| 425 | [go-github-modern-go-concurrent/go-github-modern-go-concurrent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-modern-go-concurrent/go-github-modern-go-concurrent.spec) | `Requires` | 缺少必填字段：`Requires` |
| 426 | [go-github-modern-go-reflect2/go-github-modern-go-reflect2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-modern-go-reflect2/go-github-modern-go-reflect2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 427 | [go-github-mohae-deepcopy/go-github-mohae-deepcopy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-mohae-deepcopy/go-github-mohae-deepcopy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 428 | [go-github-morikuni-aec/go-github-morikuni-aec.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-morikuni-aec/go-github-morikuni-aec.spec) | `Requires` | 缺少必填字段：`Requires` |
| 429 | [go-github-muesli-cancelreader/go-github-muesli-cancelreader.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-muesli-cancelreader/go-github-muesli-cancelreader.spec) | `Requires` | 缺少必填字段：`Requires` |
| 430 | [go-github-muesli-clusters/go-github-muesli-clusters.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-muesli-clusters/go-github-muesli-clusters.spec) | `Requires` | 缺少必填字段：`Requires` |
| 431 | [go-github-munnerz-goautoneg/go-github-munnerz-goautoneg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-munnerz-goautoneg/go-github-munnerz-goautoneg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 432 | [go-github-mxk-go-flowrate/go-github-mxk-go-flowrate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-mxk-go-flowrate/go-github-mxk-go-flowrate.spec) | `Requires` | 缺少必填字段：`Requires` |
| 433 | [go-github-ncw-directio/go-github-ncw-directio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-ncw-directio/go-github-ncw-directio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 434 | [go-github-nfnt-resize/go-github-nfnt-resize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-nfnt-resize/go-github-nfnt-resize.spec) | `Requires` | 缺少必填字段：`Requires` |
| 435 | [go-github-nsf-jsondiff/go-github-nsf-jsondiff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-nsf-jsondiff/go-github-nsf-jsondiff.spec) | `Requires` | 缺少必填字段：`Requires` |
| 436 | [go-github-nwaples-rardecode-v2/go-github-nwaples-rardecode-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-nwaples-rardecode-v2/go-github-nwaples-rardecode-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 437 | [go-github-nytimes-gziphandler/go-github-nytimes-gziphandler.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-nytimes-gziphandler/go-github-nytimes-gziphandler.spec) | `Requires` | 缺少必填字段：`Requires` |
| 438 | [go-github-oasdiff-yaml3/go-github-oasdiff-yaml3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-oasdiff-yaml3/go-github-oasdiff-yaml3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 439 | [go-github-oklog-run/go-github-oklog-run.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-oklog-run/go-github-oklog-run.spec) | `Requires` | 缺少必填字段：`Requires` |
| 440 | [go-github-olekukonko-cat/go-github-olekukonko-cat.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-olekukonko-cat/go-github-olekukonko-cat.spec) | `Requires` | 缺少必填字段：`Requires` |
| 441 | [go-github-olekukonko-errors/go-github-olekukonko-errors.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-olekukonko-errors/go-github-olekukonko-errors.spec) | `Requires` | 缺少必填字段：`Requires` |
| 442 | [go-github-olekukonko-ts/go-github-olekukonko-ts.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-olekukonko-ts/go-github-olekukonko-ts.spec) | `Requires` | 缺少必填字段：`Requires` |
| 443 | [go-github-oneofone-xxhash/go-github-oneofone-xxhash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-oneofone-xxhash/go-github-oneofone-xxhash.spec) | `Requires` | 缺少必填字段：`Requires` |
| 444 | [go-github-opencontainers-go-digest/go-github-opencontainers-go-digest.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-opencontainers-go-digest/go-github-opencontainers-go-digest.spec) | `Requires` | 缺少必填字段：`Requires` |
| 445 | [go-github-opencontainers-runtime-spec/go-github-opencontainers-runtime-spec.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-opencontainers-runtime-spec/go-github-opencontainers-runtime-spec.spec) | `Requires` | 缺少必填字段：`Requires` |
| 446 | [go-github-opencontainers-runtime-tools/go-github-opencontainers-runtime-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-opencontainers-runtime-tools/go-github-opencontainers-runtime-tools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 447 | [go-github-opentracing-opentracing-go/go-github-opentracing-opentracing-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-opentracing-opentracing-go/go-github-opentracing-opentracing-go.spec) | `Requires` | 缺少必填字段：`Requires` |
| 448 | [go-github-pascaldekloe-goe/go-github-pascaldekloe-goe.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-pascaldekloe-goe/go-github-pascaldekloe-goe.spec) | `Requires` | 缺少必填字段：`Requires` |
| 449 | [go-github-pbnjay-memory/go-github-pbnjay-memory.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-pbnjay-memory/go-github-pbnjay-memory.spec) | `Requires` | 缺少必填字段：`Requires` |
| 450 | [go-github-pborman-getopt/go-github-pborman-getopt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-pborman-getopt/go-github-pborman-getopt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 451 | [go-github-pborman-getopt-v2/go-github-pborman-getopt-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-pborman-getopt-v2/go-github-pborman-getopt-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 452 | [go-github-pborman-indent/go-github-pborman-indent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-pborman-indent/go-github-pborman-indent.spec) | `Requires` | 缺少必填字段：`Requires` |
| 453 | [go-github-pelletier-go-toml-v2/go-github-pelletier-go-toml-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-pelletier-go-toml-v2/go-github-pelletier-go-toml-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 454 | [go-github-philhofer-fwd/go-github-philhofer-fwd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-philhofer-fwd/go-github-philhofer-fwd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 455 | [go-github-pierrec-lz4-v4/go-github-pierrec-lz4-v4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-pierrec-lz4-v4/go-github-pierrec-lz4-v4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 456 | [go-github-pkg-browser/go-github-pkg-browser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-pkg-browser/go-github-pkg-browser.spec) | `Requires` | 缺少必填字段：`Requires` |
| 457 | [go-github-pkg-errors/go-github-pkg-errors.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-pkg-errors/go-github-pkg-errors.spec) | `Requires` | 缺少必填字段：`Requires` |
| 458 | [go-github-pmezard-go-difflib/go-github-pmezard-go-difflib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-pmezard-go-difflib/go-github-pmezard-go-difflib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 459 | [go-github-pquerna-cachecontrol/go-github-pquerna-cachecontrol.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-pquerna-cachecontrol/go-github-pquerna-cachecontrol.spec) | `Requires` | 缺少必填字段：`Requires` |
| 460 | [go-github-pquerna-ffjson/go-github-pquerna-ffjson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-pquerna-ffjson/go-github-pquerna-ffjson.spec) | `Requires` | 缺少必填字段：`Requires` |
| 461 | [go-github-prashantv-gostub/go-github-prashantv-gostub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-prashantv-gostub/go-github-prashantv-gostub.spec) | `Requires` | 缺少必填字段：`Requires` |
| 462 | [go-github-prometheus-otlptranslator/go-github-prometheus-otlptranslator.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-prometheus-otlptranslator/go-github-prometheus-otlptranslator.spec) | `Requires` | 缺少必填字段：`Requires` |
| 463 | [go-github-puzpuzpuz-xsync/go-github-puzpuzpuz-xsync.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-puzpuzpuz-xsync/go-github-puzpuzpuz-xsync.spec) | `Requires` | 缺少必填字段：`Requires` |
| 464 | [go-github-rabbitmq-amqp091-go/go-github-rabbitmq-amqp091-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-rabbitmq-amqp091-go/go-github-rabbitmq-amqp091-go.spec) | `Requires` | 缺少必填字段：`Requires` |
| 465 | [go-github-ravenox-go-jsoncommentstrip/go-github-ravenox-go-jsoncommentstrip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-ravenox-go-jsoncommentstrip/go-github-ravenox-go-jsoncommentstrip.spec) | `Requires` | 缺少必填字段：`Requires` |
| 466 | [go-github-rcrowley-go-metrics/go-github-rcrowley-go-metrics.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-rcrowley-go-metrics/go-github-rcrowley-go-metrics.spec) | `Requires` | 缺少必填字段：`Requires` |
| 467 | [go-github-rivo-uniseg/go-github-rivo-uniseg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-rivo-uniseg/go-github-rivo-uniseg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 468 | [go-github-rogpeppe-fastuuid/go-github-rogpeppe-fastuuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-rogpeppe-fastuuid/go-github-rogpeppe-fastuuid.spec) | `Requires` | 缺少必填字段：`Requires` |
| 469 | [go-github-rs-xid/go-github-rs-xid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-rs-xid/go-github-rs-xid.spec) | `Requires` | 缺少必填字段：`Requires` |
| 470 | [go-github-russross-blackfriday/go-github-russross-blackfriday.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-russross-blackfriday/go-github-russross-blackfriday.spec) | `Requires` | 缺少必填字段：`Requires` |
| 471 | [go-github-russross-blackfriday-v2/go-github-russross-blackfriday-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-russross-blackfriday-v2/go-github-russross-blackfriday-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 472 | [go-github-rwcarlsen-goexif/go-github-rwcarlsen-goexif.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-rwcarlsen-goexif/go-github-rwcarlsen-goexif.spec) | `Requires` | 缺少必填字段：`Requires` |
| 473 | [go-github-ryanuber-columnize/go-github-ryanuber-columnize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-ryanuber-columnize/go-github-ryanuber-columnize.spec) | `Requires` | 缺少必填字段：`Requires` |
| 474 | [go-github-saintfish-chardet/go-github-saintfish-chardet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-saintfish-chardet/go-github-saintfish-chardet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 475 | [go-github-santhosh-tekuri-jsonschema-v5/go-github-santhosh-tekuri-jsonschema-v5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-santhosh-tekuri-jsonschema-v5/go-github-santhosh-tekuri-jsonschema-v5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 476 | [go-github-sean--seed/go-github-sean--seed.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-sean--seed/go-github-sean--seed.spec) | `Requires` | 缺少必填字段：`Requires` |
| 477 | [go-github-sebdah-goldie-v2/go-github-sebdah-goldie-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-sebdah-goldie-v2/go-github-sebdah-goldie-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 478 | [go-github-segmentio-fasthash/go-github-segmentio-fasthash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-segmentio-fasthash/go-github-segmentio-fasthash.spec) | `Requires` | 缺少必填字段：`Requires` |
| 479 | [go-github-sergi-go-diff/go-github-sergi-go-diff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-sergi-go-diff/go-github-sergi-go-diff.spec) | `Requires` | 缺少必填字段：`Requires` |
| 480 | [go-github-shirou-gopsutil/go-github-shirou-gopsutil.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-shirou-gopsutil/go-github-shirou-gopsutil.spec) | `Requires` | 缺少必填字段：`Requires` |
| 481 | [go-github-shopspring-decimal/go-github-shopspring-decimal.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-shopspring-decimal/go-github-shopspring-decimal.spec) | `Requires` | 缺少必填字段：`Requires` |
| 482 | [go-github-smallnest-ringbuffer/go-github-smallnest-ringbuffer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-smallnest-ringbuffer/go-github-smallnest-ringbuffer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 483 | [go-github-spaolacci-murmur3/go-github-spaolacci-murmur3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-spaolacci-murmur3/go-github-spaolacci-murmur3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 484 | [go-github-spdx-gordf/go-github-spdx-gordf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-spdx-gordf/go-github-spdx-gordf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 485 | [go-github-spf13-pflag/go-github-spf13-pflag.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-spf13-pflag/go-github-spf13-pflag.spec) | `Requires` | 缺少必填字段：`Requires` |
| 486 | [go-github-spkg-bom/go-github-spkg-bom.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-spkg-bom/go-github-spkg-bom.spec) | `Requires` | 缺少必填字段：`Requires` |
| 487 | [go-github-stangelandcl-ppmd/go-github-stangelandcl-ppmd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-stangelandcl-ppmd/go-github-stangelandcl-ppmd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 488 | [go-github-starry-s-zip/go-github-starry-s-zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-starry-s-zip/go-github-starry-s-zip.spec) | `Requires` | 缺少必填字段：`Requires` |
| 489 | [go-github-stathat-go/go-github-stathat-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-stathat-go/go-github-stathat-go.spec) | `Requires` | 缺少必填字段：`Requires` |
| 490 | [go-github-stefanberger-go-pkcs11uri/go-github-stefanberger-go-pkcs11uri.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-stefanberger-go-pkcs11uri/go-github-stefanberger-go-pkcs11uri.spec) | `Requires` | 缺少必填字段：`Requires` |
| 491 | [go-github-stretchr-objx/go-github-stretchr-objx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-stretchr-objx/go-github-stretchr-objx.spec) | `Requires` | 缺少必填字段：`Requires` |
| 492 | [go-github-syndtr-gocapability/go-github-syndtr-gocapability.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-syndtr-gocapability/go-github-syndtr-gocapability.spec) | `Requires` | 缺少必填字段：`Requires` |
| 493 | [go-github-tchap-go-patricia-v2/go-github-tchap-go-patricia-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-tchap-go-patricia-v2/go-github-tchap-go-patricia-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 494 | [go-github-therootcompany-xz/go-github-therootcompany-xz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-therootcompany-xz/go-github-therootcompany-xz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 495 | [go-github-tidwall-match/go-github-tidwall-match.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-tidwall-match/go-github-tidwall-match.spec) | `Requires` | 缺少必填字段：`Requires` |
| 496 | [go-github-tidwall-pretty/go-github-tidwall-pretty.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-tidwall-pretty/go-github-tidwall-pretty.spec) | `Requires` | 缺少必填字段：`Requires` |
| 497 | [go-github-tinylib-msgp/go-github-tinylib-msgp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-tinylib-msgp/go-github-tinylib-msgp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 498 | [go-github-tklauser-go-numcpus/go-github-tklauser-go-numcpus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-tklauser-go-numcpus/go-github-tklauser-go-numcpus.spec) | `Requires` | 缺少必填字段：`Requires` |
| 499 | [go-github-tonistiigi-go-archvariant/go-github-tonistiigi-go-archvariant.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-tonistiigi-go-archvariant/go-github-tonistiigi-go-archvariant.spec) | `Requires` | 缺少必填字段：`Requires` |
| 500 | [go-github-tsosunchia-powclient/go-github-tsosunchia-powclient.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-tsosunchia-powclient/go-github-tsosunchia-powclient.spec) | `Requires` | 缺少必填字段：`Requires` |
| 501 | [go-github-tv42-httpunix/go-github-tv42-httpunix.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-tv42-httpunix/go-github-tv42-httpunix.spec) | `Requires` | 缺少必填字段：`Requires` |
| 502 | [go-github-ulikunitz-xz/go-github-ulikunitz-xz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-ulikunitz-xz/go-github-ulikunitz-xz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 503 | [go-github-valyala-bytebufferpool/go-github-valyala-bytebufferpool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-valyala-bytebufferpool/go-github-valyala-bytebufferpool.spec) | `Requires` | 缺少必填字段：`Requires` |
| 504 | [go-github-valyala-fastjson/go-github-valyala-fastjson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-valyala-fastjson/go-github-valyala-fastjson.spec) | `Requires` | 缺少必填字段：`Requires` |
| 505 | [go-github-viant-xunsafe/go-github-viant-xunsafe.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-viant-xunsafe/go-github-viant-xunsafe.spec) | `Requires` | 缺少必填字段：`Requires` |
| 506 | [go-github-vmihailenco-tagparser-v2/go-github-vmihailenco-tagparser-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-vmihailenco-tagparser-v2/go-github-vmihailenco-tagparser-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 507 | [go-github-wagoodman-go-partybus/go-github-wagoodman-go-partybus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-wagoodman-go-partybus/go-github-wagoodman-go-partybus.spec) | `Requires` | 缺少必填字段：`Requires` |
| 508 | [go-github-wcharczuk-go-chart/go-github-wcharczuk-go-chart.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-wcharczuk-go-chart/go-github-wcharczuk-go-chart.spec) | `Requires` | 缺少必填字段：`Requires` |
| 509 | [go-github-wi2l-jettison/go-github-wi2l-jettison.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-wi2l-jettison/go-github-wi2l-jettison.spec) | `Requires` | 缺少必填字段：`Requires` |
| 510 | [go-github-woodsbury-decimal128/go-github-woodsbury-decimal128.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-woodsbury-decimal128/go-github-woodsbury-decimal128.spec) | `Requires` | 缺少必填字段：`Requires` |
| 511 | [go-github-x448-float16/go-github-x448-float16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-x448-float16/go-github-x448-float16.spec) | `Requires` | 缺少必填字段：`Requires` |
| 512 | [go-github-xdg-scram/go-github-xdg-scram.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-xdg-scram/go-github-xdg-scram.spec) | `Requires` | 缺少必填字段：`Requires` |
| 513 | [go-github-xdg-stringprep/go-github-xdg-stringprep.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-xdg-stringprep/go-github-xdg-stringprep.spec) | `Requires` | 缺少必填字段：`Requires` |
| 514 | [go-github-xeipuuv-gojsonpointer/go-github-xeipuuv-gojsonpointer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-xeipuuv-gojsonpointer/go-github-xeipuuv-gojsonpointer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 515 | [go-github-xhit-go-str2duration-v2/go-github-xhit-go-str2duration-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-xhit-go-str2duration-v2/go-github-xhit-go-str2duration-v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 516 | [go-github-xi2-xz/go-github-xi2-xz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-xi2-xz/go-github-xi2-xz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 517 | [go-github-xiang90-probing/go-github-xiang90-probing.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-xiang90-probing/go-github-xiang90-probing.spec) | `Requires` | 缺少必填字段：`Requires` |
| 518 | [go-github-xlab-treeprint/go-github-xlab-treeprint.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-xlab-treeprint/go-github-xlab-treeprint.spec) | `Requires` | 缺少必填字段：`Requires` |
| 519 | [go-github-xo-terminfo/go-github-xo-terminfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-xo-terminfo/go-github-xo-terminfo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 520 | [go-github-xrash-smetrics/go-github-xrash-smetrics.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-xrash-smetrics/go-github-xrash-smetrics.spec) | `Requires` | 缺少必填字段：`Requires` |
| 521 | [go-github-xtgo-set/go-github-xtgo-set.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-xtgo-set/go-github-xtgo-set.spec) | `Requires` | 缺少必填字段：`Requires` |
| 522 | [go-github-xyproto-randomstring/go-github-xyproto-randomstring.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-xyproto-randomstring/go-github-xyproto-randomstring.spec) | `Requires` | 缺少必填字段：`Requires` |
| 523 | [go-github-yosida95-uritemplate-v3/go-github-yosida95-uritemplate-v3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-yosida95-uritemplate-v3/go-github-yosida95-uritemplate-v3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 524 | [go-github-yuin-goldmark/go-github-yuin-goldmark.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-yuin-goldmark/go-github-yuin-goldmark.spec) | `Requires` | 缺少必填字段：`Requires` |
| 525 | [go-github-zeebo-assert/go-github-zeebo-assert.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-zeebo-assert/go-github-zeebo-assert.spec) | `Requires` | 缺少必填字段：`Requires` |
| 526 | [go-github-zeebo-errs/go-github-zeebo-errs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-zeebo-errs/go-github-zeebo-errs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 527 | [go-go4-unsafe-assume-no-moving-gc/go-go4-unsafe-assume-no-moving-gc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-go4-unsafe-assume-no-moving-gc/go-go4-unsafe-assume-no-moving-gc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 528 | [go-golang-x-mod/go-golang-x-mod.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-golang-x-mod/go-golang-x-mod.spec) | `Requires` | 缺少必填字段：`Requires` |
| 529 | [go-golang-x-sync/go-golang-x-sync.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-golang-x-sync/go-golang-x-sync.spec) | `Requires` | 缺少必填字段：`Requires` |
| 530 | [go-golang-x-sys/go-golang-x-sys.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-golang-x-sys/go-golang-x-sys.spec) | `Requires` | 缺少必填字段：`Requires` |
| 531 | [go-golang-x-text/go-golang-x-text.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-golang-x-text/go-golang-x-text.spec) | `Requires` | 缺少必填字段：`Requires` |
| 532 | [go-golang-x-time/go-golang-x-time.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-golang-x-time/go-golang-x-time.spec) | `Requires` | 缺少必填字段：`Requires` |
| 533 | [go-golang-x-xerrors/go-golang-x-xerrors.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-golang-x-xerrors/go-golang-x-xerrors.spec) | `Requires` | 缺少必填字段：`Requires` |
| 534 | [go-google-api-support/go-google-api-support.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-google-api-support/go-google-api-support.spec) | `Requires` | 缺少必填字段：`Requires` |
| 535 | [go-googlecloud-go/go-googlecloud-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-googlecloud-go/go-googlecloud-go.spec) | `Requires` | 缺少必填字段：`Requires` |
| 536 | [go-googlecloud-go-compute-metadata/go-googlecloud-go-compute-metadata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-googlecloud-go-compute-metadata/go-googlecloud-go-compute-metadata.spec) | `Requires` | 缺少必填字段：`Requires` |
| 537 | [go-gopkg-evanphx-json-patch.v4/go-gopkg-evanphx-json-patch.v4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-gopkg-evanphx-json-patch.v4/go-gopkg-evanphx-json-patch.v4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 538 | [go-gopkg-inf.v0/go-gopkg-inf.v0.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-gopkg-inf.v0/go-gopkg-inf.v0.spec) | `Requires` | 缺少必填字段：`Requires` |
| 539 | [go-gopkg-ini.v1/go-gopkg-ini.v1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-gopkg-ini.v1/go-gopkg-ini.v1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 540 | [go-gopkg-tomb.v1/go-gopkg-tomb.v1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-gopkg-tomb.v1/go-gopkg-tomb.v1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 541 | [go-gopkg-warnings.v0/go-gopkg-warnings.v0.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-gopkg-warnings.v0/go-gopkg-warnings.v0.spec) | `Requires` | 缺少必填字段：`Requires` |
| 542 | [go-gopkg-yaml.v2/go-gopkg-yaml.v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-gopkg-yaml.v2/go-gopkg-yaml.v2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 543 | [go-gopkg-yaml.v3/go-gopkg-yaml.v3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-gopkg-yaml.v3/go-gopkg-yaml.v3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 544 | [go-gopkg-yaml.v4/go-gopkg-yaml.v4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-gopkg-yaml.v4/go-gopkg-yaml.v4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 545 | [go-k8s-sigs-json/go-k8s-sigs-json.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-k8s-sigs-json/go-k8s-sigs-json.spec) | `Requires` | 缺少必填字段：`Requires` |
| 546 | [go-k8s-sigs-randfill/go-k8s-sigs-randfill.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-k8s-sigs-randfill/go-k8s-sigs-randfill.spec) | `Requires` | 缺少必填字段：`Requires` |
| 547 | [go-k8s-sigs-structured-merge-diff-v6/go-k8s-sigs-structured-merge-diff-v6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-k8s-sigs-structured-merge-diff-v6/go-k8s-sigs-structured-merge-diff-v6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 548 | [go-md2man/go-md2man.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-md2man/go-md2man.spec) | `Requires` | 缺少必填字段：`Requires` |
| 549 | [go-opentelemetry-collector-pipeline/go-opentelemetry-collector-pipeline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-opentelemetry-collector-pipeline/go-opentelemetry-collector-pipeline.spec) | `Requires` | 缺少必填字段：`Requires` |
| 550 | [go-opentelemetry-proto/go-opentelemetry-proto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-opentelemetry-proto/go-opentelemetry-proto.spec) | `Requires` | 缺少必填字段：`Requires` |
| 551 | [go-pgregory-rapid/go-pgregory-rapid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-pgregory-rapid/go-pgregory-rapid.spec) | `Requires` | 缺少必填字段：`Requires` |
| 552 | [go-rsc-pdf/go-rsc-pdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-rsc-pdf/go-rsc-pdf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 553 | [go-toml/go-toml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-toml/go-toml.spec) | `Requires` | 缺少必填字段：`Requires` |
| 554 | [go-uber-atomic/go-uber-atomic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-uber-atomic/go-uber-atomic.spec) | `Requires` | 缺少必填字段：`Requires` |
| 555 | [go-uber-automaxprocs/go-uber-automaxprocs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-uber-automaxprocs/go-uber-automaxprocs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 556 | [gobject-introspection/gobject-introspection.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gobject-introspection/gobject-introspection.spec) | `Requires` | 缺少必填字段：`Requires` |
| 557 | [gperf/gperf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gperf/gperf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 558 | [gperftools/gperftools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gperftools/gperftools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 559 | [gpgme/gpgme.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpgme/gpgme.spec) | `Requires` | 缺少必填字段：`Requires` |
| 560 | [gpgmepp/gpgmepp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpgmepp/gpgmepp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 561 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 562 | [gptfdisk/gptfdisk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gptfdisk/gptfdisk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 563 | [graphene/graphene.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/graphene/graphene.spec) | `Requires` | 缺少必填字段：`Requires` |
| 564 | [graphite2/graphite2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/graphite2/graphite2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 565 | [graphviz/graphviz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/graphviz/graphviz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 566 | [grim/grim.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grim/grim.spec) | `Requires` | 缺少必填字段：`Requires` |
| 567 | [grpc/grpc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grpc/grpc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 568 | [gsasl/gsasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gsasl/gsasl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 569 | [gsettings-desktop-schemas/gsettings-desktop-schemas.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gsettings-desktop-schemas/gsettings-desktop-schemas.spec) | `Requires` | 缺少必填字段：`Requires` |
| 570 | [gsl/gsl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gsl/gsl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 571 | [gstreamer/gstreamer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gstreamer/gstreamer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 572 | [gtest/gtest.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gtest/gtest.spec) | `Requires` | 缺少必填字段：`Requires` |
| 573 | [gtk-layer-shell/gtk-layer-shell.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gtk-layer-shell/gtk-layer-shell.spec) | `Requires` | 缺少必填字段：`Requires` |
| 574 | [gtkmm3/gtkmm3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gtkmm3/gtkmm3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 575 | [guidelines-support-library/guidelines-support-library.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/guidelines-support-library/guidelines-support-library.spec) | `Requires` | 缺少必填字段：`Requires` |
| 576 | [guile/guile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/guile/guile.spec) | `Requires` | 缺少必填字段：`Requires` |
| 577 | [gumbo-parser/gumbo-parser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gumbo-parser/gumbo-parser.spec) | `Requires` | 缺少必填字段：`Requires` |
| 578 | [gzip/gzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gzip/gzip.spec) | `Requires` | 缺少必填字段：`Requires` |
| 579 | [half/half.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/half/half.spec) | `Requires` | 缺少必填字段：`Requires` |
| 580 | [haproxy/haproxy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/haproxy/haproxy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 581 | [harfbuzz/harfbuzz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/harfbuzz/harfbuzz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 582 | [haveged/haveged.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/haveged/haveged.spec) | `Requires` | 缺少必填字段：`Requires` |
| 583 | [hdf5/hdf5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hdf5/hdf5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 584 | [hicolor-icon-theme/hicolor-icon-theme.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hicolor-icon-theme/hicolor-icon-theme.spec) | `Requires` | 缺少必填字段：`Requires` |
| 585 | [highway/highway.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/highway/highway.spec) | `Requires` | 缺少必填字段：`Requires` |
| 586 | [hipblas/hipblas.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipblas/hipblas.spec) | `Requires` | 缺少必填字段：`Requires` |
| 587 | [hipblas-common/hipblas-common.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipblas-common/hipblas-common.spec) | `Requires` | 缺少必填字段：`Requires` |
| 588 | [hipblaslt/hipblaslt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipblaslt/hipblaslt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 589 | [hipcub/hipcub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipcub/hipcub.spec) | `Requires` | 缺少必填字段：`Requires` |
| 590 | [hipfft/hipfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipfft/hipfft.spec) | `Requires` | 缺少必填字段：`Requires` |
| 591 | [hipify/hipify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipify/hipify.spec) | `Requires` | 缺少必填字段：`Requires` |
| 592 | [hiprand/hiprand.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hiprand/hiprand.spec) | `Requires` | 缺少必填字段：`Requires` |
| 593 | [hipsolver/hipsolver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipsolver/hipsolver.spec) | `Requires` | 缺少必填字段：`Requires` |
| 594 | [hipsparse/hipsparse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipsparse/hipsparse.spec) | `Requires` | 缺少必填字段：`Requires` |
| 595 | [hipsparselt/hipsparselt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipsparselt/hipsparselt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 596 | [hostname/hostname.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hostname/hostname.spec) | `Requires` | 缺少必填字段：`Requires` |
| 597 | [htop/htop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/htop/htop.spec) | `Requires` | 缺少必填字段：`Requires` |
| 598 | [http-parser/http-parser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/http-parser/http-parser.spec) | `Requires` | 缺少必填字段：`Requires` |
| 599 | [httpd/httpd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/httpd/httpd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 600 | [hunspell/hunspell.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hunspell/hunspell.spec) | `Requires` | 缺少必填字段：`Requires` |
| 601 | [hwdata/hwdata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hwdata/hwdata.spec) | `Requires` | 缺少必填字段：`Requires` |
| 602 | [hwinfo/hwinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hwinfo/hwinfo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 603 | [hwloc/hwloc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hwloc/hwloc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 604 | [hyphen/hyphen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hyphen/hyphen.spec) | `Requires` | 缺少必填字段：`Requires` |
| 605 | [ibus/ibus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ibus/ibus.spec) | `Requires` | 缺少必填字段：`Requires` |
| 606 | [iio-sensor-proxy/iio-sensor-proxy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iio-sensor-proxy/iio-sensor-proxy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 607 | [ima-evm-utils/ima-evm-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ima-evm-utils/ima-evm-utils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 608 | [imath/imath.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/imath/imath.spec) | `Requires` | 缺少必填字段：`Requires` |
| 609 | [indent/indent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/indent/indent.spec) | `Requires` | 缺少必填字段：`Requires` |
| 610 | [inetutils/inetutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/inetutils/inetutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 611 | [inih/inih.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/inih/inih.spec) | `Requires` | 缺少必填字段：`Requires` |
| 612 | [iniparser/iniparser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iniparser/iniparser.spec) | `Requires` | 缺少必填字段：`Requires` |
| 613 | [iotop/iotop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iotop/iotop.spec) | `Requires` | 缺少必填字段：`Requires` |
| 614 | [ipcalc/ipcalc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ipcalc/ipcalc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 615 | [iperf/iperf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iperf/iperf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 616 | [ipmitool/ipmitool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ipmitool/ipmitool.spec) | `Requires` | 缺少必填字段：`Requires` |
| 617 | [iproute2/iproute2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iproute2/iproute2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 618 | [iprutils/iprutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iprutils/iprutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 619 | [ipset/ipset.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ipset/ipset.spec) | `Requires` | 缺少必填字段：`Requires` |
| 620 | [iptables/iptables.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iptables/iptables.spec) | `Requires` | 缺少必填字段：`Requires` |
| 621 | [iptraf-ng/iptraf-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iptraf-ng/iptraf-ng.spec) | `Requires` | 缺少必填字段：`Requires` |
| 622 | [iputils/iputils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iputils/iputils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 623 | [ipvsadm/ipvsadm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ipvsadm/ipvsadm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 624 | [isa-l/isa-l.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/isa-l/isa-l.spec) | `Requires` | 缺少必填字段：`Requires` |
| 625 | [isa-l_crypto/isa-l_crypto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/isa-l_crypto/isa-l_crypto.spec) | `Requires` | 缺少必填字段：`Requires` |
| 626 | [isl/isl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/isl/isl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 627 | [iso-codes/iso-codes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iso-codes/iso-codes.spec) | `Requires` | 缺少必填字段：`Requires` |
| 628 | [isomd5sum/isomd5sum.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/isomd5sum/isomd5sum.spec) | `Requires` | 缺少必填字段：`Requires` |
| 629 | [iw/iw.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iw/iw.spec) | `Requires` | 缺少必填字段：`Requires` |
| 630 | [jansson/jansson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jansson/jansson.spec) | `Requires` | 缺少必填字段：`Requires` |
| 631 | [jasper/jasper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jasper/jasper.spec) | `Requires` | 缺少必填字段：`Requires` |
| 632 | [jbig2dec/jbig2dec.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jbig2dec/jbig2dec.spec) | `Requires` | 缺少必填字段：`Requires` |
| 633 | [jemalloc/jemalloc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jemalloc/jemalloc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 634 | [jitterentropy/jitterentropy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jitterentropy/jitterentropy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 635 | [jose/jose.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jose/jose.spec) | `Requires` | 缺少必填字段：`Requires` |
| 636 | [jq/jq.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jq/jq.spec) | `Requires` | 缺少必填字段：`Requires` |
| 637 | [json-c/json-c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/json-c/json-c.spec) | `Requires` | 缺少必填字段：`Requires` |
| 638 | [json-glib/json-glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/json-glib/json-glib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 639 | [jsoncpp/jsoncpp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jsoncpp/jsoncpp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 640 | [jsonnet/jsonnet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jsonnet/jsonnet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 641 | [judy/judy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/judy/judy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 642 | [jxrlib/jxrlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jxrlib/jxrlib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 643 | [kate/kate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kate/kate.spec) | `Requires` | 缺少必填字段：`Requires` |
| 644 | [kbd/kbd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kbd/kbd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 645 | [kdecoration/kdecoration.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kdecoration/kdecoration.spec) | `Requires` | 缺少必填字段：`Requires` |
| 646 | [kdialog/kdialog.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kdialog/kdialog.spec) | `Requires` | 缺少必填字段：`Requires` |
| 647 | [kdsoap/kdsoap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kdsoap/kdsoap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 648 | [kdsoap-ws-discovery-client/kdsoap-ws-discovery-client.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kdsoap-ws-discovery-client/kdsoap-ws-discovery-client.spec) | `Requires` | 缺少必填字段：`Requires` |
| 649 | [keepalived/keepalived.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/keepalived/keepalived.spec) | `Requires` | 缺少必填字段：`Requires` |
| 650 | [kernel-hardening-checker/kernel-hardening-checker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kernel-hardening-checker/kernel-hardening-checker.spec) | `Requires` | 缺少必填字段：`Requires` |
| 651 | [kexec-tools/kexec-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kexec-tools/kexec-tools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 652 | [keybinder/keybinder.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/keybinder/keybinder.spec) | `Requires` | 缺少必填字段：`Requires` |
| 653 | [keyutils/keyutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/keyutils/keyutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 654 | [kf6-attica/kf6-attica.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-attica/kf6-attica.spec) | `Requires` | 缺少必填字段：`Requires` |
| 655 | [kf6-baloo/kf6-baloo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-baloo/kf6-baloo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 656 | [kf6-breeze-icons/kf6-breeze-icons.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-breeze-icons/kf6-breeze-icons.spec) | `Requires` | 缺少必填字段：`Requires` |
| 657 | [kf6-frameworkintegration/kf6-frameworkintegration.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-frameworkintegration/kf6-frameworkintegration.spec) | `Requires` | 缺少必填字段：`Requires` |
| 658 | [kf6-karchive/kf6-karchive.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-karchive/kf6-karchive.spec) | `Requires` | 缺少必填字段：`Requires` |
| 659 | [kf6-kauth/kf6-kauth.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kauth/kf6-kauth.spec) | `Requires` | 缺少必填字段：`Requires` |
| 660 | [kf6-kbookmarks/kf6-kbookmarks.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kbookmarks/kf6-kbookmarks.spec) | `Requires` | 缺少必填字段：`Requires` |
| 661 | [kf6-kcmutils/kf6-kcmutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kcmutils/kf6-kcmutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 662 | [kf6-kcodecs/kf6-kcodecs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kcodecs/kf6-kcodecs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 663 | [kf6-kcolorscheme/kf6-kcolorscheme.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kcolorscheme/kf6-kcolorscheme.spec) | `Requires` | 缺少必填字段：`Requires` |
| 664 | [kf6-kcompletion/kf6-kcompletion.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kcompletion/kf6-kcompletion.spec) | `Requires` | 缺少必填字段：`Requires` |
| 665 | [kf6-kconfig/kf6-kconfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kconfig/kf6-kconfig.spec) | `Requires` | 缺少必填字段：`Requires` |
| 666 | [kf6-kconfigwidgets/kf6-kconfigwidgets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kconfigwidgets/kf6-kconfigwidgets.spec) | `Requires` | 缺少必填字段：`Requires` |
| 667 | [kf6-kcrash/kf6-kcrash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kcrash/kf6-kcrash.spec) | `Requires` | 缺少必填字段：`Requires` |
| 668 | [kf6-kdbusaddons/kf6-kdbusaddons.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kdbusaddons/kf6-kdbusaddons.spec) | `Requires` | 缺少必填字段：`Requires` |
| 669 | [kf6-kdeclarative/kf6-kdeclarative.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kdeclarative/kf6-kdeclarative.spec) | `Requires` | 缺少必填字段：`Requires` |
| 670 | [kf6-kdesu/kf6-kdesu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kdesu/kf6-kdesu.spec) | `Requires` | 缺少必填字段：`Requires` |
| 671 | [kf6-kdnssd/kf6-kdnssd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kdnssd/kf6-kdnssd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 672 | [kf6-kdoctools/kf6-kdoctools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kdoctools/kf6-kdoctools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 673 | [kf6-kfilemetadata/kf6-kfilemetadata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kfilemetadata/kf6-kfilemetadata.spec) | `Requires` | 缺少必填字段：`Requires` |
| 674 | [kf6-kglobalaccel/kf6-kglobalaccel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kglobalaccel/kf6-kglobalaccel.spec) | `Requires` | 缺少必填字段：`Requires` |
| 675 | [kf6-kguiaddons/kf6-kguiaddons.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kguiaddons/kf6-kguiaddons.spec) | `Requires` | 缺少必填字段：`Requires` |
| 676 | [kf6-kholidays/kf6-kholidays.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kholidays/kf6-kholidays.spec) | `Requires` | 缺少必填字段：`Requires` |
| 677 | [kf6-ki18n/kf6-ki18n.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-ki18n/kf6-ki18n.spec) | `Requires` | 缺少必填字段：`Requires` |
| 678 | [kf6-kiconthemes/kf6-kiconthemes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kiconthemes/kf6-kiconthemes.spec) | `Requires` | 缺少必填字段：`Requires` |
| 679 | [kf6-kidletime/kf6-kidletime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kidletime/kf6-kidletime.spec) | `Requires` | 缺少必填字段：`Requires` |
| 680 | [kf6-kitemmodels/kf6-kitemmodels.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kitemmodels/kf6-kitemmodels.spec) | `Requires` | 缺少必填字段：`Requires` |
| 681 | [kf6-kitemviews/kf6-kitemviews.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kitemviews/kf6-kitemviews.spec) | `Requires` | 缺少必填字段：`Requires` |
| 682 | [kf6-kjobwidgets/kf6-kjobwidgets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kjobwidgets/kf6-kjobwidgets.spec) | `Requires` | 缺少必填字段：`Requires` |
| 683 | [kf6-knewstuff/kf6-knewstuff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-knewstuff/kf6-knewstuff.spec) | `Requires` | 缺少必填字段：`Requires` |
| 684 | [kf6-knotifications/kf6-knotifications.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-knotifications/kf6-knotifications.spec) | `Requires` | 缺少必填字段：`Requires` |
| 685 | [kf6-knotifyconfig/kf6-knotifyconfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-knotifyconfig/kf6-knotifyconfig.spec) | `Requires` | 缺少必填字段：`Requires` |
| 686 | [kf6-kpackage/kf6-kpackage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kpackage/kf6-kpackage.spec) | `Requires` | 缺少必填字段：`Requires` |
| 687 | [kf6-kparts/kf6-kparts.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kparts/kf6-kparts.spec) | `Requires` | 缺少必填字段：`Requires` |
| 688 | [kf6-kpty/kf6-kpty.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kpty/kf6-kpty.spec) | `Requires` | 缺少必填字段：`Requires` |
| 689 | [kf6-krunner/kf6-krunner.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-krunner/kf6-krunner.spec) | `Requires` | 缺少必填字段：`Requires` |
| 690 | [kf6-kservice/kf6-kservice.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kservice/kf6-kservice.spec) | `Requires` | 缺少必填字段：`Requires` |
| 691 | [kf6-kstatusnotifieritem/kf6-kstatusnotifieritem.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kstatusnotifieritem/kf6-kstatusnotifieritem.spec) | `Requires` | 缺少必填字段：`Requires` |
| 692 | [kf6-ktextwidgets/kf6-ktextwidgets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-ktextwidgets/kf6-ktextwidgets.spec) | `Requires` | 缺少必填字段：`Requires` |
| 693 | [kf6-kunitconversion/kf6-kunitconversion.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kunitconversion/kf6-kunitconversion.spec) | `Requires` | 缺少必填字段：`Requires` |
| 694 | [kf6-kuserfeedback/kf6-kuserfeedback.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kuserfeedback/kf6-kuserfeedback.spec) | `Requires` | 缺少必填字段：`Requires` |
| 695 | [kf6-kwallet/kf6-kwallet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kwallet/kf6-kwallet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 696 | [kf6-kwidgetsaddons/kf6-kwidgetsaddons.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kwidgetsaddons/kf6-kwidgetsaddons.spec) | `Requires` | 缺少必填字段：`Requires` |
| 697 | [kf6-kwindowsystem/kf6-kwindowsystem.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kwindowsystem/kf6-kwindowsystem.spec) | `Requires` | 缺少必填字段：`Requires` |
| 698 | [kf6-kxmlgui/kf6-kxmlgui.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kxmlgui/kf6-kxmlgui.spec) | `Requires` | 缺少必填字段：`Requires` |
| 699 | [kf6-modemmanager-qt/kf6-modemmanager-qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-modemmanager-qt/kf6-modemmanager-qt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 700 | [kf6-networkmanager-qt/kf6-networkmanager-qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-networkmanager-qt/kf6-networkmanager-qt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 701 | [kf6-prison/kf6-prison.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-prison/kf6-prison.spec) | `Requires` | 缺少必填字段：`Requires` |
| 702 | [kf6-solid/kf6-solid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-solid/kf6-solid.spec) | `Requires` | 缺少必填字段：`Requires` |
| 703 | [kf6-sonnet/kf6-sonnet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-sonnet/kf6-sonnet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 704 | [kf6-syndication/kf6-syndication.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-syndication/kf6-syndication.spec) | `Requires` | 缺少必填字段：`Requires` |
| 705 | [kf6-syntax-highlighting/kf6-syntax-highlighting.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-syntax-highlighting/kf6-syntax-highlighting.spec) | `Requires` | 缺少必填字段：`Requires` |
| 706 | [kf6-threadweaver/kf6-threadweaver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-threadweaver/kf6-threadweaver.spec) | `Requires` | 缺少必填字段：`Requires` |
| 707 | [kglobalacceld/kglobalacceld.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kglobalacceld/kglobalacceld.spec) | `Requires` | 缺少必填字段：`Requires` |
| 708 | [kmenuedit/kmenuedit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kmenuedit/kmenuedit.spec) | `Requires` | 缺少必填字段：`Requires` |
| 709 | [kmod/kmod.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kmod/kmod.spec) | `Requires` | 缺少必填字段：`Requires` |
| 710 | [kmscube/kmscube.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kmscube/kmscube.spec) | `Requires` | 缺少必填字段：`Requires` |
| 711 | [knighttime/knighttime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/knighttime/knighttime.spec) | `Requires` | 缺少必填字段：`Requires` |
| 712 | [kpipewire/kpipewire.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kpipewire/kpipewire.spec) | `Requires` | 缺少必填字段：`Requires` |
| 713 | [kpmcore/kpmcore.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kpmcore/kpmcore.spec) | `Requires` | 缺少必填字段：`Requires` |
| 714 | [krb5/krb5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/krb5/krb5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 715 | [kronosnet/kronosnet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kronosnet/kronosnet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 716 | [kscreenlocker/kscreenlocker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kscreenlocker/kscreenlocker.spec) | `Requires` | 缺少必填字段：`Requires` |
| 717 | [ksystemstats/ksystemstats.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ksystemstats/ksystemstats.spec) | `Requires` | 缺少必填字段：`Requires` |
| 718 | [kwayland6/kwayland6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kwayland6/kwayland6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 719 | [kyua/kyua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kyua/kyua.spec) | `Requires` | 缺少必填字段：`Requires` |
| 720 | [lame/lame.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lame/lame.spec) | `Requires` | 缺少必填字段：`Requires` |
| 721 | [layer-shell-qt/layer-shell-qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/layer-shell-qt/layer-shell-qt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 722 | [lcms2/lcms2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lcms2/lcms2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 723 | [ldns/ldns.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ldns/ldns.spec) | `Requires` | 缺少必填字段：`Requires` |
| 724 | [lerc/lerc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lerc/lerc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 725 | [less/less.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/less/less.spec) | `Requires` | 缺少必填字段：`Requires` |
| 726 | [leveldb/leveldb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/leveldb/leveldb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 727 | [libabigail/libabigail.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libabigail/libabigail.spec) | `Requires` | 缺少必填字段：`Requires` |
| 728 | [libaccounts-glib/libaccounts-glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libaccounts-glib/libaccounts-glib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 729 | [libaccounts-qt/libaccounts-qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libaccounts-qt/libaccounts-qt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 730 | [libaec/libaec.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libaec/libaec.spec) | `Requires` | 缺少必填字段：`Requires` |
| 731 | [libaio/libaio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libaio/libaio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 732 | [libarchive/libarchive.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libarchive/libarchive.spec) | `Requires` | 缺少必填字段：`Requires` |
| 733 | [libass/libass.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libass/libass.spec) | `Requires` | 缺少必填字段：`Requires` |
| 734 | [libassuan/libassuan.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libassuan/libassuan.spec) | `Requires` | 缺少必填字段：`Requires` |
| 735 | [libatasmart/libatasmart.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libatasmart/libatasmart.spec) | `Requires` | 缺少必填字段：`Requires` |
| 736 | [libatomic_ops/libatomic_ops.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libatomic_ops/libatomic_ops.spec) | `Requires` | 缺少必填字段：`Requires` |
| 737 | [libavif/libavif.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libavif/libavif.spec) | `Requires` | 缺少必填字段：`Requires` |
| 738 | [libblockdev/libblockdev.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libblockdev/libblockdev.spec) | `Requires` | 缺少必填字段：`Requires` |
| 739 | [libbluray/libbluray.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libbluray/libbluray.spec) | `Requires` | 缺少必填字段：`Requires` |
| 740 | [libbpf/libbpf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libbpf/libbpf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 741 | [libbsd/libbsd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libbsd/libbsd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 742 | [libburn/libburn.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libburn/libburn.spec) | `Requires` | 缺少必填字段：`Requires` |
| 743 | [libbytesize/libbytesize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libbytesize/libbytesize.spec) | `Requires` | 缺少必填字段：`Requires` |
| 744 | [libcaca/libcaca.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcaca/libcaca.spec) | `Requires` | 缺少必填字段：`Requires` |
| 745 | [libcanberra/libcanberra.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcanberra/libcanberra.spec) | `Requires` | 缺少必填字段：`Requires` |
| 746 | [libcap/libcap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcap/libcap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 747 | [libcap-ng/libcap-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcap-ng/libcap-ng.spec) | `Requires` | 缺少必填字段：`Requires` |
| 748 | [libcbor/libcbor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcbor/libcbor.spec) | `Requires` | 缺少必填字段：`Requires` |
| 749 | [libcdata/libcdata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcdata/libcdata.spec) | `Requires` | 缺少必填字段：`Requires` |
| 750 | [libcdio/libcdio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcdio/libcdio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 751 | [libcdio-paranoia/libcdio-paranoia.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcdio-paranoia/libcdio-paranoia.spec) | `Requires` | 缺少必填字段：`Requires` |
| 752 | [libcerror/libcerror.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcerror/libcerror.spec) | `Requires` | 缺少必填字段：`Requires` |
| 753 | [libcgroup/libcgroup.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcgroup/libcgroup.spec) | `Requires` | 缺少必填字段：`Requires` |
| 754 | [libclc/libclc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libclc/libclc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 755 | [libcnotify/libcnotify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcnotify/libcnotify.spec) | `Requires` | 缺少必填字段：`Requires` |
| 756 | [libcomps/libcomps.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcomps/libcomps.spec) | `Requires` | 缺少必填字段：`Requires` |
| 757 | [libconfig/libconfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libconfig/libconfig.spec) | `Requires` | 缺少必填字段：`Requires` |
| 758 | [libconfuse/libconfuse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libconfuse/libconfuse.spec) | `Requires` | 缺少必填字段：`Requires` |
| 759 | [libcthreads/libcthreads.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcthreads/libcthreads.spec) | `Requires` | 缺少必填字段：`Requires` |
| 760 | [libdatrie/libdatrie.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdatrie/libdatrie.spec) | `Requires` | 缺少必填字段：`Requires` |
| 761 | [libdecor/libdecor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdecor/libdecor.spec) | `Requires` | 缺少必填字段：`Requires` |
| 762 | [libdeflate/libdeflate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdeflate/libdeflate.spec) | `Requires` | 缺少必填字段：`Requires` |
| 763 | [libdisplay-info/libdisplay-info.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdisplay-info/libdisplay-info.spec) | `Requires` | 缺少必填字段：`Requires` |
| 764 | [libdmtx/libdmtx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdmtx/libdmtx.spec) | `Requires` | 缺少必填字段：`Requires` |
| 765 | [libdrm/libdrm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdrm/libdrm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 766 | [libdvdcss/libdvdcss.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdvdcss/libdvdcss.spec) | `Requires` | 缺少必填字段：`Requires` |
| 767 | [libdvdnav/libdvdnav.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdvdnav/libdvdnav.spec) | `Requires` | 缺少必填字段：`Requires` |
| 768 | [libdvdread/libdvdread.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdvdread/libdvdread.spec) | `Requires` | 缺少必填字段：`Requires` |
| 769 | [libdwarf/libdwarf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdwarf/libdwarf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 770 | [libeconf/libeconf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libeconf/libeconf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 771 | [libei/libei.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libei/libei.spec) | `Requires` | 缺少必填字段：`Requires` |
| 772 | [libepoxy/libepoxy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libepoxy/libepoxy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 773 | [libestr/libestr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libestr/libestr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 774 | [libevdev/libevdev.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libevdev/libevdev.spec) | `Requires` | 缺少必填字段：`Requires` |
| 775 | [libevent/libevent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libevent/libevent.spec) | `Requires` | 缺少必填字段：`Requires` |
| 776 | [libfcache/libfcache.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfcache/libfcache.spec) | `Requires` | 缺少必填字段：`Requires` |
| 777 | [libfdata/libfdata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfdata/libfdata.spec) | `Requires` | 缺少必填字段：`Requires` |
| 778 | [libffcall/libffcall.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libffcall/libffcall.spec) | `Requires` | 缺少必填字段：`Requires` |
| 779 | [libfontenc/libfontenc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfontenc/libfontenc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 780 | [libfyaml/libfyaml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfyaml/libfyaml.spec) | `Requires` | 缺少必填字段：`Requires` |
| 781 | [libgcrypt/libgcrypt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libgcrypt/libgcrypt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 782 | [libgee/libgee.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libgee/libgee.spec) | `Requires` | 缺少必填字段：`Requires` |
| 783 | [libgit2/libgit2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libgit2/libgit2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 784 | [libglvnd/libglvnd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libglvnd/libglvnd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 785 | [libgpg-error/libgpg-error.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libgpg-error/libgpg-error.spec) | `Requires` | 缺少必填字段：`Requires` |
| 786 | [libgudev/libgudev.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libgudev/libgudev.spec) | `Requires` | 缺少必填字段：`Requires` |
| 787 | [libgusb/libgusb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libgusb/libgusb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 788 | [libheif/libheif.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libheif/libheif.spec) | `Requires` | 缺少必填字段：`Requires` |
| 789 | [libiberty/libiberty.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libiberty/libiberty.spec) | `Requires` | 缺少必填字段：`Requires` |
| 790 | [libICE/libICE.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libICE/libICE.spec) | `Requires` | 缺少必填字段：`Requires` |
| 791 | [libidl/libidl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libidl/libidl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 792 | [libidn2/libidn2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libidn2/libidn2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 793 | [libime/libime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libime/libime.spec) | `Requires` | 缺少必填字段：`Requires` |
| 794 | [libimobiledevice/libimobiledevice.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libimobiledevice/libimobiledevice.spec) | `Requires` | 缺少必填字段：`Requires` |
| 795 | [libimobiledevice-glue/libimobiledevice-glue.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libimobiledevice-glue/libimobiledevice-glue.spec) | `Requires` | 缺少必填字段：`Requires` |
| 796 | [libinput/libinput.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libinput/libinput.spec) | `Requires` | 缺少必填字段：`Requires` |
| 797 | [libiscsi/libiscsi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libiscsi/libiscsi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 798 | [libisoburn/libisoburn.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libisoburn/libisoburn.spec) | `Requires` | 缺少必填字段：`Requires` |
| 799 | [libisofs/libisofs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libisofs/libisofs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 800 | [libjpeg-turbo/libjpeg-turbo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libjpeg-turbo/libjpeg-turbo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 801 | [libjwt/libjwt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libjwt/libjwt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 802 | [libjxl/libjxl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libjxl/libjxl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 803 | [libkexiv2/libkexiv2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libkexiv2/libkexiv2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 804 | [libklvanc/libklvanc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libklvanc/libklvanc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 805 | [libksba/libksba.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libksba/libksba.spec) | `Requires` | 缺少必填字段：`Requires` |
| 806 | [libkscreen/libkscreen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libkscreen/libkscreen.spec) | `Requires` | 缺少必填字段：`Requires` |
| 807 | [liblc3/liblc3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/liblc3/liblc3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 808 | [libliftoff/libliftoff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libliftoff/libliftoff.spec) | `Requires` | 缺少必填字段：`Requires` |
| 809 | [liblognorm/liblognorm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/liblognorm/liblognorm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 810 | [libmaxminddb/libmaxminddb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmaxminddb/libmaxminddb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 811 | [libmbim/libmbim.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmbim/libmbim.spec) | `Requires` | 缺少必填字段：`Requires` |
| 812 | [libmd/libmd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmd/libmd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 813 | [libmicrohttpd/libmicrohttpd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmicrohttpd/libmicrohttpd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 814 | [libmnl/libmnl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmnl/libmnl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 815 | [libmodulemd/libmodulemd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmodulemd/libmodulemd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 816 | [libmspack/libmspack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmspack/libmspack.spec) | `Requires` | 缺少必填字段：`Requires` |
| 817 | [libmtp/libmtp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmtp/libmtp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 818 | [libmypaint/libmypaint.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmypaint/libmypaint.spec) | `Requires` | 缺少必填字段：`Requires` |
| 819 | [libnbd/libnbd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnbd/libnbd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 820 | [libndp/libndp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libndp/libndp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 821 | [libnetfilter_acct/libnetfilter_acct.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_acct/libnetfilter_acct.spec) | `Requires` | 缺少必填字段：`Requires` |
| 822 | [libnetfilter_conntrack/libnetfilter_conntrack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_conntrack/libnetfilter_conntrack.spec) | `Requires` | 缺少必填字段：`Requires` |
| 823 | [libnetfilter_cthelper/libnetfilter_cthelper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_cthelper/libnetfilter_cthelper.spec) | `Requires` | 缺少必填字段：`Requires` |
| 824 | [libnetfilter_cttimeout/libnetfilter_cttimeout.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_cttimeout/libnetfilter_cttimeout.spec) | `Requires` | 缺少必填字段：`Requires` |
| 825 | [libnetfilter_log/libnetfilter_log.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_log/libnetfilter_log.spec) | `Requires` | 缺少必填字段：`Requires` |
| 826 | [libnetfilter_queue/libnetfilter_queue.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_queue/libnetfilter_queue.spec) | `Requires` | 缺少必填字段：`Requires` |
| 827 | [libnfnetlink/libnfnetlink.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnfnetlink/libnfnetlink.spec) | `Requires` | 缺少必填字段：`Requires` |
| 828 | [libnfs/libnfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnfs/libnfs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 829 | [libnftnl/libnftnl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnftnl/libnftnl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 830 | [libnl/libnl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnl/libnl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 831 | [libnsl/libnsl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnsl/libnsl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 832 | [libnvme/libnvme.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnvme/libnvme.spec) | `Requires` | 缺少必填字段：`Requires` |
| 833 | [libogg/libogg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libogg/libogg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 834 | [libp11/libp11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libp11/libp11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 835 | [libpaper/libpaper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libpaper/libpaper.spec) | `Requires` | 缺少必填字段：`Requires` |
| 836 | [libpcap/libpcap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libpcap/libpcap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 837 | [libpipeline/libpipeline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libpipeline/libpipeline.spec) | `Requires` | 缺少必填字段：`Requires` |
| 838 | [libpkgmanifest/libpkgmanifest.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libpkgmanifest/libpkgmanifest.spec) | `Requires` | 缺少必填字段：`Requires` |
| 839 | [libplacebo/libplacebo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libplacebo/libplacebo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 840 | [libplasma/libplasma.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libplasma/libplasma.spec) | `Requires` | 缺少必填字段：`Requires` |
| 841 | [libplist/libplist.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libplist/libplist.spec) | `Requires` | 缺少必填字段：`Requires` |
| 842 | [libpng/libpng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libpng/libpng.spec) | `Requires` | 缺少必填字段：`Requires` |
| 843 | [libproxy/libproxy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libproxy/libproxy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 844 | [libpwquality/libpwquality.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libpwquality/libpwquality.spec) | `Requires` | 缺少必填字段：`Requires` |
| 845 | [libqaccessibilityclient/libqaccessibilityclient.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libqaccessibilityclient/libqaccessibilityclient.spec) | `Requires` | 缺少必填字段：`Requires` |
| 846 | [libqalculate/libqalculate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libqalculate/libqalculate.spec) | `Requires` | 缺少必填字段：`Requires` |
| 847 | [libqb/libqb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libqb/libqb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 848 | [libqmi/libqmi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libqmi/libqmi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 849 | [libqrtr-glib/libqrtr-glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libqrtr-glib/libqrtr-glib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 850 | [librabbitmq/librabbitmq.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/librabbitmq/librabbitmq.spec) | `Requires` | 缺少必填字段：`Requires` |
| 851 | [libraqm/libraqm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libraqm/libraqm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 852 | [libraw/libraw.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libraw/libraw.spec) | `Requires` | 缺少必填字段：`Requires` |
| 853 | [librdkafka/librdkafka.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/librdkafka/librdkafka.spec) | `Requires` | 缺少必填字段：`Requires` |
| 854 | [librepo/librepo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/librepo/librepo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 855 | [libsamplerate/libsamplerate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsamplerate/libsamplerate.spec) | `Requires` | 缺少必填字段：`Requires` |
| 856 | [libsass/libsass.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsass/libsass.spec) | `Requires` | 缺少必填字段：`Requires` |
| 857 | [libseccomp/libseccomp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libseccomp/libseccomp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 858 | [libsecret/libsecret.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsecret/libsecret.spec) | `Requires` | 缺少必填字段：`Requires` |
| 859 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | `Requires` | 缺少必填字段：`Requires` |
| 860 | [libsemanage/libsemanage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsemanage/libsemanage.spec) | `Requires` | 缺少必填字段：`Requires` |
| 861 | [libsepol/libsepol.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsepol/libsepol.spec) | `Requires` | 缺少必填字段：`Requires` |
| 862 | [libsfdo/libsfdo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsfdo/libsfdo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 863 | [libsigc++/libsigc++.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsigc++/libsigc++.spec) | `Requires` | 缺少必填字段：`Requires` |
| 864 | [libsigc++2/libsigc++2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsigc++2/libsigc++2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 865 | [libslirp/libslirp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libslirp/libslirp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 866 | [libSM/libSM.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libSM/libSM.spec) | `Requires` | 缺少必填字段：`Requires` |
| 867 | [libsndfile/libsndfile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsndfile/libsndfile.spec) | `Requires` | 缺少必填字段：`Requires` |
| 868 | [libsodium/libsodium.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsodium/libsodium.spec) | `Requires` | 缺少必填字段：`Requires` |
| 869 | [libsolv/libsolv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsolv/libsolv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 870 | [libsoup/libsoup.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsoup/libsoup.spec) | `Requires` | 缺少必填字段：`Requires` |
| 871 | [libspiro/libspiro.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libspiro/libspiro.spec) | `Requires` | 缺少必填字段：`Requires` |
| 872 | [libspng/libspng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libspng/libspng.spec) | `Requires` | 缺少必填字段：`Requires` |
| 873 | [libsquish/libsquish.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsquish/libsquish.spec) | `Requires` | 缺少必填字段：`Requires` |
| 874 | [libssh2/libssh2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libssh2/libssh2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 875 | [libtar/libtar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtar/libtar.spec) | `Requires` | 缺少必填字段：`Requires` |
| 876 | [libtasn1/libtasn1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtasn1/libtasn1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 877 | [libtatsu/libtatsu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtatsu/libtatsu.spec) | `Requires` | 缺少必填字段：`Requires` |
| 878 | [libthai/libthai.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libthai/libthai.spec) | `Requires` | 缺少必填字段：`Requires` |
| 879 | [libtiff/libtiff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtiff/libtiff.spec) | `Requires` | 缺少必填字段：`Requires` |
| 880 | [libtirpc/libtirpc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtirpc/libtirpc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 881 | [libtomcrypt/libtomcrypt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtomcrypt/libtomcrypt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 882 | [libtommath/libtommath.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtommath/libtommath.spec) | `Requires` | 缺少必填字段：`Requires` |
| 883 | [libtpms/libtpms.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtpms/libtpms.spec) | `Requires` | 缺少必填字段：`Requires` |
| 884 | [libtraceevent/libtraceevent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtraceevent/libtraceevent.spec) | `Requires` | 缺少必填字段：`Requires` |
| 885 | [libtree/libtree.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtree/libtree.spec) | `Requires` | 缺少必填字段：`Requires` |
| 886 | [libudev-zero/libudev-zero.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libudev-zero/libudev-zero.spec) | `Requires` | 缺少必填字段：`Requires` |
| 887 | [libunibreak/libunibreak.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libunibreak/libunibreak.spec) | `Requires` | 缺少必填字段：`Requires` |
| 888 | [libunwind/libunwind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libunwind/libunwind.spec) | `Requires` | 缺少必填字段：`Requires` |
| 889 | [liburing/liburing.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/liburing/liburing.spec) | `Requires` | 缺少必填字段：`Requires` |
| 890 | [libusb/libusb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libusb/libusb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 891 | [libusbmuxd/libusbmuxd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libusbmuxd/libusbmuxd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 892 | [libuser/libuser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libuser/libuser.spec) | `Requires` | 缺少必填字段：`Requires` |
| 893 | [libutempter/libutempter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libutempter/libutempter.spec) | `Requires` | 缺少必填字段：`Requires` |
| 894 | [libuv/libuv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libuv/libuv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 895 | [libva/libva.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libva/libva.spec) | `Requires` | 缺少必填字段：`Requires` |
| 896 | [libvdpau/libvdpau.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libvdpau/libvdpau.spec) | `Requires` | 缺少必填字段：`Requires` |
| 897 | [libverto/libverto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libverto/libverto.spec) | `Requires` | 缺少必填字段：`Requires` |
| 898 | [libvirt-glib/libvirt-glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libvirt-glib/libvirt-glib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 899 | [libvncserver/libvncserver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libvncserver/libvncserver.spec) | `Requires` | 缺少必填字段：`Requires` |
| 900 | [libvoikko/libvoikko.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libvoikko/libvoikko.spec) | `Requires` | 缺少必填字段：`Requires` |
| 901 | [libvorbis/libvorbis.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libvorbis/libvorbis.spec) | `Requires` | 缺少必填字段：`Requires` |
| 902 | [libvpx/libvpx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libvpx/libvpx.spec) | `Requires` | 缺少必填字段：`Requires` |
| 903 | [libwebp/libwebp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libwebp/libwebp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 904 | [libwebsockets/libwebsockets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libwebsockets/libwebsockets.spec) | `Requires` | 缺少必填字段：`Requires` |
| 905 | [libX11/libX11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libX11/libX11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 906 | [libx86emu/libx86emu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libx86emu/libx86emu.spec) | `Requires` | 缺少必填字段：`Requires` |
| 907 | [libXau/libXau.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXau/libXau.spec) | `Requires` | 缺少必填字段：`Requires` |
| 908 | [libxcb/libxcb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxcb/libxcb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 909 | [libXcomposite/libXcomposite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXcomposite/libXcomposite.spec) | `Requires` | 缺少必填字段：`Requires` |
| 910 | [libxcrypt/libxcrypt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxcrypt/libxcrypt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 911 | [libXcursor/libXcursor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXcursor/libXcursor.spec) | `Requires` | 缺少必填字段：`Requires` |
| 912 | [libxcvt/libxcvt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxcvt/libxcvt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 913 | [libXdamage/libXdamage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXdamage/libXdamage.spec) | `Requires` | 缺少必填字段：`Requires` |
| 914 | [libXdmcp/libXdmcp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXdmcp/libXdmcp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 915 | [libXfixes/libXfixes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXfixes/libXfixes.spec) | `Requires` | 缺少必填字段：`Requires` |
| 916 | [libXfont2/libXfont2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXfont2/libXfont2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 917 | [libXft/libXft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXft/libXft.spec) | `Requires` | 缺少必填字段：`Requires` |
| 918 | [libXinerama/libXinerama.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXinerama/libXinerama.spec) | `Requires` | 缺少必填字段：`Requires` |
| 919 | [libxkbcommon/libxkbcommon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxkbcommon/libxkbcommon.spec) | `Requires` | 缺少必填字段：`Requires` |
| 920 | [libxkbfile/libxkbfile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxkbfile/libxkbfile.spec) | `Requires` | 缺少必填字段：`Requires` |
| 921 | [libxml2/libxml2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxml2/libxml2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 922 | [libXmu/libXmu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXmu/libXmu.spec) | `Requires` | 缺少必填字段：`Requires` |
| 923 | [libXpresent/libXpresent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXpresent/libXpresent.spec) | `Requires` | 缺少必填字段：`Requires` |
| 924 | [libXrender/libXrender.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXrender/libXrender.spec) | `Requires` | 缺少必填字段：`Requires` |
| 925 | [libXres/libXres.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXres/libXres.spec) | `Requires` | 缺少必填字段：`Requires` |
| 926 | [libXScrnSaver/libXScrnSaver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXScrnSaver/libXScrnSaver.spec) | `Requires` | 缺少必填字段：`Requires` |
| 927 | [libxshmfence/libxshmfence.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxshmfence/libxshmfence.spec) | `Requires` | 缺少必填字段：`Requires` |
| 928 | [libxslt/libxslt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxslt/libxslt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 929 | [libXv/libXv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXv/libXv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 930 | [libXxf86vm/libXxf86vm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXxf86vm/libXxf86vm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 931 | [libyaml/libyaml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libyaml/libyaml.spec) | `Requires` | 缺少必填字段：`Requires` |
| 932 | [libyang/libyang.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libyang/libyang.spec) | `Requires` | 缺少必填字段：`Requires` |
| 933 | [libyuv/libyuv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libyuv/libyuv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 934 | [libzip/libzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libzip/libzip.spec) | `Requires` | 缺少必填字段：`Requires` |
| 935 | [lksctp-tools/lksctp-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lksctp-tools/lksctp-tools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 936 | [llama-cpp/llama-cpp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llama-cpp/llama-cpp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 937 | [llhttp/llhttp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llhttp/llhttp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 938 | [lmdb/lmdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lmdb/lmdb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 939 | [log4cplus/log4cplus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/log4cplus/log4cplus.spec) | `Requires` | 缺少必填字段：`Requires` |
| 940 | [log4cxx/log4cxx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/log4cxx/log4cxx.spec) | `Requires` | 缺少必填字段：`Requires` |
| 941 | [logrotate/logrotate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/logrotate/logrotate.spec) | `Requires` | 缺少必填字段：`Requires` |
| 942 | [lsb-release/lsb-release.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lsb-release/lsb-release.spec) | `Requires` | 缺少必填字段：`Requires` |
| 943 | [lshw/lshw.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lshw/lshw.spec) | `Requires` | 缺少必填字段：`Requires` |
| 944 | [lsof/lsof.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lsof/lsof.spec) | `Requires` | 缺少必填字段：`Requires` |
| 945 | [ltp/ltp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ltp/ltp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 946 | [ltrace/ltrace.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ltrace/ltrace.spec) | `Requires` | 缺少必填字段：`Requires` |
| 947 | [lttng-ust/lttng-ust.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lttng-ust/lttng-ust.spec) | `Requires` | 缺少必填字段：`Requires` |
| 948 | [lua-lpeg/lua-lpeg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua-lpeg/lua-lpeg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 949 | [luajit/luajit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/luajit/luajit.spec) | `Requires` | 缺少必填字段：`Requires` |
| 950 | [luksmeta/luksmeta.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/luksmeta/luksmeta.spec) | `Requires` | 缺少必填字段：`Requires` |
| 951 | [lxcfs/lxcfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lxcfs/lxcfs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 952 | [lz4/lz4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lz4/lz4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 953 | [m4/m4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/m4/m4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 954 | [magic_enum/magic_enum.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/magic_enum/magic_enum.spec) | `Requires` | 缺少必填字段：`Requires` |
| 955 | [magma/magma.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/magma/magma.spec) | `Requires` | 缺少必填字段：`Requires` |
| 956 | [mailcap/mailcap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mailcap/mailcap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 957 | [mailutils/mailutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mailutils/mailutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 958 | [make/make.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/make/make.spec) | `Requires` | 缺少必填字段：`Requires` |
| 959 | [mariadb-connector-c/mariadb-connector-c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mariadb-connector-c/mariadb-connector-c.spec) | `Requires` | 缺少必填字段：`Requires` |
| 960 | [marisa/marisa.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/marisa/marisa.spec) | `Requires` | 缺少必填字段：`Requires` |
| 961 | [md4c/md4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/md4c/md4c.spec) | `Requires` | 缺少必填字段：`Requires` |
| 962 | [mdadm/mdadm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mdadm/mdadm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 963 | [mdevd/mdevd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mdevd/mdevd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 964 | [memcached/memcached.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/memcached/memcached.spec) | `Requires` | 缺少必填字段：`Requires` |
| 965 | [mergerfs/mergerfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mergerfs/mergerfs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 966 | [mesa/mesa.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mesa/mesa.spec) | `Requires` | 缺少必填字段：`Requires` |
| 967 | [mesa-demos/mesa-demos.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mesa-demos/mesa-demos.spec) | `Requires` | 缺少必填字段：`Requires` |
| 968 | [milou/milou.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/milou/milou.spec) | `Requires` | 缺少必填字段：`Requires` |
| 969 | [mimalloc/mimalloc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mimalloc/mimalloc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 970 | [minicom/minicom.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/minicom/minicom.spec) | `Requires` | 缺少必填字段：`Requires` |
| 971 | [minio/minio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/minio/minio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 972 | [minizip-ng/minizip-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/minizip-ng/minizip-ng.spec) | `Requires` | 缺少必填字段：`Requires` |
| 973 | [mksh/mksh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mksh/mksh.spec) | `Requires` | 缺少必填字段：`Requires` |
| 974 | [mlocate/mlocate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mlocate/mlocate.spec) | `Requires` | 缺少必填字段：`Requires` |
| 975 | [mobile-broadband-provider-info/mobile-broadband-provider-info.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mobile-broadband-provider-info/mobile-broadband-provider-info.spec) | `Requires` | 缺少必填字段：`Requires` |
| 976 | [ModemManager/ModemManager.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ModemManager/ModemManager.spec) | `Requires` | 缺少必填字段：`Requires` |
| 977 | [mokutil/mokutil.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mokutil/mokutil.spec) | `Requires` | 缺少必填字段：`Requires` |
| 978 | [mold/mold.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mold/mold.spec) | `Requires` | 缺少必填字段：`Requires` |
| 979 | [mpc/mpc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mpc/mpc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 980 | [mpv/mpv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mpv/mpv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 981 | [msmtp/msmtp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/msmtp/msmtp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 982 | [mtd-utils/mtd-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mtd-utils/mtd-utils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 983 | [mtdev/mtdev.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mtdev/mtdev.spec) | `Requires` | 缺少必填字段：`Requires` |
| 984 | [mtr/mtr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mtr/mtr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 985 | [mujs/mujs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mujs/mujs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 986 | [mupdf/mupdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mupdf/mupdf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 987 | [mypaint-brushes/mypaint-brushes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mypaint-brushes/mypaint-brushes.spec) | `Requires` | 缺少必填字段：`Requires` |
| 988 | [nano/nano.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nano/nano.spec) | `Requires` | 缺少必填字段：`Requires` |
| 989 | [nasm/nasm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nasm/nasm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 990 | [ncurses/ncurses.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ncurses/ncurses.spec) | `Requires` | 缺少必填字段：`Requires` |
| 991 | [ndctl/ndctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ndctl/ndctl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 992 | [netperf/netperf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/netperf/netperf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 993 | [nettle/nettle.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nettle/nettle.spec) | `Requires` | 缺少必填字段：`Requires` |
| 994 | [NetworkManager/NetworkManager.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/NetworkManager/NetworkManager.spec) | `Requires` | 缺少必填字段：`Requires` |
| 995 | [newt/newt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/newt/newt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 996 | [nexttrace/nexttrace.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nexttrace/nexttrace.spec) | `Requires` | 缺少必填字段：`Requires` |
| 997 | [nfs-utils/nfs-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nfs-utils/nfs-utils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 998 | [nfs4-acl-tools/nfs4-acl-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nfs4-acl-tools/nfs4-acl-tools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 999 | [nghttp2/nghttp2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nghttp2/nghttp2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1000 | [nghttp3/nghttp3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nghttp3/nghttp3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1001 | [ngtcp2/ngtcp2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ngtcp2/ngtcp2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1002 | [ninja/ninja.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ninja/ninja.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1003 | [nlohmann-json/nlohmann-json.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nlohmann-json/nlohmann-json.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1004 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1005 | [nspr/nspr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nspr/nspr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1006 | [nss_wrapper/nss_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nss_wrapper/nss_wrapper.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1007 | [ntfs-3g/ntfs-3g.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ntfs-3g/ntfs-3g.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1008 | [numactl/numactl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/numactl/numactl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1009 | [nvme-cli/nvme-cli.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nvme-cli/nvme-cli.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1010 | [oath-toolkit/oath-toolkit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/oath-toolkit/oath-toolkit.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1011 | [oniguruma/oniguruma.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/oniguruma/oniguruma.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1012 | [onnx/onnx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/onnx/onnx.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1013 | [onnx-optimizer/onnx-optimizer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/onnx-optimizer/onnx-optimizer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1014 | [onnxruntime/onnxruntime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/onnxruntime/onnxruntime.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1015 | [open-iscsi/open-iscsi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/open-iscsi/open-iscsi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1016 | [openblas/openblas.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openblas/openblas.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1017 | [opencc/opencc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/opencc/opencc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1018 | [openconnect/openconnect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openconnect/openconnect.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1019 | [opencv/opencv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/opencv/opencv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1020 | [openexr/openexr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openexr/openexr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1021 | [openjpeg/openjpeg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openjpeg/openjpeg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1022 | [openresolv/openresolv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openresolv/openresolv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1023 | [openssl/openssl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openssl/openssl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1024 | [openvpn/openvpn.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openvpn/openvpn.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1025 | [openvswitch/openvswitch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openvswitch/openvswitch.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1026 | [openzl/openzl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openzl/openzl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1027 | [opus/opus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/opus/opus.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1028 | [orbit2/orbit2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/orbit2/orbit2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1029 | [p11-kit/p11-kit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/p11-kit/p11-kit.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1030 | [p7zip/p7zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/p7zip/p7zip.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1031 | [PackageKit-Qt/PackageKit-Qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/PackageKit-Qt/PackageKit-Qt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1032 | [paddle2onnx/paddle2onnx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/paddle2onnx/paddle2onnx.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1033 | [pam_wrapper/pam_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pam_wrapper/pam_wrapper.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1034 | [pango/pango.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pango/pango.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1035 | [pangomm/pangomm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pangomm/pangomm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1036 | [parallel/parallel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/parallel/parallel.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1037 | [parallel-hashmap/parallel-hashmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/parallel-hashmap/parallel-hashmap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1038 | [parted/parted.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/parted/parted.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1039 | [patch/patch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/patch/patch.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1040 | [patchelf/patchelf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/patchelf/patchelf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1041 | [pbzip2/pbzip2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pbzip2/pbzip2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1042 | [pcre2/pcre2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pcre2/pcre2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1043 | [perl/perl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl/perl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1044 | [perl-Template-Toolkit/perl-Template-Toolkit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Template-Toolkit/perl-Template-Toolkit.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1045 | [phonon/phonon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/phonon/phonon.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1046 | [php/php.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/php/php.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1047 | [picocom/picocom.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/picocom/picocom.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1048 | [pigz/pigz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pigz/pigz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1049 | [pinentry/pinentry.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinentry/pinentry.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1050 | [pixman/pixman.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pixman/pixman.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1051 | [pixz/pixz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pixz/pixz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1052 | [plasma-activities/plasma-activities.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/plasma-activities/plasma-activities.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1053 | [plasma-activities-stats/plasma-activities-stats.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/plasma-activities-stats/plasma-activities-stats.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1054 | [plasma-login-manager/plasma-login-manager.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/plasma-login-manager/plasma-login-manager.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1055 | [plasma-wayland-protocols/plasma-wayland-protocols.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/plasma-wayland-protocols/plasma-wayland-protocols.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1056 | [plasma5support/plasma5support.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/plasma5support/plasma5support.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1057 | [plog/plog.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/plog/plog.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1058 | [pmix/pmix.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pmix/pmix.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1059 | [polkit/polkit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/polkit/polkit.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1060 | [polkit-kde-agent-1/polkit-kde-agent-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/polkit-kde-agent-1/polkit-kde-agent-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1061 | [polkit-qt/polkit-qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/polkit-qt/polkit-qt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1062 | [poppler/poppler.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/poppler/poppler.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1063 | [poppler-data/poppler-data.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/poppler-data/poppler-data.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1064 | [popt/popt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/popt/popt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1065 | [portaudio/portaudio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/portaudio/portaudio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1066 | [powertop/powertop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/powertop/powertop.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1067 | [priv_wrapper/priv_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/priv_wrapper/priv_wrapper.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1068 | [procmail/procmail.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/procmail/procmail.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1069 | [procps/procps.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/procps/procps.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1070 | [proj/proj.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/proj/proj.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1071 | [protobuf/protobuf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/protobuf/protobuf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1072 | [protobuf-c/protobuf-c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/protobuf-c/protobuf-c.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1073 | [prrte/prrte.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/prrte/prrte.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1074 | [psimd/psimd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/psimd/psimd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1075 | [psmisc/psmisc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/psmisc/psmisc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1076 | [psutils/psutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/psutils/psutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1077 | [pthreadpool/pthreadpool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pthreadpool/pthreadpool.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1078 | [pulseaudio-qt/pulseaudio-qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pulseaudio-qt/pulseaudio-qt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1079 | [pv/pv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pv/pv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1080 | [pybind11/pybind11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pybind11/pybind11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1081 | [python-absl-py/python-absl-py.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-absl-py/python-absl-py.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1082 | [python-accelerate/python-accelerate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-accelerate/python-accelerate.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1083 | [python-acres/python-acres.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-acres/python-acres.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1084 | [python-aiobotocore/python-aiobotocore.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-aiobotocore/python-aiobotocore.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1085 | [python-aiofiles/python-aiofiles.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-aiofiles/python-aiofiles.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1086 | [python-aiohappyeyeballs/python-aiohappyeyeballs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-aiohappyeyeballs/python-aiohappyeyeballs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1087 | [python-aiohttp/python-aiohttp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-aiohttp/python-aiohttp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1088 | [python-aioitertools/python-aioitertools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-aioitertools/python-aioitertools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1089 | [python-aiolimiter/python-aiolimiter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-aiolimiter/python-aiolimiter.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1090 | [python-aioquic/python-aioquic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-aioquic/python-aioquic.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1091 | [python-aiosignal/python-aiosignal.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-aiosignal/python-aiosignal.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1092 | [python-aiosqlite/python-aiosqlite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-aiosqlite/python-aiosqlite.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1093 | [python-alabaster/python-alabaster.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-alabaster/python-alabaster.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1094 | [python-altair/python-altair.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-altair/python-altair.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1095 | [python-aniso8601/python-aniso8601.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-aniso8601/python-aniso8601.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1096 | [python-annotated-doc/python-annotated-doc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-annotated-doc/python-annotated-doc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1097 | [python-annotated-types/python-annotated-types.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-annotated-types/python-annotated-types.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1098 | [python-ansible-core/python-ansible-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ansible-core/python-ansible-core.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1099 | [python-anthropic/python-anthropic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-anthropic/python-anthropic.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1100 | [python-antlr4-python3-runtime/python-antlr4-python3-runtime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-antlr4-python3-runtime/python-antlr4-python3-runtime.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1101 | [python-anyio/python-anyio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-anyio/python-anyio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1102 | [python-appdirs/python-appdirs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-appdirs/python-appdirs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1103 | [python-apscheduler/python-apscheduler.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-apscheduler/python-apscheduler.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1104 | [python-apsw/python-apsw.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-apsw/python-apsw.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1105 | [python-archinfo/python-archinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-archinfo/python-archinfo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1106 | [python-argcomplete/python-argcomplete.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-argcomplete/python-argcomplete.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1107 | [python-argon2-cffi/python-argon2-cffi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-argon2-cffi/python-argon2-cffi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1108 | [python-argon2-cffi-bindings/python-argon2-cffi-bindings.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-argon2-cffi-bindings/python-argon2-cffi-bindings.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1109 | [python-argparse-manpage/python-argparse-manpage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-argparse-manpage/python-argparse-manpage.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1110 | [python-arpy/python-arpy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-arpy/python-arpy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1111 | [python-array-api-strict/python-array-api-strict.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-array-api-strict/python-array-api-strict.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1112 | [python-arrow/python-arrow.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-arrow/python-arrow.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1113 | [python-asgiref/python-asgiref.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-asgiref/python-asgiref.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1114 | [python-asn1crypto/python-asn1crypto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-asn1crypto/python-asn1crypto.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1115 | [python-astor/python-astor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-astor/python-astor.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1116 | [python-astropy/python-astropy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-astropy/python-astropy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1117 | [python-astropy-iers-data/python-astropy-iers-data.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-astropy-iers-data/python-astropy-iers-data.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1118 | [python-asttokens/python-asttokens.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-asttokens/python-asttokens.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1119 | [python-async-timeout/python-async-timeout.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-async-timeout/python-async-timeout.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1120 | [python-asyncmock/python-asyncmock.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-asyncmock/python-asyncmock.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1121 | [python-attrs/python-attrs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-attrs/python-attrs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1122 | [python-audioop-lts/python-audioop-lts.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-audioop-lts/python-audioop-lts.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1123 | [python-audioread/python-audioread.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-audioread/python-audioread.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1124 | [python-authlib/python-authlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-authlib/python-authlib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1125 | [python-av/python-av.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-av/python-av.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1126 | [python-aws-xray-sdk/python-aws-xray-sdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-aws-xray-sdk/python-aws-xray-sdk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1127 | [python-awscrt/python-awscrt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-awscrt/python-awscrt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1128 | [python-backoff/python-backoff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-backoff/python-backoff.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1129 | [python-backports-zstd/python-backports-zstd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-backports-zstd/python-backports-zstd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1130 | [python-bcrypt/python-bcrypt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-bcrypt/python-bcrypt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1131 | [python-beaker/python-beaker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-beaker/python-beaker.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1132 | [python-beniget/python-beniget.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-beniget/python-beniget.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1133 | [python-bibtexparser/python-bibtexparser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-bibtexparser/python-bibtexparser.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1134 | [python-binaryornot/python-binaryornot.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-binaryornot/python-binaryornot.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1135 | [python-bingimagecreator/python-bingimagecreator.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-bingimagecreator/python-bingimagecreator.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1136 | [python-bitarray/python-bitarray.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-bitarray/python-bitarray.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1137 | [python-bitstring/python-bitstring.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-bitstring/python-bitstring.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1138 | [python-bleach/python-bleach.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-bleach/python-bleach.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1139 | [python-blinker/python-blinker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-blinker/python-blinker.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1140 | [python-blis/python-blis.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-blis/python-blis.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1141 | [python-blobfile/python-blobfile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-blobfile/python-blobfile.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1142 | [python-bokeh/python-bokeh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-bokeh/python-bokeh.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1143 | [python-boolean-py/python-boolean-py.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-boolean-py/python-boolean-py.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1144 | [python-booleanoperations/python-booleanoperations.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-booleanoperations/python-booleanoperations.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1145 | [python-boto3/python-boto3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-boto3/python-boto3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1146 | [python-botocore/python-botocore.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-botocore/python-botocore.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1147 | [python-bottle/python-bottle.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-bottle/python-bottle.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1148 | [python-brotli/python-brotli.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-brotli/python-brotli.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1149 | [python-bson/python-bson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-bson/python-bson.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1150 | [python-cacheout/python-cacheout.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cacheout/python-cacheout.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1151 | [python-cachetools/python-cachetools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cachetools/python-cachetools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1152 | [python-cachey/python-cachey.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cachey/python-cachey.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1153 | [python-cart/python-cart.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cart/python-cart.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1154 | [python-catalogue/python-catalogue.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-catalogue/python-catalogue.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1155 | [python-cattrs/python-cattrs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cattrs/python-cattrs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1156 | [python-cbor/python-cbor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cbor/python-cbor.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1157 | [python-cbor2/python-cbor2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cbor2/python-cbor2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1158 | [python-cffsubr/python-cffsubr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cffsubr/python-cffsubr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1159 | [python-cfgrib/python-cfgrib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cfgrib/python-cfgrib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1160 | [python-cfgv/python-cfgv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cfgv/python-cfgv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1161 | [python-cftime/python-cftime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cftime/python-cftime.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1162 | [python-chameleon/python-chameleon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-chameleon/python-chameleon.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1163 | [python-chardet/python-chardet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-chardet/python-chardet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1164 | [python-charset-normalizer/python-charset-normalizer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-charset-normalizer/python-charset-normalizer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1165 | [python-cheroot/python-cheroot.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cheroot/python-cheroot.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1166 | [python-ci-info/python-ci-info.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ci-info/python-ci-info.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1167 | [python-claripy/python-claripy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-claripy/python-claripy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1168 | [python-click/python-click.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-click/python-click.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1169 | [python-cloudpathlib/python-cloudpathlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cloudpathlib/python-cloudpathlib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1170 | [python-cloudpickle/python-cloudpickle.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cloudpickle/python-cloudpickle.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1171 | [python-cmd2/python-cmd2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cmd2/python-cmd2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1172 | [python-codecarbon/python-codecarbon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-codecarbon/python-codecarbon.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1173 | [python-cohere/python-cohere.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cohere/python-cohere.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1174 | [python-coherent-licensed/python-coherent-licensed.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-coherent-licensed/python-coherent-licensed.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1175 | [python-colorlog/python-colorlog.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-colorlog/python-colorlog.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1176 | [python-comm/python-comm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-comm/python-comm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1177 | [python-compreffor/python-compreffor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-compreffor/python-compreffor.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1178 | [python-concurrent-log-handler/python-concurrent-log-handler.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-concurrent-log-handler/python-concurrent-log-handler.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1179 | [python-confection/python-confection.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-confection/python-confection.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1180 | [python-configobj/python-configobj.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-configobj/python-configobj.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1181 | [python-configparser/python-configparser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-configparser/python-configparser.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1182 | [python-construct/python-construct.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-construct/python-construct.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1183 | [python-cppy/python-cppy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cppy/python-cppy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1184 | [python-cram/python-cram.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cram/python-cram.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1185 | [python-cron-converter/python-cron-converter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cron-converter/python-cron-converter.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1186 | [python-csvw/python-csvw.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-csvw/python-csvw.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1187 | [python-cycler/python-cycler.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cycler/python-cycler.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1188 | [python-cymem/python-cymem.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cymem/python-cymem.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1189 | [python-cysqlite/python-cysqlite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cysqlite/python-cysqlite.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1190 | [python-dasbus/python-dasbus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-dasbus/python-dasbus.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1191 | [python-dashscope/python-dashscope.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-dashscope/python-dashscope.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1192 | [python-dask/python-dask.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-dask/python-dask.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1193 | [python-datasets/python-datasets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-datasets/python-datasets.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1194 | [python-dbus-python/python-dbus-python.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-dbus-python/python-dbus-python.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1195 | [python-debugpy/python-debugpy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-debugpy/python-debugpy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1196 | [python-decorator/python-decorator.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-decorator/python-decorator.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1197 | [python-deepdiff/python-deepdiff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-deepdiff/python-deepdiff.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1198 | [python-defusedxml/python-defusedxml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-defusedxml/python-defusedxml.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1199 | [python-deprecation/python-deprecation.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-deprecation/python-deprecation.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1200 | [python-diff-cover/python-diff-cover.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-diff-cover/python-diff-cover.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1201 | [python-diffusers/python-diffusers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-diffusers/python-diffusers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1202 | [python-dill/python-dill.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-dill/python-dill.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1203 | [python-discord/python-discord.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-discord/python-discord.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1204 | [python-distlib/python-distlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-distlib/python-distlib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1205 | [python-distributed/python-distributed.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-distributed/python-distributed.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1206 | [python-distro/python-distro.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-distro/python-distro.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1207 | [python-dlinfo/python-dlinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-dlinfo/python-dlinfo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1208 | [python-dnspython/python-dnspython.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-dnspython/python-dnspython.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1209 | [python-docopt/python-docopt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-docopt/python-docopt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1210 | [python-docopt-ng/python-docopt-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-docopt-ng/python-docopt-ng.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1211 | [python-docstring-parser/python-docstring-parser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-docstring-parser/python-docstring-parser.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1212 | [python-donfig/python-donfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-donfig/python-donfig.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1213 | [python-dunamai/python-dunamai.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-dunamai/python-dunamai.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1214 | [python-durationpy/python-durationpy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-durationpy/python-durationpy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1215 | [python-editables/python-editables.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-editables/python-editables.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1216 | [python-editdistance/python-editdistance.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-editdistance/python-editdistance.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1217 | [python-editorconfig/python-editorconfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-editorconfig/python-editorconfig.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1218 | [python-einops/python-einops.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-einops/python-einops.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1219 | [python-email-validator/python-email-validator.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-email-validator/python-email-validator.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1220 | [python-emoji/python-emoji.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-emoji/python-emoji.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1221 | [python-environs/python-environs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-environs/python-environs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1222 | [python-etelemetry/python-etelemetry.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-etelemetry/python-etelemetry.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1223 | [python-ethtool/python-ethtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ethtool/python-ethtool.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1224 | [python-eval-type-backport/python-eval-type-backport.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-eval-type-backport/python-eval-type-backport.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1225 | [python-exceptiongroup/python-exceptiongroup.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-exceptiongroup/python-exceptiongroup.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1226 | [python-executing/python-executing.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-executing/python-executing.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1227 | [python-expandvars/python-expandvars.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-expandvars/python-expandvars.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1228 | [python-expecttest/python-expecttest.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-expecttest/python-expecttest.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1229 | [python-extension-helpers/python-extension-helpers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-extension-helpers/python-extension-helpers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1230 | [python-faiss/python-faiss.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-faiss/python-faiss.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1231 | [python-fakeredis/python-fakeredis.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fakeredis/python-fakeredis.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1232 | [python-fastavro/python-fastavro.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fastavro/python-fastavro.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1233 | [python-fastjsonschema/python-fastjsonschema.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fastjsonschema/python-fastjsonschema.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1234 | [python-faust-cchardet/python-faust-cchardet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-faust-cchardet/python-faust-cchardet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1235 | [python-ffmpy/python-ffmpy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ffmpy/python-ffmpy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1236 | [python-fido2/python-fido2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fido2/python-fido2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1237 | [python-filelock/python-filelock.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-filelock/python-filelock.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1238 | [python-filetype/python-filetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-filetype/python-filetype.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1239 | [python-findlibs/python-findlibs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-findlibs/python-findlibs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1240 | [python-fitsio/python-fitsio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fitsio/python-fitsio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1241 | [python-flagembedding/python-flagembedding.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-flagembedding/python-flagembedding.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1242 | [python-flaky/python-flaky.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-flaky/python-flaky.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1243 | [python-flask/python-flask.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-flask/python-flask.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1244 | [python-flask-cors/python-flask-cors.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-flask-cors/python-flask-cors.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1245 | [python-flask-restful/python-flask-restful.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-flask-restful/python-flask-restful.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1246 | [python-flatten-dict/python-flatten-dict.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-flatten-dict/python-flatten-dict.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1247 | [python-flexcache/python-flexcache.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-flexcache/python-flexcache.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1248 | [python-flexparser/python-flexparser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-flexparser/python-flexparser.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1249 | [python-flit-scm/python-flit-scm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-flit-scm/python-flit-scm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1250 | [python-fmf/python-fmf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fmf/python-fmf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1251 | [python-fontmake/python-fontmake.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fontmake/python-fontmake.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1252 | [python-fontmath/python-fontmath.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fontmath/python-fontmath.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1253 | [python-fonttools/python-fonttools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fonttools/python-fonttools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1254 | [python-fqdn/python-fqdn.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fqdn/python-fqdn.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1255 | [python-freecell-solver/python-freecell-solver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-freecell-solver/python-freecell-solver.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1256 | [python-freezegun/python-freezegun.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-freezegun/python-freezegun.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1257 | [python-frozenlist/python-frozenlist.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-frozenlist/python-frozenlist.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1258 | [python-fsspec/python-fsspec.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fsspec/python-fsspec.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1259 | [python-ftfy/python-ftfy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ftfy/python-ftfy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1260 | [python-gast/python-gast.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gast/python-gast.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1261 | [python-gcloud-aio-auth/python-gcloud-aio-auth.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gcloud-aio-auth/python-gcloud-aio-auth.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1262 | [python-gcloud-aio-storage/python-gcloud-aio-storage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gcloud-aio-storage/python-gcloud-aio-storage.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1263 | [python-geventhttpclient/python-geventhttpclient.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-geventhttpclient/python-geventhttpclient.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1264 | [python-gguf/python-gguf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gguf/python-gguf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1265 | [python-gitdb/python-gitdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gitdb/python-gitdb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1266 | [python-gitpython/python-gitpython.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gitpython/python-gitpython.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1267 | [python-glad2/python-glad2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-glad2/python-glad2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1268 | [python-glyphslib/python-glyphslib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-glyphslib/python-glyphslib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1269 | [python-google-auth/python-google-auth.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-google-auth/python-google-auth.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1270 | [python-google-crc32c/python-google-crc32c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-google-crc32c/python-google-crc32c.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1271 | [python-googleapis-common-protos/python-googleapis-common-protos.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-googleapis-common-protos/python-googleapis-common-protos.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1272 | [python-gradio/python-gradio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gradio/python-gradio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1273 | [python-gradio-client/python-gradio-client.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gradio-client/python-gradio-client.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1274 | [python-graphene/python-graphene.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-graphene/python-graphene.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1275 | [python-graphql-core/python-graphql-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-graphql-core/python-graphql-core.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1276 | [python-graphql-relay/python-graphql-relay.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-graphql-relay/python-graphql-relay.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1277 | [python-greenlet/python-greenlet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-greenlet/python-greenlet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1278 | [python-griffecli/python-griffecli.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-griffecli/python-griffecli.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1279 | [python-griffelib/python-griffelib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-griffelib/python-griffelib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1280 | [python-groovy/python-groovy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-groovy/python-groovy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1281 | [python-grpcio-reflection/python-grpcio-reflection.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-grpcio-reflection/python-grpcio-reflection.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1282 | [python-grpcio-status/python-grpcio-status.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-grpcio-status/python-grpcio-status.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1283 | [python-grpcio-tools/python-grpcio-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-grpcio-tools/python-grpcio-tools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1284 | [python-gssapi/python-gssapi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gssapi/python-gssapi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1285 | [python-h11/python-h11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-h11/python-h11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1286 | [python-h2/python-h2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-h2/python-h2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1287 | [python-h5py/python-h5py.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-h5py/python-h5py.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1288 | [python-harvesttext/python-harvesttext.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-harvesttext/python-harvesttext.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1289 | [python-hatch-fancy-pypi-readme/python-hatch-fancy-pypi-readme.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-hatch-fancy-pypi-readme/python-hatch-fancy-pypi-readme.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1290 | [python-hatch-jupyter-builder/python-hatch-jupyter-builder.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-hatch-jupyter-builder/python-hatch-jupyter-builder.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1291 | [python-hatch-nodejs-version/python-hatch-nodejs-version.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-hatch-nodejs-version/python-hatch-nodejs-version.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1292 | [python-hatch-requirements-txt/python-hatch-requirements-txt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-hatch-requirements-txt/python-hatch-requirements-txt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1293 | [python-hatch-vcs/python-hatch-vcs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-hatch-vcs/python-hatch-vcs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1294 | [python-heapdict/python-heapdict.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-heapdict/python-heapdict.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1295 | [python-hf-gradio/python-hf-gradio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-hf-gradio/python-hf-gradio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1296 | [python-hf-xet/python-hf-xet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-hf-xet/python-hf-xet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1297 | [python-hiredis/python-hiredis.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-hiredis/python-hiredis.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1298 | [python-hpack/python-hpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-hpack/python-hpack.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1299 | [python-html5lib/python-html5lib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-html5lib/python-html5lib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1300 | [python-httpcore/python-httpcore.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-httpcore/python-httpcore.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1301 | [python-httplib2/python-httplib2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-httplib2/python-httplib2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1302 | [python-httptools/python-httptools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-httptools/python-httptools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1303 | [python-httpx/python-httpx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-httpx/python-httpx.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1304 | [python-httpx-sse/python-httpx-sse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-httpx-sse/python-httpx-sse.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1305 | [python-huggingface-hub/python-huggingface-hub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-huggingface-hub/python-huggingface-hub.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1306 | [python-hydra-core/python-hydra-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-hydra-core/python-hydra-core.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1307 | [python-hyperframe/python-hyperframe.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-hyperframe/python-hyperframe.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1308 | [python-hypothesis/python-hypothesis.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-hypothesis/python-hypothesis.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1309 | [python-icalendar/python-icalendar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-icalendar/python-icalendar.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1310 | [python-id/python-id.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-id/python-id.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1311 | [python-identify/python-identify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-identify/python-identify.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1312 | [python-idna/python-idna.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-idna/python-idna.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1313 | [python-ijson/python-ijson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ijson/python-ijson.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1314 | [python-imagecodecs/python-imagecodecs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-imagecodecs/python-imagecodecs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1315 | [python-imageio/python-imageio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-imageio/python-imageio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1316 | [python-imageio-ffmpeg/python-imageio-ffmpeg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-imageio-ffmpeg/python-imageio-ffmpeg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1317 | [python-imagesize/python-imagesize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-imagesize/python-imagesize.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1318 | [python-importlib-metadata/python-importlib-metadata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-importlib-metadata/python-importlib-metadata.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1319 | [python-importlib-resources/python-importlib-resources.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-importlib-resources/python-importlib-resources.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1320 | [python-iniconfig/python-iniconfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-iniconfig/python-iniconfig.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1321 | [python-iniparse/python-iniparse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-iniparse/python-iniparse.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1322 | [python-inscriptis/python-inscriptis.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-inscriptis/python-inscriptis.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1323 | [python-interegular/python-interegular.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-interegular/python-interegular.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1324 | [python-ipdb/python-ipdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ipdb/python-ipdb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1325 | [python-ipycytoscape/python-ipycytoscape.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ipycytoscape/python-ipycytoscape.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1326 | [python-ipykernel/python-ipykernel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ipykernel/python-ipykernel.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1327 | [python-ipyparallel/python-ipyparallel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ipyparallel/python-ipyparallel.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1328 | [python-ipython-pygments-lexers/python-ipython-pygments-lexers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ipython-pygments-lexers/python-ipython-pygments-lexers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1329 | [python-ipywidgets/python-ipywidgets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ipywidgets/python-ipywidgets.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1330 | [python-ir-datasets/python-ir-datasets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ir-datasets/python-ir-datasets.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1331 | [python-iso639/python-iso639.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-iso639/python-iso639.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1332 | [python-isodate/python-isodate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-isodate/python-isodate.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1333 | [python-isoduration/python-isoduration.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-isoduration/python-isoduration.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1334 | [python-itsdangerous/python-itsdangerous.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-itsdangerous/python-itsdangerous.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1335 | [python-jaraco-collections/python-jaraco-collections.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jaraco-collections/python-jaraco-collections.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1336 | [python-jaraco-context/python-jaraco-context.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jaraco-context/python-jaraco-context.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1337 | [python-jaraco-functools/python-jaraco-functools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jaraco-functools/python-jaraco-functools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1338 | [python-jaraco-text/python-jaraco-text.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jaraco-text/python-jaraco-text.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1339 | [python-jedi/python-jedi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jedi/python-jedi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1340 | [python-jieba/python-jieba.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jieba/python-jieba.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1341 | [python-jiter/python-jiter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jiter/python-jiter.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1342 | [python-jmespath/python-jmespath.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jmespath/python-jmespath.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1343 | [python-joblib/python-joblib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-joblib/python-joblib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1344 | [python-joserfc/python-joserfc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-joserfc/python-joserfc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1345 | [python-json5/python-json5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-json5/python-json5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1346 | [python-jsonlines/python-jsonlines.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jsonlines/python-jsonlines.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1347 | [python-jsonpatch/python-jsonpatch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jsonpatch/python-jsonpatch.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1348 | [python-jsonpath-ng/python-jsonpath-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jsonpath-ng/python-jsonpath-ng.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1349 | [python-jsonpath-python/python-jsonpath-python.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jsonpath-python/python-jsonpath-python.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1350 | [python-jsonpointer/python-jsonpointer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jsonpointer/python-jsonpointer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1351 | [python-jsonschema/python-jsonschema.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jsonschema/python-jsonschema.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1352 | [python-jsonschema-specifications/python-jsonschema-specifications.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jsonschema-specifications/python-jsonschema-specifications.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1353 | [python-jupyter-client/python-jupyter-client.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jupyter-client/python-jupyter-client.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1354 | [python-jupyter-core/python-jupyter-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jupyter-core/python-jupyter-core.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1355 | [python-jupyter-events/python-jupyter-events.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jupyter-events/python-jupyter-events.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1356 | [python-jupyter-packaging/python-jupyter-packaging.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jupyter-packaging/python-jupyter-packaging.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1357 | [python-jupyter-server/python-jupyter-server.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jupyter-server/python-jupyter-server.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1358 | [python-jupyter-server-terminals/python-jupyter-server-terminals.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jupyter-server-terminals/python-jupyter-server-terminals.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1359 | [python-jupyterlab-pygments/python-jupyterlab-pygments.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jupyterlab-pygments/python-jupyterlab-pygments.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1360 | [python-jupyterlab-widgets/python-jupyterlab-widgets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jupyterlab-widgets/python-jupyterlab-widgets.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1361 | [python-kenlm/python-kenlm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-kenlm/python-kenlm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1362 | [python-kerchunk/python-kerchunk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-kerchunk/python-kerchunk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1363 | [python-kernels-data/python-kernels-data.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-kernels-data/python-kernels-data.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1364 | [python-kiwisolver/python-kiwisolver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-kiwisolver/python-kiwisolver.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1365 | [python-kubernetes/python-kubernetes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-kubernetes/python-kubernetes.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1366 | [python-langchain/python-langchain.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-langchain/python-langchain.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1367 | [python-langchain-core/python-langchain-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-langchain-core/python-langchain-core.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1368 | [python-langchain-protocol/python-langchain-protocol.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-langchain-protocol/python-langchain-protocol.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1369 | [python-langcodes/python-langcodes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-langcodes/python-langcodes.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1370 | [python-langgraph/python-langgraph.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-langgraph/python-langgraph.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1371 | [python-langgraph-checkpoint/python-langgraph-checkpoint.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-langgraph-checkpoint/python-langgraph-checkpoint.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1372 | [python-langgraph-prebuilt/python-langgraph-prebuilt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-langgraph-prebuilt/python-langgraph-prebuilt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1373 | [python-langgraph-sdk/python-langgraph-sdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-langgraph-sdk/python-langgraph-sdk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1374 | [python-langsmith/python-langsmith.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-langsmith/python-langsmith.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1375 | [python-langtable/python-langtable.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-langtable/python-langtable.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1376 | [python-language-data/python-language-data.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-language-data/python-language-data.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1377 | [python-language-tags/python-language-tags.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-language-tags/python-language-tags.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1378 | [python-lark/python-lark.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-lark/python-lark.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1379 | [python-lazy-loader/python-lazy-loader.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-lazy-loader/python-lazy-loader.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1380 | [python-legacy-cgi/python-legacy-cgi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-legacy-cgi/python-legacy-cgi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1381 | [python-libcst/python-libcst.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-libcst/python-libcst.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1382 | [python-libevdev/python-libevdev.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-libevdev/python-libevdev.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1383 | [python-libnacl/python-libnacl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-libnacl/python-libnacl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1384 | [python-librt/python-librt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-librt/python-librt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1385 | [python-libvirt/python-libvirt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-libvirt/python-libvirt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1386 | [python-license-expression/python-license-expression.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-license-expression/python-license-expression.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1387 | [python-lightning-utilities/python-lightning-utilities.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-lightning-utilities/python-lightning-utilities.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1388 | [python-linkify-it-py/python-linkify-it-py.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-linkify-it-py/python-linkify-it-py.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1389 | [python-llguidance/python-llguidance.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-llguidance/python-llguidance.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1390 | [python-llvmlite/python-llvmlite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-llvmlite/python-llvmlite.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1391 | [python-lm-format-enforcer/python-lm-format-enforcer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-lm-format-enforcer/python-lm-format-enforcer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1392 | [python-lmdb/python-lmdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-lmdb/python-lmdb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1393 | [python-locket/python-locket.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-locket/python-locket.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1394 | [python-loguru/python-loguru.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-loguru/python-loguru.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1395 | [python-looseversion/python-looseversion.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-looseversion/python-looseversion.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1396 | [python-lupa/python-lupa.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-lupa/python-lupa.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1397 | [python-lxml/python-lxml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-lxml/python-lxml.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1398 | [python-lz4/python-lz4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-lz4/python-lz4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1399 | [python-marisa-trie/python-marisa-trie.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-marisa-trie/python-marisa-trie.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1400 | [python-markdown-it-py/python-markdown-it-py.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-markdown-it-py/python-markdown-it-py.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1401 | [python-marshmallow/python-marshmallow.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-marshmallow/python-marshmallow.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1402 | [python-matplotlib/python-matplotlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-matplotlib/python-matplotlib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1403 | [python-matplotlib-inline/python-matplotlib-inline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-matplotlib-inline/python-matplotlib-inline.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1404 | [python-maturin/python-maturin.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-maturin/python-maturin.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1405 | [python-mccabe/python-mccabe.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mccabe/python-mccabe.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1406 | [python-mcp/python-mcp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mcp/python-mcp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1407 | [python-mdit-py-plugins/python-mdit-py-plugins.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mdit-py-plugins/python-mdit-py-plugins.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1408 | [python-mdurl/python-mdurl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mdurl/python-mdurl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1409 | [python-memray/python-memray.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-memray/python-memray.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1410 | [python-mercantile/python-mercantile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mercantile/python-mercantile.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1411 | [python-milvus-model/python-milvus-model.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-milvus-model/python-milvus-model.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1412 | [python-minidump/python-minidump.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-minidump/python-minidump.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1413 | [python-mistralai/python-mistralai.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mistralai/python-mistralai.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1414 | [python-mistune/python-mistune.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mistune/python-mistune.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1415 | [python-mitogen/python-mitogen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mitogen/python-mitogen.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1416 | [python-ml-dtypes/python-ml-dtypes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ml-dtypes/python-ml-dtypes.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1417 | [python-mmh3/python-mmh3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mmh3/python-mmh3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1418 | [python-mock/python-mock.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mock/python-mock.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1419 | [python-model-hosting-container-standards/python-model-hosting-container-standards.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-model-hosting-container-standards/python-model-hosting-container-standards.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1420 | [python-more-itertools/python-more-itertools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-more-itertools/python-more-itertools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1421 | [python-moto/python-moto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-moto/python-moto.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1422 | [python-multidict/python-multidict.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-multidict/python-multidict.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1423 | [python-multipart/python-multipart.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-multipart/python-multipart.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1424 | [python-multiprocess/python-multiprocess.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-multiprocess/python-multiprocess.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1425 | [python-munkres/python-munkres.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-munkres/python-munkres.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1426 | [python-murmurhash/python-murmurhash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-murmurhash/python-murmurhash.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1427 | [python-mypy-extensions/python-mypy-extensions.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mypy-extensions/python-mypy-extensions.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1428 | [python-mysql-connector-python/python-mysql-connector-python.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mysql-connector-python/python-mysql-connector-python.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1429 | [python-narwhals/python-narwhals.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-narwhals/python-narwhals.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1430 | [python-natsort/python-natsort.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-natsort/python-natsort.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1431 | [python-nbclient/python-nbclient.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-nbclient/python-nbclient.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1432 | [python-nbconvert/python-nbconvert.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-nbconvert/python-nbconvert.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1433 | [python-nbformat/python-nbformat.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-nbformat/python-nbformat.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1434 | [python-nest-asyncio/python-nest-asyncio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-nest-asyncio/python-nest-asyncio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1435 | [python-netaddr/python-netaddr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-netaddr/python-netaddr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1436 | [python-networkx/python-networkx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-networkx/python-networkx.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1437 | [python-nibabel/python-nibabel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-nibabel/python-nibabel.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1438 | [python-nipype/python-nipype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-nipype/python-nipype.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1439 | [python-nodeenv/python-nodeenv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-nodeenv/python-nodeenv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1440 | [python-nomic/python-nomic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-nomic/python-nomic.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1441 | [python-ntplib/python-ntplib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ntplib/python-ntplib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1442 | [python-numba/python-numba.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-numba/python-numba.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1443 | [python-numcodecs/python-numcodecs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-numcodecs/python-numcodecs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1444 | [python-numpy/python-numpy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-numpy/python-numpy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1445 | [python-oauthlib/python-oauthlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-oauthlib/python-oauthlib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1446 | [python-omegaconf/python-omegaconf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-omegaconf/python-omegaconf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1447 | [python-openai/python-openai.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-openai/python-openai.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1448 | [python-openai-harmony/python-openai-harmony.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-openai-harmony/python-openai-harmony.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1449 | [python-opencc-python-reimplemented/python-opencc-python-reimplemented.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-opencc-python-reimplemented/python-opencc-python-reimplemented.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1450 | [python-openstep-plist/python-openstep-plist.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-openstep-plist/python-openstep-plist.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1451 | [python-opentelemetry-exporter-otlp/python-opentelemetry-exporter-otlp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-opentelemetry-exporter-otlp/python-opentelemetry-exporter-otlp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1452 | [python-opentelemetry-exporter-otlp-proto-common/python-opentelemetry-exporter-otlp-proto-common.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-opentelemetry-exporter-otlp-proto-common/python-opentelemetry-exporter-otlp-proto-common.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1453 | [python-opentelemetry-exporter-otlp-proto-grpc/python-opentelemetry-exporter-otlp-proto-grpc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-opentelemetry-exporter-otlp-proto-grpc/python-opentelemetry-exporter-otlp-proto-grpc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1454 | [python-opentelemetry-exporter-otlp-proto-http/python-opentelemetry-exporter-otlp-proto-http.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-opentelemetry-exporter-otlp-proto-http/python-opentelemetry-exporter-otlp-proto-http.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1455 | [python-opentelemetry-proto/python-opentelemetry-proto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-opentelemetry-proto/python-opentelemetry-proto.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1456 | [python-opentelemetry-sdk/python-opentelemetry-sdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-opentelemetry-sdk/python-opentelemetry-sdk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1457 | [python-opentelemetry-semantic-conventions-ai/python-opentelemetry-semantic-conventions-ai.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-opentelemetry-semantic-conventions-ai/python-opentelemetry-semantic-conventions-ai.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1458 | [python-opt-einsum/python-opt-einsum.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-opt-einsum/python-opt-einsum.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1459 | [python-optimum/python-optimum.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-optimum/python-optimum.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1460 | [python-optimum-benchmark/python-optimum-benchmark.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-optimum-benchmark/python-optimum-benchmark.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1461 | [python-optuna/python-optuna.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-optuna/python-optuna.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1462 | [python-ordered-set/python-ordered-set.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ordered-set/python-ordered-set.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1463 | [python-orderly-set/python-orderly-set.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-orderly-set/python-orderly-set.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1464 | [python-orjson/python-orjson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-orjson/python-orjson.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1465 | [python-ormsgpack/python-ormsgpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ormsgpack/python-ormsgpack.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1466 | [python-outcome/python-outcome.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-outcome/python-outcome.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1467 | [python-outlines-core/python-outlines-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-outlines-core/python-outlines-core.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1468 | [python-paddlepaddle/python-paddlepaddle.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-paddlepaddle/python-paddlepaddle.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1469 | [python-pandocfilters/python-pandocfilters.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pandocfilters/python-pandocfilters.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1470 | [python-parameterized/python-parameterized.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-parameterized/python-parameterized.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1471 | [python-paramiko/python-paramiko.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-paramiko/python-paramiko.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1472 | [python-parso/python-parso.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-parso/python-parso.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1473 | [python-partd/python-partd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-partd/python-partd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1474 | [python-partial-json-parser/python-partial-json-parser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-partial-json-parser/python-partial-json-parser.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1475 | [python-paste/python-paste.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-paste/python-paste.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1476 | [python-patch-ng/python-patch-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-patch-ng/python-patch-ng.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1477 | [python-pathspec/python-pathspec.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pathspec/python-pathspec.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1478 | [python-pecan/python-pecan.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pecan/python-pecan.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1479 | [python-peewee/python-peewee.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-peewee/python-peewee.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1480 | [python-pefile/python-pefile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pefile/python-pefile.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1481 | [python-peft/python-peft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-peft/python-peft.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1482 | [python-pg8000/python-pg8000.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pg8000/python-pg8000.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1483 | [python-phonemizer/python-phonemizer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-phonemizer/python-phonemizer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1484 | [python-phonenumbers/python-phonenumbers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-phonenumbers/python-phonenumbers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1485 | [python-pid/python-pid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pid/python-pid.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1486 | [python-pint/python-pint.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pint/python-pint.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1487 | [python-pipdeptree/python-pipdeptree.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pipdeptree/python-pipdeptree.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1488 | [python-pkgconfig/python-pkgconfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pkgconfig/python-pkgconfig.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1489 | [python-plac/python-plac.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-plac/python-plac.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1490 | [python-platformdirs/python-platformdirs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-platformdirs/python-platformdirs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1491 | [python-pluggy/python-pluggy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pluggy/python-pluggy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1492 | [python-ply/python-ply.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ply/python-ply.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1493 | [python-poetry-core/python-poetry-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-poetry-core/python-poetry-core.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1494 | [python-polib/python-polib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-polib/python-polib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1495 | [python-pooch/python-pooch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pooch/python-pooch.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1496 | [python-portalocker/python-portalocker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-portalocker/python-portalocker.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1497 | [python-portend/python-portend.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-portend/python-portend.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1498 | [python-preshed/python-preshed.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-preshed/python-preshed.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1499 | [python-prettytable/python-prettytable.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-prettytable/python-prettytable.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1500 | [python-process-tests/python-process-tests.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-process-tests/python-process-tests.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1501 | [python-productmd/python-productmd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-productmd/python-productmd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1502 | [python-progressbar2/python-progressbar2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-progressbar2/python-progressbar2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1503 | [python-prometheus-client/python-prometheus-client.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-prometheus-client/python-prometheus-client.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1504 | [python-prometheus-fastapi-instrumentator/python-prometheus-fastapi-instrumentator.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-prometheus-fastapi-instrumentator/python-prometheus-fastapi-instrumentator.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1505 | [python-prompt-toolkit/python-prompt-toolkit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-prompt-toolkit/python-prompt-toolkit.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1506 | [python-propcache/python-propcache.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-propcache/python-propcache.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1507 | [python-prov/python-prov.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-prov/python-prov.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1508 | [python-psutil/python-psutil.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-psutil/python-psutil.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1509 | [python-psycopg/python-psycopg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-psycopg/python-psycopg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1510 | [python-ptyprocess/python-ptyprocess.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ptyprocess/python-ptyprocess.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1511 | [python-puccinialin/python-puccinialin.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-puccinialin/python-puccinialin.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1512 | [python-pure-eval/python-pure-eval.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pure-eval/python-pure-eval.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1513 | [python-puremagic/python-puremagic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-puremagic/python-puremagic.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1514 | [python-py/python-py.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-py/python-py.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1515 | [python-py-cpuinfo/python-py-cpuinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-py-cpuinfo/python-py-cpuinfo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1516 | [python-py4j/python-py4j.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-py4j/python-py4j.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1517 | [python-pyarrow/python-pyarrow.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyarrow/python-pyarrow.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1518 | [python-pyasn1/python-pyasn1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyasn1/python-pyasn1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1519 | [python-pybase64/python-pybase64.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pybase64/python-pybase64.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1520 | [python-pybeam/python-pybeam.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pybeam/python-pybeam.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1521 | [python-pybind11-stubgen/python-pybind11-stubgen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pybind11-stubgen/python-pybind11-stubgen.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1522 | [python-pycairo/python-pycairo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pycairo/python-pycairo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1523 | [python-pycares/python-pycares.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pycares/python-pycares.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1524 | [python-pycdlib/python-pycdlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pycdlib/python-pycdlib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1525 | [python-pyclipper/python-pyclipper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyclipper/python-pyclipper.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1526 | [python-pycotap/python-pycotap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pycotap/python-pycotap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1527 | [python-pycountry/python-pycountry.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pycountry/python-pycountry.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1528 | [python-pycparser/python-pycparser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pycparser/python-pycparser.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1529 | [python-pycryptodome/python-pycryptodome.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pycryptodome/python-pycryptodome.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1530 | [python-pycryptodomex/python-pycryptodomex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pycryptodomex/python-pycryptodomex.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1531 | [python-pycups/python-pycups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pycups/python-pycups.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1532 | [python-pycurl/python-pycurl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pycurl/python-pycurl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1533 | [python-pydantic/python-pydantic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pydantic/python-pydantic.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1534 | [python-pydantic-core/python-pydantic-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pydantic-core/python-pydantic-core.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1535 | [python-pydantic-extra-types/python-pydantic-extra-types.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pydantic-extra-types/python-pydantic-extra-types.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1536 | [python-pydbus/python-pydbus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pydbus/python-pydbus.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1537 | [python-pydot/python-pydot.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pydot/python-pydot.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1538 | [python-pydub/python-pydub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pydub/python-pydub.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1539 | [python-pyelftools/python-pyelftools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyelftools/python-pyelftools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1540 | [python-pyerfa/python-pyerfa.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyerfa/python-pyerfa.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1541 | [python-pyfakefs/python-pyfakefs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyfakefs/python-pyfakefs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1542 | [python-pygit2/python-pygit2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pygit2/python-pygit2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1543 | [python-pygobject/python-pygobject.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pygobject/python-pygobject.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1544 | [python-pygtrie/python-pygtrie.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pygtrie/python-pygtrie.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1545 | [python-pyiceberg/python-pyiceberg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyiceberg/python-pyiceberg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1546 | [python-pyinotify/python-pyinotify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyinotify/python-pyinotify.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1547 | [python-pyjwt/python-pyjwt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyjwt/python-pyjwt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1548 | [python-pylsqpack/python-pylsqpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pylsqpack/python-pylsqpack.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1549 | [python-pymilvus/python-pymilvus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pymilvus/python-pymilvus.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1550 | [python-pymongo/python-pymongo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pymongo/python-pymongo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1551 | [python-pymupdf/python-pymupdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pymupdf/python-pymupdf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1552 | [python-pymysql/python-pymysql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pymysql/python-pymysql.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1553 | [python-pynacl/python-pynacl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pynacl/python-pynacl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1554 | [python-pynamodb/python-pynamodb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pynamodb/python-pynamodb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1555 | [python-pyopenssl/python-pyopenssl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyopenssl/python-pyopenssl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1556 | [python-pyparsing/python-pyparsing.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyparsing/python-pyparsing.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1557 | [python-pyparted/python-pyparted.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyparted/python-pyparted.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1558 | [python-pyperclip/python-pyperclip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyperclip/python-pyperclip.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1559 | [python-pypinyin/python-pypinyin.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pypinyin/python-pypinyin.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1560 | [python-pyproject-hooks/python-pyproject-hooks.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyproject-hooks/python-pyproject-hooks.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1561 | [python-pyproject-metadata/python-pyproject-metadata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyproject-metadata/python-pyproject-metadata.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1562 | [python-pyroaring/python-pyroaring.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyroaring/python-pyroaring.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1563 | [python-pyroute2/python-pyroute2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyroute2/python-pyroute2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1564 | [python-pyrsistent/python-pyrsistent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyrsistent/python-pyrsistent.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1565 | [python-pyscard/python-pyscard.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyscard/python-pyscard.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1566 | [python-pyside6/python-pyside6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyside6/python-pyside6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1567 | [python-pysocks/python-pysocks.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pysocks/python-pysocks.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1568 | [python-pysol-cards/python-pysol-cards.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pysol-cards/python-pysol-cards.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1569 | [python-pyspark/python-pyspark.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyspark/python-pyspark.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1570 | [python-pysqlcipher3/python-pysqlcipher3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pysqlcipher3/python-pysqlcipher3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1571 | [python-pytest/python-pytest.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest/python-pytest.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1572 | [python-pytest-asyncio/python-pytest-asyncio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-asyncio/python-pytest-asyncio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1573 | [python-pytest-cov/python-pytest-cov.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-cov/python-pytest-cov.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1574 | [python-pytest-dependency/python-pytest-dependency.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-dependency/python-pytest-dependency.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1575 | [python-pytest-dotenv/python-pytest-dotenv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-dotenv/python-pytest-dotenv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1576 | [python-pytest-env/python-pytest-env.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-env/python-pytest-env.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1577 | [python-pytest-forked/python-pytest-forked.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-forked/python-pytest-forked.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1578 | [python-pytest-freezer/python-pytest-freezer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-freezer/python-pytest-freezer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1579 | [python-pytest-mock/python-pytest-mock.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-mock/python-pytest-mock.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1580 | [python-pytest-order/python-pytest-order.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-order/python-pytest-order.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1581 | [python-pytest-random-order/python-pytest-random-order.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-random-order/python-pytest-random-order.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1582 | [python-pytest-randomly/python-pytest-randomly.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-randomly/python-pytest-randomly.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1583 | [python-pytest-relaxed/python-pytest-relaxed.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-relaxed/python-pytest-relaxed.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1584 | [python-pytest-remotedata/python-pytest-remotedata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-remotedata/python-pytest-remotedata.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1585 | [python-pytest-rerunfailures/python-pytest-rerunfailures.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-rerunfailures/python-pytest-rerunfailures.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1586 | [python-pytest-rich/python-pytest-rich.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-rich/python-pytest-rich.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1587 | [python-pytest-runner/python-pytest-runner.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-runner/python-pytest-runner.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1588 | [python-pytest-timeout/python-pytest-timeout.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-timeout/python-pytest-timeout.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1589 | [python-python-debian/python-python-debian.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-debian/python-python-debian.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1590 | [python-python-json-logger/python-python-json-logger.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-json-logger/python-python-json-logger.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1591 | [python-python-louvain/python-python-louvain.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-louvain/python-python-louvain.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1592 | [python-python-magic/python-python-magic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-magic/python-python-magic.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1593 | [python-python-multipart/python-python-multipart.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-multipart/python-python-multipart.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1594 | [python-python-pam/python-python-pam.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-pam/python-python-pam.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1595 | [python-python-rapidjson/python-python-rapidjson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-rapidjson/python-python-rapidjson.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1596 | [python-python-slugify/python-python-slugify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-slugify/python-python-slugify.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1597 | [python-python-socks/python-python-socks.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-socks/python-python-socks.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1598 | [python-python-utils/python-python-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-utils/python-python-utils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1599 | [python-pythran/python-pythran.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pythran/python-pythran.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1600 | [python-pytokens/python-pytokens.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytokens/python-pytokens.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1601 | [python-pytorch-lightning/python-pytorch-lightning.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytorch-lightning/python-pytorch-lightning.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1602 | [python-pyvex/python-pyvex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyvex/python-pyvex.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1603 | [python-pyxbe/python-pyxbe.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyxbe/python-pyxbe.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1604 | [python-pyxnat/python-pyxnat.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyxnat/python-pyxnat.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1605 | [python-pyyaml/python-pyyaml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyyaml/python-pyyaml.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1606 | [python-pyyaml-ft/python-pyyaml-ft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyyaml-ft/python-pyyaml-ft.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1607 | [python-pyzstd/python-pyzstd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyzstd/python-pyzstd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1608 | [python-questionary/python-questionary.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-questionary/python-questionary.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1609 | [python-rapidfuzz/python-rapidfuzz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rapidfuzz/python-rapidfuzz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1610 | [python-rawpy/python-rawpy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rawpy/python-rawpy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1611 | [python-rdflib/python-rdflib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rdflib/python-rdflib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1612 | [python-redis/python-redis.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-redis/python-redis.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1613 | [python-referencing/python-referencing.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-referencing/python-referencing.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1614 | [python-regex/python-regex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-regex/python-regex.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1615 | [python-repoze-lru/python-repoze-lru.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-repoze-lru/python-repoze-lru.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1616 | [python-requests-file/python-requests-file.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-requests-file/python-requests-file.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1617 | [python-requests-ftp/python-requests-ftp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-requests-ftp/python-requests-ftp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1618 | [python-requests-mock/python-requests-mock.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-requests-mock/python-requests-mock.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1619 | [python-requests-oauthlib/python-requests-oauthlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-requests-oauthlib/python-requests-oauthlib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1620 | [python-resolvelib/python-resolvelib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-resolvelib/python-resolvelib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1621 | [python-responses/python-responses.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-responses/python-responses.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1622 | [python-reuse/python-reuse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-reuse/python-reuse.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1623 | [python-rfc3161-client/python-rfc3161-client.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rfc3161-client/python-rfc3161-client.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1624 | [python-rfc3339-validator/python-rfc3339-validator.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rfc3339-validator/python-rfc3339-validator.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1625 | [python-rfc3986/python-rfc3986.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rfc3986/python-rfc3986.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1626 | [python-rfc3986-validator/python-rfc3986-validator.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rfc3986-validator/python-rfc3986-validator.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1627 | [python-rfc3987/python-rfc3987.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rfc3987/python-rfc3987.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1628 | [python-rfc3987-syntax/python-rfc3987-syntax.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rfc3987-syntax/python-rfc3987-syntax.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1629 | [python-rfc8785/python-rfc8785.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rfc8785/python-rfc8785.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1630 | [python-rhoknp/python-rhoknp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rhoknp/python-rhoknp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1631 | [python-rich/python-rich.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rich/python-rich.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1632 | [python-rjieba/python-rjieba.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rjieba/python-rjieba.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1633 | [python-roman-numerals/python-roman-numerals.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-roman-numerals/python-roman-numerals.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1634 | [python-rouge-score/python-rouge-score.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rouge-score/python-rouge-score.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1635 | [python-routes/python-routes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-routes/python-routes.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1636 | [python-rpds-py/python-rpds-py.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rpds-py/python-rpds-py.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1637 | [python-rpmautospec-core/python-rpmautospec-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rpmautospec-core/python-rpmautospec-core.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1638 | [python-rsa/python-rsa.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rsa/python-rsa.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1639 | [python-rtslib-fb/python-rtslib-fb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rtslib-fb/python-rtslib-fb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1640 | [python-s3fs/python-s3fs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-s3fs/python-s3fs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1641 | [python-s3transfer/python-s3transfer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-s3transfer/python-s3transfer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1642 | [python-sacrebleu/python-sacrebleu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sacrebleu/python-sacrebleu.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1643 | [python-sacremoses/python-sacremoses.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sacremoses/python-sacremoses.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1644 | [python-safehttpx/python-safehttpx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-safehttpx/python-safehttpx.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1645 | [python-safetensors/python-safetensors.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-safetensors/python-safetensors.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1646 | [python-sagemaker/python-sagemaker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sagemaker/python-sagemaker.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1647 | [python-sagemaker-core/python-sagemaker-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sagemaker-core/python-sagemaker-core.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1648 | [python-sagemaker-mlops/python-sagemaker-mlops.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sagemaker-mlops/python-sagemaker-mlops.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1649 | [python-sagemaker-serve/python-sagemaker-serve.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sagemaker-serve/python-sagemaker-serve.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1650 | [python-sagemaker-train/python-sagemaker-train.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sagemaker-train/python-sagemaker-train.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1651 | [python-schedulefree/python-schedulefree.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-schedulefree/python-schedulefree.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1652 | [python-schedutils/python-schedutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-schedutils/python-schedutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1653 | [python-schema/python-schema.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-schema/python-schema.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1654 | [python-scikit-build/python-scikit-build.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-scikit-build/python-scikit-build.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1655 | [python-scikit-build-core/python-scikit-build-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-scikit-build-core/python-scikit-build-core.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1656 | [python-scikit-image/python-scikit-image.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-scikit-image/python-scikit-image.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1657 | [python-scramp/python-scramp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-scramp/python-scramp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1658 | [python-securesystemslib/python-securesystemslib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-securesystemslib/python-securesystemslib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1659 | [python-segments/python-segments.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-segments/python-segments.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1660 | [python-semantic-version/python-semantic-version.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-semantic-version/python-semantic-version.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1661 | [python-semver/python-semver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-semver/python-semver.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1662 | [python-send2trash/python-send2trash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-send2trash/python-send2trash.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1663 | [python-sentencepiece/python-sentencepiece.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sentencepiece/python-sentencepiece.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1664 | [python-service-identity/python-service-identity.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-service-identity/python-service-identity.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1665 | [python-setuptools-gettext/python-setuptools-gettext.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-setuptools-gettext/python-setuptools-gettext.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1666 | [python-setuptools-git-ls-files/python-setuptools-git-ls-files.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-setuptools-git-ls-files/python-setuptools-git-ls-files.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1667 | [python-setuptools-git-versioning/python-setuptools-git-versioning.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-setuptools-git-versioning/python-setuptools-git-versioning.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1668 | [python-setuptools-rust/python-setuptools-rust.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-setuptools-rust/python-setuptools-rust.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1669 | [python-setuptools-scm/python-setuptools-scm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-setuptools-scm/python-setuptools-scm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1670 | [python-shellingham/python-shellingham.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-shellingham/python-shellingham.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1671 | [python-sigstore/python-sigstore.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sigstore/python-sigstore.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1672 | [python-sigstore-models/python-sigstore-models.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sigstore-models/python-sigstore-models.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1673 | [python-sigstore-rekor-types/python-sigstore-rekor-types.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sigstore-rekor-types/python-sigstore-rekor-types.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1674 | [python-sip/python-sip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sip/python-sip.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1675 | [python-six/python-six.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-six/python-six.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1676 | [python-smart-open/python-smart-open.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-smart-open/python-smart-open.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1677 | [python-smartypants/python-smartypants.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-smartypants/python-smartypants.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1678 | [python-smdebug-rulesconfig/python-smdebug-rulesconfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-smdebug-rulesconfig/python-smdebug-rulesconfig.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1679 | [python-smmap/python-smmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-smmap/python-smmap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1680 | [python-sniffio/python-sniffio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sniffio/python-sniffio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1681 | [python-snowballstemmer/python-snowballstemmer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-snowballstemmer/python-snowballstemmer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1682 | [python-socksio/python-socksio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-socksio/python-socksio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1683 | [python-sortedcontainers/python-sortedcontainers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sortedcontainers/python-sortedcontainers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1684 | [python-soupsieve/python-soupsieve.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-soupsieve/python-soupsieve.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1685 | [python-soxr/python-soxr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-soxr/python-soxr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1686 | [python-spacy/python-spacy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-spacy/python-spacy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1687 | [python-spacy-legacy/python-spacy-legacy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-spacy-legacy/python-spacy-legacy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1688 | [python-spacy-loggers/python-spacy-loggers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-spacy-loggers/python-spacy-loggers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1689 | [python-sparse/python-sparse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sparse/python-sparse.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1690 | [python-spectate/python-spectate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-spectate/python-spectate.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1691 | [python-sphinx/python-sphinx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sphinx/python-sphinx.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1692 | [python-sphinxcontrib-applehelp/python-sphinxcontrib-applehelp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sphinxcontrib-applehelp/python-sphinxcontrib-applehelp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1693 | [python-sphinxcontrib-devhelp/python-sphinxcontrib-devhelp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sphinxcontrib-devhelp/python-sphinxcontrib-devhelp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1694 | [python-sphinxcontrib-htmlhelp/python-sphinxcontrib-htmlhelp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sphinxcontrib-htmlhelp/python-sphinxcontrib-htmlhelp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1695 | [python-sphinxcontrib-jsmath/python-sphinxcontrib-jsmath.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sphinxcontrib-jsmath/python-sphinxcontrib-jsmath.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1696 | [python-sphinxcontrib-qthelp/python-sphinxcontrib-qthelp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sphinxcontrib-qthelp/python-sphinxcontrib-qthelp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1697 | [python-sphinxcontrib-serializinghtml/python-sphinxcontrib-serializinghtml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sphinxcontrib-serializinghtml/python-sphinxcontrib-serializinghtml.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1698 | [python-sqlparse/python-sqlparse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sqlparse/python-sqlparse.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1699 | [python-srsly/python-srsly.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-srsly/python-srsly.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1700 | [python-sse-starlette/python-sse-starlette.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sse-starlette/python-sse-starlette.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1701 | [python-stack-data/python-stack-data.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-stack-data/python-stack-data.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1702 | [python-standard-aifc/python-standard-aifc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-standard-aifc/python-standard-aifc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1703 | [python-standard-chunk/python-standard-chunk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-standard-chunk/python-standard-chunk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1704 | [python-standard-sunau/python-standard-sunau.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-standard-sunau/python-standard-sunau.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1705 | [python-sudachidict-core/python-sudachidict-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sudachidict-core/python-sudachidict-core.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1706 | [python-sudachipy/python-sudachipy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sudachipy/python-sudachipy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1707 | [python-supervisor/python-supervisor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-supervisor/python-supervisor.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1708 | [python-systemd/python-systemd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-systemd/python-systemd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1709 | [python-tabulate/python-tabulate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tabulate/python-tabulate.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1710 | [python-tblib/python-tblib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tblib/python-tblib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1711 | [python-tempita/python-tempita.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tempita/python-tempita.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1712 | [python-tempora/python-tempora.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tempora/python-tempora.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1713 | [python-tenacity/python-tenacity.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tenacity/python-tenacity.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1714 | [python-tensorizer/python-tensorizer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tensorizer/python-tensorizer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1715 | [python-termcolor/python-termcolor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-termcolor/python-termcolor.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1716 | [python-terminado/python-terminado.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-terminado/python-terminado.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1717 | [python-testcloud/python-testcloud.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-testcloud/python-testcloud.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1718 | [python-text-unidecode/python-text-unidecode.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-text-unidecode/python-text-unidecode.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1719 | [python-textual/python-textual.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-textual/python-textual.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1720 | [python-thinc/python-thinc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-thinc/python-thinc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1721 | [python-threadpoolctl/python-threadpoolctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-threadpoolctl/python-threadpoolctl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1722 | [python-tifffile/python-tifffile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tifffile/python-tifffile.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1723 | [python-time-machine/python-time-machine.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-time-machine/python-time-machine.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1724 | [python-timeout-decorator/python-timeout-decorator.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-timeout-decorator/python-timeout-decorator.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1725 | [python-timm/python-timm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-timm/python-timm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1726 | [python-tinycss2/python-tinycss2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tinycss2/python-tinycss2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1727 | [python-tokenize-rt/python-tokenize-rt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tokenize-rt/python-tokenize-rt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1728 | [python-tokenizers/python-tokenizers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tokenizers/python-tokenizers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1729 | [python-toml/python-toml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-toml/python-toml.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1730 | [python-tomli-w/python-tomli-w.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tomli-w/python-tomli-w.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1731 | [python-tomlkit/python-tomlkit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tomlkit/python-tomlkit.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1732 | [python-toolz/python-toolz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-toolz/python-toolz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1733 | [python-torchaudio/python-torchaudio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-torchaudio/python-torchaudio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1734 | [python-torchmetrics/python-torchmetrics.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-torchmetrics/python-torchmetrics.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1735 | [python-tornado/python-tornado.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tornado/python-tornado.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1736 | [python-tox/python-tox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tox/python-tox.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1737 | [python-tox-current-env/python-tox-current-env.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tox-current-env/python-tox-current-env.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1738 | [python-tqdm/python-tqdm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tqdm/python-tqdm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1739 | [python-traitlets/python-traitlets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-traitlets/python-traitlets.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1740 | [python-traits/python-traits.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-traits/python-traits.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1741 | [python-transformers/python-transformers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-transformers/python-transformers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1742 | [python-trec-car-tools/python-trec-car-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-trec-car-tools/python-trec-car-tools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1743 | [python-trio/python-trio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-trio/python-trio.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1744 | [python-triton/python-triton.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-triton/python-triton.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1745 | [python-tritonclient/python-tritonclient.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tritonclient/python-tritonclient.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1746 | [python-trove-classifiers/python-trove-classifiers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-trove-classifiers/python-trove-classifiers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1747 | [python-twython/python-twython.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-twython/python-twython.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1748 | [python-typer/python-typer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-typer/python-typer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1749 | [python-types-dataclasses/python-types-dataclasses.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-types-dataclasses/python-types-dataclasses.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1750 | [python-types-psutil/python-types-psutil.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-types-psutil/python-types-psutil.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1751 | [python-types-pyyaml/python-types-pyyaml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-types-pyyaml/python-types-pyyaml.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1752 | [python-types-requests/python-types-requests.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-types-requests/python-types-requests.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1753 | [python-types-setuptools/python-types-setuptools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-types-setuptools/python-types-setuptools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1754 | [python-typing-extensions/python-typing-extensions.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-typing-extensions/python-typing-extensions.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1755 | [python-typing-inspection/python-typing-inspection.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-typing-inspection/python-typing-inspection.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1756 | [python-typogrify/python-typogrify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-typogrify/python-typogrify.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1757 | [python-tzdata/python-tzdata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tzdata/python-tzdata.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1758 | [python-tzlocal/python-tzlocal.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tzlocal/python-tzlocal.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1759 | [python-uc-micro-py/python-uc-micro-py.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-uc-micro-py/python-uc-micro-py.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1760 | [python-ufo2ft/python-ufo2ft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ufo2ft/python-ufo2ft.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1761 | [python-ufolib2/python-ufolib2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ufolib2/python-ufolib2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1762 | [python-ujson/python-ujson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ujson/python-ujson.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1763 | [python-unicodedata2/python-unicodedata2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-unicodedata2/python-unicodedata2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1764 | [python-unidic/python-unidic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-unidic/python-unidic.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1765 | [python-unidic-lite/python-unidic-lite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-unidic-lite/python-unidic-lite.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1766 | [python-unlzw3/python-unlzw3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-unlzw3/python-unlzw3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1767 | [python-uri-template/python-uri-template.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-uri-template/python-uri-template.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1768 | [python-uritemplate/python-uritemplate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-uritemplate/python-uritemplate.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1769 | [python-urlgrabber/python-urlgrabber.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-urlgrabber/python-urlgrabber.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1770 | [python-uuid-utils/python-uuid-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-uuid-utils/python-uuid-utils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1771 | [python-uv-dynamic-versioning/python-uv-dynamic-versioning.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-uv-dynamic-versioning/python-uv-dynamic-versioning.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1772 | [python-uvloop/python-uvloop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-uvloop/python-uvloop.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1773 | [python-vcs-versioning/python-vcs-versioning.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-vcs-versioning/python-vcs-versioning.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1774 | [python-versioneer/python-versioneer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-versioneer/python-versioneer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1775 | [python-versioningit/python-versioningit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-versioningit/python-versioningit.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1776 | [python-w3lib/python-w3lib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-w3lib/python-w3lib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1777 | [python-warc3-wet/python-warc3-wet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-warc3-wet/python-warc3-wet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1778 | [python-warc3-wet-clueweb09/python-warc3-wet-clueweb09.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-warc3-wet-clueweb09/python-warc3-wet-clueweb09.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1779 | [python-wasabi/python-wasabi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-wasabi/python-wasabi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1780 | [python-watchfiles/python-watchfiles.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-watchfiles/python-watchfiles.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1781 | [python-wcwidth/python-wcwidth.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-wcwidth/python-wcwidth.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1782 | [python-weasel/python-weasel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-weasel/python-weasel.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1783 | [python-webcolors/python-webcolors.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-webcolors/python-webcolors.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1784 | [python-webencodings/python-webencodings.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-webencodings/python-webencodings.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1785 | [python-webob/python-webob.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-webob/python-webob.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1786 | [python-websocket-client/python-websocket-client.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-websocket-client/python-websocket-client.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1787 | [python-websockets/python-websockets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-websockets/python-websockets.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1788 | [python-werkzeug/python-werkzeug.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-werkzeug/python-werkzeug.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1789 | [python-wheel/python-wheel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-wheel/python-wheel.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1790 | [python-Whoosh/python-Whoosh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-Whoosh/python-Whoosh.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1791 | [python-widgetsnbextension/python-widgetsnbextension.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-widgetsnbextension/python-widgetsnbextension.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1792 | [python-wrapt/python-wrapt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-wrapt/python-wrapt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1793 | [python-xarray/python-xarray.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-xarray/python-xarray.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1794 | [python-xgrammar/python-xgrammar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-xgrammar/python-xgrammar.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1795 | [python-xmltodict/python-xmltodict.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-xmltodict/python-xmltodict.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1796 | [python-xxhash/python-xxhash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-xxhash/python-xxhash.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1797 | [python-xyzservices/python-xyzservices.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-xyzservices/python-xyzservices.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1798 | [python-yarl/python-yarl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-yarl/python-yarl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1799 | [python-zarr/python-zarr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-zarr/python-zarr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1800 | [python-zc-lockfile/python-zc-lockfile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-zc-lockfile/python-zc-lockfile.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1801 | [python-zfpy/python-zfpy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-zfpy/python-zfpy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1802 | [python-zhconv/python-zhconv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-zhconv/python-zhconv.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1803 | [python-zict/python-zict.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-zict/python-zict.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1804 | [python-zipp/python-zipp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-zipp/python-zipp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1805 | [python-zlib-state/python-zlib-state.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-zlib-state/python-zlib-state.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1806 | [python-zmq/python-zmq.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-zmq/python-zmq.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1807 | [python-zope-event/python-zope-event.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-zope-event/python-zope-event.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1808 | [python-zope-interface/python-zope-interface.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-zope-interface/python-zope-interface.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1809 | [python-zstandard/python-zstandard.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-zstandard/python-zstandard.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1810 | [pyxdg/pyxdg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pyxdg/pyxdg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1811 | [qalculate-qt/qalculate-qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qalculate-qt/qalculate-qt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1812 | [qca/qca.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qca/qca.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1813 | [qcoro/qcoro.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qcoro/qcoro.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1814 | [qhull/qhull.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qhull/qhull.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1815 | [qmpbackup/qmpbackup.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qmpbackup/qmpbackup.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1816 | [qrencode/qrencode.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qrencode/qrencode.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1817 | [qt6-qt3d/qt6-qt3d.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qt3d/qt6-qt3d.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1818 | [qt6-qt5compat/qt6-qt5compat.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qt5compat/qt6-qt5compat.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1819 | [qt6-qtbase/qt6-qtbase.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtbase/qt6-qtbase.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1820 | [qt6-qtcharts/qt6-qtcharts.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtcharts/qt6-qtcharts.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1821 | [qt6-qtcoap/qt6-qtcoap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtcoap/qt6-qtcoap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1822 | [qt6-qtconnectivity/qt6-qtconnectivity.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtconnectivity/qt6-qtconnectivity.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1823 | [qt6-qtdatavis3d/qt6-qtdatavis3d.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtdatavis3d/qt6-qtdatavis3d.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1824 | [qt6-qtdeclarative/qt6-qtdeclarative.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtdeclarative/qt6-qtdeclarative.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1825 | [qt6-qtgraphs/qt6-qtgraphs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtgraphs/qt6-qtgraphs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1826 | [qt6-qtgrpc/qt6-qtgrpc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtgrpc/qt6-qtgrpc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1827 | [qt6-qthttpserver/qt6-qthttpserver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qthttpserver/qt6-qthttpserver.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1828 | [qt6-qtimageformats/qt6-qtimageformats.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtimageformats/qt6-qtimageformats.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1829 | [qt6-qtlanguageserver/qt6-qtlanguageserver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtlanguageserver/qt6-qtlanguageserver.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1830 | [qt6-qtlocation/qt6-qtlocation.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtlocation/qt6-qtlocation.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1831 | [qt6-qtlottie/qt6-qtlottie.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtlottie/qt6-qtlottie.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1832 | [qt6-qtmqtt/qt6-qtmqtt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtmqtt/qt6-qtmqtt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1833 | [qt6-qtmultimedia/qt6-qtmultimedia.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtmultimedia/qt6-qtmultimedia.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1834 | [qt6-qtnetworkauth/qt6-qtnetworkauth.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtnetworkauth/qt6-qtnetworkauth.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1835 | [qt6-qtopcua/qt6-qtopcua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtopcua/qt6-qtopcua.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1836 | [qt6-qtpositioning/qt6-qtpositioning.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtpositioning/qt6-qtpositioning.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1837 | [qt6-qtquick3d/qt6-qtquick3d.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtquick3d/qt6-qtquick3d.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1838 | [qt6-qtquick3dphysics/qt6-qtquick3dphysics.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtquick3dphysics/qt6-qtquick3dphysics.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1839 | [qt6-qtquickeffectmaker/qt6-qtquickeffectmaker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtquickeffectmaker/qt6-qtquickeffectmaker.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1840 | [qt6-qtquicktimeline/qt6-qtquicktimeline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtquicktimeline/qt6-qtquicktimeline.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1841 | [qt6-qtremoteobjects/qt6-qtremoteobjects.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtremoteobjects/qt6-qtremoteobjects.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1842 | [qt6-qtscxml/qt6-qtscxml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtscxml/qt6-qtscxml.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1843 | [qt6-qtsensors/qt6-qtsensors.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtsensors/qt6-qtsensors.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1844 | [qt6-qtserialbus/qt6-qtserialbus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtserialbus/qt6-qtserialbus.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1845 | [qt6-qtserialport/qt6-qtserialport.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtserialport/qt6-qtserialport.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1846 | [qt6-qtshadertools/qt6-qtshadertools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtshadertools/qt6-qtshadertools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1847 | [qt6-qtspeech/qt6-qtspeech.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtspeech/qt6-qtspeech.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1848 | [qt6-qtsvg/qt6-qtsvg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtsvg/qt6-qtsvg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1849 | [qt6-qttranslations/qt6-qttranslations.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qttranslations/qt6-qttranslations.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1850 | [qt6-qtvirtualkeyboard/qt6-qtvirtualkeyboard.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtvirtualkeyboard/qt6-qtvirtualkeyboard.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1851 | [qt6-qtwayland/qt6-qtwayland.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtwayland/qt6-qtwayland.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1852 | [qt6-qtwebchannel/qt6-qtwebchannel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtwebchannel/qt6-qtwebchannel.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1853 | [qt6-qtwebengine/qt6-qtwebengine.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtwebengine/qt6-qtwebengine.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1854 | [qt6-qtwebsockets/qt6-qtwebsockets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtwebsockets/qt6-qtwebsockets.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1855 | [qt6-qtwebview/qt6-qtwebview.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtwebview/qt6-qtwebview.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1856 | [qtkeychain/qtkeychain.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qtkeychain/qtkeychain.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1857 | [ragel/ragel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ragel/ragel.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1858 | [range-v3/range-v3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/range-v3/range-v3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1859 | [rapidjson/rapidjson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rapidjson/rapidjson.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1860 | [rdfind/rdfind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rdfind/rdfind.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1861 | [re2/re2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/re2/re2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1862 | [re2c/re2c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/re2c/re2c.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1863 | [readline/readline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/readline/readline.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1864 | [recode/recode.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/recode/recode.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1865 | [recutils/recutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/recutils/recutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1866 | [resource-agents/resource-agents.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/resource-agents/resource-agents.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1867 | [rest/rest.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rest/rest.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1868 | [rhash/rhash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rhash/rhash.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1869 | [rinutils/rinutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rinutils/rinutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1870 | [rocblas/rocblas.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocblas/rocblas.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1871 | [rocclr/rocclr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocclr/rocclr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1872 | [rocfft/rocfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocfft/rocfft.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1873 | [rocksdb/rocksdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocksdb/rocksdb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1874 | [rocm-bandwidth-test/rocm-bandwidth-test.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocm-bandwidth-test/rocm-bandwidth-test.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1875 | [rocm-core/rocm-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocm-core/rocm-core.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1876 | [rocm-origami/rocm-origami.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocm-origami/rocm-origami.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1877 | [rocm-smi/rocm-smi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocm-smi/rocm-smi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1878 | [rocminfo/rocminfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocminfo/rocminfo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1879 | [rocprim/rocprim.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocprim/rocprim.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1880 | [rocprofiler-register/rocprofiler-register.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocprofiler-register/rocprofiler-register.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1881 | [rocr-runtime/rocr-runtime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocr-runtime/rocr-runtime.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1882 | [rocrand/rocrand.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocrand/rocrand.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1883 | [rocsolver/rocsolver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocsolver/rocsolver.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1884 | [rocsparse/rocsparse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocsparse/rocsparse.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1885 | [rocthrust/rocthrust.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocthrust/rocthrust.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1886 | [roctracer/roctracer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/roctracer/roctracer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1887 | [rpcsvc-proto/rpcsvc-proto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpcsvc-proto/rpcsvc-proto.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1888 | [rsyslog/rsyslog.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rsyslog/rsyslog.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1889 | [rubberband/rubberband.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rubberband/rubberband.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1890 | [ruby/ruby.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ruby/ruby.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1891 | [runc/runc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/runc/runc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1892 | [rust-accesskit-0.21/rust-accesskit-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-accesskit-0.21/rust-accesskit-0.21.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1893 | [rust-adler2-2/rust-adler2-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-adler2-2/rust-adler2-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1894 | [rust-adler32-1/rust-adler32-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-adler32-1/rust-adler32-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1895 | [rust-aho-corasick-1/rust-aho-corasick-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-aho-corasick-1/rust-aho-corasick-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1896 | [rust-aliasable-0.1/rust-aliasable-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-aliasable-0.1/rust-aliasable-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1897 | [rust-allocator-api2-0.2/rust-allocator-api2-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-allocator-api2-0.2/rust-allocator-api2-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1898 | [rust-android-properties-0.2/rust-android-properties-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-android-properties-0.2/rust-android-properties-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1899 | [rust-anes-0.1/rust-anes-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-anes-0.1/rust-anes-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1900 | [rust-anpa-0.10/rust-anpa-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-anpa-0.10/rust-anpa-0.10.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1901 | [rust-anstyle-1/rust-anstyle-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-anstyle-1/rust-anstyle-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1902 | [rust-anstyle-parse-0.2/rust-anstyle-parse-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-anstyle-parse-0.2/rust-anstyle-parse-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1903 | [rust-anstyle-parse-1/rust-anstyle-parse-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-anstyle-parse-1/rust-anstyle-parse-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1904 | [rust-anyhow-1/rust-anyhow-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-anyhow-1/rust-anyhow-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1905 | [rust-appendlist-1/rust-appendlist-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-appendlist-1/rust-appendlist-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1906 | [rust-ar-0.9/rust-ar-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ar-0.9/rust-ar-0.9.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1907 | [rust-arbitrary-1/rust-arbitrary-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-arbitrary-1/rust-arbitrary-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1908 | [rust-archery-1/rust-archery-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-archery-1/rust-archery-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1909 | [rust-arrayref-0.3/rust-arrayref-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-arrayref-0.3/rust-arrayref-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1910 | [rust-arrayvec-0.7/rust-arrayvec-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-arrayvec-0.7/rust-arrayvec-0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1911 | [rust-as-raw-xcb-connection-1/rust-as-raw-xcb-connection-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-as-raw-xcb-connection-1/rust-as-raw-xcb-connection-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1912 | [rust-ash-0.38/rust-ash-0.38.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ash-0.38/rust-ash-0.38.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1913 | [rust-assert-approx-eq-1/rust-assert-approx-eq-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-assert-approx-eq-1/rust-assert-approx-eq-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1914 | [rust-associative-cache-2/rust-associative-cache-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-associative-cache-2/rust-associative-cache-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1915 | [rust-async-task-4/rust-async-task-4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-async-task-4/rust-async-task-4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1916 | [rust-atomic-float-1/rust-atomic-float-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-atomic-float-1/rust-atomic-float-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1917 | [rust-atomic-waker-1/rust-atomic-waker-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-atomic-waker-1/rust-atomic-waker-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1918 | [rust-autocfg-1/rust-autocfg-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-autocfg-1/rust-autocfg-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1919 | [rust-base16ct-0.2/rust-base16ct-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-base16ct-0.2/rust-base16ct-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1920 | [rust-base16ct-1/rust-base16ct-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-base16ct-1/rust-base16ct-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1921 | [rust-base64-0.13/rust-base64-0.13.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-base64-0.13/rust-base64-0.13.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1922 | [rust-base64-0.21/rust-base64-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-base64-0.21/rust-base64-0.21.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1923 | [rust-base64-0.22/rust-base64-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-base64-0.22/rust-base64-0.22.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1924 | [rust-base64ct-1/rust-base64ct-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-base64ct-1/rust-base64ct-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1925 | [rust-bit-field-0.10/rust-bit-field-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bit-field-0.10/rust-bit-field-0.10.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1926 | [rust-bit-vec-0.6/rust-bit-vec-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bit-vec-0.6/rust-bit-vec-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1927 | [rust-bit-vec-0.8/rust-bit-vec-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bit-vec-0.8/rust-bit-vec-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1928 | [rust-bitflags-1/rust-bitflags-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bitflags-1/rust-bitflags-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1929 | [rust-bitflags-2/rust-bitflags-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bitflags-2/rust-bitflags-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1930 | [rust-block-0.1/rust-block-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-block-0.1/rust-block-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1931 | [rust-borrow-or-share-0.2/rust-borrow-or-share-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-borrow-or-share-0.2/rust-borrow-or-share-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1932 | [rust-boxcar-0.2/rust-boxcar-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-boxcar-0.2/rust-boxcar-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1933 | [rust-bs58-0.5/rust-bs58-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bs58-0.5/rust-bs58-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1934 | [rust-built-0.8/rust-built-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-built-0.8/rust-built-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1935 | [rust-bumpalo-3/rust-bumpalo-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bumpalo-3/rust-bumpalo-3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1936 | [rust-by-address-1/rust-by-address-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-by-address-1/rust-by-address-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1937 | [rust-byte-slice-cast-1/rust-byte-slice-cast-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-byte-slice-cast-1/rust-byte-slice-cast-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1938 | [rust-bytecount-0.6/rust-bytecount-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bytecount-0.6/rust-bytecount-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1939 | [rust-bytemuck-1/rust-bytemuck-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bytemuck-1/rust-bytemuck-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1940 | [rust-byteorder-1/rust-byteorder-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-byteorder-1/rust-byteorder-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1941 | [rust-byteorder-lite-0.1/rust-byteorder-lite-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-byteorder-lite-0.1/rust-byteorder-lite-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1942 | [rust-bytes-1/rust-bytes-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bytes-1/rust-bytes-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1943 | [rust-bytesize-2/rust-bytesize-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bytesize-2/rust-bytesize-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1944 | [rust-bzip2-0.5/rust-bzip2-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bzip2-0.5/rust-bzip2-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1945 | [rust-bzip2-0.6/rust-bzip2-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bzip2-0.6/rust-bzip2-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1946 | [rust-camino-1/rust-camino-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-camino-1/rust-camino-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1947 | [rust-cast-0.3/rust-cast-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cast-0.3/rust-cast-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1948 | [rust-cc-traits-2/rust-cc-traits-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cc-traits-2/rust-cc-traits-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1949 | [rust-cesu8-1/rust-cesu8-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cesu8-1/rust-cesu8-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1950 | [rust-cfg-aliases-0.2/rust-cfg-aliases-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cfg-aliases-0.2/rust-cfg-aliases-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1951 | [rust-cfg-if-0.1/rust-cfg-if-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cfg-if-0.1/rust-cfg-if-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1952 | [rust-cfg-if-1/rust-cfg-if-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cfg-if-1/rust-cfg-if-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1953 | [rust-ciborium-io-0.2/rust-ciborium-io-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ciborium-io-0.2/rust-ciborium-io-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1954 | [rust-cint-0.3/rust-cint-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cint-0.3/rust-cint-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1955 | [rust-clap-lex-0.7/rust-clap-lex-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-clap-lex-0.7/rust-clap-lex-0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1956 | [rust-clap-lex-1/rust-clap-lex-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-clap-lex-1/rust-clap-lex-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1957 | [rust-cmov-0.5/rust-cmov-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cmov-0.5/rust-cmov-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1958 | [rust-color-quant-1/rust-color-quant-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-color-quant-1/rust-color-quant-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1959 | [rust-colorchoice-1/rust-colorchoice-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-colorchoice-1/rust-colorchoice-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1960 | [rust-comma-1/rust-comma-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-comma-1/rust-comma-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1961 | [rust-configparser-3/rust-configparser-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-configparser-3/rust-configparser-3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1962 | [rust-const-oid-0.10/rust-const-oid-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-const-oid-0.10/rust-const-oid-0.10.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1963 | [rust-const-oid-0.9/rust-const-oid-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-const-oid-0.9/rust-const-oid-0.9.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1964 | [rust-const-str-1/rust-const-str-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-const-str-1/rust-const-str-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1965 | [rust-constant-time-eq-0.3/rust-constant-time-eq-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-constant-time-eq-0.3/rust-constant-time-eq-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1966 | [rust-constant-time-eq-0.4/rust-constant-time-eq-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-constant-time-eq-0.4/rust-constant-time-eq-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1967 | [rust-cookie-factory-0.3/rust-cookie-factory-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cookie-factory-0.3/rust-cookie-factory-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1968 | [rust-core-foundation-sys-0.8/rust-core-foundation-sys-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-core-foundation-sys-0.8/rust-core-foundation-sys-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1969 | [rust-countio-0.3/rust-countio-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-countio-0.3/rust-countio-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1970 | [rust-cpubits-0.1/rust-cpubits-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cpubits-0.1/rust-cpubits-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1971 | [rust-crc-catalog-2/rust-crc-catalog-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-crc-catalog-2/rust-crc-catalog-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1972 | [rust-critical-section-1/rust-critical-section-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-critical-section-1/rust-critical-section-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1973 | [rust-crossbeam-utils-0.8/rust-crossbeam-utils-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-crossbeam-utils-0.8/rust-crossbeam-utils-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1974 | [rust-crunchy-0.2/rust-crunchy-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-crunchy-0.2/rust-crunchy-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1975 | [rust-csscolorparser-0.6/rust-csscolorparser-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-csscolorparser-0.6/rust-csscolorparser-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1976 | [rust-ct-codecs-1/rust-ct-codecs-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ct-codecs-1/rust-ct-codecs-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1977 | [rust-ctor-0.6/rust-ctor-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ctor-0.6/rust-ctor-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1978 | [rust-ctor-1/rust-ctor-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ctor-1/rust-ctor-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1979 | [rust-ctor-proc-macro-0.0.7/rust-ctor-proc-macro-0.0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ctor-proc-macro-0.0.7/rust-ctor-proc-macro-0.0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1980 | [rust-cursor-icon-1/rust-cursor-icon-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cursor-icon-1/rust-cursor-icon-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1981 | [rust-dary-heap-0.3/rust-dary-heap-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-dary-heap-0.3/rust-dary-heap-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1982 | [rust-data-encoding-2/rust-data-encoding-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-data-encoding-2/rust-data-encoding-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1983 | [rust-data-url-0.3/rust-data-url-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-data-url-0.3/rust-data-url-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1984 | [rust-deadpool-runtime-0.1/rust-deadpool-runtime-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-deadpool-runtime-0.1/rust-deadpool-runtime-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1985 | [rust-deadpool-runtime-0.3/rust-deadpool-runtime-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-deadpool-runtime-0.3/rust-deadpool-runtime-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1986 | [rust-deflate64-0.1/rust-deflate64-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-deflate64-0.1/rust-deflate64-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1987 | [rust-deltae-0.3/rust-deltae-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-deltae-0.3/rust-deltae-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1988 | [rust-der-0.7/rust-der-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-der-0.7/rust-der-0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1989 | [rust-der-0.8/rust-der-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-der-0.8/rust-der-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1990 | [rust-deranged-0.5/rust-deranged-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-deranged-0.5/rust-deranged-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1991 | [rust-diff-0.1/rust-diff-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-diff-0.1/rust-diff-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1992 | [rust-difflib-0.4/rust-difflib-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-difflib-0.4/rust-difflib-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1993 | [rust-dispatch-0.2/rust-dispatch-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-dispatch-0.2/rust-dispatch-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1994 | [rust-downcast-0.11/rust-downcast-0.11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-downcast-0.11/rust-downcast-0.11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1995 | [rust-downcast-rs-1/rust-downcast-rs-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-downcast-rs-1/rust-downcast-rs-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1996 | [rust-dpi-0.1/rust-dpi-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-dpi-0.1/rust-dpi-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1997 | [rust-drm-fourcc-2/rust-drm-fourcc-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-drm-fourcc-2/rust-drm-fourcc-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1998 | [rust-dtoa-1/rust-dtoa-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-dtoa-1/rust-dtoa-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 1999 | [rust-dtor-0.1/rust-dtor-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-dtor-0.1/rust-dtor-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2000 | [rust-dtor-proc-macro-0.0.6/rust-dtor-proc-macro-0.0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-dtor-proc-macro-0.0.6/rust-dtor-proc-macro-0.0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2001 | [rust-dyn-clone-1/rust-dyn-clone-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-dyn-clone-1/rust-dyn-clone-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2002 | [rust-ed25519-compact-2/rust-ed25519-compact-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ed25519-compact-2/rust-ed25519-compact-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2003 | [rust-either-1/rust-either-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-either-1/rust-either-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2004 | [rust-email-address-0.2/rust-email-address-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-email-address-0.2/rust-email-address-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2005 | [rust-embedded-io-0.4/rust-embedded-io-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-embedded-io-0.4/rust-embedded-io-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2006 | [rust-embedded-io-0.6/rust-embedded-io-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-embedded-io-0.6/rust-embedded-io-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2007 | [rust-encode-unicode-1/rust-encode-unicode-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-encode-unicode-1/rust-encode-unicode-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2008 | [rust-endi-1/rust-endi-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-endi-1/rust-endi-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2009 | [rust-endian-type-0.1/rust-endian-type-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-endian-type-0.1/rust-endian-type-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2010 | [rust-equivalent-1/rust-equivalent-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-equivalent-1/rust-equivalent-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2011 | [rust-error-code-3/rust-error-code-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-error-code-3/rust-error-code-3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2012 | [rust-esaxx-rs-0.1/rust-esaxx-rs-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-esaxx-rs-0.1/rust-esaxx-rs-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2013 | [rust-event-listener-2/rust-event-listener-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-event-listener-2/rust-event-listener-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2014 | [rust-fallible-collections-0.4/rust-fallible-collections-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-fallible-collections-0.4/rust-fallible-collections-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2015 | [rust-fallible-iterator-0.3/rust-fallible-iterator-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-fallible-iterator-0.3/rust-fallible-iterator-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2016 | [rust-fallible-streaming-iterator-0.1/rust-fallible-streaming-iterator-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-fallible-streaming-iterator-0.1/rust-fallible-streaming-iterator-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2017 | [rust-fast-srgb8-1/rust-fast-srgb8-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-fast-srgb8-1/rust-fast-srgb8-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2018 | [rust-fastrand-2/rust-fastrand-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-fastrand-2/rust-fastrand-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2019 | [rust-fax-0.2/rust-fax-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-fax-0.2/rust-fax-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2020 | [rust-fdt-0.1/rust-fdt-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-fdt-0.1/rust-fdt-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2021 | [rust-fiat-crypto-0.3/rust-fiat-crypto-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-fiat-crypto-0.3/rust-fiat-crypto-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2022 | [rust-find-msvc-tools-0.1/rust-find-msvc-tools-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-find-msvc-tools-0.1/rust-find-msvc-tools-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2023 | [rust-fixedbitset-0.4/rust-fixedbitset-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-fixedbitset-0.4/rust-fixedbitset-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2024 | [rust-float-cmp-0.10/rust-float-cmp-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-float-cmp-0.10/rust-float-cmp-0.10.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2025 | [rust-float-cmp-0.9/rust-float-cmp-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-float-cmp-0.9/rust-float-cmp-0.9.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2026 | [rust-fnv-1/rust-fnv-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-fnv-1/rust-fnv-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2027 | [rust-foldhash-0.1/rust-foldhash-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-foldhash-0.1/rust-foldhash-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2028 | [rust-foldhash-0.2/rust-foldhash-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-foldhash-0.2/rust-foldhash-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2029 | [rust-font-types-0.9/rust-font-types-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-font-types-0.9/rust-font-types-0.9.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2030 | [rust-foreign-types-shared-0.1/rust-foreign-types-shared-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-foreign-types-shared-0.1/rust-foreign-types-shared-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2031 | [rust-foreign-types-shared-0.3/rust-foreign-types-shared-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-foreign-types-shared-0.3/rust-foreign-types-shared-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2032 | [rust-fragile-2/rust-fragile-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-fragile-2/rust-fragile-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2033 | [rust-fs-extra-1/rust-fs-extra-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-fs-extra-1/rust-fs-extra-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2034 | [rust-fst-0.4/rust-fst-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-fst-0.4/rust-fst-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2035 | [rust-funty-2/rust-funty-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-funty-2/rust-funty-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2036 | [rust-futures-timer-3/rust-futures-timer-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-futures-timer-3/rust-futures-timer-3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2037 | [rust-gimli-0.32/rust-gimli-0.32.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gimli-0.32/rust-gimli-0.32.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2038 | [rust-gix-trace-0.1/rust-gix-trace-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gix-trace-0.1/rust-gix-trace-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2039 | [rust-glam-0.14/rust-glam-0.14.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.14/rust-glam-0.14.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2040 | [rust-glam-0.15/rust-glam-0.15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.15/rust-glam-0.15.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2041 | [rust-glam-0.16/rust-glam-0.16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.16/rust-glam-0.16.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2042 | [rust-glam-0.17/rust-glam-0.17.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.17/rust-glam-0.17.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2043 | [rust-glam-0.18/rust-glam-0.18.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.18/rust-glam-0.18.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2044 | [rust-glam-0.19/rust-glam-0.19.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.19/rust-glam-0.19.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2045 | [rust-glam-0.20/rust-glam-0.20.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.20/rust-glam-0.20.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2046 | [rust-glam-0.21/rust-glam-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.21/rust-glam-0.21.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2047 | [rust-glam-0.22/rust-glam-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.22/rust-glam-0.22.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2048 | [rust-glam-0.23/rust-glam-0.23.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.23/rust-glam-0.23.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2049 | [rust-glam-0.24/rust-glam-0.24.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.24/rust-glam-0.24.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2050 | [rust-glam-0.25/rust-glam-0.25.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.25/rust-glam-0.25.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2051 | [rust-glam-0.27/rust-glam-0.27.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.27/rust-glam-0.27.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2052 | [rust-glam-0.28/rust-glam-0.28.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.28/rust-glam-0.28.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2053 | [rust-glam-0.29/rust-glam-0.29.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.29/rust-glam-0.29.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2054 | [rust-glam-0.30/rust-glam-0.30.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.30/rust-glam-0.30.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2055 | [rust-glam-0.31/rust-glam-0.31.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.31/rust-glam-0.31.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2056 | [rust-glam-0.32/rust-glam-0.32.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glam-0.32/rust-glam-0.32.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2057 | [rust-glob-0.3/rust-glob-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glob-0.3/rust-glob-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2058 | [rust-hashbrown-0.12/rust-hashbrown-0.12.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hashbrown-0.12/rust-hashbrown-0.12.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2059 | [rust-hashbrown-0.13/rust-hashbrown-0.13.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hashbrown-0.13/rust-hashbrown-0.13.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2060 | [rust-hashbrown-0.14/rust-hashbrown-0.14.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hashbrown-0.14/rust-hashbrown-0.14.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2061 | [rust-hashbrown-0.15/rust-hashbrown-0.15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hashbrown-0.15/rust-hashbrown-0.15.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2062 | [rust-hashbrown-0.16/rust-hashbrown-0.16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hashbrown-0.16/rust-hashbrown-0.16.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2063 | [rust-hashbrown-0.17/rust-hashbrown-0.17.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hashbrown-0.17/rust-hashbrown-0.17.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2064 | [rust-heapify-0.2/rust-heapify-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-heapify-0.2/rust-heapify-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2065 | [rust-heck-0.4/rust-heck-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-heck-0.4/rust-heck-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2066 | [rust-heck-0.5/rust-heck-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-heck-0.5/rust-heck-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2067 | [rust-hermit-abi-0.3/rust-hermit-abi-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hermit-abi-0.3/rust-hermit-abi-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2068 | [rust-hermit-abi-0.5/rust-hermit-abi-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hermit-abi-0.5/rust-hermit-abi-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2069 | [rust-hex-0.4/rust-hex-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hex-0.4/rust-hex-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2070 | [rust-hex-literal-1/rust-hex-literal-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hex-literal-1/rust-hex-literal-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2071 | [rust-httparse-1/rust-httparse-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-httparse-1/rust-httparse-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2072 | [rust-httpdate-1/rust-httpdate-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-httpdate-1/rust-httpdate-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2073 | [rust-humantime-2/rust-humantime-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-humantime-2/rust-humantime-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2074 | [rust-iced-x86-1/rust-iced-x86-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-iced-x86-1/rust-iced-x86-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2075 | [rust-id-arena-2/rust-id-arena-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-id-arena-2/rust-id-arena-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2076 | [rust-ident-case-1/rust-ident-case-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ident-case-1/rust-ident-case-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2077 | [rust-imagesize-0.13/rust-imagesize-0.13.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-imagesize-0.13/rust-imagesize-0.13.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2078 | [rust-include-flate-compress-0.3/rust-include-flate-compress-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-include-flate-compress-0.3/rust-include-flate-compress-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2079 | [rust-indenter-0.3/rust-indenter-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-indenter-0.3/rust-indenter-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2080 | [rust-input-sys-1/rust-input-sys-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-input-sys-1/rust-input-sys-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2081 | [rust-io-lifetimes-1/rust-io-lifetimes-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-io-lifetimes-1/rust-io-lifetimes-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2082 | [rust-iommufd-bindings-0.1/rust-iommufd-bindings-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-iommufd-bindings-0.1/rust-iommufd-bindings-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2083 | [rust-ipnet-2/rust-ipnet-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ipnet-2/rust-ipnet-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2084 | [rust-ipnetwork-0.20/rust-ipnetwork-0.20.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ipnetwork-0.20/rust-ipnetwork-0.20.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2085 | [rust-iri-string-0.7/rust-iri-string-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-iri-string-0.7/rust-iri-string-0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2086 | [rust-is-ci-1/rust-is-ci-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-is-ci-1/rust-is-ci-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2087 | [rust-is-terminal-polyfill-1/rust-is-terminal-polyfill-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-is-terminal-polyfill-1/rust-is-terminal-polyfill-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2088 | [rust-itoa-1/rust-itoa-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-itoa-1/rust-itoa-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2089 | [rust-itoap-1/rust-itoap-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-itoap-1/rust-itoap-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2090 | [rust-jiff-tzdb-0.1/rust-jiff-tzdb-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-jiff-tzdb-0.1/rust-jiff-tzdb-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2091 | [rust-jni-sys-0.3/rust-jni-sys-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-jni-sys-0.3/rust-jni-sys-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2092 | [rust-khronos-api-3/rust-khronos-api-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-khronos-api-3/rust-khronos-api-3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2093 | [rust-konst-proc-macros-0.4/rust-konst-proc-macros-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-konst-proc-macros-0.4/rust-konst-proc-macros-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2094 | [rust-kvm-bindings-0.14/rust-kvm-bindings-0.14.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-kvm-bindings-0.14/rust-kvm-bindings-0.14.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2095 | [rust-lab-0.11/rust-lab-0.11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-lab-0.11/rust-lab-0.11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2096 | [rust-language-tags-0.3/rust-language-tags-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-language-tags-0.3/rust-language-tags-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2097 | [rust-lazy-static-1/rust-lazy-static-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-lazy-static-1/rust-lazy-static-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2098 | [rust-lazycell-1/rust-lazycell-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-lazycell-1/rust-lazycell-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2099 | [rust-leb128fmt-0.1/rust-leb128fmt-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-leb128fmt-0.1/rust-leb128fmt-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2100 | [rust-lebe-0.5/rust-lebe-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-lebe-0.5/rust-lebe-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2101 | [rust-levenshtein-1/rust-levenshtein-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-levenshtein-1/rust-levenshtein-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2102 | [rust-lexical-util-1/rust-lexical-util-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-lexical-util-1/rust-lexical-util-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2103 | [rust-libbz2-rs-sys-0.2/rust-libbz2-rs-sys-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-libbz2-rs-sys-0.2/rust-libbz2-rs-sys-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2104 | [rust-libc-0.2/rust-libc-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-libc-0.2/rust-libc-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2105 | [rust-libm-0.2/rust-libm-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-libm-0.2/rust-libm-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2106 | [rust-libredox-0.1/rust-libredox-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-libredox-0.1/rust-libredox-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2107 | [rust-libseccomp-sys-0.2/rust-libseccomp-sys-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-libseccomp-sys-0.2/rust-libseccomp-sys-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2108 | [rust-libsqlite3-sys-0.28/rust-libsqlite3-sys-0.28.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-libsqlite3-sys-0.28/rust-libsqlite3-sys-0.28.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2109 | [rust-libsqlite3-sys-0.34/rust-libsqlite3-sys-0.34.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-libsqlite3-sys-0.34/rust-libsqlite3-sys-0.34.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2110 | [rust-link-section-0.18/rust-link-section-0.18.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-link-section-0.18/rust-link-section-0.18.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2111 | [rust-linked-hash-map-0.5/rust-linked-hash-map-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-linked-hash-map-0.5/rust-linked-hash-map-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2112 | [rust-linktime-proc-macro-0.2/rust-linktime-proc-macro-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-linktime-proc-macro-0.2/rust-linktime-proc-macro-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2113 | [rust-linux-raw-sys-0.11/rust-linux-raw-sys-0.11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-linux-raw-sys-0.11/rust-linux-raw-sys-0.11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2114 | [rust-linux-raw-sys-0.12/rust-linux-raw-sys-0.12.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-linux-raw-sys-0.12/rust-linux-raw-sys-0.12.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2115 | [rust-linux-raw-sys-0.3/rust-linux-raw-sys-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-linux-raw-sys-0.3/rust-linux-raw-sys-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2116 | [rust-linux-raw-sys-0.4/rust-linux-raw-sys-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-linux-raw-sys-0.4/rust-linux-raw-sys-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2117 | [rust-linux-raw-sys-0.9/rust-linux-raw-sys-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-linux-raw-sys-0.9/rust-linux-raw-sys-0.9.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2118 | [rust-litemap-0.8/rust-litemap-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-litemap-0.8/rust-litemap-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2119 | [rust-litrs-1/rust-litrs-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-litrs-1/rust-litrs-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2120 | [rust-log-0.4/rust-log-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-log-0.4/rust-log-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2121 | [rust-lru-0.16/rust-lru-0.16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-lru-0.16/rust-lru-0.16.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2122 | [rust-lru-0.18/rust-lru-0.18.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-lru-0.18/rust-lru-0.18.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2123 | [rust-lru-slab-0.1/rust-lru-slab-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-lru-slab-0.1/rust-lru-slab-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2124 | [rust-lz4-flex-0.13/rust-lz4-flex-0.13.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-lz4-flex-0.13/rust-lz4-flex-0.13.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2125 | [rust-lzma-rust2-0.16/rust-lzma-rust2-0.16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-lzma-rust2-0.16/rust-lzma-rust2-0.16.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2126 | [rust-lzxd-0.2/rust-lzxd-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-lzxd-0.2/rust-lzxd-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2127 | [rust-mac-0.1/rust-mac-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-mac-0.1/rust-mac-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2128 | [rust-macro-rules-attribute-proc-macro-0.2/rust-macro-rules-attribute-proc-macro-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-macro-rules-attribute-proc-macro-0.2/rust-macro-rules-attribute-proc-macro-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2129 | [rust-managed-0.8/rust-managed-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-managed-0.8/rust-managed-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2130 | [rust-matches-0.1/rust-matches-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-matches-0.1/rust-matches-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2131 | [rust-matchit-0.7/rust-matchit-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-matchit-0.7/rust-matchit-0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2132 | [rust-matchit-0.8/rust-matchit-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-matchit-0.8/rust-matchit-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2133 | [rust-md5-0.7/rust-md5-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-md5-0.7/rust-md5-0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2134 | [rust-memchr-2/rust-memchr-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-memchr-2/rust-memchr-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2135 | [rust-memmem-0.1/rust-memmem-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-memmem-0.1/rust-memmem-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2136 | [rust-memo-map-0.3/rust-memo-map-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-memo-map-0.3/rust-memo-map-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2137 | [rust-micromath-2/rust-micromath-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-micromath-2/rust-micromath-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2138 | [rust-mime-0.3/rust-mime-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-mime-0.3/rust-mime-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2139 | [rust-minicbor-0.19/rust-minicbor-0.19.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-minicbor-0.19/rust-minicbor-0.19.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2140 | [rust-minimal-lexical-0.2/rust-minimal-lexical-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-minimal-lexical-0.2/rust-minimal-lexical-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2141 | [rust-minisign-verify-0.2/rust-minisign-verify-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-minisign-verify-0.2/rust-minisign-verify-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2142 | [rust-mint-0.5/rust-mint-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-mint-0.5/rust-mint-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2143 | [rust-mintex-0.1/rust-mintex-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-mintex-0.1/rust-mintex-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2144 | [rust-more-asserts-0.3/rust-more-asserts-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-more-asserts-0.3/rust-more-asserts-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2145 | [rust-multimap-0.8/rust-multimap-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-multimap-0.8/rust-multimap-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2146 | [rust-mutants-0.0.3/rust-mutants-0.0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-mutants-0.0.3/rust-mutants-0.0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2147 | [rust-nanorand-0.7/rust-nanorand-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-nanorand-0.7/rust-nanorand-0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2148 | [rust-natord-1/rust-natord-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-natord-1/rust-natord-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2149 | [rust-ndk-context-0.1/rust-ndk-context-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ndk-context-0.1/rust-ndk-context-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2150 | [rust-new-debug-unreachable-1/rust-new-debug-unreachable-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-new-debug-unreachable-1/rust-new-debug-unreachable-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2151 | [rust-no-std-net-0.6/rust-no-std-net-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-no-std-net-0.6/rust-no-std-net-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2152 | [rust-noop-proc-macro-0.3/rust-noop-proc-macro-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-noop-proc-macro-0.3/rust-noop-proc-macro-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2153 | [rust-normalize-line-endings-0.3/rust-normalize-line-endings-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-normalize-line-endings-0.3/rust-normalize-line-endings-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2154 | [rust-num-cmp-0.1/rust-num-cmp-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-num-cmp-0.1/rust-num-cmp-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2155 | [rust-num-conv-0.1/rust-num-conv-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-num-conv-0.1/rust-num-conv-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2156 | [rust-num-conv-0.2/rust-num-conv-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-num-conv-0.2/rust-num-conv-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2157 | [rust-number-prefix-0.4/rust-number-prefix-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-number-prefix-0.4/rust-number-prefix-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2158 | [rust-numtoa-0.2/rust-numtoa-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-numtoa-0.2/rust-numtoa-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2159 | [rust-objc-sys-0.3/rust-objc-sys-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-objc-sys-0.3/rust-objc-sys-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2160 | [rust-objc2-core-foundation-0.3/rust-objc2-core-foundation-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-objc2-core-foundation-0.3/rust-objc2-core-foundation-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2161 | [rust-objc2-encode-4/rust-objc2-encode-4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-objc2-encode-4/rust-objc2-encode-4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2162 | [rust-objc2-io-surface-0.3/rust-objc2-io-surface-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-objc2-io-surface-0.3/rust-objc2-io-surface-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2163 | [rust-once-cell-1/rust-once-cell-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-once-cell-1/rust-once-cell-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2164 | [rust-once-cell-polyfill-1/rust-once-cell-polyfill-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-once-cell-polyfill-1/rust-once-cell-polyfill-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2165 | [rust-oneshot-0.1/rust-oneshot-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-oneshot-0.1/rust-oneshot-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2166 | [rust-oorandom-11/rust-oorandom-11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-oorandom-11/rust-oorandom-11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2167 | [rust-opaque-debug-0.3/rust-opaque-debug-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-opaque-debug-0.3/rust-opaque-debug-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2168 | [rust-openssl-probe-0.1/rust-openssl-probe-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-openssl-probe-0.1/rust-openssl-probe-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2169 | [rust-openssl-probe-0.2/rust-openssl-probe-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-openssl-probe-0.2/rust-openssl-probe-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2170 | [rust-option-ext-0.2/rust-option-ext-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-option-ext-0.2/rust-option-ext-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2171 | [rust-ordered-channel-1/rust-ordered-channel-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ordered-channel-1/rust-ordered-channel-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2172 | [rust-os-str-bytes-6/rust-os-str-bytes-6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-os-str-bytes-6/rust-os-str-bytes-6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2173 | [rust-outref-0.5/rust-outref-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-outref-0.5/rust-outref-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2174 | [rust-owo-colors-3/rust-owo-colors-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-owo-colors-3/rust-owo-colors-3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2175 | [rust-owo-colors-4/rust-owo-colors-4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-owo-colors-4/rust-owo-colors-4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2176 | [rust-parking-2/rust-parking-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-parking-2/rust-parking-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2177 | [rust-paste-1/rust-paste-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-paste-1/rust-paste-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2178 | [rust-pastey-0.1/rust-pastey-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pastey-0.1/rust-pastey-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2179 | [rust-pastey-0.2/rust-pastey-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pastey-0.2/rust-pastey-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2180 | [rust-path-slash-0.2/rust-path-slash-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-path-slash-0.2/rust-path-slash-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2181 | [rust-pathdiff-0.2/rust-pathdiff-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pathdiff-0.2/rust-pathdiff-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2182 | [rust-peg-runtime-0.8/rust-peg-runtime-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-peg-runtime-0.8/rust-peg-runtime-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2183 | [rust-percent-encoding-2/rust-percent-encoding-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-percent-encoding-2/rust-percent-encoding-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2184 | [rust-pico-args-0.5/rust-pico-args-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pico-args-0.5/rust-pico-args-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2185 | [rust-pin-project-lite-0.2/rust-pin-project-lite-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pin-project-lite-0.2/rust-pin-project-lite-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2186 | [rust-pin-utils-0.1/rust-pin-utils-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pin-utils-0.1/rust-pin-utils-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2187 | [rust-pixman-sys-0.1/rust-pixman-sys-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pixman-sys-0.1/rust-pixman-sys-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2188 | [rust-pkg-config-0.3/rust-pkg-config-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pkg-config-0.3/rust-pkg-config-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2189 | [rust-plain-0.2/rust-plain-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-plain-0.2/rust-plain-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2190 | [rust-pocket-resources-0.3/rust-pocket-resources-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pocket-resources-0.3/rust-pocket-resources-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2191 | [rust-portable-atomic-1/rust-portable-atomic-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-portable-atomic-1/rust-portable-atomic-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2192 | [rust-powerfmt-0.2/rust-powerfmt-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-powerfmt-0.2/rust-powerfmt-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2193 | [rust-precomputed-hash-0.1/rust-precomputed-hash-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-precomputed-hash-0.1/rust-precomputed-hash-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2194 | [rust-predicates-core-1/rust-predicates-core-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-predicates-core-1/rust-predicates-core-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2195 | [rust-prodash-30/rust-prodash-30.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-prodash-30/rust-prodash-30.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2196 | [rust-profiling-1/rust-profiling-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-profiling-1/rust-profiling-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2197 | [rust-protobuf-2/rust-protobuf-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-protobuf-2/rust-protobuf-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2198 | [rust-pxfm-0.1/rust-pxfm-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pxfm-0.1/rust-pxfm-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2199 | [rust-quick-error-1/rust-quick-error-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-quick-error-1/rust-quick-error-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2200 | [rust-quick-error-2/rust-quick-error-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-quick-error-2/rust-quick-error-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2201 | [rust-quoted-printable-0.5/rust-quoted-printable-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-quoted-printable-0.5/rust-quoted-printable-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2202 | [rust-r-efi-5/rust-r-efi-5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-r-efi-5/rust-r-efi-5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2203 | [rust-r-efi-6/rust-r-efi-6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-r-efi-6/rust-r-efi-6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2204 | [rust-radium-0.7/rust-radium-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-radium-0.7/rust-radium-0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2205 | [rust-range-map-vec-0.2/rust-range-map-vec-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-range-map-vec-0.2/rust-range-map-vec-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2206 | [rust-range-traits-0.3/rust-range-traits-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-range-traits-0.3/rust-range-traits-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2207 | [rust-rangemap-1/rust-rangemap-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rangemap-1/rust-rangemap-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2208 | [rust-raw-window-handle-0.6/rust-raw-window-handle-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-raw-window-handle-0.6/rust-raw-window-handle-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2209 | [rust-rawpointer-0.2/rust-rawpointer-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rawpointer-0.2/rust-rawpointer-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2210 | [rust-rctree-0.6/rust-rctree-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rctree-0.6/rust-rctree-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2211 | [rust-regex-automata-0.4/rust-regex-automata-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-regex-automata-0.4/rust-regex-automata-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2212 | [rust-regex-syntax-0.8/rust-regex-syntax-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-regex-syntax-0.8/rust-regex-syntax-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2213 | [rust-rend-0.4/rust-rend-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rend-0.4/rust-rend-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2214 | [rust-retry-2/rust-retry-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-retry-2/rust-retry-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2215 | [rust-rle-decode-fast-1/rust-rle-decode-fast-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rle-decode-fast-1/rust-rle-decode-fast-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2216 | [rust-roff-0.2/rust-roff-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-roff-0.2/rust-roff-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2217 | [rust-roxmltree-0.20/rust-roxmltree-0.20.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-roxmltree-0.20/rust-roxmltree-0.20.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2218 | [rust-rs-tracing-1/rust-rs-tracing-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rs-tracing-1/rust-rs-tracing-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2219 | [rust-rustc-demangle-0.1/rust-rustc-demangle-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rustc-demangle-0.1/rust-rustc-demangle-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2220 | [rust-rustc-hash-1/rust-rustc-hash-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rustc-hash-1/rust-rustc-hash-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2221 | [rust-rustc-hash-2/rust-rustc-hash-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rustc-hash-2/rust-rustc-hash-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2222 | [rust-rustc-stable-hash-0.1/rust-rustc-stable-hash-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rustc-stable-hash-0.1/rust-rustc-stable-hash-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2223 | [rust-rustflags-0.1/rust-rustflags-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rustflags-0.1/rust-rustflags-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2224 | [rust-rustls-pki-types-1/rust-rustls-pki-types-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rustls-pki-types-1/rust-rustls-pki-types-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2225 | [rust-rustls-platform-verifier-android-0.1/rust-rustls-platform-verifier-android-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rustls-platform-verifier-android-0.1/rust-rustls-platform-verifier-android-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2226 | [rust-rustversion-1/rust-rustversion-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rustversion-1/rust-rustversion-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2227 | [rust-ruzstd-0.8/rust-ruzstd-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ruzstd-0.8/rust-ruzstd-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2228 | [rust-ryu-1/rust-ryu-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ryu-1/rust-ryu-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2229 | [rust-safe-arch-0.7/rust-safe-arch-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-safe-arch-0.7/rust-safe-arch-0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2230 | [rust-safe-arch-0.9/rust-safe-arch-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-safe-arch-0.9/rust-safe-arch-0.9.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2231 | [rust-safe-transmute-0.11/rust-safe-transmute-0.11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-safe-transmute-0.11/rust-safe-transmute-0.11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2232 | [rust-scoped-tls-1/rust-scoped-tls-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-scoped-tls-1/rust-scoped-tls-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2233 | [rust-scopeguard-1/rust-scopeguard-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-scopeguard-1/rust-scopeguard-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2234 | [rust-scroll-0.13/rust-scroll-0.13.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-scroll-0.13/rust-scroll-0.13.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2235 | [rust-sdd-3/rust-sdd-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-sdd-3/rust-sdd-3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2236 | [rust-seahash-4/rust-seahash-4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-seahash-4/rust-seahash-4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2237 | [rust-sec1-0.7/rust-sec1-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-sec1-0.7/rust-sec1-0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2238 | [rust-sec1-0.8/rust-sec1-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-sec1-0.8/rust-sec1-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2239 | [rust-self-cell-1/rust-self-cell-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-self-cell-1/rust-self-cell-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2240 | [rust-semver-1/rust-semver-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-semver-1/rust-semver-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2241 | [rust-send-wrapper-0.6/rust-send-wrapper-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-send-wrapper-0.6/rust-send-wrapper-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2242 | [rust-serde-spanned-0.6/rust-serde-spanned-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-serde-spanned-0.6/rust-serde-spanned-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2243 | [rust-serde-spanned-1/rust-serde-spanned-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-serde-spanned-1/rust-serde-spanned-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2244 | [rust-sha1-smol-1/rust-sha1-smol-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-sha1-smol-1/rust-sha1-smol-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2245 | [rust-shell-escape-0.1/rust-shell-escape-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-shell-escape-0.1/rust-shell-escape-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2246 | [rust-shell-words-1/rust-shell-words-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-shell-words-1/rust-shell-words-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2247 | [rust-shellexpand-3/rust-shellexpand-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-shellexpand-3/rust-shellexpand-3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2248 | [rust-shlex-1/rust-shlex-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-shlex-1/rust-shlex-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2249 | [rust-shlex-2/rust-shlex-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-shlex-2/rust-shlex-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2250 | [rust-signature-2/rust-signature-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-signature-2/rust-signature-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2251 | [rust-signature-3/rust-signature-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-signature-3/rust-signature-3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2252 | [rust-simd-adler32-0.3/rust-simd-adler32-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-simd-adler32-0.3/rust-simd-adler32-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2253 | [rust-simdutf8-0.1/rust-simdutf8-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-simdutf8-0.1/rust-simdutf8-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2254 | [rust-similar-2/rust-similar-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-similar-2/rust-similar-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2255 | [rust-similar-3/rust-similar-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-similar-3/rust-similar-3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2256 | [rust-slab-0.4/rust-slab-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-slab-0.4/rust-slab-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2257 | [rust-smallvec-1/rust-smallvec-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-smallvec-1/rust-smallvec-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2258 | [rust-smawk-0.3/rust-smawk-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-smawk-0.3/rust-smawk-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2259 | [rust-smol-str-0.2/rust-smol-str-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-smol-str-0.2/rust-smol-str-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2260 | [rust-snapbox-macros-1/rust-snapbox-macros-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-snapbox-macros-1/rust-snapbox-macros-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2261 | [rust-spin-0.10/rust-spin-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-spin-0.10/rust-spin-0.10.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2262 | [rust-spin-0.9/rust-spin-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-spin-0.9/rust-spin-0.9.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2263 | [rust-ssh-encoding-0.2/rust-ssh-encoding-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ssh-encoding-0.2/rust-ssh-encoding-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2264 | [rust-stable-deref-trait-1/rust-stable-deref-trait-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-stable-deref-trait-1/rust-stable-deref-trait-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2265 | [rust-static-assertions-1/rust-static-assertions-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-static-assertions-1/rust-static-assertions-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2266 | [rust-str-stack-0.1/rust-str-stack-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-str-stack-0.1/rust-str-stack-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2267 | [rust-strict-num-0.1/rust-strict-num-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-strict-num-0.1/rust-strict-num-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2268 | [rust-stringmetrics-2/rust-stringmetrics-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-stringmetrics-2/rust-stringmetrics-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2269 | [rust-strsim-0.11/rust-strsim-0.11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-strsim-0.11/rust-strsim-0.11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2270 | [rust-strum-0.27/rust-strum-0.27.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-strum-0.27/rust-strum-0.27.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2271 | [rust-strum-0.28/rust-strum-0.28.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-strum-0.28/rust-strum-0.28.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2272 | [rust-supports-hyperlinks-3/rust-supports-hyperlinks-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-supports-hyperlinks-3/rust-supports-hyperlinks-3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2273 | [rust-supports-unicode-3/rust-supports-unicode-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-supports-unicode-3/rust-supports-unicode-3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2274 | [rust-symlink-0.1/rust-symlink-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-symlink-0.1/rust-symlink-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2275 | [rust-tap-1/rust-tap-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tap-1/rust-tap-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2276 | [rust-target-lexicon-0.12/rust-target-lexicon-0.12.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-target-lexicon-0.12/rust-target-lexicon-0.12.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2277 | [rust-target-lexicon-0.13/rust-target-lexicon-0.13.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-target-lexicon-0.13/rust-target-lexicon-0.13.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2278 | [rust-target-triple-1/rust-target-triple-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-target-triple-1/rust-target-triple-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2279 | [rust-termtree-0.5/rust-termtree-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-termtree-0.5/rust-termtree-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2280 | [rust-textwrap-0.15/rust-textwrap-0.15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-textwrap-0.15/rust-textwrap-0.15.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2281 | [rust-textwrap-0.16/rust-textwrap-0.16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-textwrap-0.16/rust-textwrap-0.16.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2282 | [rust-thousands-0.2/rust-thousands-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-thousands-0.2/rust-thousands-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2283 | [rust-time-core-0.1/rust-time-core-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-time-core-0.1/rust-time-core-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2284 | [rust-tinyvec-1/rust-tinyvec-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tinyvec-1/rust-tinyvec-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2285 | [rust-tinyvec-macros-0.1/rust-tinyvec-macros-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tinyvec-macros-0.1/rust-tinyvec-macros-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2286 | [rust-toml-datetime-0.6/rust-toml-datetime-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-toml-datetime-0.6/rust-toml-datetime-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2287 | [rust-toml-datetime-0.7/rust-toml-datetime-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-toml-datetime-0.7/rust-toml-datetime-0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2288 | [rust-toml-datetime-1/rust-toml-datetime-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-toml-datetime-1/rust-toml-datetime-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2289 | [rust-toml-write-0.1/rust-toml-write-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-toml-write-0.1/rust-toml-write-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2290 | [rust-toml-writer-1/rust-toml-writer-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-toml-writer-1/rust-toml-writer-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2291 | [rust-tower-layer-0.3/rust-tower-layer-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tower-layer-0.3/rust-tower-layer-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2292 | [rust-tower-service-0.3/rust-tower-service-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tower-service-0.3/rust-tower-service-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2293 | [rust-triomphe-0.1/rust-triomphe-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-triomphe-0.1/rust-triomphe-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2294 | [rust-try-lock-0.2/rust-try-lock-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-try-lock-0.2/rust-try-lock-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2295 | [rust-ttf-parser-0.25/rust-ttf-parser-0.25.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ttf-parser-0.25/rust-ttf-parser-0.25.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2296 | [rust-twox-hash-2/rust-twox-hash-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-twox-hash-2/rust-twox-hash-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2297 | [rust-typed-path-0.12/rust-typed-path-0.12.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-typed-path-0.12/rust-typed-path-0.12.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2298 | [rust-typeid-1/rust-typeid-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-typeid-1/rust-typeid-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2299 | [rust-typenum-1/rust-typenum-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-typenum-1/rust-typenum-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2300 | [rust-typewit-1/rust-typewit-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-typewit-1/rust-typewit-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2301 | [rust-ucd-trie-0.1/rust-ucd-trie-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ucd-trie-0.1/rust-ucd-trie-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2302 | [rust-ucd-util-0.1/rust-ucd-util-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ucd-util-0.1/rust-ucd-util-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2303 | [rust-unarray-0.1/rust-unarray-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unarray-0.1/rust-unarray-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2304 | [rust-unicase-2/rust-unicase-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicase-2/rust-unicase-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2305 | [rust-unicode-bidi-0.3/rust-unicode-bidi-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-bidi-0.3/rust-unicode-bidi-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2306 | [rust-unicode-bidi-mirroring-0.4/rust-unicode-bidi-mirroring-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-bidi-mirroring-0.4/rust-unicode-bidi-mirroring-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2307 | [rust-unicode-bom-2/rust-unicode-bom-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-bom-2/rust-unicode-bom-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2308 | [rust-unicode-categories-0.1/rust-unicode-categories-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-categories-0.1/rust-unicode-categories-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2309 | [rust-unicode-ccc-0.4/rust-unicode-ccc-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-ccc-0.4/rust-unicode-ccc-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2310 | [rust-unicode-general-category-1/rust-unicode-general-category-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-general-category-1/rust-unicode-general-category-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2311 | [rust-unicode-ident-1/rust-unicode-ident-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-ident-1/rust-unicode-ident-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2312 | [rust-unicode-linebreak-0.1/rust-unicode-linebreak-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-linebreak-0.1/rust-unicode-linebreak-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2313 | [rust-unicode-properties-0.1/rust-unicode-properties-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-properties-0.1/rust-unicode-properties-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2314 | [rust-unicode-script-0.5/rust-unicode-script-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-script-0.5/rust-unicode-script-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2315 | [rust-unicode-segmentation-1/rust-unicode-segmentation-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-segmentation-1/rust-unicode-segmentation-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2316 | [rust-unicode-vo-0.1/rust-unicode-vo-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-vo-0.1/rust-unicode-vo-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2317 | [rust-unicode-width-0.1/rust-unicode-width-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-width-0.1/rust-unicode-width-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2318 | [rust-unicode-width-0.2/rust-unicode-width-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-width-0.2/rust-unicode-width-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2319 | [rust-unicode-xid-0.2/rust-unicode-xid-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unicode-xid-0.2/rust-unicode-xid-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2320 | [rust-unindent-0.2/rust-unindent-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unindent-0.2/rust-unindent-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2321 | [rust-unit-prefix-0.5/rust-unit-prefix-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unit-prefix-0.5/rust-unit-prefix-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2322 | [rust-unsafe-libyaml-0.2/rust-unsafe-libyaml-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unsafe-libyaml-0.2/rust-unsafe-libyaml-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2323 | [rust-unscanny-0.1/rust-unscanny-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unscanny-0.1/rust-unscanny-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2324 | [rust-untrusted-0.9/rust-untrusted-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-untrusted-0.9/rust-untrusted-0.9.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2325 | [rust-unty-0.0.4/rust-unty-0.0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-unty-0.0.4/rust-unty-0.0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2326 | [rust-utf-8-0.7/rust-utf-8-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-utf-8-0.7/rust-utf-8-0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2327 | [rust-utf8-zero-0.8/rust-utf8-zero-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-utf8-zero-0.8/rust-utf8-zero-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2328 | [rust-utf8parse-0.2/rust-utf8parse-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-utf8parse-0.2/rust-utf8parse-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2329 | [rust-uuid-1/rust-uuid-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-uuid-1/rust-uuid-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2330 | [rust-valuable-0.1/rust-valuable-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-valuable-0.1/rust-valuable-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2331 | [rust-value-bag-1/rust-value-bag-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-value-bag-1/rust-value-bag-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2332 | [rust-vcpkg-0.2/rust-vcpkg-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-vcpkg-0.2/rust-vcpkg-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2333 | [rust-version-check-0.9/rust-version-check-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-version-check-0.9/rust-version-check-0.9.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2334 | [rust-vfio-bindings-0.6/rust-vfio-bindings-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-vfio-bindings-0.6/rust-vfio-bindings-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2335 | [rust-virtio-bindings-0.2/rust-virtio-bindings-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-virtio-bindings-0.2/rust-virtio-bindings-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2336 | [rust-virtue-0.0.18/rust-virtue-0.0.18.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-virtue-0.0.18/rust-virtue-0.0.18.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2337 | [rust-vm-fdt-0.3/rust-vm-fdt-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-vm-fdt-0.3/rust-vm-fdt-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2338 | [rust-vsimd-0.8/rust-vsimd-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-vsimd-0.8/rust-vsimd-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2339 | [rust-waker-fn-1/rust-waker-fn-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-waker-fn-1/rust-waker-fn-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2340 | [rust-wasi-0.11/rust-wasi-0.11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-wasi-0.11/rust-wasi-0.11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2341 | [rust-webpki-roots-0.26/rust-webpki-roots-0.26.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-webpki-roots-0.26/rust-webpki-roots-0.26.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2342 | [rust-weezl-0.1/rust-weezl-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-weezl-0.1/rust-weezl-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2343 | [rust-which-8/rust-which-8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-which-8/rust-which-8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2344 | [rust-whoami-2/rust-whoami-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-whoami-2/rust-whoami-2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2345 | [rust-winapi-i686-pc-windows-gnu-0.4/rust-winapi-i686-pc-windows-gnu-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-winapi-i686-pc-windows-gnu-0.4/rust-winapi-i686-pc-windows-gnu-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2346 | [rust-winapi-x86-64-pc-windows-gnu-0.4/rust-winapi-x86-64-pc-windows-gnu-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-winapi-x86-64-pc-windows-gnu-0.4/rust-winapi-x86-64-pc-windows-gnu-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2347 | [rust-windows-aarch64-gnullvm-0.42/rust-windows-aarch64-gnullvm-0.42.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-aarch64-gnullvm-0.42/rust-windows-aarch64-gnullvm-0.42.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2348 | [rust-windows-aarch64-gnullvm-0.48/rust-windows-aarch64-gnullvm-0.48.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-aarch64-gnullvm-0.48/rust-windows-aarch64-gnullvm-0.48.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2349 | [rust-windows-aarch64-gnullvm-0.52/rust-windows-aarch64-gnullvm-0.52.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-aarch64-gnullvm-0.52/rust-windows-aarch64-gnullvm-0.52.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2350 | [rust-windows-aarch64-gnullvm-0.53/rust-windows-aarch64-gnullvm-0.53.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-aarch64-gnullvm-0.53/rust-windows-aarch64-gnullvm-0.53.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2351 | [rust-windows-aarch64-msvc-0.42/rust-windows-aarch64-msvc-0.42.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-aarch64-msvc-0.42/rust-windows-aarch64-msvc-0.42.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2352 | [rust-windows-aarch64-msvc-0.48/rust-windows-aarch64-msvc-0.48.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-aarch64-msvc-0.48/rust-windows-aarch64-msvc-0.48.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2353 | [rust-windows-aarch64-msvc-0.52/rust-windows-aarch64-msvc-0.52.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-aarch64-msvc-0.52/rust-windows-aarch64-msvc-0.52.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2354 | [rust-windows-aarch64-msvc-0.53/rust-windows-aarch64-msvc-0.53.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-aarch64-msvc-0.53/rust-windows-aarch64-msvc-0.53.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2355 | [rust-windows-i686-gnu-0.42/rust-windows-i686-gnu-0.42.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-i686-gnu-0.42/rust-windows-i686-gnu-0.42.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2356 | [rust-windows-i686-gnu-0.48/rust-windows-i686-gnu-0.48.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-i686-gnu-0.48/rust-windows-i686-gnu-0.48.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2357 | [rust-windows-i686-gnu-0.52/rust-windows-i686-gnu-0.52.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-i686-gnu-0.52/rust-windows-i686-gnu-0.52.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2358 | [rust-windows-i686-gnu-0.53/rust-windows-i686-gnu-0.53.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-i686-gnu-0.53/rust-windows-i686-gnu-0.53.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2359 | [rust-windows-i686-gnullvm-0.52/rust-windows-i686-gnullvm-0.52.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-i686-gnullvm-0.52/rust-windows-i686-gnullvm-0.52.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2360 | [rust-windows-i686-gnullvm-0.53/rust-windows-i686-gnullvm-0.53.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-i686-gnullvm-0.53/rust-windows-i686-gnullvm-0.53.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2361 | [rust-windows-i686-msvc-0.42/rust-windows-i686-msvc-0.42.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-i686-msvc-0.42/rust-windows-i686-msvc-0.42.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2362 | [rust-windows-i686-msvc-0.48/rust-windows-i686-msvc-0.48.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-i686-msvc-0.48/rust-windows-i686-msvc-0.48.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2363 | [rust-windows-i686-msvc-0.52/rust-windows-i686-msvc-0.52.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-i686-msvc-0.52/rust-windows-i686-msvc-0.52.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2364 | [rust-windows-i686-msvc-0.53/rust-windows-i686-msvc-0.53.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-i686-msvc-0.53/rust-windows-i686-msvc-0.53.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2365 | [rust-windows-link-0.1/rust-windows-link-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-link-0.1/rust-windows-link-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2366 | [rust-windows-link-0.2/rust-windows-link-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-link-0.2/rust-windows-link-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2367 | [rust-windows-x86-64-gnu-0.42/rust-windows-x86-64-gnu-0.42.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-x86-64-gnu-0.42/rust-windows-x86-64-gnu-0.42.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2368 | [rust-windows-x86-64-gnu-0.48/rust-windows-x86-64-gnu-0.48.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-x86-64-gnu-0.48/rust-windows-x86-64-gnu-0.48.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2369 | [rust-windows-x86-64-gnu-0.52/rust-windows-x86-64-gnu-0.52.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-x86-64-gnu-0.52/rust-windows-x86-64-gnu-0.52.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2370 | [rust-windows-x86-64-gnu-0.53/rust-windows-x86-64-gnu-0.53.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-x86-64-gnu-0.53/rust-windows-x86-64-gnu-0.53.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2371 | [rust-windows-x86-64-gnullvm-0.42/rust-windows-x86-64-gnullvm-0.42.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-x86-64-gnullvm-0.42/rust-windows-x86-64-gnullvm-0.42.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2372 | [rust-windows-x86-64-gnullvm-0.48/rust-windows-x86-64-gnullvm-0.48.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-x86-64-gnullvm-0.48/rust-windows-x86-64-gnullvm-0.48.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2373 | [rust-windows-x86-64-gnullvm-0.52/rust-windows-x86-64-gnullvm-0.52.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-x86-64-gnullvm-0.52/rust-windows-x86-64-gnullvm-0.52.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2374 | [rust-windows-x86-64-gnullvm-0.53/rust-windows-x86-64-gnullvm-0.53.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-x86-64-gnullvm-0.53/rust-windows-x86-64-gnullvm-0.53.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2375 | [rust-windows-x86-64-msvc-0.42/rust-windows-x86-64-msvc-0.42.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-x86-64-msvc-0.42/rust-windows-x86-64-msvc-0.42.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2376 | [rust-windows-x86-64-msvc-0.48/rust-windows-x86-64-msvc-0.48.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-x86-64-msvc-0.48/rust-windows-x86-64-msvc-0.48.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2377 | [rust-windows-x86-64-msvc-0.52/rust-windows-x86-64-msvc-0.52.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-x86-64-msvc-0.52/rust-windows-x86-64-msvc-0.52.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2378 | [rust-windows-x86-64-msvc-0.53/rust-windows-x86-64-msvc-0.53.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-windows-x86-64-msvc-0.53/rust-windows-x86-64-msvc-0.53.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2379 | [rust-winnow-0.5/rust-winnow-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-winnow-0.5/rust-winnow-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2380 | [rust-winnow-0.7/rust-winnow-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-winnow-0.7/rust-winnow-0.7.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2381 | [rust-winnow-1/rust-winnow-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-winnow-1/rust-winnow-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2382 | [rust-winsafe-0.0.19/rust-winsafe-0.0.19.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-winsafe-0.0.19/rust-winsafe-0.0.19.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2383 | [rust-wit-bindgen-0.51/rust-wit-bindgen-0.51.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-wit-bindgen-0.51/rust-wit-bindgen-0.51.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2384 | [rust-wit-bindgen-0.57/rust-wit-bindgen-0.57.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-wit-bindgen-0.57/rust-wit-bindgen-0.57.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2385 | [rust-writeable-0.6/rust-writeable-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-writeable-0.6/rust-writeable-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2386 | [rust-x11rb-protocol-0.13/rust-x11rb-protocol-0.13.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-x11rb-protocol-0.13/rust-x11rb-protocol-0.13.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2387 | [rust-xcursor-0.3/rust-xcursor-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-xcursor-0.3/rust-xcursor-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2388 | [rust-xkeysym-0.2/rust-xkeysym-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-xkeysym-0.2/rust-xkeysym-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2389 | [rust-xmlwriter-0.1/rust-xmlwriter-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-xmlwriter-0.1/rust-xmlwriter-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2390 | [rust-xshell-macros-0.2/rust-xshell-macros-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-xshell-macros-0.2/rust-xshell-macros-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2391 | [rust-xxhash-rust-0.8/rust-xxhash-rust-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-xxhash-rust-0.8/rust-xxhash-rust-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2392 | [rust-y4m-0.8/rust-y4m-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-y4m-0.8/rust-y4m-0.8.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2393 | [rust-yada-0.5/rust-yada-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-yada-0.5/rust-yada-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2394 | [rust-yansi-1/rust-yansi-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-yansi-1/rust-yansi-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2395 | [rust-yasna-0.5/rust-yasna-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-yasna-0.5/rust-yasna-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2396 | [rust-yazi-0.2/rust-yazi-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-yazi-0.2/rust-yazi-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2397 | [rust-yazi-prebuilt-0.1/rust-yazi-prebuilt-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-yazi-prebuilt-0.1/rust-yazi-prebuilt-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2398 | [rust-zeno-0.3/rust-zeno-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-zeno-0.3/rust-zeno-0.3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2399 | [rust-zerofrom-0.1/rust-zerofrom-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-zerofrom-0.1/rust-zerofrom-0.1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2400 | [rust-zeroize-1/rust-zeroize-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-zeroize-1/rust-zeroize-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2401 | [rust-zlib-rs-0.6/rust-zlib-rs-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-zlib-rs-0.6/rust-zlib-rs-0.6.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2402 | [rust-zmij-1/rust-zmij-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-zmij-1/rust-zmij-1.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2403 | [rust-zune-core-0.4/rust-zune-core-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-zune-core-0.4/rust-zune-core-0.4.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2404 | [rust-zune-core-0.5/rust-zune-core-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-zune-core-0.5/rust-zune-core-0.5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2405 | [rust-zune-inflate-0.2/rust-zune-inflate-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-zune-inflate-0.2/rust-zune-inflate-0.2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2406 | [rustup/rustup.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rustup/rustup.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2407 | [safeint/safeint.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/safeint/safeint.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2408 | [samurai/samurai.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/samurai/samurai.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2409 | [sassc/sassc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sassc/sassc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2410 | [sbsigntools/sbsigntools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sbsigntools/sbsigntools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2411 | [sccache/sccache.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sccache/sccache.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2412 | [scdoc/scdoc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/scdoc/scdoc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2413 | [scons/scons.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/scons/scons.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2414 | [sdbus-cpp/sdbus-cpp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sdbus-cpp/sdbus-cpp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2415 | [sddm-kcm/sddm-kcm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sddm-kcm/sddm-kcm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2416 | [SDL2/SDL2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/SDL2/SDL2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2417 | [SDL3/SDL3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/SDL3/SDL3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2418 | [seastar/seastar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/seastar/seastar.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2419 | [seatd/seatd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/seatd/seatd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2420 | [sed/sed.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sed/sed.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2421 | [serf/serf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/serf/serf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2422 | [sg3_utils/sg3_utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sg3_utils/sg3_utils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2423 | [shaderc/shaderc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/shaderc/shaderc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2424 | [shared-mime-info/shared-mime-info.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/shared-mime-info/shared-mime-info.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2425 | [sharutils/sharutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sharutils/sharutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2426 | [shim/shim.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/shim/shim.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2427 | [signon-kwallet-extension/signon-kwallet-extension.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/signon-kwallet-extension/signon-kwallet-extension.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2428 | [signon-plugin-oauth2/signon-plugin-oauth2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/signon-plugin-oauth2/signon-plugin-oauth2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2429 | [simdjson/simdjson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/simdjson/simdjson.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2430 | [simdutf/simdutf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/simdutf/simdutf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2431 | [skalibs/skalibs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/skalibs/skalibs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2432 | [slang/slang.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/slang/slang.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2433 | [sleef/sleef.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sleef/sleef.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2434 | [slibtool/slibtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/slibtool/slibtool.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2435 | [slurp/slurp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/slurp/slurp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2436 | [smartmontools/smartmontools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/smartmontools/smartmontools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2437 | [snappy/snappy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/snappy/snappy.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2438 | [socat/socat.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/socat/socat.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2439 | [socket_wrapper/socket_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/socket_wrapper/socket_wrapper.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2440 | [source-highlight/source-highlight.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/source-highlight/source-highlight.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2441 | [soxr/soxr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/soxr/soxr.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2442 | [sparse/sparse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sparse/sparse.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2443 | [spdlog/spdlog.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/spdlog/spdlog.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2444 | [speex/speex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/speex/speex.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2445 | [speexdsp/speexdsp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/speexdsp/speexdsp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2446 | [spirv-cross/spirv-cross.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/spirv-cross/spirv-cross.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2447 | [spirv-headers/spirv-headers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/spirv-headers/spirv-headers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2448 | [spirv-llvm-translator/spirv-llvm-translator.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/spirv-llvm-translator/spirv-llvm-translator.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2449 | [spirv-tools/spirv-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/spirv-tools/spirv-tools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2450 | [sqlcipher/sqlcipher.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sqlcipher/sqlcipher.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2451 | [sqlite/sqlite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sqlite/sqlite.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2452 | [squashfs-tools/squashfs-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/squashfs-tools/squashfs-tools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2453 | [squashfs-tools-ng/squashfs-tools-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/squashfs-tools-ng/squashfs-tools-ng.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2454 | [squashfuse/squashfuse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/squashfuse/squashfuse.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2455 | [srt/srt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/srt/srt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2456 | [sscg/sscg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sscg/sscg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2457 | [sshpass/sshpass.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sshpass/sshpass.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2458 | [sssd/sssd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sssd/sssd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2459 | [sst-ctl/sst-ctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sst-ctl/sst-ctl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2460 | [strace/strace.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/strace/strace.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2461 | [stress-ng/stress-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/stress-ng/stress-ng.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2462 | [strongswan/strongswan.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/strongswan/strongswan.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2463 | [swaybg/swaybg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/swaybg/swaybg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2464 | [swayidle/swayidle.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/swayidle/swayidle.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2465 | [swaylock/swaylock.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/swaylock/swaylock.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2466 | [swig/swig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/swig/swig.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2467 | [sysbench/sysbench.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sysbench/sysbench.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2468 | [sysfsutils/sysfsutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sysfsutils/sysfsutils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2469 | [sysrepo/sysrepo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sysrepo/sysrepo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2470 | [taglib/taglib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/taglib/taglib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2471 | [talloc/talloc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/talloc/talloc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2472 | [tar/tar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tar/tar.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2473 | [tbb/tbb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tbb/tbb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2474 | [tclap/tclap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tclap/tclap.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2475 | [tcpdump/tcpdump.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tcpdump/tcpdump.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2476 | [tcsh/tcsh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tcsh/tcsh.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2477 | [tensorpipe/tensorpipe.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tensorpipe/tensorpipe.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2478 | [tevent/tevent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tevent/tevent.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2479 | [tftp/tftp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tftp/tftp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2480 | [thrift/thrift.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/thrift/thrift.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2481 | [tidy-html5/tidy-html5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tidy-html5/tidy-html5.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2482 | [tini/tini.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tini/tini.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2483 | [tinysparql/tinysparql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tinysparql/tinysparql.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2484 | [tinyxml2/tinyxml2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tinyxml2/tinyxml2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2485 | [tllist/tllist.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tllist/tllist.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2486 | [tmux/tmux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tmux/tmux.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2487 | [toml11/toml11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/toml11/toml11.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2488 | [tpm2-tss/tpm2-tss.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tpm2-tss/tpm2-tss.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2489 | [tre/tre.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tre/tre.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2490 | [tree/tree.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tree/tree.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2491 | [ttfautohint/ttfautohint.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ttfautohint/ttfautohint.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2492 | [twolame/twolame.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/twolame/twolame.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2493 | [uchardet/uchardet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uchardet/uchardet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2494 | [uid_wrapper/uid_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uid_wrapper/uid_wrapper.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2495 | [ulogd/ulogd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ulogd/ulogd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2496 | [umoci/umoci.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/umoci/umoci.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2497 | [unicorn/unicorn.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unicorn/unicorn.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2498 | [universal-ctags/universal-ctags.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/universal-ctags/universal-ctags.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2499 | [unixbench/unixbench.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unixbench/unixbench.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2500 | [unixODBC/unixODBC.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unixODBC/unixODBC.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2501 | [unrar-free/unrar-free.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unrar-free/unrar-free.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2502 | [upower/upower.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/upower/upower.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2503 | [userspace-rcu/userspace-rcu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/userspace-rcu/userspace-rcu.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2504 | [utf8cpp/utf8cpp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/utf8cpp/utf8cpp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2505 | [utf8proc/utf8proc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/utf8proc/utf8proc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2506 | [util-macros/util-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/util-macros/util-macros.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2507 | [vala/vala.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vala/vala.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2508 | [valgrind/valgrind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/valgrind/valgrind.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2509 | [vapoursynth/vapoursynth.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vapoursynth/vapoursynth.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2510 | [vdo/vdo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vdo/vdo.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2511 | [vid.stab/vid.stab.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vid.stab/vid.stab.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2512 | [vim/vim.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vim/vim.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2513 | [virtiofsd/virtiofsd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/virtiofsd/virtiofsd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2514 | [vlc/vlc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vlc/vlc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2515 | [vmaf/vmaf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vmaf/vmaf.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2516 | [volume_key/volume_key.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/volume_key/volume_key.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2517 | [vorbis-tools/vorbis-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vorbis-tools/vorbis-tools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2518 | [vte/vte.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vte/vte.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2519 | [vulkan-headers/vulkan-headers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vulkan-headers/vulkan-headers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2520 | [vulkan-loader/vulkan-loader.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vulkan-loader/vulkan-loader.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2521 | [vulkan-utility-libraries/vulkan-utility-libraries.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vulkan-utility-libraries/vulkan-utility-libraries.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2522 | [vulkan-validation-layers/vulkan-validation-layers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vulkan-validation-layers/vulkan-validation-layers.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2523 | [wabt/wabt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wabt/wabt.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2524 | [warp-ctc/warp-ctc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/warp-ctc/warp-ctc.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2525 | [warp-transducer/warp-transducer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/warp-transducer/warp-transducer.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2526 | [wavpack/wavpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wavpack/wavpack.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2527 | [waybar/waybar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/waybar/waybar.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2528 | [wayland/wayland.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wayland/wayland.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2529 | [wayland-protocols/wayland-protocols.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wayland-protocols/wayland-protocols.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2530 | [wayland-utils/wayland-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wayland-utils/wayland-utils.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2531 | [wiiuse/wiiuse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wiiuse/wiiuse.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2532 | [wireguard-tools/wireguard-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wireguard-tools/wireguard-tools.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2533 | [wl-clipboard/wl-clipboard.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wl-clipboard/wl-clipboard.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2534 | [wlogout/wlogout.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wlogout/wlogout.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2535 | [wlroots/wlroots.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wlroots/wlroots.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2536 | [wlroots-0.19/wlroots-0.19.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wlroots-0.19/wlroots-0.19.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2537 | [woff2/woff2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/woff2/woff2.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2538 | [wofi/wofi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wofi/wofi.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2539 | [wolfssl/wolfssl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wolfssl/wolfssl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2540 | [wpa_supplicant/wpa_supplicant.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wpa_supplicant/wpa_supplicant.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2541 | [wtmpdb/wtmpdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wtmpdb/wtmpdb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2542 | [xapian/xapian.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xapian/xapian.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2543 | [xauth/xauth.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xauth/xauth.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2544 | [xcb-imdkit/xcb-imdkit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-imdkit/xcb-imdkit.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2545 | [xcb-proto/xcb-proto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-proto/xcb-proto.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2546 | [xcb-util/xcb-util.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-util/xcb-util.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2547 | [xcb-util-cursor/xcb-util-cursor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-util-cursor/xcb-util-cursor.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2548 | [xcb-util-image/xcb-util-image.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-util-image/xcb-util-image.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2549 | [xcb-util-keysyms/xcb-util-keysyms.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-util-keysyms/xcb-util-keysyms.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2550 | [xcb-util-renderutil/xcb-util-renderutil.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-util-renderutil/xcb-util-renderutil.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2551 | [xcb-util-wm/xcb-util-wm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-util-wm/xcb-util-wm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2552 | [xcb-util-xrm/xcb-util-xrm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-util-xrm/xcb-util-xrm.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2553 | [xcursor-themes/xcursor-themes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcursor-themes/xcursor-themes.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2554 | [xcursorgen/xcursorgen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcursorgen/xcursorgen.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2555 | [xdg-user-dirs/xdg-user-dirs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xdg-user-dirs/xdg-user-dirs.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2556 | [xerces-c/xerces-c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xerces-c/xerces-c.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2557 | [xevd/xevd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xevd/xevd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2558 | [xeve/xeve.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xeve/xeve.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2559 | [xinetd/xinetd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xinetd/xinetd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2560 | [xkbcomp/xkbcomp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xkbcomp/xkbcomp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2561 | [xkeyboard-config/xkeyboard-config.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xkeyboard-config/xkeyboard-config.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2562 | [xmlsec/xmlsec.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xmlsec/xmlsec.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2563 | [xmlstarlet/xmlstarlet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xmlstarlet/xmlstarlet.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2564 | [xnnpack/xnnpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xnnpack/xnnpack.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2565 | [xorg-server/xorg-server.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xorg-server/xorg-server.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2566 | [xorgproto/xorgproto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xorgproto/xorgproto.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2567 | [xrdb/xrdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xrdb/xrdb.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2568 | [xsimd/xsimd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xsimd/xsimd.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2569 | [xtrans/xtrans.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xtrans/xtrans.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2570 | [xxhash/xxhash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xxhash/xxhash.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2571 | [xz/xz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xz/xz.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2572 | [yajl/yajl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/yajl/yajl.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2573 | [yaml-cpp/yaml-cpp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/yaml-cpp/yaml-cpp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2574 | [yarpgen/yarpgen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/yarpgen/yarpgen.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2575 | [z3/z3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/z3/z3.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2576 | [zchunk/zchunk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zchunk/zchunk.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2577 | [zeromq/zeromq.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zeromq/zeromq.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2578 | [zfp/zfp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zfp/zfp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2579 | [zimg/zimg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zimg/zimg.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2580 | [zlib-ng/zlib-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zlib-ng/zlib-ng.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2581 | [zsh/zsh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zsh/zsh.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2582 | [zxing-cpp/zxing-cpp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zxing-cpp/zxing-cpp.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2583 | [zziplib/zziplib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zziplib/zziplib.spec) | `Requires` | 缺少必填字段：`Requires` |
| 2584 | [autossh/autossh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/autossh/autossh.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2585 | [chrony/chrony.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/chrony/chrony.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2586 | [docbook2x/docbook2x.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook2x/docbook2x.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2587 | [help2man/help2man.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/help2man/help2man.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2588 | [intltool/intltool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/intltool/intltool.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2589 | [libkcapi/libkcapi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libkcapi/libkcapi.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2590 | [libotf/libotf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libotf/libotf.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2591 | [lmbench/lmbench.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lmbench/lmbench.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2592 | [openjade/openjade.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openjade/openjade.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2593 | [opensp/opensp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/opensp/opensp.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2594 | [perl-Alien-Build/perl-Alien-Build.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Alien-Build/perl-Alien-Build.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2595 | [perl-Alien-cmake3/perl-Alien-cmake3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Alien-cmake3/perl-Alien-cmake3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2596 | [perl-Alien-Libxml2/perl-Alien-Libxml2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Alien-Libxml2/perl-Alien-Libxml2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2597 | [perl-AnyEvent-I3/perl-AnyEvent-I3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-AnyEvent-I3/perl-AnyEvent-I3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2598 | [perl-Archive-Tar/perl-Archive-Tar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Archive-Tar/perl-Archive-Tar.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2599 | [perl-Archive-Zip/perl-Archive-Zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Archive-Zip/perl-Archive-Zip.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2600 | [perl-autodie/perl-autodie.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-autodie/perl-autodie.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2601 | [perl-B-Hooks-EndOfScope/perl-B-Hooks-EndOfScope.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-B-Hooks-EndOfScope/perl-B-Hooks-EndOfScope.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2602 | [perl-bignum/perl-bignum.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-bignum/perl-bignum.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2603 | [perl-Business-ISMN/perl-Business-ISMN.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Business-ISMN/perl-Business-ISMN.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2604 | [perl-Cache-Cache/perl-Cache-Cache.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Cache-Cache/perl-Cache-Cache.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2605 | [perl-Carp-Assert/perl-Carp-Assert.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Carp-Assert/perl-Carp-Assert.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2606 | [perl-CHI/perl-CHI.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-CHI/perl-CHI.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2607 | [perl-Class-Inspector/perl-Class-Inspector.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Class-Inspector/perl-Class-Inspector.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2608 | [perl-Class-Load/perl-Class-Load.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Class-Load/perl-Class-Load.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2609 | [perl-Config-AutoConf/perl-Config-AutoConf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Config-AutoConf/perl-Config-AutoConf.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2610 | [perl-Config-IniFiles/perl-Config-IniFiles.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Config-IniFiles/perl-Config-IniFiles.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2611 | [perl-Config-Tiny/perl-Config-Tiny.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Config-Tiny/perl-Config-Tiny.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2612 | [perl-CPAN-Meta/perl-CPAN-Meta.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-CPAN-Meta/perl-CPAN-Meta.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2613 | [perl-CPAN-Meta-Check/perl-CPAN-Meta-Check.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-CPAN-Meta-Check/perl-CPAN-Meta-Check.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2614 | [perl-CPAN-Meta-Requirements/perl-CPAN-Meta-Requirements.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-CPAN-Meta-Requirements/perl-CPAN-Meta-Requirements.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2615 | [perl-Crypt-URandom/perl-Crypt-URandom.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Crypt-URandom/perl-Crypt-URandom.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2616 | [perl-Data-Compare/perl-Data-Compare.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Data-Compare/perl-Data-Compare.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2617 | [perl-Data-OptList/perl-Data-OptList.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Data-OptList/perl-Data-OptList.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2618 | [perl-DateTime/perl-DateTime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DateTime/perl-DateTime.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2619 | [perl-DateTime-Calendar-Julian/perl-DateTime-Calendar-Julian.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DateTime-Calendar-Julian/perl-DateTime-Calendar-Julian.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2620 | [perl-DateTime-Format-Builder/perl-DateTime-Format-Builder.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DateTime-Format-Builder/perl-DateTime-Format-Builder.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2621 | [perl-DateTime-Format-Strptime/perl-DateTime-Format-Strptime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DateTime-Format-Strptime/perl-DateTime-Format-Strptime.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2622 | [perl-DateTime-Locale/perl-DateTime-Locale.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DateTime-Locale/perl-DateTime-Locale.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2623 | [perl-DateTime-TimeZone/perl-DateTime-TimeZone.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DateTime-TimeZone/perl-DateTime-TimeZone.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2624 | [perl-DateTime-TimeZone-Tzfile/perl-DateTime-TimeZone-Tzfile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DateTime-TimeZone-Tzfile/perl-DateTime-TimeZone-Tzfile.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2625 | [perl-DBD-CSV/perl-DBD-CSV.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DBD-CSV/perl-DBD-CSV.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2626 | [perl-DBD-SQLite/perl-DBD-SQLite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DBD-SQLite/perl-DBD-SQLite.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2627 | [perl-Devel-CallChecker/perl-Devel-CallChecker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Devel-CallChecker/perl-Devel-CallChecker.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2628 | [perl-Devel-Caller/perl-Devel-Caller.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Devel-Caller/perl-Devel-Caller.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2629 | [perl-Devel-CheckLib/perl-Devel-CheckLib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Devel-CheckLib/perl-Devel-CheckLib.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2630 | [perl-Devel-GlobalDestruction/perl-Devel-GlobalDestruction.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Devel-GlobalDestruction/perl-Devel-GlobalDestruction.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2631 | [perl-Devel-Hide/perl-Devel-Hide.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Devel-Hide/perl-Devel-Hide.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2632 | [perl-Devel-LexAlias/perl-Devel-LexAlias.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Devel-LexAlias/perl-Devel-LexAlias.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2633 | [perl-Digest-HMAC/perl-Digest-HMAC.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Digest-HMAC/perl-Digest-HMAC.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2634 | [perl-Digest-MD5/perl-Digest-MD5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Digest-MD5/perl-Digest-MD5.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2635 | [perl-Digest-SHA1/perl-Digest-SHA1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Digest-SHA1/perl-Digest-SHA1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2636 | [perl-Dist-CheckConflicts/perl-Dist-CheckConflicts.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Dist-CheckConflicts/perl-Dist-CheckConflicts.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2637 | [perl-Encode/perl-Encode.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Encode/perl-Encode.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2638 | [perl-Encode-EUCJPASCII/perl-Encode-EUCJPASCII.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Encode-EUCJPASCII/perl-Encode-EUCJPASCII.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2639 | [perl-Encode-HanExtra/perl-Encode-HanExtra.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Encode-HanExtra/perl-Encode-HanExtra.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2640 | [perl-Encode-JIS2K/perl-Encode-JIS2K.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Encode-JIS2K/perl-Encode-JIS2K.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2641 | [perl-Encode-Locale/perl-Encode-Locale.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Encode-Locale/perl-Encode-Locale.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2642 | [perl-Eval-Closure/perl-Eval-Closure.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Eval-Closure/perl-Eval-Closure.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2643 | [perl-Exception-Class/perl-Exception-Class.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Exception-Class/perl-Exception-Class.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2644 | [perl-Exporter/perl-Exporter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Exporter/perl-Exporter.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2645 | [perl-ExtUtils-Depends/perl-ExtUtils-Depends.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-ExtUtils-Depends/perl-ExtUtils-Depends.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2646 | [perl-ExtUtils-Helpers/perl-ExtUtils-Helpers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-ExtUtils-Helpers/perl-ExtUtils-Helpers.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2647 | [perl-ExtUtils-Install/perl-ExtUtils-Install.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-ExtUtils-Install/perl-ExtUtils-Install.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2648 | [perl-ExtUtils-InstallPaths/perl-ExtUtils-InstallPaths.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-ExtUtils-InstallPaths/perl-ExtUtils-InstallPaths.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2649 | [perl-ExtUtils-Manifest/perl-ExtUtils-Manifest.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-ExtUtils-Manifest/perl-ExtUtils-Manifest.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2650 | [perl-ExtUtils-ParseXS/perl-ExtUtils-ParseXS.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-ExtUtils-ParseXS/perl-ExtUtils-ParseXS.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2651 | [perl-FFI-CheckLib/perl-FFI-CheckLib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-FFI-CheckLib/perl-FFI-CheckLib.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2652 | [perl-File-chdir/perl-File-chdir.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-chdir/perl-File-chdir.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2653 | [perl-File-Fetch/perl-File-Fetch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Fetch/perl-File-Fetch.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2654 | [perl-File-Find-Rule/perl-File-Find-Rule.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Find-Rule/perl-File-Find-Rule.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2655 | [perl-File-Find-Rule-Perl/perl-File-Find-Rule-Perl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Find-Rule-Perl/perl-File-Find-Rule-Perl.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2656 | [perl-File-HomeDir/perl-File-HomeDir.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-HomeDir/perl-File-HomeDir.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2657 | [perl-File-Listing/perl-File-Listing.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Listing/perl-File-Listing.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2658 | [perl-File-Remove/perl-File-Remove.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Remove/perl-File-Remove.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2659 | [perl-File-ShareDir/perl-File-ShareDir.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-ShareDir/perl-File-ShareDir.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2660 | [perl-File-Slurp/perl-File-Slurp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Slurp/perl-File-Slurp.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2661 | [perl-File-Slurper/perl-File-Slurper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Slurper/perl-File-Slurper.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2662 | [perl-File-Temp/perl-File-Temp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Temp/perl-File-Temp.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2663 | [perl-Filter/perl-Filter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Filter/perl-Filter.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2664 | [perl-Filter-Simple/perl-Filter-Simple.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Filter-Simple/perl-Filter-Simple.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2665 | [perl-Games-Solitaire-Verify/perl-Games-Solitaire-Verify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Games-Solitaire-Verify/perl-Games-Solitaire-Verify.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2666 | [perl-HTML-Form/perl-HTML-Form.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-HTML-Form/perl-HTML-Form.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2667 | [perl-HTML-Formatter/perl-HTML-Formatter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-HTML-Formatter/perl-HTML-Formatter.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2668 | [perl-HTML-Tree/perl-HTML-Tree.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-HTML-Tree/perl-HTML-Tree.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2669 | [perl-HTTP-CookieJar/perl-HTTP-CookieJar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-HTTP-CookieJar/perl-HTTP-CookieJar.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2670 | [perl-HTTP-Cookies/perl-HTTP-Cookies.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-HTTP-Cookies/perl-HTTP-Cookies.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2671 | [perl-HTTP-Daemon/perl-HTTP-Daemon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-HTTP-Daemon/perl-HTTP-Daemon.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2672 | [perl-HTTP-Date/perl-HTTP-Date.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-HTTP-Date/perl-HTTP-Date.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2673 | [perl-HTTP-Message/perl-HTTP-Message.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-HTTP-Message/perl-HTTP-Message.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2674 | [perl-HTTP-Negotiate/perl-HTTP-Negotiate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-HTTP-Negotiate/perl-HTTP-Negotiate.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2675 | [perl-HTTP-Response-Encoding/perl-HTTP-Response-Encoding.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-HTTP-Response-Encoding/perl-HTTP-Response-Encoding.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2676 | [perl-HTTP-Tiny/perl-HTTP-Tiny.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-HTTP-Tiny/perl-HTTP-Tiny.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2677 | [perl-Inline/perl-Inline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Inline/perl-Inline.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2678 | [perl-Inline-C/perl-Inline-C.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Inline-C/perl-Inline-C.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2679 | [perl-IO-All/perl-IO-All.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IO-All/perl-IO-All.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2680 | [perl-IO-Compress/perl-IO-Compress.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IO-Compress/perl-IO-Compress.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2681 | [perl-IO-Compress-Lzma/perl-IO-Compress-Lzma.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IO-Compress-Lzma/perl-IO-Compress-Lzma.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2682 | [perl-IO-HTML/perl-IO-HTML.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IO-HTML/perl-IO-HTML.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2683 | [perl-IO-Socket-IP/perl-IO-Socket-IP.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IO-Socket-IP/perl-IO-Socket-IP.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2684 | [perl-IO-Socket-SSL/perl-IO-Socket-SSL.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IO-Socket-SSL/perl-IO-Socket-SSL.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2685 | [perl-IO-Stringy/perl-IO-Stringy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IO-Stringy/perl-IO-Stringy.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2686 | [perl-IPC-Cmd/perl-IPC-Cmd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IPC-Cmd/perl-IPC-Cmd.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2687 | [perl-IPC-Run/perl-IPC-Run.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IPC-Run/perl-IPC-Run.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2688 | [perl-IPC-Run3/perl-IPC-Run3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IPC-Run3/perl-IPC-Run3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2689 | [perl-IPC-SysV/perl-IPC-SysV.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IPC-SysV/perl-IPC-SysV.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2690 | [perl-Jcode/perl-Jcode.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Jcode/perl-Jcode.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2691 | [perl-JSON/perl-JSON.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-JSON/perl-JSON.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2692 | [perl-JSON-PP/perl-JSON-PP.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-JSON-PP/perl-JSON-PP.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2693 | [perl-libintl-perl/perl-libintl-perl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-libintl-perl/perl-libintl-perl.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2694 | [perl-libwww-perl/perl-libwww-perl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-libwww-perl/perl-libwww-perl.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2695 | [perl-List-AllUtils/perl-List-AllUtils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-List-AllUtils/perl-List-AllUtils.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2696 | [perl-List-BinarySearch/perl-List-BinarySearch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-List-BinarySearch/perl-List-BinarySearch.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2697 | [perl-List-MoreUtils/perl-List-MoreUtils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-List-MoreUtils/perl-List-MoreUtils.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2698 | [perl-List-MoreUtils-XS/perl-List-MoreUtils-XS.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-List-MoreUtils-XS/perl-List-MoreUtils-XS.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2699 | [perl-List-SomeUtils/perl-List-SomeUtils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-List-SomeUtils/perl-List-SomeUtils.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2700 | [perl-List-UtilsBy/perl-List-UtilsBy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-List-UtilsBy/perl-List-UtilsBy.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2701 | [perl-Locale-Maketext/perl-Locale-Maketext.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Locale-Maketext/perl-Locale-Maketext.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2702 | [perl-Log-Dispatch/perl-Log-Dispatch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Log-Dispatch/perl-Log-Dispatch.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2703 | [perl-Log-Dispatch-FileRotate/perl-Log-Dispatch-FileRotate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Log-Dispatch-FileRotate/perl-Log-Dispatch-FileRotate.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2704 | [perl-Log-Log4perl/perl-Log-Log4perl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Log-Log4perl/perl-Log-Log4perl.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2705 | [perl-LWP-Protocol-https/perl-LWP-Protocol-https.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-LWP-Protocol-https/perl-LWP-Protocol-https.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2706 | [perl-MailTools/perl-MailTools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-MailTools/perl-MailTools.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2707 | [perl-Math-BigInt/perl-Math-BigInt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Math-BigInt/perl-Math-BigInt.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2708 | [perl-Math-BigInt-FastCalc/perl-Math-BigInt-FastCalc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Math-BigInt-FastCalc/perl-Math-BigInt-FastCalc.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2709 | [perl-MLDBM/perl-MLDBM.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-MLDBM/perl-MLDBM.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2710 | [perl-Module-Build/perl-Module-Build.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-Build/perl-Module-Build.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2711 | [perl-Module-Build-Tiny/perl-Module-Build-Tiny.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-Build-Tiny/perl-Module-Build-Tiny.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2712 | [perl-Module-Build-XSUtil/perl-Module-Build-XSUtil.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-Build-XSUtil/perl-Module-Build-XSUtil.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2713 | [perl-Module-CoreList/perl-Module-CoreList.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-CoreList/perl-Module-CoreList.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2714 | [perl-Module-Implementation/perl-Module-Implementation.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-Implementation/perl-Module-Implementation.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2715 | [perl-Module-Install/perl-Module-Install.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-Install/perl-Module-Install.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2716 | [perl-Module-Load-Conditional/perl-Module-Load-Conditional.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-Load-Conditional/perl-Module-Load-Conditional.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2717 | [perl-Module-Mask/perl-Module-Mask.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-Mask/perl-Module-Mask.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2718 | [perl-Module-Metadata/perl-Module-Metadata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-Metadata/perl-Module-Metadata.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2719 | [perl-Module-Pluggable/perl-Module-Pluggable.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-Pluggable/perl-Module-Pluggable.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2720 | [perl-Module-ScanDeps/perl-Module-ScanDeps.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-ScanDeps/perl-Module-ScanDeps.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2721 | [perl-Mojo-DOM58/perl-Mojo-DOM58.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Mojo-DOM58/perl-Mojo-DOM58.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2722 | [perl-Moo/perl-Moo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Moo/perl-Moo.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2723 | [perl-MooX-late/perl-MooX-late.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-MooX-late/perl-MooX-late.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2724 | [perl-MooX-Types-MooseLike/perl-MooX-Types-MooseLike.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-MooX-Types-MooseLike/perl-MooX-Types-MooseLike.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2725 | [perl-MooX-Types-MooseLike-Numeric/perl-MooX-Types-MooseLike-Numeric.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-MooX-Types-MooseLike-Numeric/perl-MooX-Types-MooseLike-Numeric.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2726 | [perl-namespace-autoclean/perl-namespace-autoclean.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-namespace-autoclean/perl-namespace-autoclean.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2727 | [perl-namespace-clean/perl-namespace-clean.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-namespace-clean/perl-namespace-clean.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2728 | [perl-Net-Daemon/perl-Net-Daemon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Net-Daemon/perl-Net-Daemon.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2729 | [perl-Net-SMTP-SSL/perl-Net-SMTP-SSL.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Net-SMTP-SSL/perl-Net-SMTP-SSL.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2730 | [perl-Package-Stash/perl-Package-Stash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Package-Stash/perl-Package-Stash.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2731 | [perl-Params-Classify/perl-Params-Classify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Params-Classify/perl-Params-Classify.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2732 | [perl-Params-Util/perl-Params-Util.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Params-Util/perl-Params-Util.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2733 | [perl-Params-Validate/perl-Params-Validate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Params-Validate/perl-Params-Validate.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2734 | [perl-Params-ValidationCompiler/perl-Params-ValidationCompiler.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Params-ValidationCompiler/perl-Params-ValidationCompiler.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2735 | [perl-Parse-RecDescent/perl-Parse-RecDescent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Parse-RecDescent/perl-Parse-RecDescent.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2736 | [perl-Path-Tiny/perl-Path-Tiny.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Path-Tiny/perl-Path-Tiny.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2737 | [perl-Pegex/perl-Pegex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Pegex/perl-Pegex.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2738 | [perl-Perl-Critic/perl-Perl-Critic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Perl-Critic/perl-Perl-Critic.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2739 | [perl-Perl-MinimumVersion/perl-Perl-MinimumVersion.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Perl-MinimumVersion/perl-Perl-MinimumVersion.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2740 | [perl-Pod-Checker/perl-Pod-Checker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Pod-Checker/perl-Pod-Checker.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2741 | [perl-Pod-Coverage/perl-Pod-Coverage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Pod-Coverage/perl-Pod-Coverage.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2742 | [perl-Pod-Eventual/perl-Pod-Eventual.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Pod-Eventual/perl-Pod-Eventual.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2743 | [perl-Pod-Markdown/perl-Pod-Markdown.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Pod-Markdown/perl-Pod-Markdown.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2744 | [perl-Pod-Parser/perl-Pod-Parser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Pod-Parser/perl-Pod-Parser.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2745 | [perl-Pod-Perldoc/perl-Pod-Perldoc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Pod-Perldoc/perl-Pod-Perldoc.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2746 | [perl-Pod-Simple/perl-Pod-Simple.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Pod-Simple/perl-Pod-Simple.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2747 | [perl-Pod-Spell/perl-Pod-Spell.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Pod-Spell/perl-Pod-Spell.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2748 | [perl-Pod-Usage/perl-Pod-Usage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Pod-Usage/perl-Pod-Usage.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2749 | [perl-PPI/perl-PPI.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-PPI/perl-PPI.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2750 | [perl-PPIx-QuoteLike/perl-PPIx-QuoteLike.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-PPIx-QuoteLike/perl-PPIx-QuoteLike.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2751 | [perl-PPIx-Regexp/perl-PPIx-Regexp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-PPIx-Regexp/perl-PPIx-Regexp.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2752 | [perl-PPIx-Utilities/perl-PPIx-Utilities.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-PPIx-Utilities/perl-PPIx-Utilities.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2753 | [perl-PPIx-Utils/perl-PPIx-Utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-PPIx-Utils/perl-PPIx-Utils.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2754 | [perl-Readonly-XS/perl-Readonly-XS.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Readonly-XS/perl-Readonly-XS.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2755 | [perl-Ref-Util/perl-Ref-Util.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Ref-Util/perl-Ref-Util.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2756 | [perl-Role-Hooks/perl-Role-Hooks.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Role-Hooks/perl-Role-Hooks.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2757 | [perl-Role-Tiny/perl-Role-Tiny.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Role-Tiny/perl-Role-Tiny.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2758 | [perl-Safe-Isa/perl-Safe-Isa.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Safe-Isa/perl-Safe-Isa.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2759 | [perl-Scalar-Properties/perl-Scalar-Properties.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Scalar-Properties/perl-Scalar-Properties.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2760 | [perl-Specio/perl-Specio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Specio/perl-Specio.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2761 | [perl-Spreadsheet-ParseExcel/perl-Spreadsheet-ParseExcel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Spreadsheet-ParseExcel/perl-Spreadsheet-ParseExcel.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2762 | [perl-Spreadsheet-WriteExcel/perl-Spreadsheet-WriteExcel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Spreadsheet-WriteExcel/perl-Spreadsheet-WriteExcel.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2763 | [perl-SQL-Statement/perl-SQL-Statement.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-SQL-Statement/perl-SQL-Statement.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2764 | [perl-String-RewritePrefix/perl-String-RewritePrefix.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-String-RewritePrefix/perl-String-RewritePrefix.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2765 | [perl-Sub-Exporter/perl-Sub-Exporter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Sub-Exporter/perl-Sub-Exporter.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2766 | [perl-Sub-HandlesVia/perl-Sub-HandlesVia.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Sub-HandlesVia/perl-Sub-HandlesVia.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2767 | [perl-Sub-HandlesVia-XS/perl-Sub-HandlesVia-XS.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Sub-HandlesVia-XS/perl-Sub-HandlesVia-XS.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2768 | [perl-Term-Cap/perl-Term-Cap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Term-Cap/perl-Term-Cap.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2769 | [perl-Test-Class/perl-Test-Class.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Class/perl-Test-Class.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2770 | [perl-Test-CPAN-Meta/perl-Test-CPAN-Meta.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-CPAN-Meta/perl-Test-CPAN-Meta.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2771 | [perl-Test-Data-Split/perl-Test-Data-Split.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Data-Split/perl-Test-Data-Split.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2772 | [perl-Test-Deep/perl-Test-Deep.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Deep/perl-Test-Deep.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2773 | [perl-Test-Differences/perl-Test-Differences.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Differences/perl-Test-Differences.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2774 | [perl-Test-Exception/perl-Test-Exception.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Exception/perl-Test-Exception.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2775 | [perl-Test-Fatal/perl-Test-Fatal.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Fatal/perl-Test-Fatal.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2776 | [perl-Test-File-ShareDir/perl-Test-File-ShareDir.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-File-ShareDir/perl-Test-File-ShareDir.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2777 | [perl-Test-Fork/perl-Test-Fork.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Fork/perl-Test-Fork.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2778 | [perl-Test-Harness/perl-Test-Harness.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Harness/perl-Test-Harness.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2779 | [perl-Test-LeakTrace/perl-Test-LeakTrace.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-LeakTrace/perl-Test-LeakTrace.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2780 | [perl-Test-Memory-Cycle/perl-Test-Memory-Cycle.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Memory-Cycle/perl-Test-Memory-Cycle.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2781 | [perl-Test-MinimumVersion/perl-Test-MinimumVersion.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-MinimumVersion/perl-Test-MinimumVersion.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2782 | [perl-Test-NoWarnings/perl-Test-NoWarnings.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-NoWarnings/perl-Test-NoWarnings.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2783 | [perl-Test-Object/perl-Test-Object.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Object/perl-Test-Object.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2784 | [perl-Test-Output/perl-Test-Output.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Output/perl-Test-Output.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2785 | [perl-Test-Pod/perl-Test-Pod.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Pod/perl-Test-Pod.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2786 | [perl-Test-Requires/perl-Test-Requires.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Requires/perl-Test-Requires.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2787 | [perl-Test-RunValgrind/perl-Test-RunValgrind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-RunValgrind/perl-Test-RunValgrind.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2788 | [perl-Test-Simple/perl-Test-Simple.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Simple/perl-Test-Simple.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2789 | [perl-Test-SubCalls/perl-Test-SubCalls.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-SubCalls/perl-Test-SubCalls.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2790 | [perl-Test-TrailingSpace/perl-Test-TrailingSpace.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-TrailingSpace/perl-Test-TrailingSpace.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2791 | [perl-Test-Trap/perl-Test-Trap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Trap/perl-Test-Trap.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2792 | [perl-Test-Warn/perl-Test-Warn.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Warn/perl-Test-Warn.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2793 | [perl-Test2-Plugin-NoWarnings/perl-Test2-Plugin-NoWarnings.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test2-Plugin-NoWarnings/perl-Test2-Plugin-NoWarnings.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2794 | [perl-Text-BibTeX/perl-Text-BibTeX.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Text-BibTeX/perl-Text-BibTeX.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2795 | [perl-Text-CSV/perl-Text-CSV.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Text-CSV/perl-Text-CSV.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2796 | [perl-Text-CSV_XS/perl-Text-CSV_XS.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Text-CSV_XS/perl-Text-CSV_XS.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2797 | [perl-Text-Diff/perl-Text-Diff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Text-Diff/perl-Text-Diff.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2798 | [perl-Thread-Queue/perl-Thread-Queue.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Thread-Queue/perl-Thread-Queue.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2799 | [perl-Time-Duration-Parse/perl-Time-Duration-Parse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Time-Duration-Parse/perl-Time-Duration-Parse.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2800 | [perl-Try-Tiny/perl-Try-Tiny.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Try-Tiny/perl-Try-Tiny.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2801 | [perl-Type-Tiny/perl-Type-Tiny.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Type-Tiny/perl-Type-Tiny.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2802 | [perl-URI/perl-URI.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-URI/perl-URI.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2803 | [perl-WWW-Mechanize/perl-WWW-Mechanize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-WWW-Mechanize/perl-WWW-Mechanize.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2804 | [perl-WWW-RobotRules/perl-WWW-RobotRules.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-WWW-RobotRules/perl-WWW-RobotRules.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2805 | [perl-X11-XCB/perl-X11-XCB.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-X11-XCB/perl-X11-XCB.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2806 | [perl-XML-Descent/perl-XML-Descent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-Descent/perl-XML-Descent.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2807 | [perl-XML-DOM/perl-XML-DOM.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-DOM/perl-XML-DOM.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2808 | [perl-XML-LibXML/perl-XML-LibXML.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-LibXML/perl-XML-LibXML.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2809 | [perl-XML-LibXSLT/perl-XML-LibXSLT.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-LibXSLT/perl-XML-LibXSLT.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2810 | [perl-XML-Parser/perl-XML-Parser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-Parser/perl-XML-Parser.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2811 | [perl-XML-SAX/perl-XML-SAX.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-SAX/perl-XML-SAX.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2812 | [perl-XML-SAX-Expat/perl-XML-SAX-Expat.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-SAX-Expat/perl-XML-SAX-Expat.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2813 | [perl-XML-Simple/perl-XML-Simple.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-Simple/perl-XML-Simple.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2814 | [perl-XML-TokeParser/perl-XML-TokeParser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-TokeParser/perl-XML-TokeParser.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2815 | [perl-XML-XPath/perl-XML-XPath.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-XPath/perl-XML-XPath.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2816 | [perl-XXX/perl-XXX.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XXX/perl-XXX.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2817 | [perl-YAML-PP/perl-YAML-PP.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-YAML-PP/perl-YAML-PP.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2818 | [postfix/postfix.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postfix/postfix.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2819 | [python-linux-procfs/python-linux-procfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-linux-procfs/python-linux-procfs.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2820 | [python-mako/python-mako.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mako/python-mako.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2821 | [python-pre-commit/python-pre-commit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pre-commit/python-pre-commit.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2822 | [python-pyqt6/python-pyqt6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyqt6/python-pyqt6.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2823 | [python-pytz/python-pytz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytz/python-pytz.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2824 | [python-pyudev/python-pyudev.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyudev/python-pyudev.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2825 | [rust-ansi-to-tui-8/rust-ansi-to-tui-8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ansi-to-tui-8/rust-ansi-to-tui-8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2826 | [rust-avif-serialize-0.8/rust-avif-serialize-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-avif-serialize-0.8/rust-avif-serialize-0.8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2827 | [rust-bindgen-0.69/rust-bindgen-0.69.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bindgen-0.69/rust-bindgen-0.69.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2828 | [rust-bindgen-0.70/rust-bindgen-0.70.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bindgen-0.70/rust-bindgen-0.70.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2829 | [rust-bindgen-0.72/rust-bindgen-0.72.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bindgen-0.72/rust-bindgen-0.72.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2830 | [rust-bitvec-1/rust-bitvec-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bitvec-1/rust-bitvec-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2831 | [rust-bon-3/rust-bon-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bon-3/rust-bon-3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2832 | [rust-bon-macros-3/rust-bon-macros-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bon-macros-3/rust-bon-macros-3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2833 | [rust-borsh-1/rust-borsh-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-borsh-1/rust-borsh-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2834 | [rust-borsh-derive-1/rust-borsh-derive-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-borsh-derive-1/rust-borsh-derive-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2835 | [rust-cairo-rs-0.21/rust-cairo-rs-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cairo-rs-0.21/rust-cairo-rs-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2836 | [rust-cairo-rs-0.22/rust-cairo-rs-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cairo-rs-0.22/rust-cairo-rs-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2837 | [rust-cairo-sys-rs-0.21/rust-cairo-sys-rs-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cairo-sys-rs-0.21/rust-cairo-sys-rs-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2838 | [rust-cairo-sys-rs-0.22/rust-cairo-sys-rs-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cairo-sys-rs-0.22/rust-cairo-sys-rs-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2839 | [rust-cargo-0.91/rust-cargo-0.91.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cargo-0.91/rust-cargo-0.91.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2840 | [rust-cargo-cyclonedx-0.5/rust-cargo-cyclonedx-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cargo-cyclonedx-0.5/rust-cargo-cyclonedx-0.5.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2841 | [rust-cargo-lock-10/rust-cargo-lock-10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cargo-lock-10/rust-cargo-lock-10.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2842 | [rust-charset-0.1/rust-charset-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-charset-0.1/rust-charset-0.1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2843 | [rust-criterion-0.4/rust-criterion-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-criterion-0.4/rust-criterion-0.4.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2844 | [rust-criterion-0.5/rust-criterion-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-criterion-0.5/rust-criterion-0.5.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2845 | [rust-criterion-0.7/rust-criterion-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-criterion-0.7/rust-criterion-0.7.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2846 | [rust-cyclonedx-bom-0.8/rust-cyclonedx-bom-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cyclonedx-bom-0.8/rust-cyclonedx-bom-0.8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2847 | [rust-cyclonedx-bom-macros-0.1/rust-cyclonedx-bom-macros-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-cyclonedx-bom-macros-0.1/rust-cyclonedx-bom-macros-0.1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2848 | [rust-debugid-0.8/rust-debugid-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-debugid-0.8/rust-debugid-0.8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2849 | [rust-defmt-1/rust-defmt-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-defmt-1/rust-defmt-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2850 | [rust-document-features-0.2/rust-document-features-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-document-features-0.2/rust-document-features-0.2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2851 | [rust-encoding-rs-0.8/rust-encoding-rs-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-encoding-rs-0.8/rust-encoding-rs-0.8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2852 | [rust-futures-0.3/rust-futures-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-futures-0.3/rust-futures-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2853 | [rust-futures-channel-0.3/rust-futures-channel-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-futures-channel-0.3/rust-futures-channel-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2854 | [rust-futures-executor-0.3/rust-futures-executor-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-futures-executor-0.3/rust-futures-executor-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2855 | [rust-futures-macro-0.3/rust-futures-macro-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-futures-macro-0.3/rust-futures-macro-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2856 | [rust-futures-util-0.3/rust-futures-util-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-futures-util-0.3/rust-futures-util-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2857 | [rust-gdk-pixbuf-0.21/rust-gdk-pixbuf-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gdk-pixbuf-0.21/rust-gdk-pixbuf-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2858 | [rust-gdk-pixbuf-0.22/rust-gdk-pixbuf-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gdk-pixbuf-0.22/rust-gdk-pixbuf-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2859 | [rust-gdk-pixbuf-sys-0.21/rust-gdk-pixbuf-sys-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gdk-pixbuf-sys-0.21/rust-gdk-pixbuf-sys-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2860 | [rust-gdk-pixbuf-sys-0.22/rust-gdk-pixbuf-sys-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gdk-pixbuf-sys-0.22/rust-gdk-pixbuf-sys-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2861 | [rust-gdk4-0.10/rust-gdk4-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gdk4-0.10/rust-gdk4-0.10.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2862 | [rust-gdk4-0.11/rust-gdk4-0.11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gdk4-0.11/rust-gdk4-0.11.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2863 | [rust-gdk4-sys-0.10/rust-gdk4-sys-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gdk4-sys-0.10/rust-gdk4-sys-0.10.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2864 | [rust-gdk4-sys-0.11/rust-gdk4-sys-0.11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gdk4-sys-0.11/rust-gdk4-sys-0.11.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2865 | [rust-gif-dispose-5/rust-gif-dispose-5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gif-dispose-5/rust-gif-dispose-5.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2866 | [rust-gifski-1/rust-gifski-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gifski-1/rust-gifski-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2867 | [rust-gio-0.21/rust-gio-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gio-0.21/rust-gio-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2868 | [rust-gio-0.22/rust-gio-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gio-0.22/rust-gio-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2869 | [rust-gio-sys-0.21/rust-gio-sys-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gio-sys-0.21/rust-gio-sys-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2870 | [rust-gio-sys-0.22/rust-gio-sys-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gio-sys-0.22/rust-gio-sys-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2871 | [rust-gio-unix-0.22/rust-gio-unix-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gio-unix-0.22/rust-gio-unix-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2872 | [rust-gio-unix-sys-0.22/rust-gio-unix-sys-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gio-unix-sys-0.22/rust-gio-unix-sys-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2873 | [rust-gio-win32-0.22/rust-gio-win32-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gio-win32-0.22/rust-gio-win32-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2874 | [rust-gio-win32-sys-0.22/rust-gio-win32-sys-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gio-win32-sys-0.22/rust-gio-win32-sys-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2875 | [rust-glib-0.21/rust-glib-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glib-0.21/rust-glib-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2876 | [rust-glib-0.22/rust-glib-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glib-0.22/rust-glib-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2877 | [rust-glib-macros-0.21/rust-glib-macros-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glib-macros-0.21/rust-glib-macros-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2878 | [rust-glib-macros-0.22/rust-glib-macros-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glib-macros-0.22/rust-glib-macros-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2879 | [rust-glib-sys-0.21/rust-glib-sys-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glib-sys-0.21/rust-glib-sys-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2880 | [rust-glib-sys-0.22/rust-glib-sys-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-glib-sys-0.22/rust-glib-sys-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2881 | [rust-gobject-sys-0.21/rust-gobject-sys-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gobject-sys-0.21/rust-gobject-sys-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2882 | [rust-gobject-sys-0.22/rust-gobject-sys-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gobject-sys-0.22/rust-gobject-sys-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2883 | [rust-graphene-rs-0.21/rust-graphene-rs-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-graphene-rs-0.21/rust-graphene-rs-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2884 | [rust-graphene-rs-0.22/rust-graphene-rs-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-graphene-rs-0.22/rust-graphene-rs-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2885 | [rust-graphene-sys-0.21/rust-graphene-sys-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-graphene-sys-0.21/rust-graphene-sys-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2886 | [rust-graphene-sys-0.22/rust-graphene-sys-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-graphene-sys-0.22/rust-graphene-sys-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2887 | [rust-gsk4-0.10/rust-gsk4-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gsk4-0.10/rust-gsk4-0.10.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2888 | [rust-gsk4-0.11/rust-gsk4-0.11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gsk4-0.11/rust-gsk4-0.11.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2889 | [rust-gsk4-sys-0.10/rust-gsk4-sys-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gsk4-sys-0.10/rust-gsk4-sys-0.10.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2890 | [rust-gsk4-sys-0.11/rust-gsk4-sys-0.11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gsk4-sys-0.11/rust-gsk4-sys-0.11.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2891 | [rust-gtk4-0.10/rust-gtk4-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gtk4-0.10/rust-gtk4-0.10.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2892 | [rust-gtk4-0.11/rust-gtk4-0.11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gtk4-0.11/rust-gtk4-0.11.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2893 | [rust-gtk4-macros-0.10/rust-gtk4-macros-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gtk4-macros-0.10/rust-gtk4-macros-0.10.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2894 | [rust-gtk4-macros-0.11/rust-gtk4-macros-0.11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gtk4-macros-0.11/rust-gtk4-macros-0.11.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2895 | [rust-gtk4-sys-0.10/rust-gtk4-sys-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gtk4-sys-0.10/rust-gtk4-sys-0.10.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2896 | [rust-gtk4-sys-0.11/rust-gtk4-sys-0.11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-gtk4-sys-0.11/rust-gtk4-sys-0.11.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2897 | [rust-headers-0.4/rust-headers-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-headers-0.4/rust-headers-0.4.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2898 | [rust-headers-core-0.3/rust-headers-core-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-headers-core-0.3/rust-headers-core-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2899 | [rust-hickory-client-0.25/rust-hickory-client-0.25.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hickory-client-0.25/rust-hickory-client-0.25.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2900 | [rust-hickory-proto-0.25/rust-hickory-proto-0.25.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hickory-proto-0.25/rust-hickory-proto-0.25.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2901 | [rust-hickory-server-0.25/rust-hickory-server-0.25.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hickory-server-0.25/rust-hickory-server-0.25.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2902 | [rust-hyper-1/rust-hyper-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hyper-1/rust-hyper-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2903 | [rust-hyper-tls-0.6/rust-hyper-tls-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hyper-tls-0.6/rust-hyper-tls-0.6.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2904 | [rust-hyper-util-0.1/rust-hyper-util-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hyper-util-0.1/rust-hyper-util-0.1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2905 | [rust-icu-collections-2/rust-icu-collections-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-icu-collections-2/rust-icu-collections-2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2906 | [rust-icu-locale-core-2/rust-icu-locale-core-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-icu-locale-core-2/rust-icu-locale-core-2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2907 | [rust-icu-normalizer-2/rust-icu-normalizer-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-icu-normalizer-2/rust-icu-normalizer-2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2908 | [rust-icu-properties-2/rust-icu-properties-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-icu-properties-2/rust-icu-properties-2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2909 | [rust-icu-provider-2/rust-icu-provider-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-icu-provider-2/rust-icu-provider-2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2910 | [rust-idna-adapter-1/rust-idna-adapter-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-idna-adapter-1/rust-idna-adapter-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2911 | [rust-im-rc-15/rust-im-rc-15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-im-rc-15/rust-im-rc-15.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2912 | [rust-imagequant-4/rust-imagequant-4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-imagequant-4/rust-imagequant-4.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2913 | [rust-insta-1/rust-insta-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-insta-1/rust-insta-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2914 | [rust-js-sys-0.3/rust-js-sys-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-js-sys-0.3/rust-js-sys-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2915 | [rust-landlock-0.4/rust-landlock-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-landlock-0.4/rust-landlock-0.4.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2916 | [rust-libadwaita-0.8/rust-libadwaita-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-libadwaita-0.8/rust-libadwaita-0.8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2917 | [rust-libadwaita-0.9/rust-libadwaita-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-libadwaita-0.9/rust-libadwaita-0.9.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2918 | [rust-libadwaita-sys-0.8/rust-libadwaita-sys-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-libadwaita-sys-0.8/rust-libadwaita-sys-0.8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2919 | [rust-libadwaita-sys-0.9/rust-libadwaita-sys-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-libadwaita-sys-0.9/rust-libadwaita-sys-0.9.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2920 | [rust-libspa-0.9/rust-libspa-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-libspa-0.9/rust-libspa-0.9.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2921 | [rust-libspa-sys-0.9/rust-libspa-sys-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-libspa-sys-0.9/rust-libspa-sys-0.9.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2922 | [rust-lodepng-3/rust-lodepng-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-lodepng-3/rust-lodepng-3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2923 | [rust-loop9-0.1/rust-loop9-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-loop9-0.1/rust-loop9-0.1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2924 | [rust-macro-rules-attribute-0.2/rust-macro-rules-attribute-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-macro-rules-attribute-0.2/rust-macro-rules-attribute-0.2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2925 | [rust-nalgebra-0.33/rust-nalgebra-0.33.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-nalgebra-0.33/rust-nalgebra-0.33.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2926 | [rust-nalgebra-0.34/rust-nalgebra-0.34.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-nalgebra-0.34/rust-nalgebra-0.34.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2927 | [rust-nalgebra-macros-0.3/rust-nalgebra-macros-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-nalgebra-macros-0.3/rust-nalgebra-macros-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2928 | [rust-native-tls-0.2/rust-native-tls-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-native-tls-0.2/rust-native-tls-0.2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2929 | [rust-openssl-macros-0.1/rust-openssl-macros-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-openssl-macros-0.1/rust-openssl-macros-0.1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2930 | [rust-pango-0.21/rust-pango-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pango-0.21/rust-pango-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2931 | [rust-pango-0.22/rust-pango-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pango-0.22/rust-pango-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2932 | [rust-pango-sys-0.21/rust-pango-sys-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pango-sys-0.21/rust-pango-sys-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2933 | [rust-pango-sys-0.22/rust-pango-sys-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pango-sys-0.22/rust-pango-sys-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2934 | [rust-pangocairo-0.21/rust-pangocairo-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pangocairo-0.21/rust-pangocairo-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2935 | [rust-pangocairo-0.22/rust-pangocairo-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pangocairo-0.22/rust-pangocairo-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2936 | [rust-pangocairo-sys-0.21/rust-pangocairo-sys-0.21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pangocairo-sys-0.21/rust-pangocairo-sys-0.21.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2937 | [rust-pangocairo-sys-0.22/rust-pangocairo-sys-0.22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pangocairo-sys-0.22/rust-pangocairo-sys-0.22.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2938 | [rust-pest-2/rust-pest-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pest-2/rust-pest-2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2939 | [rust-pest-derive-2/rust-pest-derive-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pest-derive-2/rust-pest-derive-2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2940 | [rust-pest-generator-2/rust-pest-generator-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pest-generator-2/rust-pest-generator-2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2941 | [rust-pest-meta-2/rust-pest-meta-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pest-meta-2/rust-pest-meta-2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2942 | [rust-pipewire-0.9/rust-pipewire-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pipewire-0.9/rust-pipewire-0.9.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2943 | [rust-pipewire-sys-0.9/rust-pipewire-sys-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pipewire-sys-0.9/rust-pipewire-sys-0.9.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2944 | [rust-plotters-0.3/rust-plotters-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-plotters-0.3/rust-plotters-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2945 | [rust-plotters-svg-0.3/rust-plotters-svg-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-plotters-svg-0.3/rust-plotters-svg-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2946 | [rust-proptest-1/rust-proptest-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-proptest-1/rust-proptest-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2947 | [rust-proptest-derive-0.8/rust-proptest-derive-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-proptest-derive-0.8/rust-proptest-derive-0.8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2948 | [rust-proptest-macro-0.5/rust-proptest-macro-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-proptest-macro-0.5/rust-proptest-macro-0.5.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2949 | [rust-rand-0.10/rust-rand-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rand-0.10/rust-rand-0.10.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2950 | [rust-rand-0.8/rust-rand-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rand-0.8/rust-rand-0.8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2951 | [rust-rand-0.9/rust-rand-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rand-0.9/rust-rand-0.9.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2952 | [rust-rand-chacha-0.3/rust-rand-chacha-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rand-chacha-0.3/rust-rand-chacha-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2953 | [rust-rand-chacha-0.9/rust-rand-chacha-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rand-chacha-0.9/rust-rand-chacha-0.9.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2954 | [rust-rand-distr-0.6/rust-rand-distr-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rand-distr-0.6/rust-rand-distr-0.6.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2955 | [rust-rand-xorshift-0.3/rust-rand-xorshift-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rand-xorshift-0.3/rust-rand-xorshift-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2956 | [rust-rand-xorshift-0.4/rust-rand-xorshift-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rand-xorshift-0.4/rust-rand-xorshift-0.4.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2957 | [rust-rand-xoshiro-0.6/rust-rand-xoshiro-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rand-xoshiro-0.6/rust-rand-xoshiro-0.6.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2958 | [rust-ratatui-0.30/rust-ratatui-0.30.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ratatui-0.30/rust-ratatui-0.30.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2959 | [rust-ratatui-core-0.1/rust-ratatui-core-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ratatui-core-0.1/rust-ratatui-core-0.1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2960 | [rust-ratatui-crossterm-0.1/rust-ratatui-crossterm-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ratatui-crossterm-0.1/rust-ratatui-crossterm-0.1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2961 | [rust-ratatui-termion-0.1/rust-ratatui-termion-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ratatui-termion-0.1/rust-ratatui-termion-0.1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2962 | [rust-ratatui-termwiz-0.1/rust-ratatui-termwiz-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ratatui-termwiz-0.1/rust-ratatui-termwiz-0.1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2963 | [rust-ratatui-widgets-0.3/rust-ratatui-widgets-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ratatui-widgets-0.3/rust-ratatui-widgets-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2964 | [rust-ravif-0.13/rust-ravif-0.13.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-ravif-0.13/rust-ravif-0.13.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2965 | [rust-redb-3/rust-redb-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-redb-3/rust-redb-3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2966 | [rust-rust-embed-8/rust-rust-embed-8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rust-embed-8/rust-rust-embed-8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2967 | [rust-rust-embed-impl-8/rust-rust-embed-impl-8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rust-embed-impl-8/rust-rust-embed-impl-8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2968 | [rust-rust-embed-utils-8/rust-rust-embed-utils-8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rust-embed-utils-8/rust-rust-embed-utils-8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2969 | [rust-schemars-0.8/rust-schemars-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-schemars-0.8/rust-schemars-0.8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2970 | [rust-schemars-0.9/rust-schemars-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-schemars-0.9/rust-schemars-0.9.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2971 | [rust-schemars-1/rust-schemars-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-schemars-1/rust-schemars-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2972 | [rust-schemars-derive-0.8/rust-schemars-derive-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-schemars-derive-0.8/rust-schemars-derive-0.8.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2973 | [rust-schemars-derive-1/rust-schemars-derive-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-schemars-derive-1/rust-schemars-derive-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2974 | [rust-security-framework-2/rust-security-framework-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-security-framework-2/rust-security-framework-2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2975 | [rust-security-framework-3/rust-security-framework-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-security-framework-3/rust-security-framework-3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2976 | [rust-security-framework-sys-2/rust-security-framework-sys-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-security-framework-sys-2/rust-security-framework-sys-2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2977 | [rust-serde-1/rust-serde-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-serde-1/rust-serde-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2978 | [rust-serde-core-1/rust-serde-core-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-serde-core-1/rust-serde-core-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2979 | [rust-serde-derive-1/rust-serde-derive-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-serde-derive-1/rust-serde-derive-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2980 | [rust-serde-derive-internals-0.29/rust-serde-derive-internals-0.29.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-serde-derive-internals-0.29/rust-serde-derive-internals-0.29.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2981 | [rust-smithay-0.7/rust-smithay-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-smithay-0.7/rust-smithay-0.7.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2982 | [rust-spanned-0.4/rust-spanned-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-spanned-0.4/rust-spanned-0.4.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2983 | [rust-tempfile-3/rust-tempfile-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tempfile-3/rust-tempfile-3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2984 | [rust-time-0.3/rust-time-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-time-0.3/rust-time-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2985 | [rust-tokio-1/rust-tokio-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tokio-1/rust-tokio-1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2986 | [rust-tokio-macros-2/rust-tokio-macros-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tokio-macros-2/rust-tokio-macros-2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2987 | [rust-tokio-native-tls-0.3/rust-tokio-native-tls-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tokio-native-tls-0.3/rust-tokio-native-tls-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2988 | [rust-tokio-stream-0.1/rust-tokio-stream-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tokio-stream-0.1/rust-tokio-stream-0.1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2989 | [rust-tokio-util-0.7/rust-tokio-util-0.7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tokio-util-0.7/rust-tokio-util-0.7.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2990 | [rust-tracing-0.1/rust-tracing-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tracing-0.1/rust-tracing-0.1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2991 | [rust-tracing-appender-0.2/rust-tracing-appender-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tracing-appender-0.2/rust-tracing-appender-0.2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2992 | [rust-tracing-attributes-0.1/rust-tracing-attributes-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tracing-attributes-0.1/rust-tracing-attributes-0.1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2993 | [rust-tracing-error-0.2/rust-tracing-error-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tracing-error-0.2/rust-tracing-error-0.2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2994 | [rust-tracing-log-0.2/rust-tracing-log-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tracing-log-0.2/rust-tracing-log-0.2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2995 | [rust-tracing-serde-0.2/rust-tracing-serde-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tracing-serde-0.2/rust-tracing-serde-0.2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2996 | [rust-tracing-subscriber-0.3/rust-tracing-subscriber-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tracing-subscriber-0.3/rust-tracing-subscriber-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2997 | [rust-wasm-bindgen-0.2/rust-wasm-bindgen-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-wasm-bindgen-0.2/rust-wasm-bindgen-0.2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2998 | [rust-wasm-bindgen-futures-0.4/rust-wasm-bindgen-futures-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-wasm-bindgen-futures-0.4/rust-wasm-bindgen-futures-0.4.spec) | `VCS` | 缺少必填字段：`VCS` |
| 2999 | [rust-wasm-bindgen-macro-0.2/rust-wasm-bindgen-macro-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-wasm-bindgen-macro-0.2/rust-wasm-bindgen-macro-0.2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 3000 | [rust-wasm-bindgen-macro-support-0.2/rust-wasm-bindgen-macro-support-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-wasm-bindgen-macro-support-0.2/rust-wasm-bindgen-macro-support-0.2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 3001 | [rust-wasm-bindgen-shared-0.2/rust-wasm-bindgen-shared-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-wasm-bindgen-shared-0.2/rust-wasm-bindgen-shared-0.2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 3002 | [rust-web-sys-0.3/rust-web-sys-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-web-sys-0.3/rust-web-sys-0.3.spec) | `VCS` | 缺少必填字段：`VCS` |
| 3003 | [rust-wild-2/rust-wild-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-wild-2/rust-wild-2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 3004 | [rust-wyz-0.5/rust-wyz-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-wyz-0.5/rust-wyz-0.5.spec) | `VCS` | 缺少必填字段：`VCS` |
| 3005 | [rust-yuv-0.1/rust-yuv-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-yuv-0.1/rust-yuv-0.1.spec) | `VCS` | 缺少必填字段：`VCS` |
| 3006 | [rust-zerotrie-0.2/rust-zerotrie-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-zerotrie-0.2/rust-zerotrie-0.2.spec) | `VCS` | 缺少必填字段：`VCS` |
| 3007 | [sgml-common/sgml-common.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sgml-common/sgml-common.spec) | `VCS` | 缺少必填字段：`VCS` |
| 3008 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `VCS` | 缺少必填字段：`VCS` |
| 3009 | [acpid/acpid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/acpid/acpid.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3010 | [alsa-lib/alsa-lib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/alsa-lib/alsa-lib.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3011 | [bc/bc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bc/bc.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3012 | [bdfresize/bdfresize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bdfresize/bdfresize.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3013 | [blktrace/blktrace.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/blktrace/blktrace.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3014 | [busybox/busybox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/busybox/busybox.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3015 | [byacc/byacc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/byacc/byacc.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3016 | [bzip2/bzip2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bzip2/bzip2.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3017 | [cdparanoia/cdparanoia.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cdparanoia/cdparanoia.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3018 | [clzip/clzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/clzip/clzip.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3019 | [cunit/cunit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cunit/cunit.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3020 | [diffstat/diffstat.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/diffstat/diffstat.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3021 | [dos2unix/dos2unix.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dos2unix/dos2unix.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3022 | [doxygen/doxygen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/doxygen/doxygen.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3023 | [e2fsprogs/e2fsprogs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/e2fsprogs/e2fsprogs.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3024 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3025 | [giflib/giflib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/giflib/giflib.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3026 | [gsm/gsm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gsm/gsm.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3027 | [hdparm/hdparm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hdparm/hdparm.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3028 | [jbigkit/jbigkit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jbigkit/jbigkit.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3029 | [libdaemon/libdaemon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdaemon/libdaemon.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3030 | [libedit/libedit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libedit/libedit.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3031 | [libev/libev.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libev/libev.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3032 | [libmng/libmng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmng/libmng.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3033 | [lsscsi/lsscsi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lsscsi/lsscsi.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3034 | [lzlib/lzlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lzlib/lzlib.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3035 | [lzop/lzop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lzop/lzop.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3036 | [mandoc/mandoc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mandoc/mandoc.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3037 | [mpdecimal/mpdecimal.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mpdecimal/mpdecimal.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3038 | [msgpack/msgpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/msgpack/msgpack.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3039 | [musl/musl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/musl/musl.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3040 | [passt/passt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/passt/passt.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3041 | [perl-Algorithm-Diff/perl-Algorithm-Diff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Algorithm-Diff/perl-Algorithm-Diff.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3042 | [perl-Alien-Build-Plugin-Download-GitLab/perl-Alien-Build-Plugin-Download-GitLab.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Alien-Build-Plugin-Download-GitLab/perl-Alien-Build-Plugin-Download-GitLab.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3043 | [perl-AnyEvent/perl-AnyEvent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-AnyEvent/perl-AnyEvent.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3044 | [perl-Authen-SASL/perl-Authen-SASL.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Authen-SASL/perl-Authen-SASL.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3045 | [perl-autovivification/perl-autovivification.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-autovivification/perl-autovivification.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3046 | [perl-B-COW/perl-B-COW.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-B-COW/perl-B-COW.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3047 | [perl-B-Keywords/perl-B-Keywords.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-B-Keywords/perl-B-Keywords.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3048 | [perl-Business-ISSN/perl-Business-ISSN.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Business-ISSN/perl-Business-ISSN.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3049 | [perl-Canary-Stability/perl-Canary-Stability.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Canary-Stability/perl-Canary-Stability.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3050 | [perl-Capture-Tiny/perl-Capture-Tiny.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Capture-Tiny/perl-Capture-Tiny.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3051 | [perl-Class-Data-Inheritable/perl-Class-Data-Inheritable.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Class-Data-Inheritable/perl-Class-Data-Inheritable.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3052 | [perl-Class-Method-Modifiers/perl-Class-Method-Modifiers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Class-Method-Modifiers/perl-Class-Method-Modifiers.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3053 | [perl-Class-Singleton/perl-Class-Singleton.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Class-Singleton/perl-Class-Singleton.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3054 | [perl-Class-Tiny/perl-Class-Tiny.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Class-Tiny/perl-Class-Tiny.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3055 | [perl-Class-XSAccessor/perl-Class-XSAccessor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Class-XSAccessor/perl-Class-XSAccessor.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3056 | [perl-Clone/perl-Clone.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Clone/perl-Clone.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3057 | [perl-Clone-PP/perl-Clone-PP.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Clone-PP/perl-Clone-PP.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3058 | [perl-common-sense/perl-common-sense.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-common-sense/perl-common-sense.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3059 | [perl-Compress-Raw-Bzip2/perl-Compress-Raw-Bzip2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Compress-Raw-Bzip2/perl-Compress-Raw-Bzip2.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3060 | [perl-Compress-Raw-Lzma/perl-Compress-Raw-Lzma.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Compress-Raw-Lzma/perl-Compress-Raw-Lzma.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3061 | [perl-Compress-Raw-Zlib/perl-Compress-Raw-Zlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Compress-Raw-Zlib/perl-Compress-Raw-Zlib.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3062 | [perl-Config-Perl-V/perl-Config-Perl-V.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Config-Perl-V/perl-Config-Perl-V.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3063 | [perl-constant/perl-constant.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-constant/perl-constant.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3064 | [perl-CPAN-Meta-YAML/perl-CPAN-Meta-YAML.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-CPAN-Meta-YAML/perl-CPAN-Meta-YAML.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3065 | [perl-CPAN-Requirements-Dynamic/perl-CPAN-Requirements-Dynamic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-CPAN-Requirements-Dynamic/perl-CPAN-Requirements-Dynamic.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3066 | [perl-Crypt-RC4/perl-Crypt-RC4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Crypt-RC4/perl-Crypt-RC4.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3067 | [perl-Cwd-Guard/perl-Cwd-Guard.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Cwd-Guard/perl-Cwd-Guard.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3068 | [perl-Data-Dump/perl-Data-Dump.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Data-Dump/perl-Data-Dump.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3069 | [perl-Data-Dumper/perl-Data-Dumper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Data-Dumper/perl-Data-Dumper.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3070 | [perl-Data-Uniqid/perl-Data-Uniqid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Data-Uniqid/perl-Data-Uniqid.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3071 | [perl-Data-UUID/perl-Data-UUID.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Data-UUID/perl-Data-UUID.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3072 | [perl-Date-ISO8601/perl-Date-ISO8601.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Date-ISO8601/perl-Date-ISO8601.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3073 | [perl-Date-Manip/perl-Date-Manip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Date-Manip/perl-Date-Manip.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3074 | [perl-DateTime-TimeZone-SystemV/perl-DateTime-TimeZone-SystemV.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DateTime-TimeZone-SystemV/perl-DateTime-TimeZone-SystemV.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3075 | [perl-DBI/perl-DBI.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DBI/perl-DBI.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3076 | [perl-Devel-CheckCompiler/perl-Devel-CheckCompiler.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Devel-CheckCompiler/perl-Devel-CheckCompiler.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3077 | [perl-Devel-Cycle/perl-Devel-Cycle.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Devel-Cycle/perl-Devel-Cycle.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3078 | [perl-Devel-PPPort/perl-Devel-PPPort.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Devel-PPPort/perl-Devel-PPPort.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3079 | [perl-Devel-StackTrace/perl-Devel-StackTrace.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Devel-StackTrace/perl-Devel-StackTrace.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3080 | [perl-Devel-Symdump/perl-Devel-Symdump.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Devel-Symdump/perl-Devel-Symdump.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3081 | [perl-Digest/perl-Digest.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Digest/perl-Digest.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3082 | [perl-Digest-JHash/perl-Digest-JHash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Digest-JHash/perl-Digest-JHash.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3083 | [perl-Digest-Perl-MD5/perl-Digest-Perl-MD5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Digest-Perl-MD5/perl-Digest-Perl-MD5.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3084 | [perl-Digest-SHA/perl-Digest-SHA.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Digest-SHA/perl-Digest-SHA.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3085 | [perl-Dir-Manifest/perl-Dir-Manifest.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Dir-Manifest/perl-Dir-Manifest.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3086 | [perl-DynaLoader-Functions/perl-DynaLoader-Functions.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DynaLoader-Functions/perl-DynaLoader-Functions.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3087 | [perl-Env/perl-Env.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Env/perl-Env.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3088 | [perl-Env-Path/perl-Env-Path.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Env-Path/perl-Env-Path.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3089 | [perl-Error/perl-Error.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Error/perl-Error.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3090 | [perl-experimental/perl-experimental.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-experimental/perl-experimental.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3091 | [perl-Exporter-Tiny/perl-Exporter-Tiny.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Exporter-Tiny/perl-Exporter-Tiny.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3092 | [perl-ExtUtils-Config/perl-ExtUtils-Config.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-ExtUtils-Config/perl-ExtUtils-Config.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3093 | [perl-ExtUtils-HasCompiler/perl-ExtUtils-HasCompiler.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-ExtUtils-HasCompiler/perl-ExtUtils-HasCompiler.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3094 | [perl-ExtUtils-LibBuilder/perl-ExtUtils-LibBuilder.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-ExtUtils-LibBuilder/perl-ExtUtils-LibBuilder.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3095 | [perl-ExtUtils-PkgConfig/perl-ExtUtils-PkgConfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-ExtUtils-PkgConfig/perl-ExtUtils-PkgConfig.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3096 | [perl-File-Copy-Recursive/perl-File-Copy-Recursive.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Copy-Recursive/perl-File-Copy-Recursive.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3097 | [perl-File-Copy-Recursive-Reduced/perl-File-Copy-Recursive-Reduced.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Copy-Recursive-Reduced/perl-File-Copy-Recursive-Reduced.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3098 | [perl-File-Find-Object/perl-File-Find-Object.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Find-Object/perl-File-Find-Object.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3099 | [perl-File-Find-Object-Rule/perl-File-Find-Object-Rule.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Find-Object-Rule/perl-File-Find-Object-Rule.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3100 | [perl-File-Path/perl-File-Path.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Path/perl-File-Path.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3101 | [perl-File-ShareDir-Install/perl-File-ShareDir-Install.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-ShareDir-Install/perl-File-ShareDir-Install.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3102 | [perl-File-TreeCreate/perl-File-TreeCreate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-TreeCreate/perl-File-TreeCreate.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3103 | [perl-File-Which/perl-File-Which.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-File-Which/perl-File-Which.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3104 | [perl-Font-AFM/perl-Font-AFM.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Font-AFM/perl-Font-AFM.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3105 | [perl-Font-TTF/perl-Font-TTF.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Font-TTF/perl-Font-TTF.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3106 | [perl-GD/perl-GD.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-GD/perl-GD.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3107 | [perl-GSSAPI/perl-GSSAPI.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-GSSAPI/perl-GSSAPI.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3108 | [perl-Hash-MoreUtils/perl-Hash-MoreUtils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Hash-MoreUtils/perl-Hash-MoreUtils.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3109 | [perl-Hook-LexWrap/perl-Hook-LexWrap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Hook-LexWrap/perl-Hook-LexWrap.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3110 | [perl-HTML-Parser/perl-HTML-Parser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-HTML-Parser/perl-HTML-Parser.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3111 | [perl-HTML-Tagset/perl-HTML-Tagset.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-HTML-Tagset/perl-HTML-Tagset.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3112 | [perl-Import-Into/perl-Import-Into.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Import-Into/perl-Import-Into.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3113 | [perl-IO-Compress-Brotli/perl-IO-Compress-Brotli.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IO-Compress-Brotli/perl-IO-Compress-Brotli.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3114 | [perl-IO-String/perl-IO-String.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IO-String/perl-IO-String.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3115 | [perl-IO-Tty/perl-IO-Tty.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IO-Tty/perl-IO-Tty.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3116 | [perl-IPC-ShareLite/perl-IPC-ShareLite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IPC-ShareLite/perl-IPC-ShareLite.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3117 | [perl-IPC-System-Simple/perl-IPC-System-Simple.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-IPC-System-Simple/perl-IPC-System-Simple.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3118 | [perl-JSON-MaybeXS/perl-JSON-MaybeXS.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-JSON-MaybeXS/perl-JSON-MaybeXS.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3119 | [perl-JSON-XS/perl-JSON-XS.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-JSON-XS/perl-JSON-XS.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3120 | [perl-libxml-perl/perl-libxml-perl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-libxml-perl/perl-libxml-perl.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3121 | [perl-Lingua-EN-Inflect/perl-Lingua-EN-Inflect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Lingua-EN-Inflect/perl-Lingua-EN-Inflect.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3122 | [perl-List-BinarySearch-XS/perl-List-BinarySearch-XS.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-List-BinarySearch-XS/perl-List-BinarySearch-XS.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3123 | [perl-Locale-Codes/perl-Locale-Codes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Locale-Codes/perl-Locale-Codes.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3124 | [perl-Locale-gettext/perl-Locale-gettext.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Locale-gettext/perl-Locale-gettext.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3125 | [perl-Log-Any/perl-Log-Any.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Log-Any/perl-Log-Any.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3126 | [perl-LWP-MediaTypes/perl-LWP-MediaTypes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-LWP-MediaTypes/perl-LWP-MediaTypes.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3127 | [perl-Math-Base-Convert/perl-Math-Base-Convert.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Math-Base-Convert/perl-Math-Base-Convert.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3128 | [perl-Math-Gradient/perl-Math-Gradient.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Math-Gradient/perl-Math-Gradient.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3129 | [perl-MIME-Base32/perl-MIME-Base32.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-MIME-Base32/perl-MIME-Base32.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3130 | [perl-MIME-Base64/perl-MIME-Base64.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-MIME-Base64/perl-MIME-Base64.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3131 | [perl-Mixin-Linewise/perl-Mixin-Linewise.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Mixin-Linewise/perl-Mixin-Linewise.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3132 | [perl-Mock-Config/perl-Mock-Config.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Mock-Config/perl-Mock-Config.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3133 | [perl-Module-Load/perl-Module-Load.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-Load/perl-Module-Load.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3134 | [perl-Module-Runtime/perl-Module-Runtime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-Runtime/perl-Module-Runtime.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3135 | [perl-Module-Util/perl-Module-Util.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Module-Util/perl-Module-Util.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3136 | [perl-MooX/perl-MooX.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-MooX/perl-MooX.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3137 | [perl-Mouse/perl-Mouse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Mouse/perl-Mouse.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3138 | [perl-Mozilla-CA/perl-Mozilla-CA.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Mozilla-CA/perl-Mozilla-CA.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3139 | [perl-Mozilla-PublicSuffix/perl-Mozilla-PublicSuffix.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Mozilla-PublicSuffix/perl-Mozilla-PublicSuffix.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3140 | [perl-MRO-Compat/perl-MRO-Compat.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-MRO-Compat/perl-MRO-Compat.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3141 | [perl-Net-HTTP/perl-Net-HTTP.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Net-HTTP/perl-Net-HTTP.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3142 | [perl-Net-SSLeay/perl-Net-SSLeay.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Net-SSLeay/perl-Net-SSLeay.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3143 | [perl-NTLM/perl-NTLM.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-NTLM/perl-NTLM.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3144 | [perl-Number-Compare/perl-Number-Compare.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Number-Compare/perl-Number-Compare.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3145 | [perl-OLE-Storage_Lite/perl-OLE-Storage_Lite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-OLE-Storage_Lite/perl-OLE-Storage_Lite.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3146 | [perl-Package-Stash-XS/perl-Package-Stash-XS.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Package-Stash-XS/perl-Package-Stash-XS.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3147 | [perl-PadWalker/perl-PadWalker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-PadWalker/perl-PadWalker.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3148 | [perl-PAR-Dist/perl-PAR-Dist.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-PAR-Dist/perl-PAR-Dist.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3149 | [perl-Params-Check/perl-Params-Check.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Params-Check/perl-Params-Check.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3150 | [perl-parent/perl-parent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-parent/perl-parent.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3151 | [perl-Parse-Yapp/perl-Parse-Yapp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Parse-Yapp/perl-Parse-Yapp.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3152 | [perl-Perl-OSType/perl-Perl-OSType.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Perl-OSType/perl-Perl-OSType.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3153 | [perl-Perl-Tidy/perl-Perl-Tidy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Perl-Tidy/perl-Perl-Tidy.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3154 | [perl-perlfaq/perl-perlfaq.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-perlfaq/perl-perlfaq.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3155 | [perl-PerlIO-utf8_strict/perl-PerlIO-utf8_strict.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-PerlIO-utf8_strict/perl-PerlIO-utf8_strict.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3156 | [perl-PerlIO-via-QuotedPrint/perl-PerlIO-via-QuotedPrint.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-PerlIO-via-QuotedPrint/perl-PerlIO-via-QuotedPrint.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3157 | [perl-Pod-Coverage-TrustPod/perl-Pod-Coverage-TrustPod.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Pod-Coverage-TrustPod/perl-Pod-Coverage-TrustPod.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3158 | [perl-Pod-Escapes/perl-Pod-Escapes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Pod-Escapes/perl-Pod-Escapes.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3159 | [perl-Readonly/perl-Readonly.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Readonly/perl-Readonly.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3160 | [perl-Scalar-List-Utils/perl-Scalar-List-Utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Scalar-List-Utils/perl-Scalar-List-Utils.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3161 | [perl-Scope-Guard/perl-Scope-Guard.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Scope-Guard/perl-Scope-Guard.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3162 | [perl-SGMLSpm/perl-SGMLSpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-SGMLSpm/perl-SGMLSpm.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3163 | [perl-Socket/perl-Socket.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Socket/perl-Socket.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3164 | [perl-Sort-Versions/perl-Sort-Versions.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Sort-Versions/perl-Sort-Versions.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3165 | [perl-Storable/perl-Storable.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Storable/perl-Storable.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3166 | [perl-strictures/perl-strictures.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-strictures/perl-strictures.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3167 | [perl-String-Format/perl-String-Format.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-String-Format/perl-String-Format.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3168 | [perl-String-ShellQuote/perl-String-ShellQuote.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-String-ShellQuote/perl-String-ShellQuote.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3169 | [perl-Sub-Exporter-Progressive/perl-Sub-Exporter-Progressive.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Sub-Exporter-Progressive/perl-Sub-Exporter-Progressive.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3170 | [perl-Sub-Identify/perl-Sub-Identify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Sub-Identify/perl-Sub-Identify.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3171 | [perl-Sub-Install/perl-Sub-Install.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Sub-Install/perl-Sub-Install.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3172 | [perl-Sub-Quote/perl-Sub-Quote.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Sub-Quote/perl-Sub-Quote.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3173 | [perl-Sub-Uplevel/perl-Sub-Uplevel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Sub-Uplevel/perl-Sub-Uplevel.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3174 | [perl-Sys-Syslog/perl-Sys-Syslog.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Sys-Syslog/perl-Sys-Syslog.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3175 | [perl-Task-Weaken/perl-Task-Weaken.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Task-Weaken/perl-Task-Weaken.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3176 | [perl-Term-ANSIColor/perl-Term-ANSIColor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Term-ANSIColor/perl-Term-ANSIColor.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3177 | [perl-TermReadKey/perl-TermReadKey.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-TermReadKey/perl-TermReadKey.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3178 | [perl-Test-File/perl-Test-File.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-File/perl-Test-File.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3179 | [perl-Test-Inter/perl-Test-Inter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Inter/perl-Test-Inter.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3180 | [perl-Test-Needs/perl-Test-Needs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Needs/perl-Test-Needs.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3181 | [perl-Test-Pod-Coverage/perl-Test-Pod-Coverage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Pod-Coverage/perl-Test-Pod-Coverage.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3182 | [perl-Test-RequiresInternet/perl-Test-RequiresInternet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-RequiresInternet/perl-Test-RequiresInternet.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3183 | [perl-Test-Some/perl-Test-Some.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Some/perl-Test-Some.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3184 | [perl-Test-Taint/perl-Test-Taint.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Taint/perl-Test-Taint.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3185 | [perl-Test-Warnings/perl-Test-Warnings.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Warnings/perl-Test-Warnings.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3186 | [perl-Test-Without-Module/perl-Test-Without-Module.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Test-Without-Module/perl-Test-Without-Module.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3187 | [perl-Text-Balanced/perl-Text-Balanced.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Text-Balanced/perl-Text-Balanced.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3188 | [perl-Text-Glob/perl-Text-Glob.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Text-Glob/perl-Text-Glob.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3189 | [perl-Text-ParseWords/perl-Text-ParseWords.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Text-ParseWords/perl-Text-ParseWords.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3190 | [perl-Text-Roman/perl-Text-Roman.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Text-Roman/perl-Text-Roman.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3191 | [perl-Text-Soundex/perl-Text-Soundex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Text-Soundex/perl-Text-Soundex.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3192 | [perl-Text-Tabs-Wrap/perl-Text-Tabs-Wrap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Text-Tabs-Wrap/perl-Text-Tabs-Wrap.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3193 | [perl-Text-Unidecode/perl-Text-Unidecode.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Text-Unidecode/perl-Text-Unidecode.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3194 | [perl-Tie-Cycle/perl-Tie-Cycle.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Tie-Cycle/perl-Tie-Cycle.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3195 | [perl-Tie-IxHash/perl-Tie-IxHash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Tie-IxHash/perl-Tie-IxHash.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3196 | [perl-Time-Duration/perl-Time-Duration.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Time-Duration/perl-Time-Duration.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3197 | [perl-Time-HiRes/perl-Time-HiRes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Time-HiRes/perl-Time-HiRes.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3198 | [perl-Time-Local/perl-Time-Local.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Time-Local/perl-Time-Local.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3199 | [perl-TimeDate/perl-TimeDate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-TimeDate/perl-TimeDate.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3200 | [perl-Types-Serialiser/perl-Types-Serialiser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Types-Serialiser/perl-Types-Serialiser.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3201 | [perl-Unicode-Collate/perl-Unicode-Collate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Unicode-Collate/perl-Unicode-Collate.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3202 | [perl-Unicode-Normalize/perl-Unicode-Normalize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Unicode-Normalize/perl-Unicode-Normalize.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3203 | [perl-Unicode-UTF8/perl-Unicode-UTF8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Unicode-UTF8/perl-Unicode-UTF8.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3204 | [perl-XML-NamespaceSupport/perl-XML-NamespaceSupport.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-NamespaceSupport/perl-XML-NamespaceSupport.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3205 | [perl-XML-RegExp/perl-XML-RegExp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-RegExp/perl-XML-RegExp.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3206 | [perl-XML-SAX-Base/perl-XML-SAX-Base.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-SAX-Base/perl-XML-SAX-Base.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3207 | [perl-XML-Writer/perl-XML-Writer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XML-Writer/perl-XML-Writer.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3208 | [perl-XS-Object-Magic/perl-XS-Object-Magic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XS-Object-Magic/perl-XS-Object-Magic.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3209 | [perl-XString/perl-XString.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-XString/perl-XString.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3210 | [perl-YAML-LibYAML/perl-YAML-LibYAML.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-YAML-LibYAML/perl-YAML-LibYAML.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3211 | [perl-YAML-Tiny/perl-YAML-Tiny.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-YAML-Tiny/perl-YAML-Tiny.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3212 | [plzip/plzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/plzip/plzip.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3213 | [potrace/potrace.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/potrace/potrace.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3214 | [python/python.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python/python.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3215 | [python-aiohttp-socks/python-aiohttp-socks.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-aiohttp-socks/python-aiohttp-socks.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3216 | [python-asyncssh/python-asyncssh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-asyncssh/python-asyncssh.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3217 | [python-azure-core/python-azure-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-azure-core/python-azure-core.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3218 | [python-azure-storage-blob/python-azure-storage-blob.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-azure-storage-blob/python-azure-storage-blob.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3219 | [python-babel/python-babel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-babel/python-babel.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3220 | [python-beautifulsoup4/python-beautifulsoup4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-beautifulsoup4/python-beautifulsoup4.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3221 | [python-build/python-build.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-build/python-build.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3222 | [python-certifi/python-certifi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-certifi/python-certifi.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3223 | [python-cffi/python-cffi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cffi/python-cffi.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3224 | [python-cherrypy/python-cherrypy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cherrypy/python-cherrypy.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3225 | [python-colorama/python-colorama.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-colorama/python-colorama.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3226 | [python-contourpy/python-contourpy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-contourpy/python-contourpy.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3227 | [python-cppheaderparser/python-cppheaderparser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cppheaderparser/python-cppheaderparser.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3228 | [python-cython/python-cython.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cython/python-cython.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3229 | [python-diskcache/python-diskcache.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-diskcache/python-diskcache.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3230 | [python-django/python-django.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-django/python-django.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3231 | [python-docutils/python-docutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-docutils/python-docutils.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3232 | [python-execnet/python-execnet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-execnet/python-execnet.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3233 | [python-genshi/python-genshi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-genshi/python-genshi.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3234 | [python-hatchling/python-hatchling.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-hatchling/python-hatchling.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3235 | [python-installer/python-installer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-installer/python-installer.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3236 | [python-invoke/python-invoke.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-invoke/python-invoke.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3237 | [python-ipython/python-ipython.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ipython/python-ipython.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3238 | [python-jinja2/python-jinja2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-jinja2/python-jinja2.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3239 | [python-markdown/python-markdown.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-markdown/python-markdown.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3240 | [python-markupsafe/python-markupsafe.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-markupsafe/python-markupsafe.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3241 | [python-mpmath/python-mpmath.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mpmath/python-mpmath.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3242 | [python-msgpack/python-msgpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-msgpack/python-msgpack.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3243 | [python-mypy/python-mypy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mypy/python-mypy.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3244 | [python-nanobind/python-nanobind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-nanobind/python-nanobind.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3245 | [python-nltk/python-nltk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-nltk/python-nltk.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3246 | [python-nvidia-ml-py/python-nvidia-ml-py.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-nvidia-ml-py/python-nvidia-ml-py.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3247 | [python-pandas/python-pandas.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pandas/python-pandas.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3248 | [python-passlib/python-passlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-passlib/python-passlib.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3249 | [python-pdm-backend/python-pdm-backend.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pdm-backend/python-pdm-backend.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3250 | [python-pexpect/python-pexpect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pexpect/python-pexpect.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3251 | [python-pillow/python-pillow.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pillow/python-pillow.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3252 | [python-protobuf/python-protobuf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-protobuf/python-protobuf.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3253 | [python-pygments/python-pygments.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pygments/python-pygments.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3254 | [python-pyproject-api/python-pyproject-api.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyproject-api/python-pyproject-api.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3255 | [python-pyqt-builder/python-pyqt-builder.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyqt-builder/python-pyqt-builder.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3256 | [python-pyqt6-sip/python-pyqt6-sip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyqt6-sip/python-pyqt6-sip.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3257 | [python-pyserial/python-pyserial.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyserial/python-pyserial.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3258 | [python-pytest-datadir/python-pytest-datadir.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-datadir/python-pytest-datadir.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3259 | [python-python-dotenv/python-python-dotenv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-dotenv/python-python-dotenv.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3260 | [python-qemu-qmp/python-qemu-qmp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-qemu-qmp/python-qemu-qmp.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3261 | [python-requests/python-requests.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-requests/python-requests.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3262 | [python-ruamel-yaml/python-ruamel-yaml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ruamel-yaml/python-ruamel-yaml.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3263 | [python-ruamel-yaml-clib/python-ruamel-yaml-clib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ruamel-yaml-clib/python-ruamel-yaml-clib.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3264 | [python-sagemaker-schema-inference-artifacts/python-sagemaker-schema-inference-artifacts.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sagemaker-schema-inference-artifacts/python-sagemaker-schema-inference-artifacts.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3265 | [python-scipy/python-scipy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-scipy/python-scipy.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3266 | [python-sentence-transformers/python-sentence-transformers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sentence-transformers/python-sentence-transformers.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3267 | [python-setproctitle/python-setproctitle.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-setproctitle/python-setproctitle.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3268 | [python-simplejson/python-simplejson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-simplejson/python-simplejson.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3269 | [python-sympy/python-sympy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sympy/python-sympy.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3270 | [python-tiktoken/python-tiktoken.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tiktoken/python-tiktoken.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3271 | [python-urllib3/python-urllib3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-urllib3/python-urllib3.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3272 | [python-voyageai/python-voyageai.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-voyageai/python-voyageai.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3273 | [qt6-qttools/qt6-qttools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qttools/qt6-qttools.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3274 | [ranger/ranger.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ranger/ranger.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3275 | [rpcbind/rpcbind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpcbind/rpcbind.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3276 | [rust-async-std-1/rust-async-std-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-async-std-1/rust-async-std-1.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3277 | [rust-bssl-sys-0.1/rust-bssl-sys-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bssl-sys-0.1/rust-bssl-sys-0.1.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3278 | [rust-crc-any-2/rust-crc-any-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-crc-any-2/rust-crc-any-2.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3279 | [rust-debug-helper-0.3/rust-debug-helper-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-debug-helper-0.3/rust-debug-helper-0.3.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3280 | [rust-dunce-1/rust-dunce-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-dunce-1/rust-dunce-1.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3281 | [rust-finl-unicode-1/rust-finl-unicode-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-finl-unicode-1/rust-finl-unicode-1.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3282 | [rust-futures-core-0.3/rust-futures-core-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-futures-core-0.3/rust-futures-core-0.3.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3283 | [rust-futures-io-0.3/rust-futures-io-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-futures-io-0.3/rust-futures-io-0.3.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3284 | [rust-futures-sink-0.3/rust-futures-sink-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-futures-sink-0.3/rust-futures-sink-0.3.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3285 | [rust-futures-task-0.3/rust-futures-task-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-futures-task-0.3/rust-futures-task-0.3.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3286 | [rust-html-escape-0.2/rust-html-escape-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-html-escape-0.2/rust-html-escape-0.2.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3287 | [rust-icu-normalizer-data-2/rust-icu-normalizer-data-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-icu-normalizer-data-2/rust-icu-normalizer-data-2.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3288 | [rust-icu-properties-data-2/rust-icu-properties-data-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-icu-properties-data-2/rust-icu-properties-data-2.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3289 | [rust-imgref-1/rust-imgref-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-imgref-1/rust-imgref-1.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3290 | [rust-platforms-3/rust-platforms-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-platforms-3/rust-platforms-3.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3291 | [rust-platforms-4/rust-platforms-4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-platforms-4/rust-platforms-4.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3292 | [rust-plotters-backend-0.3/rust-plotters-backend-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-plotters-backend-0.3/rust-plotters-backend-0.3.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3293 | [rust-potential-utf-0.1/rust-potential-utf-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-potential-utf-0.1/rust-potential-utf-0.1.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3294 | [rust-rand-core-0.10/rust-rand-core-0.10.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rand-core-0.10/rust-rand-core-0.10.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3295 | [rust-rand-core-0.6/rust-rand-core-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rand-core-0.6/rust-rand-core-0.6.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3296 | [rust-rand-core-0.9/rust-rand-core-0.9.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rand-core-0.9/rust-rand-core-0.9.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3297 | [rust-rgb-0.8/rust-rgb-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rgb-0.8/rust-rgb-0.8.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3298 | [rust-siphasher-1/rust-siphasher-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-siphasher-1/rust-siphasher-1.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3299 | [rust-subtle-2/rust-subtle-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-subtle-2/rust-subtle-2.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3300 | [rust-sync-wrapper-1/rust-sync-wrapper-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-sync-wrapper-1/rust-sync-wrapper-1.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3301 | [rust-tracing-core-0.1/rust-tracing-core-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tracing-core-0.1/rust-tracing-core-0.1.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3302 | [rust-urlencoding-2/rust-urlencoding-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-urlencoding-2/rust-urlencoding-2.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3303 | [rust-utf8-iter-1/rust-utf8-iter-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-utf8-iter-1/rust-utf8-iter-1.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3304 | [rust-version-compare-0.2/rust-version-compare-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-version-compare-0.2/rust-version-compare-0.2.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3305 | [rust-xml-rs-0.8/rust-xml-rs-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-xml-rs-0.8/rust-xml-rs-0.8.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3306 | [startup-notification/startup-notification.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/startup-notification/startup-notification.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3307 | [symlinks/symlinks.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/symlinks/symlinks.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3308 | [tdb/tdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tdb/tdb.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3309 | [traceroute/traceroute.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/traceroute/traceroute.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3310 | [tunctl/tunctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tunctl/tunctl.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3311 | [tzdata/tzdata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tzdata/tzdata.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3312 | [u-boot-tools/u-boot-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/u-boot-tools/u-boot-tools.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3313 | [unifont/unifont.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unifont/unifont.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3314 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3315 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3316 | [xmlrpc-c/xmlrpc-c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xmlrpc-c/xmlrpc-c.spec) | `VCS, Requires` | 缺少必填字段：`VCS, Requires` |
| 3317 | [btrbk/btrbk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/btrbk/btrbk.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3318 | [ca-certificates/ca-certificates.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ca-certificates/ca-certificates.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3319 | [calamares/calamares.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/calamares/calamares.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3320 | [dejagnu/dejagnu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dejagnu/dejagnu.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3321 | [dkms/dkms.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dkms/dkms.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3322 | [firefox/firefox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/firefox/firefox.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3323 | [fonts-noto/fonts-noto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fonts-noto/fonts-noto.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3324 | [fonts-noto-sans-cjk/fonts-noto-sans-cjk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fonts-noto-sans-cjk/fonts-noto-sans-cjk.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3325 | [fonts-noto-serif-cjk/fonts-noto-serif-cjk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fonts-noto-serif-cjk/fonts-noto-serif-cjk.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3326 | [go/go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go/go.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3327 | [gpsd/gpsd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpsd/gpsd.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3328 | [kiwi/kiwi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kiwi/kiwi.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3329 | [libtool/libtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtool/libtool.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3330 | [linux-firmware/linux-firmware.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/linux-firmware/linux-firmware.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3331 | [llvm-snapshot/llvm-snapshot.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvm-snapshot/llvm-snapshot.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3332 | [llvm22/llvm22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvm22/llvm22.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3333 | [llvmir-converter/llvmir-converter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvmir-converter/llvmir-converter.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3334 | [lynis/lynis.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lynis/lynis.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3335 | [meson/meson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/meson/meson.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3336 | [mmtests/mmtests.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mmtests/mmtests.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3337 | [mock/mock.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mock/mock.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3338 | [muon/muon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/muon/muon.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3339 | [obs-build/obs-build.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/obs-build/obs-build.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3340 | [openruyi-desktop-setup-kde/openruyi-desktop-setup-kde.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openruyi-desktop-setup-kde/openruyi-desktop-setup-kde.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3341 | [openruyi-logo/openruyi-logo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openruyi-logo/openruyi-logo.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3342 | [osc/osc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/osc/osc.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3343 | [osinfo-db/osinfo-db.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/osinfo-db/osinfo-db.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3344 | [phoronix-test-suite/phoronix-test-suite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/phoronix-test-suite/phoronix-test-suite.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3345 | [php-fpdf/php-fpdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/php-fpdf/php-fpdf.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3346 | [pkgconf/pkgconf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pkgconf/pkgconf.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3347 | [pyproject-rpm-macros/pyproject-rpm-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pyproject-rpm-macros/pyproject-rpm-macros.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3348 | [python-packaging/python-packaging.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-packaging/python-packaging.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3349 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3350 | [rrdtool/rrdtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3351 | [setup/setup.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/setup/setup.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3352 | [texlive-texmf/texlive-texmf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/texlive-texmf/texlive-texmf.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3353 | [tuned/tuned.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tuned/tuned.spec) | `BuildSystem` | 缺少必填字段：`BuildSystem` |
| 3354 | [containers-common/containers-common.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/containers-common/containers-common.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3355 | [dotnet10.0/dotnet10.0.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dotnet10.0/dotnet10.0.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3356 | [etcd/etcd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/etcd/etcd.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3357 | [filesystem/filesystem.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/filesystem/filesystem.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3358 | [fonts-dejavu/fonts-dejavu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fonts-dejavu/fonts-dejavu.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3359 | [fonts-fontawesome/fonts-fontawesome.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fonts-fontawesome/fonts-fontawesome.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3360 | [fonts-hack/fonts-hack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fonts-hack/fonts-hack.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3361 | [fonts-sarasa-gothic/fonts-sarasa-gothic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fonts-sarasa-gothic/fonts-sarasa-gothic.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3362 | [grep/grep.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grep/grep.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3363 | [grub/grub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grub/grub.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3364 | [hunspell-en/hunspell-en.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hunspell-en/hunspell-en.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3365 | [jack2/jack2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jack2/jack2.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3366 | [libffi/libffi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libffi/libffi.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3367 | [linux-headers/linux-headers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/linux-headers/linux-headers.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3368 | [lua-lunitx/lua-lunitx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua-lunitx/lua-lunitx.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3369 | [man-pages/man-pages.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/man-pages/man-pages.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3370 | [mpfr/mpfr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mpfr/mpfr.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3371 | [numad/numad.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/numad/numad.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3372 | [openjdk-17/openjdk-17.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openjdk-17/openjdk-17.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3373 | [openjdk-21/openjdk-21.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openjdk-21/openjdk-21.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3374 | [openjdk-25/openjdk-25.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openjdk-25/openjdk-25.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3375 | [openjdk-latest/openjdk-latest.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openjdk-latest/openjdk-latest.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3376 | [opensbi/opensbi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/opensbi/opensbi.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3377 | [ovmf/ovmf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ovmf/ovmf.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3378 | [picoclaw/picoclaw.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/picoclaw/picoclaw.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3379 | [pocketfft/pocketfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pocketfft/pocketfft.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3380 | [rocm-llvm/rocm-llvm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocm-llvm/rocm-llvm.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3381 | [rust/rust.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust/rust.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3382 | [zstd/zstd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zstd/zstd.spec) | `BuildSystem, Requires` | 缺少必填字段：`BuildSystem, Requires` |
| 3383 | [autoconf-archive/autoconf-archive.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/autoconf-archive/autoconf-archive.spec) | `BuildRequires, Requires` | 缺少必填字段：`BuildRequires, Requires` |
| 3384 | [diffutils/diffutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/diffutils/diffutils.spec) | `BuildRequires, Requires` | 缺少必填字段：`BuildRequires, Requires` |
| 3385 | [libfaketime/libfaketime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfaketime/libfaketime.spec) | `BuildRequires, Requires` | 缺少必填字段：`BuildRequires, Requires` |
| 3386 | [libfastjson/libfastjson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfastjson/libfastjson.spec) | `BuildRequires, Requires` | 缺少必填字段：`BuildRequires, Requires` |
| 3387 | [libiconv/libiconv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libiconv/libiconv.spec) | `BuildRequires, Requires` | 缺少必填字段：`BuildRequires, Requires` |
| 3388 | [libsigsegv/libsigsegv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsigsegv/libsigsegv.spec) | `BuildRequires, Requires` | 缺少必填字段：`BuildRequires, Requires` |
| 3389 | [libunistring/libunistring.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libunistring/libunistring.spec) | `BuildRequires, Requires` | 缺少必填字段：`BuildRequires, Requires` |
| 3390 | [npth/npth.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/npth/npth.spec) | `BuildRequires, Requires` | 缺少必填字段：`BuildRequires, Requires` |
| 3391 | [openntpd/openntpd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openntpd/openntpd.spec) | `BuildRequires, Requires` | 缺少必填字段：`BuildRequires, Requires` |
| 3392 | [rust-rpm-macros/rust-rpm-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rpm-macros/rust-rpm-macros.spec) | `BuildRequires, Requires` | 缺少必填字段：`BuildRequires, Requires` |
| 3393 | [time/time.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/time/time.spec) | `BuildRequires, Requires` | 缺少必填字段：`BuildRequires, Requires` |
| 3394 | [trinity/trinity.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/trinity/trinity.spec) | `BuildRequires, Requires` | 缺少必填字段：`BuildRequires, Requires` |
| 3395 | [which/which.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/which/which.spec) | `BuildRequires, Requires` | 缺少必填字段：`BuildRequires, Requires` |
| 3396 | [cldr-emoji-annotation/cldr-emoji-annotation.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cldr-emoji-annotation/cldr-emoji-annotation.spec) | `BuildSystem, BuildRequires, Requires` | 缺少必填字段：`BuildSystem, BuildRequires, Requires` |
| 3397 | [distribution-gpg-keys/distribution-gpg-keys.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/distribution-gpg-keys/distribution-gpg-keys.spec) | `BuildSystem, BuildRequires, Requires` | 缺少必填字段：`BuildSystem, BuildRequires, Requires` |
| 3398 | [fonts-codenewroman-nerd/fonts-codenewroman-nerd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fonts-codenewroman-nerd/fonts-codenewroman-nerd.spec) | `BuildSystem, BuildRequires, Requires` | 缺少必填字段：`BuildSystem, BuildRequires, Requires` |
| 3399 | [fonts-firacode-nerd/fonts-firacode-nerd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fonts-firacode-nerd/fonts-firacode-nerd.spec) | `BuildSystem, BuildRequires, Requires` | 缺少必填字段：`BuildSystem, BuildRequires, Requires` |
| 3400 | [fonts-iosevka-nerd/fonts-iosevka-nerd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fonts-iosevka-nerd/fonts-iosevka-nerd.spec) | `BuildSystem, BuildRequires, Requires` | 缺少必填字段：`BuildSystem, BuildRequires, Requires` |
| 3401 | [fonts-jetbrainsmono-nerd/fonts-jetbrainsmono-nerd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fonts-jetbrainsmono-nerd/fonts-jetbrainsmono-nerd.spec) | `BuildSystem, BuildRequires, Requires` | 缺少必填字段：`BuildSystem, BuildRequires, Requires` |
| 3402 | [go-rpm-macros/go-rpm-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-rpm-macros/go-rpm-macros.spec) | `BuildSystem, BuildRequires, Requires` | 缺少必填字段：`BuildSystem, BuildRequires, Requires` |
| 3403 | [python-rpm-generators/python-rpm-generators.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rpm-generators/python-rpm-generators.spec) | `BuildSystem, BuildRequires, Requires` | 缺少必填字段：`BuildSystem, BuildRequires, Requires` |
| 3404 | [sof-firmware/sof-firmware.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sof-firmware/sof-firmware.spec) | `BuildSystem, BuildRequires, Requires` | 缺少必填字段：`BuildSystem, BuildRequires, Requires` |
| 3405 | [stb/stb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/stb/stb.spec) | `BuildSystem, BuildRequires, Requires` | 缺少必填字段：`BuildSystem, BuildRequires, Requires` |
| 3406 | [u-boot-menu-ng/u-boot-menu-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/u-boot-menu-ng/u-boot-menu-ng.spec) | `BuildSystem, BuildRequires, Requires` | 缺少必填字段：`BuildSystem, BuildRequires, Requires` |
| 3407 | [wyhash/wyhash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wyhash/wyhash.spec) | `BuildSystem, BuildRequires, Requires` | 缺少必填字段：`BuildSystem, BuildRequires, Requires` |
| 3408 | [ca-certificates-mozilla/ca-certificates-mozilla.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ca-certificates-mozilla/ca-certificates-mozilla.spec) | `VCS, BuildSystem, Requires` | 缺少必填字段：`VCS, BuildSystem, Requires` |
| 3409 | [config/config.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/config/config.spec) | `VCS, BuildSystem, Requires` | 缺少必填字段：`VCS, BuildSystem, Requires` |
| 3410 | [db/db.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/db/db.spec) | `VCS, BuildSystem, Requires` | 缺少必填字段：`VCS, BuildSystem, Requires` |
| 3411 | [dotnet10.0-bin/dotnet10.0-bin.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dotnet10.0-bin/dotnet10.0-bin.spec) | `VCS, BuildSystem, Requires` | 缺少必填字段：`VCS, BuildSystem, Requires` |
| 3412 | [ed/ed.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ed/ed.spec) | `VCS, BuildSystem, Requires` | 缺少必填字段：`VCS, BuildSystem, Requires` |
| 3413 | [glibc/glibc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glibc/glibc.spec) | `VCS, BuildSystem, Requires` | 缺少必填字段：`VCS, BuildSystem, Requires` |
| 3414 | [iozone/iozone.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iozone/iozone.spec) | `VCS, BuildSystem, Requires` | 缺少必填字段：`VCS, BuildSystem, Requires` |
| 3415 | [llvm-defaults/llvm-defaults.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvm-defaults/llvm-defaults.spec) | `VCS, BuildSystem, Requires` | 缺少必填字段：`VCS, BuildSystem, Requires` |
| 3416 | [lzip/lzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lzip/lzip.spec) | `VCS, BuildSystem, Requires` | 缺少必填字段：`VCS, BuildSystem, Requires` |
| 3417 | [python-setuptools/python-setuptools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-setuptools/python-setuptools.spec) | `VCS, BuildSystem, Requires` | 缺少必填字段：`VCS, BuildSystem, Requires` |
| 3418 | [rust-bin/rust-bin.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bin/rust-bin.spec) | `VCS, BuildSystem, Requires` | 缺少必填字段：`VCS, BuildSystem, Requires` |
| 3419 | [unicode-ucd/unicode-ucd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unicode-ucd/unicode-ucd.spec) | `VCS, BuildSystem, Requires` | 缺少必填字段：`VCS, BuildSystem, Requires` |
| 3420 | [docbook-dtds/docbook-dtds.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-dtds/docbook-dtds.spec) | `VCS, BuildSystem` | 缺少必填字段：`VCS, BuildSystem` |
| 3421 | [docbook-style-dsssl/docbook-style-dsssl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-style-dsssl/docbook-style-dsssl.spec) | `VCS, BuildSystem` | 缺少必填字段：`VCS, BuildSystem` |
| 3422 | [gcc/gcc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc/gcc.spec) | `VCS, BuildSystem` | 缺少必填字段：`VCS, BuildSystem` |
| 3423 | [gcc16/gcc16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc16/gcc16.spec) | `VCS, BuildSystem` | 缺少必填字段：`VCS, BuildSystem` |
| 3424 | [linux/linux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/linux/linux.spec) | `VCS, BuildSystem` | 缺少必填字段：`VCS, BuildSystem` |
| 3425 | [linux-lts/linux-lts.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/linux-lts/linux-lts.spec) | `VCS, BuildSystem` | 缺少必填字段：`VCS, BuildSystem` |
| 3426 | [linux-lts-kmhv2/linux-lts-kmhv2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/linux-lts-kmhv2/linux-lts-kmhv2.spec) | `VCS, BuildSystem` | 缺少必填字段：`VCS, BuildSystem` |
| 3427 | [python-flit-core/python-flit-core.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-flit-core/python-flit-core.spec) | `VCS, BuildSystem` | 缺少必填字段：`VCS, BuildSystem` |
| 3428 | [python-pip/python-pip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pip/python-pip.spec) | `VCS, BuildSystem` | 缺少必填字段：`VCS, BuildSystem` |
| 3429 | [crontabs/crontabs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crontabs/crontabs.spec) | `BuildSystem, BuildRequires` | 缺少必填字段：`BuildSystem, BuildRequires` |
| 3430 | [docbook-xsl/docbook-xsl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-xsl/docbook-xsl.spec) | `BuildSystem, BuildRequires` | 缺少必填字段：`BuildSystem, BuildRequires` |
| 3431 | [fonts-noto-color-emoji/fonts-noto-color-emoji.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fonts-noto-color-emoji/fonts-noto-color-emoji.spec) | `BuildSystem, BuildRequires` | 缺少必填字段：`BuildSystem, BuildRequires` |
| 3432 | [mock-core-configs/mock-core-configs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mock-core-configs/mock-core-configs.spec) | `BuildSystem, BuildRequires` | 缺少必填字段：`BuildSystem, BuildRequires` |
| 3433 | [perl-rpm-packaging/perl-rpm-packaging.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-rpm-packaging/perl-rpm-packaging.spec) | `BuildSystem, BuildRequires` | 缺少必填字段：`BuildSystem, BuildRequires` |
| 3434 | [python-rpm-macros/python-rpm-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rpm-macros/python-rpm-macros.spec) | `BuildSystem, BuildRequires` | 缺少必填字段：`BuildSystem, BuildRequires` |
| 3435 | [libcroco/libcroco.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcroco/libcroco.spec) | `URL, VCS, Requires` | 缺少必填字段：`URL, VCS, Requires` |
| 3436 | [mtools/mtools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mtools/mtools.spec) | `URL, VCS, Requires` | 缺少必填字段：`URL, VCS, Requires` |
| 3437 | [openal-soft/openal-soft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openal-soft/openal-soft.spec) | `URL, VCS, Requires` | 缺少必填字段：`URL, VCS, Requires` |
| 3438 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | `URL, VCS, Requires` | 缺少必填字段：`URL, VCS, Requires` |
| 3439 | [python-norpm/python-norpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-norpm/python-norpm.spec) | `URL, VCS, Requires` | 缺少必填字段：`URL, VCS, Requires` |
| 3440 | [openruyi-config-linux-dnf/openruyi-config-linux-dnf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openruyi-config-linux-dnf/openruyi-config-linux-dnf.spec) | `Source, BuildSystem, BuildRequires` | 缺少必填字段：`Source, BuildSystem, BuildRequires` |
| 3441 | [python-griffe/python-griffe.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-griffe/python-griffe.spec) | `Source, BuildSystem, BuildRequires` | 缺少必填字段：`Source, BuildSystem, BuildRequires` |
| 3442 | [rpm-config-openruyi/rpm-config-openruyi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm-config-openruyi/rpm-config-openruyi.spec) | `Source, BuildSystem, BuildRequires` | 缺少必填字段：`Source, BuildSystem, BuildRequires` |
| 3443 | [kf6-rpm-macros/kf6-rpm-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-rpm-macros/kf6-rpm-macros.spec) | `URL, VCS, BuildSystem, BuildRequires` | 缺少必填字段：`URL, VCS, BuildSystem, BuildRequires` |
| 3444 | [openruyi-systemd-default-preset/openruyi-systemd-default-preset.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openruyi-systemd-default-preset/openruyi-systemd-default-preset.spec) | `URL, VCS, BuildSystem, BuildRequires` | 缺少必填字段：`URL, VCS, BuildSystem, BuildRequires` |
| 3445 | [qt6-macros/qt6-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-macros/qt6-macros.spec) | `URL, VCS, BuildSystem, BuildRequires` | 缺少必填字段：`URL, VCS, BuildSystem, BuildRequires` |
| 3446 | [db-ip/db-ip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/db-ip/db-ip.spec) | `VCS, BuildSystem, BuildRequires, Requires` | 缺少必填字段：`VCS, BuildSystem, BuildRequires, Requires` |
| 3447 | [openruyi-release/openruyi-release.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openruyi-release/openruyi-release.spec) | `VCS, BuildSystem, BuildRequires, Requires` | 缺少必填字段：`VCS, BuildSystem, BuildRequires, Requires` |
| 3448 | [publicsuffix-list/publicsuffix-list.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/publicsuffix-list/publicsuffix-list.spec) | `VCS, BuildSystem, BuildRequires, Requires` | 缺少必填字段：`VCS, BuildSystem, BuildRequires, Requires` |
| 3449 | [cloud-utils/cloud-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cloud-utils/cloud-utils.spec) | `BuildRequires` | 缺少必填字段：`BuildRequires` |
| 3450 | [perl-rpm-macros/perl-rpm-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-rpm-macros/perl-rpm-macros.spec) | `BuildRequires` | 缺少必填字段：`BuildRequires` |
| 3451 | [kaccounts-integration/kaccounts-integration.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kaccounts-integration/kaccounts-integration.spec) | `URL` | 缺少必填字段：`URL` |
| 3452 | [kaccounts-providers/kaccounts-providers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kaccounts-providers/kaccounts-providers.spec) | `URL` | 缺少必填字段：`URL` |
| 3453 | [osinfo-db-tools/osinfo-db-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/osinfo-db-tools/osinfo-db-tools.spec) | `URL, Requires` | 缺少必填字段：`URL, Requires` |
| 3454 | [postgresql/postgresql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postgresql/postgresql.spec) | `URL, Requires` | 缺少必填字段：`URL, Requires` |
| 3455 | [openruyi-desktop-setup-labwc/openruyi-desktop-setup-labwc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openruyi-desktop-setup-labwc/openruyi-desktop-setup-labwc.spec) | `URL, BuildSystem, BuildRequires` | 缺少必填字段：`URL, BuildSystem, BuildRequires` |
| 3456 | [cloud-hypervisor/cloud-hypervisor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cloud-hypervisor/cloud-hypervisor.spec) | `URL, VCS` | 缺少必填字段：`URL, VCS` |
| 3457 | [fonts-rpm-macros/fonts-rpm-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fonts-rpm-macros/fonts-rpm-macros.spec) | `URL, VCS, BuildSystem, BuildRequires, Requires` | 缺少必填字段：`URL, VCS, BuildSystem, BuildRequires, Requires` |
| 3458 | [color-rpm-macros/color-rpm-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/color-rpm-macros/color-rpm-macros.spec) | `URL, VCS, Source, BuildSystem, BuildRequires` | 缺少必填字段：`URL, VCS, Source, BuildSystem, BuildRequires` |
| 3459 | [langpacks/langpacks.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/langpacks/langpacks.spec) | `URL, VCS, Source, BuildSystem, BuildRequires, Requires` | 缺少必填字段：`URL, VCS, Source, BuildSystem, BuildRequires, Requires` |
| 3460 | [lzo/lzo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lzo/lzo.spec) | `VCS, BuildRequires, Requires` | 缺少必填字段：`VCS, BuildRequires, Requires` |
| 3461 | [openruyi-minimal/openruyi-minimal.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openruyi-minimal/openruyi-minimal.spec) | `VCS, Source, BuildSystem, BuildRequires` | 缺少必填字段：`VCS, Source, BuildSystem, BuildRequires` |
| 3462 | [openruyi-repos/openruyi-repos.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openruyi-repos/openruyi-repos.spec) | `VCS, Source, BuildSystem, BuildRequires, Requires` | 缺少必填字段：`VCS, Source, BuildSystem, BuildRequires, Requires` |
### 2. 头部字段乱序

| # | spec 文件 | 字段值 | 问题类型 |
| --- | --- | --- | --- |
| 1 | [aardvark-dns/aardvark-dns.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aardvark-dns/aardvark-dns.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 2 | [acl/acl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/acl/acl.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 3 | [binutils/binutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/binutils/binutils.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 4 | [boost/boost.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/boost/boost.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 5 | [chkconfig/chkconfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/chkconfig/chkconfig.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 6 | [clang-wrap/clang-wrap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/clang-wrap/clang-wrap.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 7 | [cloud-hypervisor/cloud-hypervisor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cloud-hypervisor/cloud-hypervisor.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 8 | [coreutils/coreutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/coreutils/coreutils.spec) | `Name` | 头部字段乱序：`Name` 出现在 `Summary` 之后 |
| 9 | [dkms/dkms.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dkms/dkms.spec) | `Name` | 头部字段乱序：`Name` 出现在 `Summary` 之后 |
| 10 | [gcc/gcc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc/gcc.spec) | `Version` | 头部字段乱序：`Version` 出现在 `URL` 之后 |
| 11 | [gcc16/gcc16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc16/gcc16.spec) | `Version` | 头部字段乱序：`Version` 出现在 `URL` 之后 |
| 12 | [glibc/glibc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glibc/glibc.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 13 | [gmp/gmp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gmp/gmp.spec) | `License` | 头部字段乱序：`License` 出现在 `URL` 之后 |
| 14 | [go-github-azure-azure-sdk-for-go/go-github-azure-azure-sdk-for-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-azure-azure-sdk-for-go/go-github-azure-azure-sdk-for-go.spec) | `Source` | 头部字段乱序：`Source` 出现在 `BuildSystem` 之后 |
| 15 | [go-github-moby-sys/go-github-moby-sys.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-moby-sys/go-github-moby-sys.spec) | `Source` | 头部字段乱序：`Source` 出现在 `BuildSystem` 之后 |
| 16 | [go-github-rcrowley-go-metrics/go-github-rcrowley-go-metrics.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-rcrowley-go-metrics/go-github-rcrowley-go-metrics.spec) | `BuildSystem` | 头部字段乱序：`BuildSystem` 出现在 `BuildRequires` 之后 |
| 17 | [graphviz/graphviz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/graphviz/graphviz.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 18 | [hipfft/hipfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipfft/hipfft.spec) | `License` | 头部字段乱序：`License` 出现在 `URL` 之后 |
| 19 | [hwloc/hwloc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hwloc/hwloc.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 20 | [iptstate/iptstate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iptstate/iptstate.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 21 | [ipvsadm/ipvsadm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ipvsadm/ipvsadm.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 22 | [kf6-kirigami/kf6-kirigami.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kirigami/kf6-kirigami.spec) | `BuildRequires` | 头部字段乱序：`BuildRequires` 出现在 `Requires` 之后 |
| 23 | [libcroco/libcroco.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcroco/libcroco.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 24 | [libdrm/libdrm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdrm/libdrm.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 25 | [libiscsi/libiscsi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libiscsi/libiscsi.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 26 | [libplacebo/libplacebo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libplacebo/libplacebo.spec) | `Release` | 头部字段乱序：`Release` 出现在 `License` 之后 |
| 27 | [libyuv/libyuv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libyuv/libyuv.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 28 | [lua/lua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua/lua.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 29 | [lzo/lzo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lzo/lzo.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 30 | [mesa/mesa.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mesa/mesa.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 31 | [minicom/minicom.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/minicom/minicom.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 32 | [mkosi/mkosi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mkosi/mkosi.spec) | `BuildSystem` | 头部字段乱序：`BuildSystem` 出现在 `BuildRequires` 之后 |
| 33 | [mlocate/mlocate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mlocate/mlocate.spec) | `Name` | 头部字段乱序：`Name` 出现在 `Summary` 之后 |
| 34 | [mtools/mtools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mtools/mtools.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 35 | [netavark/netavark.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/netavark/netavark.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 36 | [pigz/pigz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pigz/pigz.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 37 | [popt/popt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/popt/popt.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 38 | [procmail/procmail.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/procmail/procmail.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 39 | [pulseaudio/pulseaudio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pulseaudio/pulseaudio.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 40 | [pulseaudio-qt/pulseaudio-qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pulseaudio-qt/pulseaudio-qt.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 41 | [python-meson-python/python-meson-python.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-meson-python/python-meson-python.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 42 | [python-pdm-backend/python-pdm-backend.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pdm-backend/python-pdm-backend.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 43 | [python-pynacl/python-pynacl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pynacl/python-pynacl.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 44 | [python-pytest-asyncio/python-pytest-asyncio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-asyncio/python-pytest-asyncio.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 45 | [python-python-dotenv/python-python-dotenv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-dotenv/python-python-dotenv.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 46 | [python-torch/python-torch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-torch/python-torch.spec) | `Summary` | 头部字段乱序：`Summary` 出现在 `License` 之后 |
| 47 | [qca/qca.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qca/qca.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 48 | [range-v3/range-v3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/range-v3/range-v3.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 49 | [re2c/re2c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/re2c/re2c.spec) | `Name` | 头部字段乱序：`Name` 出现在 `Summary` 之后 |
| 50 | [rocblas/rocblas.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocblas/rocblas.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 51 | [rocthrust/rocthrust.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocthrust/rocthrust.spec) | `License` | 头部字段乱序：`License` 出现在 `URL` 之后 |
| 52 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 53 | [smartmontools/smartmontools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/smartmontools/smartmontools.spec) | `Name` | 头部字段乱序：`Name` 出现在 `Summary` 之后 |
| 54 | [taglib/taglib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/taglib/taglib.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 55 | [tbb/tbb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tbb/tbb.spec) | `Version` | 头部字段乱序：`Version` 出现在 `Summary` 之后 |
| 56 | [vdo/vdo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vdo/vdo.spec) | `Name` | 头部字段乱序：`Name` 出现在 `Summary` 之后 |

### 3. 段落前缺少空行

`%description`、`%files`、`%changelog`、`%package`、`%prep`、`%build`、`%install`、`%check`
段落之间必须以空行分隔。

| # | spec 文件 | 字段值 | 问题类型 |
| --- | --- | --- | --- |
| 1 | [bluez/bluez.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bluez/bluez.spec) | `%files hid2hci` | 段落前缺少空行 |
| 2 | [cloud-utils/cloud-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cloud-utils/cloud-utils.spec) | `%description    vcs-run` | 段落前缺少空行 |
| 3 | [drpm/drpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/drpm/drpm.spec) | `%changelog` | 段落前缺少空行 |
| 4 | [glib/glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glib/glib.spec) | `%description    tests` | 段落前缺少空行 |
| 5 | [htop/htop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/htop/htop.spec) | `%description` | 段落前缺少空行 |
| 6 | [iprutils/iprutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iprutils/iprutils.spec) | `%changelog` | 段落前缺少空行 |
| 7 | [lzo/lzo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lzo/lzo.spec) | `%description` | 段落前缺少空行 |
| 8 | [mkosi/mkosi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mkosi/mkosi.spec) | `%description   addon` | 段落前缺少空行 |
| 9 | [NetworkManager/NetworkManager.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/NetworkManager/NetworkManager.spec) | `%files tui` | 段落前缺少空行 |
| 10 | [python-qemu-qmp/python-qemu-qmp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-qemu-qmp/python-qemu-qmp.spec) | `%description    doc` | 段落前缺少空行 |
| 11 | [xfsprogs/xfsprogs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xfsprogs/xfsprogs.spec) | `%check` | 段落前缺少空行 |

## 说明

- 本次扫描基于 [check-spec-structure](../docs/check-spec-structure.md) 规则的校验逻辑。
- 扫描脚本与本仓库 hook 使用同一套判定逻辑（`_check_spec_structure`），无额外过滤。
- `%if`/`%endif` 条件块后紧跟段落属于 RPM 合法写法，不判违规。
- `Source` 匹配 `Source`/`Source0`/`Source1` 等所有变体。
- 当 `URL` 为源代码仓库链接时，`VCS` 缺失不判违规。
