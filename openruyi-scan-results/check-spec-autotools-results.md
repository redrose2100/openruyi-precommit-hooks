# check-spec-autotools 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-autotools` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | autotools | 通过 | 问题 |
| --- | ---: | ---: | ---: |
| 5267 | 675 | 193 | 482 |

## 问题类型分布

按缺失依赖统计：

| 缺失依赖 | 文件数 |
| --- | ---: |
| `autoconf` | 364 |
| `automake` | 363 |
| `libtool` | 388 |
| `make` | 232 |

按缺失组合统计：

| 缺失组合 | 文件数 |
| --- | ---: |
| 缺 3 项：`autoconf`, `automake`, `libtool` | 180 |
| 缺 4 项：`autoconf`, `automake`, `libtool`, `make` | 138 |
| 缺 1 项：`make` | 52 |
| 缺 1 项：`libtool` | 35 |
| 缺 3 项：`autoconf`, `automake`, `make` | 15 |
| 缺 2 项：`libtool`, `make` | 14 |
| 缺 2 项：`autoconf`, `automake` | 13 |
| 缺 1 项：`autoconf` | 7 |
| 缺 3 项：`automake`, `libtool`, `make` | 6 |
| 缺 2 项：`autoconf`, `libtool` | 6 |
| 缺 2 项：`automake`, `libtool` | 5 |
| 缺 1 项：`automake` | 4 |
| 缺 3 项：`autoconf`, `libtool`, `make` | 4 |
| 缺 2 项：`automake`, `make` | 2 |
| 缺 2 项：`autoconf`, `make` | 1 |

## 问题清单（482 条）

| # | spec 文件 | 缺失依赖 | BuildSystem 所在行数 |
| --- | --- | --- | ---: |
| 1 | [accounts-qml-module/accounts-qml-module.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/accounts-qml-module/accounts-qml-module.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 2 | [acl/acl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/acl/acl.spec) | `make` | 18 |
| 3 | [acpica/acpica.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/acpica/acpica.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 4 | [acpid/acpid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/acpid/acpid.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 5 | [aflplusplus/aflplusplus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aflplusplus/aflplusplus.spec) | `autoconf`, `automake`, `libtool` | 27 |
| 6 | [aha/aha.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aha/aha.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 7 | [apr/apr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/apr/apr.spec) | `automake` | 17 |
| 8 | [apr-util/apr-util.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/apr-util/apr-util.spec) | `automake`, `libtool`, `make` | 23 |
| 9 | [argon2/argon2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/argon2/argon2.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 10 | [asn1c/asn1c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/asn1c/asn1c.spec) | `make` | 18 |
| 11 | [atf/atf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/atf/atf.spec) | `autoconf` | 17 |
| 12 | [attr/attr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/attr/attr.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 13 | [audiofile/audiofile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/audiofile/audiofile.spec) | `autoconf`, `automake` | 15 |
| 14 | [audit/audit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/audit/audit.spec) | `automake`, `make` | 19 |
| 15 | [authselect/authselect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/authselect/authselect.spec) | `make` | 27 |
| 16 | [autoconf/autoconf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/autoconf/autoconf.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 17 | [autoconf-archive/autoconf-archive.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/autoconf-archive/autoconf-archive.spec) | `autoconf`, `automake`, `libtool`, `make` | 21 |
| 18 | [autofs/autofs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/autofs/autofs.spec) | `libtool` | 18 |
| 19 | [automake/automake.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/automake/automake.spec) | `automake`, `libtool`, `make` | 20 |
| 20 | [bash/bash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bash/bash.spec) | `automake`, `libtool` | 23 |
| 21 | [bash-completion/bash-completion.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bash-completion/bash-completion.spec) | `autoconf`, `libtool` | 18 |
| 22 | [bc/bc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bc/bc.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 23 | [bdfresize/bdfresize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bdfresize/bdfresize.spec) | `libtool` | 17 |
| 24 | [beakerlib/beakerlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/beakerlib/beakerlib.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 25 | [bind/bind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bind/bind.spec) | `make` | 30 |
| 26 | [bindfs/bindfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bindfs/bindfs.spec) | `libtool` | 18 |
| 27 | [binutils/binutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/binutils/binutils.spec) | `autoconf`, `automake`, `libtool`, `make` | 24 |
| 28 | [bison/bison.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bison/bison.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 29 | [blktests/blktests.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/blktests/blktests.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 30 | [blktrace/blktrace.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/blktrace/blktrace.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 31 | [boost/boost.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/boost/boost.spec) | `autoconf`, `automake`, `libtool`, `make` | 25 |
| 32 | [bpftool/bpftool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bpftool/bpftool.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 33 | [btrfs-progs/btrfs-progs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/btrfs-progs/btrfs-progs.spec) | `libtool` | 19 |
| 34 | [buildah/buildah.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/buildah/buildah.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 35 | [busybox/busybox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/busybox/busybox.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 36 | [byacc/byacc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/byacc/byacc.spec) | `autoconf`, `automake`, `libtool`, `make` | 21 |
| 37 | [bzip2/bzip2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bzip2/bzip2.spec) | `automake`, `make` | 21 |
| 38 | [cdparanoia/cdparanoia.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cdparanoia/cdparanoia.spec) | `libtool` | 16 |
| 39 | [check/check.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/check/check.spec) | `make` | 18 |
| 40 | [checkpolicy/checkpolicy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/checkpolicy/checkpolicy.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 41 | [chkconfig/chkconfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/chkconfig/chkconfig.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 42 | [chrony/chrony.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/chrony/chrony.spec) | `autoconf`, `automake`, `libtool` | 21 |
| 43 | [chrpath/chrpath.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/chrpath/chrpath.spec) | `libtool` | 16 |
| 44 | [ck/ck.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ck/ck.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 45 | [cloud-utils/cloud-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cloud-utils/cloud-utils.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 46 | [clzip/clzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/clzip/clzip.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 47 | [cmake/cmake.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cmake/cmake.spec) | `autoconf`, `automake`, `libtool`, `make` | 33 |
| 48 | [cockpit/cockpit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cockpit/cockpit.spec) | `libtool` | 19 |
| 49 | [compsize/compsize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/compsize/compsize.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 50 | [conmon/conmon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/conmon/conmon.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 51 | [conntrack-tools/conntrack-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/conntrack-tools/conntrack-tools.spec) | `autoconf`, `automake`, `libtool` | 22 |
| 52 | [console-setup/console-setup.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/console-setup/console-setup.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 53 | [convmv/convmv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/convmv/convmv.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 54 | [coreutils/coreutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/coreutils/coreutils.spec) | `libtool`, `make` | 17 |
| 55 | [cpio/cpio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cpio/cpio.spec) | `libtool`, `make` | 20 |
| 56 | [cpp-threadpool/cpp-threadpool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cpp-threadpool/cpp-threadpool.spec) | `autoconf`, `automake`, `libtool`, `make` | 21 |
| 57 | [cppunit/cppunit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cppunit/cppunit.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 58 | [cracklib/cracklib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cracklib/cracklib.spec) | `autoconf`, `automake`, `libtool`, `make` | 21 |
| 59 | [crash/crash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crash/crash.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 60 | [crun/crun.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crun/crun.spec) | `make` | 20 |
| 61 | [cryptopp/cryptopp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cryptopp/cryptopp.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 62 | [cunit/cunit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cunit/cunit.spec) | `make` | 20 |
| 63 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `autoconf`, `libtool` | 22 |
| 64 | [curl/curl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/curl/curl.spec) | `autoconf`, `automake`, `make` | 23 |
| 65 | [curl-impersonate-chrome/curl-impersonate-chrome.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/curl-impersonate-chrome/curl-impersonate-chrome.spec) | `autoconf`, `automake` | 20 |
| 66 | [cyrus-sasl/cyrus-sasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cyrus-sasl/cyrus-sasl.spec) | `autoconf`, `automake`, `make` | 18 |
| 67 | [dash/dash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dash/dash.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 68 | [dbus-glib/dbus-glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dbus-glib/dbus-glib.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 69 | [debugedit/debugedit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/debugedit/debugedit.spec) | `libtool`, `make` | 18 |
| 70 | [deltarpm/deltarpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/deltarpm/deltarpm.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 71 | [dhcpcd/dhcpcd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dhcpcd/dhcpcd.spec) | `autoconf`, `automake`, `libtool` | 24 |
| 72 | [diffutils/diffutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/diffutils/diffutils.spec) | `autoconf`, `automake`, `libtool`, `make` | 22 |
| 73 | [ding-libs/ding-libs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ding-libs/ding-libs.spec) | `make` | 17 |
| 74 | [djvulibre/djvulibre.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/djvulibre/djvulibre.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 75 | [dmidecode/dmidecode.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dmidecode/dmidecode.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 76 | [dnsmasq/dnsmasq.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dnsmasq/dnsmasq.spec) | `autoconf`, `automake`, `libtool`, `make` | 22 |
| 77 | [docbook2x/docbook2x.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook2x/docbook2x.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 78 | [dos2unix/dos2unix.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dos2unix/dos2unix.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 79 | [dosfstools/dosfstools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dosfstools/dosfstools.spec) | `libtool`, `make` | 16 |
| 80 | [dracut/dracut.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dracut/dracut.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 81 | [dropbear/dropbear.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dropbear/dropbear.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 82 | [dtc/dtc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dtc/dtc.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 83 | [duktape/duktape.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/duktape/duktape.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 84 | [dwz/dwz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dwz/dwz.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 85 | [e2fsprogs/e2fsprogs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/e2fsprogs/e2fsprogs.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 86 | [efi-rpm-macros/efi-rpm-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/efi-rpm-macros/efi-rpm-macros.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 87 | [efibootmgr/efibootmgr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/efibootmgr/efibootmgr.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 88 | [efitools/efitools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/efitools/efitools.spec) | `autoconf`, `automake`, `libtool` | 21 |
| 89 | [efivar/efivar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/efivar/efivar.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 90 | [elfutils/elfutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/elfutils/elfutils.spec) | `libtool` | 18 |
| 91 | [erofs-utils/erofs-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/erofs-utils/erofs-utils.spec) | `make` | 17 |
| 92 | [ethtool/ethtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ethtool/ethtool.spec) | `autoconf`, `automake`, `libtool`, `make` | 22 |
| 93 | [expat/expat.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expat/expat.spec) | `automake` | 19 |
| 94 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `automake`, `libtool`, `make` | 20 |
| 95 | [fdk-aac/fdk-aac.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fdk-aac/fdk-aac.spec) | `autoconf` | 16 |
| 96 | [fdupes/fdupes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fdupes/fdupes.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 97 | [ffmpeg/ffmpeg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ffmpeg/ffmpeg.spec) | `autoconf`, `automake`, `libtool` | 40 |
| 98 | [ffnvcodec/ffnvcodec.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ffnvcodec/ffnvcodec.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 99 | [findutils/findutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/findutils/findutils.spec) | `autoconf`, `libtool`, `make` | 21 |
| 100 | [fio/fio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fio/fio.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 101 | [flex/flex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/flex/flex.spec) | `make` | 16 |
| 102 | [fscryptctl/fscryptctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fscryptctl/fscryptctl.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 103 | [fzf/fzf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fzf/fzf.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 104 | [gawk/gawk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gawk/gawk.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 105 | [gc/gc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gc/gc.spec) | `autoconf`, `automake`, `make` | 19 |
| 106 | [gd/gd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gd/gd.spec) | `make` | 21 |
| 107 | [gdb/gdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gdb/gdb.spec) | `autoconf`, `automake`, `libtool`, `make` | 22 |
| 108 | [gdbm/gdbm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gdbm/gdbm.spec) | `autoconf`, `automake`, `make` | 19 |
| 109 | [genimage/genimage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/genimage/genimage.spec) | `make` | 17 |
| 110 | [giflib/giflib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/giflib/giflib.spec) | `autoconf`, `automake` | 18 |
| 111 | [git/git.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/git/git.spec) | `autoconf`, `automake`, `libtool` | 30 |
| 112 | [glew/glew.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glew/glew.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 113 | [gmp/gmp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gmp/gmp.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 114 | [gnu-efi/gnu-efi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gnu-efi/gnu-efi.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 115 | [gnulib/gnulib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gnulib/gnulib.spec) | `make` | 19 |
| 116 | [gnupg/gnupg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gnupg/gnupg.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 117 | [gnutls/gnutls.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gnutls/gnutls.spec) | `autoconf`, `automake` | 18 |
| 118 | [gperf/gperf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gperf/gperf.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 119 | [gpgme/gpgme.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpgme/gpgme.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 120 | [gptfdisk/gptfdisk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gptfdisk/gptfdisk.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 121 | [groff/groff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/groff/groff.spec) | `autoconf`, `automake`, `libtool`, `make` | 21 |
| 122 | [gsasl/gsasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gsasl/gsasl.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 123 | [gsm/gsm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gsm/gsm.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 124 | [guile/guile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/guile/guile.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 125 | [gzip/gzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gzip/gzip.spec) | `libtool`, `make` | 19 |
| 126 | [haproxy/haproxy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/haproxy/haproxy.spec) | `autoconf`, `automake`, `libtool`, `make` | 22 |
| 127 | [haveged/haveged.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/haveged/haveged.spec) | `autoconf`, `libtool` | 19 |
| 128 | [hdparm/hdparm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hdparm/hdparm.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 129 | [help2man/help2man.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/help2man/help2man.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 130 | [hostname/hostname.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hostname/hostname.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 131 | [htop/htop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/htop/htop.spec) | `libtool`, `make` | 18 |
| 132 | [httpd/httpd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/httpd/httpd.spec) | `make` | 31 |
| 133 | [hwdata/hwdata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hwdata/hwdata.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 134 | [hwinfo/hwinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hwinfo/hwinfo.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 135 | [hwloc/hwloc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hwloc/hwloc.spec) | `autoconf`, `automake`, `libtool` | 22 |
| 136 | [i2c-tools/i2c-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/i2c-tools/i2c-tools.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 137 | [ibus/ibus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ibus/ibus.spec) | `autoconf`, `libtool`, `make` | 15 |
| 138 | [icu4c/icu4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/icu4c/icu4c.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 139 | [indent/indent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/indent/indent.spec) | `libtool` | 16 |
| 140 | [inetutils/inetutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/inetutils/inetutils.spec) | `libtool` | 16 |
| 141 | [intltool/intltool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/intltool/intltool.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 142 | [iotop/iotop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iotop/iotop.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 143 | [iperf/iperf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iperf/iperf.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 144 | [iproute2/iproute2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iproute2/iproute2.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 145 | [iprutils/iprutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iprutils/iprutils.spec) | `make` | 20 |
| 146 | [iptables/iptables.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iptables/iptables.spec) | `autoconf`, `automake`, `make` | 23 |
| 147 | [iptraf-ng/iptraf-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iptraf-ng/iptraf-ng.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 148 | [iptstate/iptstate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iptstate/iptstate.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 149 | [ipvsadm/ipvsadm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ipvsadm/ipvsadm.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 150 | [isl/isl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/isl/isl.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 151 | [iso-codes/iso-codes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iso-codes/iso-codes.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 152 | [isomd5sum/isomd5sum.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/isomd5sum/isomd5sum.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 153 | [itstool/itstool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/itstool/itstool.spec) | `make` | 18 |
| 154 | [iw/iw.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iw/iw.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 155 | [iwd/iwd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iwd/iwd.spec) | `autoconf`, `automake` | 17 |
| 156 | [jansson/jansson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jansson/jansson.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 157 | [jbigkit/jbigkit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jbigkit/jbigkit.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 158 | [jitterentropy/jitterentropy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jitterentropy/jitterentropy.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 159 | [jq/jq.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jq/jq.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 160 | [kbd/kbd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kbd/kbd.spec) | `autoconf`, `libtool` | 20 |
| 161 | [keepalived/keepalived.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/keepalived/keepalived.spec) | `autoconf`, `automake`, `libtool` | 27 |
| 162 | [kexec-tools/kexec-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kexec-tools/kexec-tools.spec) | `libtool`, `make` | 18 |
| 163 | [keybinder/keybinder.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/keybinder/keybinder.spec) | `autoconf`, `automake` | 18 |
| 164 | [keyutils/keyutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/keyutils/keyutils.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 165 | [kmod/kmod.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kmod/kmod.spec) | `autoconf` | 16 |
| 166 | [krb5/krb5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/krb5/krb5.spec) | `automake`, `libtool`, `make` | 24 |
| 167 | [lame/lame.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lame/lame.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 168 | [ldns/ldns.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ldns/ldns.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 169 | [less/less.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/less/less.spec) | `autoconf`, `libtool`, `make` | 18 |
| 170 | [libabigail/libabigail.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libabigail/libabigail.spec) | `autoconf`, `automake`, `make` | 16 |
| 171 | [libaccounts-qt/libaccounts-qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libaccounts-qt/libaccounts-qt.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 172 | [libaio/libaio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libaio/libaio.spec) | `autoconf`, `automake`, `libtool` | 22 |
| 173 | [libarchive/libarchive.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libarchive/libarchive.spec) | `autoconf`, `automake`, `make` | 18 |
| 174 | [libass/libass.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libass/libass.spec) | `make` | 16 |
| 175 | [libassuan/libassuan.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libassuan/libassuan.spec) | `autoconf`, `automake` | 23 |
| 176 | [libatasmart/libatasmart.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libatasmart/libatasmart.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 177 | [libatomic_ops/libatomic_ops.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libatomic_ops/libatomic_ops.spec) | `make` | 17 |
| 178 | [libblockdev/libblockdev.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libblockdev/libblockdev.spec) | `autoconf` | 17 |
| 179 | [libbpf/libbpf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libbpf/libbpf.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 180 | [libbsd/libbsd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libbsd/libbsd.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 181 | [libcaca/libcaca.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcaca/libcaca.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 182 | [libcanberra/libcanberra.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcanberra/libcanberra.spec) | `autoconf`, `automake` | 16 |
| 183 | [libcap/libcap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcap/libcap.spec) | `autoconf`, `automake`, `libtool`, `make` | 25 |
| 184 | [libcap-ng/libcap-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcap-ng/libcap-ng.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 185 | [libcdata/libcdata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcdata/libcdata.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 186 | [libcdio/libcdio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcdio/libcdio.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 187 | [libcdio-paranoia/libcdio-paranoia.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcdio-paranoia/libcdio-paranoia.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 188 | [libcerror/libcerror.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcerror/libcerror.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 189 | [libcgroup/libcgroup.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcgroup/libcgroup.spec) | `make` | 17 |
| 190 | [libcnotify/libcnotify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcnotify/libcnotify.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 191 | [libconfuse/libconfuse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libconfuse/libconfuse.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 192 | [libcroco/libcroco.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcroco/libcroco.spec) | `autoconf`, `automake`, `libtool`, `make` | 15 |
| 193 | [libcthreads/libcthreads.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcthreads/libcthreads.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 194 | [libdaemon/libdaemon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdaemon/libdaemon.spec) | `make` | 18 |
| 195 | [libedit/libedit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libedit/libedit.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 196 | [libestr/libestr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libestr/libestr.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 197 | [libev/libev.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libev/libev.spec) | `autoconf`, `automake`, `libtool`, `make` | 24 |
| 198 | [libevdev/libevdev.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libevdev/libevdev.spec) | `autoconf`, `make` | 17 |
| 199 | [libevent/libevent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libevent/libevent.spec) | `make` | 19 |
| 200 | [libfaketime/libfaketime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfaketime/libfaketime.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 201 | [libfastjson/libfastjson.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfastjson/libfastjson.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 202 | [libfcache/libfcache.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfcache/libfcache.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 203 | [libfdata/libfdata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfdata/libfdata.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 204 | [libgcrypt/libgcrypt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libgcrypt/libgcrypt.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 205 | [libgpg-error/libgpg-error.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libgpg-error/libgpg-error.spec) | `autoconf`, `automake`, `make` | 17 |
| 206 | [libiberty/libiberty.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libiberty/libiberty.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 207 | [libICE/libICE.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libICE/libICE.spec) | `make` | 18 |
| 208 | [libiconv/libiconv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libiconv/libiconv.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 209 | [libidn2/libidn2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libidn2/libidn2.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 210 | [libiscsi/libiscsi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libiscsi/libiscsi.spec) | `make` | 16 |
| 211 | [libkcapi/libkcapi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libkcapi/libkcapi.spec) | `autoconf`, `automake`, `make` | 20 |
| 212 | [libklvanc/libklvanc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libklvanc/libklvanc.spec) | `make` | 16 |
| 213 | [libksba/libksba.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libksba/libksba.spec) | `make` | 22 |
| 214 | [liblognorm/liblognorm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/liblognorm/liblognorm.spec) | `make` | 18 |
| 215 | [libmd/libmd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmd/libmd.spec) | `autoconf`, `automake`, `libtool`, `make` | 21 |
| 216 | [libmicrohttpd/libmicrohttpd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmicrohttpd/libmicrohttpd.spec) | `autoconf`, `automake`, `make` | 18 |
| 217 | [libmnl/libmnl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmnl/libmnl.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 218 | [libmspack/libmspack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmspack/libmspack.spec) | `make` | 18 |
| 219 | [libmtp/libmtp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmtp/libmtp.spec) | `autoconf`, `automake` | 15 |
| 220 | [libmypaint/libmypaint.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmypaint/libmypaint.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 221 | [libndp/libndp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libndp/libndp.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 222 | [libnetfilter_acct/libnetfilter_acct.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_acct/libnetfilter_acct.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 223 | [libnetfilter_cttimeout/libnetfilter_cttimeout.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_cttimeout/libnetfilter_cttimeout.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 224 | [libnfs/libnfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnfs/libnfs.spec) | `autoconf` | 17 |
| 225 | [libnftnl/libnftnl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnftnl/libnftnl.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 226 | [libnl/libnl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnl/libnl.spec) | `autoconf`, `automake`, `make` | 19 |
| 227 | [libotf/libotf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libotf/libotf.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 228 | [libpcap/libpcap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libpcap/libpcap.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 229 | [libpipeline/libpipeline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libpipeline/libpipeline.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 230 | [libplist/libplist.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libplist/libplist.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 231 | [libpwquality/libpwquality.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libpwquality/libpwquality.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 232 | [libsamplerate/libsamplerate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsamplerate/libsamplerate.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 233 | [libseccomp/libseccomp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libseccomp/libseccomp.spec) | `make` | 20 |
| 234 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | `autoconf`, `automake`, `libtool`, `make` | 21 |
| 235 | [libsemanage/libsemanage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsemanage/libsemanage.spec) | `autoconf`, `automake`, `libtool` | 21 |
| 236 | [libsepol/libsepol.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsepol/libsepol.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 237 | [libsigsegv/libsigsegv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsigsegv/libsigsegv.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 238 | [libSM/libSM.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libSM/libSM.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 239 | [libsndfile/libsndfile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsndfile/libsndfile.spec) | `autoconf`, `automake` | 16 |
| 240 | [libsodium/libsodium.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsodium/libsodium.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 241 | [libspiro/libspiro.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libspiro/libspiro.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 242 | [libssh2/libssh2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libssh2/libssh2.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 243 | [libtar/libtar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtar/libtar.spec) | `make` | 18 |
| 244 | [libtasn1/libtasn1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtasn1/libtasn1.spec) | `libtool`, `make` | 19 |
| 245 | [libthai/libthai.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libthai/libthai.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 246 | [libtirpc/libtirpc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtirpc/libtirpc.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 247 | [libtomcrypt/libtomcrypt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtomcrypt/libtomcrypt.spec) | `autoconf`, `automake` | 20 |
| 248 | [libtommath/libtommath.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtommath/libtommath.spec) | `autoconf`, `automake` | 21 |
| 249 | [libtree/libtree.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtree/libtree.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 250 | [libudev-zero/libudev-zero.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libudev-zero/libudev-zero.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 251 | [libunibreak/libunibreak.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libunibreak/libunibreak.spec) | `make` | 18 |
| 252 | [libunistring/libunistring.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libunistring/libunistring.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 253 | [liburing/liburing.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/liburing/liburing.spec) | `make` | 17 |
| 254 | [libutempter/libutempter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libutempter/libutempter.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 255 | [libuv/libuv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libuv/libuv.spec) | `make` | 20 |
| 256 | [libvpx/libvpx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libvpx/libvpx.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 257 | [libX11/libX11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libX11/libX11.spec) | `make` | 18 |
| 258 | [libx86emu/libx86emu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libx86emu/libx86emu.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 259 | [libXau/libXau.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXau/libXau.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 260 | [libxcb/libxcb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxcb/libxcb.spec) | `make` | 22 |
| 261 | [libxcrypt/libxcrypt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxcrypt/libxcrypt.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 262 | [libXdmcp/libXdmcp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXdmcp/libXdmcp.spec) | `make` | 17 |
| 263 | [libXfixes/libXfixes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXfixes/libXfixes.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 264 | [libXi/libXi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXi/libXi.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 265 | [libxkbfile/libxkbfile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxkbfile/libxkbfile.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 266 | [libxml2/libxml2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxml2/libxml2.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 267 | [libXrandr/libXrandr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXrandr/libXrandr.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 268 | [libxshmfence/libxshmfence.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxshmfence/libxshmfence.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 269 | [libxslt/libxslt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxslt/libxslt.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 270 | [libXtst/libXtst.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXtst/libXtst.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 271 | [libXxf86vm/libXxf86vm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXxf86vm/libXxf86vm.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 272 | [libyaml/libyaml.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libyaml/libyaml.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 273 | [lighttpd/lighttpd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lighttpd/lighttpd.spec) | `make` | 30 |
| 274 | [lm_sensors/lm_sensors.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lm_sensors/lm_sensors.spec) | `autoconf`, `automake`, `libtool`, `make` | 34 |
| 275 | [lmbench/lmbench.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lmbench/lmbench.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 276 | [lmdb/lmdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lmdb/lmdb.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 277 | [log4cplus/log4cplus.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/log4cplus/log4cplus.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 278 | [lsb-release/lsb-release.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lsb-release/lsb-release.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 279 | [lshw/lshw.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lshw/lshw.spec) | `autoconf`, `automake`, `libtool` | 21 |
| 280 | [lsof/lsof.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lsof/lsof.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 281 | [lsscsi/lsscsi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lsscsi/lsscsi.spec) | `libtool` | 17 |
| 282 | [ltp/ltp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ltp/ltp.spec) | `libtool`, `make` | 20 |
| 283 | [lua-json/lua-json.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua-json/lua-json.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 284 | [lua-lpeg/lua-lpeg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua-lpeg/lua-lpeg.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 285 | [luajit/luajit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/luajit/luajit.spec) | `autoconf`, `automake`, `libtool` | 27 |
| 286 | [luarocks/luarocks.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/luarocks/luarocks.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 287 | [lvm2/lvm2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lvm2/lvm2.spec) | `autoconf`, `automake`, `libtool` | 26 |
| 288 | [lz4/lz4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lz4/lz4.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 289 | [lzlib/lzlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lzlib/lzlib.spec) | `libtool`, `make` | 17 |
| 290 | [lzo/lzo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lzo/lzo.spec) | `autoconf`, `automake`, `libtool`, `make` | 15 |
| 291 | [m4/m4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/m4/m4.spec) | `libtool` | 25 |
| 292 | [mailcap/mailcap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mailcap/mailcap.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 293 | [make/make.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/make/make.spec) | `libtool` | 19 |
| 294 | [man-db/man-db.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/man-db/man-db.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 295 | [mandoc/mandoc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mandoc/mandoc.spec) | `autoconf`, `automake`, `libtool`, `make` | 21 |
| 296 | [mdadm/mdadm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mdadm/mdadm.spec) | `autoconf`, `automake`, `libtool` | 24 |
| 297 | [mdevd/mdevd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mdevd/mdevd.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 298 | [memcached/memcached.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/memcached/memcached.spec) | `libtool`, `make` | 23 |
| 299 | [mergerfs/mergerfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mergerfs/mergerfs.spec) | `autoconf`, `automake`, `make` | 16 |
| 300 | [mergerfs-tools/mergerfs-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mergerfs-tools/mergerfs-tools.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 301 | [minicom/minicom.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/minicom/minicom.spec) | `libtool` | 17 |
| 302 | [mksh/mksh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mksh/mksh.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 303 | [mlocate/mlocate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mlocate/mlocate.spec) | `libtool`, `make` | 19 |
| 304 | [mod_http2/mod_http2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mod_http2/mod_http2.spec) | `automake` | 18 |
| 305 | [mokutil/mokutil.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mokutil/mokutil.spec) | `make` | 17 |
| 306 | [mpc/mpc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mpc/mpc.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 307 | [mpdecimal/mpdecimal.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mpdecimal/mpdecimal.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 308 | [mtdev/mtdev.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mtdev/mtdev.spec) | `make` | 18 |
| 309 | [mtools/mtools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mtools/mtools.spec) | `libtool` | 16 |
| 310 | [mujs/mujs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mujs/mujs.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 311 | [multipath-tools/multipath-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/multipath-tools/multipath-tools.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 312 | [mupdf/mupdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mupdf/mupdf.spec) | `autoconf`, `automake`, `libtool` | 21 |
| 313 | [musl/musl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/musl/musl.spec) | `autoconf`, `automake`, `libtool` | 25 |
| 314 | [nano/nano.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nano/nano.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 315 | [nasm/nasm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nasm/nasm.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 316 | [ncurses/ncurses.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ncurses/ncurses.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 317 | [netperf/netperf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/netperf/netperf.spec) | `libtool` | 20 |
| 318 | [nettle/nettle.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nettle/nettle.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 319 | [newt/newt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/newt/newt.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 320 | [nfs-utils/nfs-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nfs-utils/nfs-utils.spec) | `make` | 22 |
| 321 | [nghttp2/nghttp2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nghttp2/nghttp2.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 322 | [nginx/nginx.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nginx/nginx.spec) | `autoconf`, `automake`, `libtool` | 24 |
| 323 | [ngtcp2/ngtcp2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ngtcp2/ngtcp2.spec) | `automake` | 19 |
| 324 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `autoconf`, `automake`, `libtool` | 38 |
| 325 | [npth/npth.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/npth/npth.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 326 | [nspr/nspr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nspr/nspr.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 327 | [nss/nss.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nss/nss.spec) | `autoconf`, `automake`, `libtool` | 25 |
| 328 | [oniguruma/oniguruma.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/oniguruma/oniguruma.spec) | `make` | 18 |
| 329 | [open-vmdk/open-vmdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/open-vmdk/open-vmdk.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 330 | [openblas/openblas.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openblas/openblas.spec) | `autoconf`, `automake`, `libtool`, `make` | 21 |
| 331 | [openjade/openjade.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openjade/openjade.spec) | `libtool` | 16 |
| 332 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `autoconf`, `automake`, `make` | 37 |
| 333 | [openntpd/openntpd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openntpd/openntpd.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 334 | [openresolv/openresolv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openresolv/openresolv.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 335 | [openssh/openssh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openssh/openssh.spec) | `libtool` | 35 |
| 336 | [openssl/openssl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openssl/openssl.spec) | `autoconf`, `automake`, `libtool` | 28 |
| 337 | [os-prober/os-prober.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/os-prober/os-prober.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 338 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | `libtool` | 18 |
| 339 | [p7zip/p7zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/p7zip/p7zip.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 340 | [parallel/parallel.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/parallel/parallel.spec) | `libtool` | 21 |
| 341 | [passt/passt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/passt/passt.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 342 | [patch/patch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/patch/patch.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 343 | [pbzip2/pbzip2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pbzip2/pbzip2.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 344 | [pciutils/pciutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pciutils/pciutils.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 345 | [perl/perl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl/perl.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 346 | [perl-libintl-perl/perl-libintl-perl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-libintl-perl/perl-libintl-perl.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 347 | [perl-Locale-gettext/perl-Locale-gettext.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Locale-gettext/perl-Locale-gettext.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 348 | [perl-rpm-macros/perl-rpm-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-rpm-macros/perl-rpm-macros.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 349 | [pesign/pesign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `autoconf`, `automake`, `libtool` | 21 |
| 350 | [php/php.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/php/php.spec) | `autoconf`, `automake`, `libtool`, `make` | 24 |
| 351 | [picocom/picocom.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/picocom/picocom.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 352 | [pigz/pigz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pigz/pigz.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 353 | [pinentry/pinentry.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinentry/pinentry.spec) | `libtool` | 28 |
| 354 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `autoconf` | 17 |
| 355 | [pixz/pixz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pixz/pixz.spec) | `libtool`, `make` | 17 |
| 356 | [plzip/plzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/plzip/plzip.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 357 | [podman/podman.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/podman/podman.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 358 | [policycoreutils/policycoreutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/policycoreutils/policycoreutils.spec) | `autoconf`, `automake`, `libtool` | 37 |
| 359 | [poppler-data/poppler-data.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/poppler-data/poppler-data.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 360 | [popt/popt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/popt/popt.spec) | `make` | 16 |
| 361 | [postfix/postfix.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postfix/postfix.spec) | `autoconf`, `automake`, `libtool` | 25 |
| 362 | [postgresql/postgresql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postgresql/postgresql.spec) | `autoconf`, `automake`, `libtool` | 32 |
| 363 | [procmail/procmail.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/procmail/procmail.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 364 | [protobuf-c/protobuf-c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/protobuf-c/protobuf-c.spec) | `libtool` | 17 |
| 365 | [prrte/prrte.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/prrte/prrte.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 366 | [psutils/psutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/psutils/psutils.spec) | `libtool` | 20 |
| 367 | [pv/pv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pv/pv.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 368 | [python/python.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python/python.spec) | `automake`, `libtool` | 120 |
| 369 | [python-blivet/python-blivet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-blivet/python-blivet.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 370 | [python-meh/python-meh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-meh/python-meh.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 371 | [python-pyparted/python-pyparted.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyparted/python-pyparted.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 372 | [python-pyqt6/python-pyqt6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyqt6/python-pyqt6.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 373 | [python-simpleline/python-simpleline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-simpleline/python-simpleline.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 374 | [qalculate-qt/qalculate-qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qalculate-qt/qalculate-qt.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 375 | [qemu/qemu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qemu/qemu.spec) | `autoconf`, `automake`, `libtool` | 194 |
| 376 | [quota/quota.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/quota/quota.spec) | `libtool` | 21 |
| 377 | [rdfind/rdfind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rdfind/rdfind.spec) | `libtool` | 19 |
| 378 | [re2c/re2c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/re2c/re2c.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 379 | [readline/readline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/readline/readline.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 380 | [rhash/rhash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rhash/rhash.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 381 | [rpcbind/rpcbind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpcbind/rpcbind.spec) | `make` | 18 |
| 382 | [rpmdevtools/rpmdevtools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpmdevtools/rpmdevtools.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 383 | [rust-rpm-macros/rust-rpm-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-rpm-macros/rust-rpm-macros.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 384 | [samurai/samurai.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/samurai/samurai.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 385 | [sbsigntools/sbsigntools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sbsigntools/sbsigntools.spec) | `libtool` | 19 |
| 386 | [scdoc/scdoc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/scdoc/scdoc.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 387 | [sed/sed.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sed/sed.spec) | `autoconf`, `automake`, `libtool`, `make` | 19 |
| 388 | [sg3_utils/sg3_utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sg3_utils/sg3_utils.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 389 | [sgml-common/sgml-common.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sgml-common/sgml-common.spec) | `autoconf`, `libtool` | 33 |
| 390 | [shim/shim.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/shim/shim.spec) | `autoconf`, `automake`, `libtool` | 27 |
| 391 | [signon/signon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/signon/signon.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 392 | [signon-plugin-oauth2/signon-plugin-oauth2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/signon-plugin-oauth2/signon-plugin-oauth2.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 393 | [skalibs/skalibs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/skalibs/skalibs.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 394 | [skopeo/skopeo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/skopeo/skopeo.spec) | `autoconf`, `libtool`, `make` | 17 |
| 395 | [slang/slang.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/slang/slang.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 396 | [slibtool/slibtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/slibtool/slibtool.spec) | `autoconf`, `automake`, `libtool` | 21 |
| 397 | [smartmontools/smartmontools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/smartmontools/smartmontools.spec) | `autoconf`, `libtool` | 19 |
| 398 | [socat/socat.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/socat/socat.spec) | `automake`, `libtool` | 16 |
| 399 | [source-highlight/source-highlight.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/source-highlight/source-highlight.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 400 | [sparse/sparse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sparse/sparse.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 401 | [spdk/spdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/spdk/spdk.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 402 | [speex/speex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/speex/speex.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 403 | [speexdsp/speexdsp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/speexdsp/speexdsp.spec) | `make` | 17 |
| 404 | [sqlcipher/sqlcipher.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sqlcipher/sqlcipher.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 405 | [sqlite/sqlite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sqlite/sqlite.spec) | `automake`, `libtool` | 27 |
| 406 | [squashfs-tools/squashfs-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/squashfs-tools/squashfs-tools.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 407 | [squashfs-tools-ng/squashfs-tools-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/squashfs-tools-ng/squashfs-tools-ng.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 408 | [sshpass/sshpass.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sshpass/sshpass.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 409 | [sssd/sssd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sssd/sssd.spec) | `make` | 21 |
| 410 | [startup-notification/startup-notification.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/startup-notification/startup-notification.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 411 | [strace/strace.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/strace/strace.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 412 | [stress-ng/stress-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/stress-ng/stress-ng.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 413 | [sudo/sudo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sudo/sudo.spec) | `make` | 21 |
| 414 | [swig/swig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/swig/swig.spec) | `libtool` | 21 |
| 415 | [symlinks/symlinks.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/symlinks/symlinks.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 416 | [sysstat/sysstat.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sysstat/sysstat.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 417 | [system-config-printer/system-config-printer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/system-config-printer/system-config-printer.spec) | `libtool` | 15 |
| 418 | [systemtap/systemtap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/systemtap/systemtap.spec) | `autoconf`, `automake`, `libtool` | 21 |
| 419 | [talloc/talloc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/talloc/talloc.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 420 | [tar/tar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tar/tar.spec) | `libtool` | 19 |
| 421 | [tcl/tcl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tcl/tcl.spec) | `automake`, `libtool`, `make` | 23 |
| 422 | [tclap/tclap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tclap/tclap.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 423 | [tcpdump/tcpdump.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tcpdump/tcpdump.spec) | `libtool` | 19 |
| 424 | [tcsh/tcsh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tcsh/tcsh.spec) | `automake`, `libtool`, `make` | 18 |
| 425 | [tdb/tdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tdb/tdb.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 426 | [tevent/tevent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tevent/tevent.spec) | `autoconf`, `automake`, `libtool` | 20 |
| 427 | [texinfo/texinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/texinfo/texinfo.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 428 | [tftp/tftp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tftp/tftp.spec) | `automake`, `libtool` | 18 |
| 429 | [time/time.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/time/time.spec) | `autoconf`, `automake`, `libtool`, `make` | 20 |
| 430 | [tmux/tmux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tmux/tmux.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 431 | [tpm2-tss/tpm2-tss.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tpm2-tss/tpm2-tss.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 432 | [traceroute/traceroute.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/traceroute/traceroute.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 433 | [tre/tre.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tre/tre.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 434 | [tree/tree.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tree/tree.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 435 | [trinity/trinity.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/trinity/trinity.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 436 | [tunctl/tunctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tunctl/tunctl.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 437 | [tzdata/tzdata.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tzdata/tzdata.spec) | `autoconf`, `automake`, `libtool` | 23 |
| 438 | [udisks2/udisks2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/udisks2/udisks2.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 439 | [ulogd/ulogd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ulogd/ulogd.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 440 | [unbound/unbound.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unbound/unbound.spec) | `make` | 42 |
| 441 | [unifont/unifont.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unifont/unifont.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 442 | [universal-ctags/universal-ctags.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/universal-ctags/universal-ctags.spec) | `libtool` | 16 |
| 443 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 444 | [usermode/usermode.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/usermode/usermode.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 445 | [utf8proc/utf8proc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/utf8proc/utf8proc.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 446 | [util-macros/util-macros.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/util-macros/util-macros.spec) | `make` | 18 |
| 447 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | `autoconf`, `automake` | 17 |
| 448 | [valgrind/valgrind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/valgrind/valgrind.spec) | `libtool` | 33 |
| 449 | [valkey/valkey.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/valkey/valkey.spec) | `autoconf`, `automake`, `libtool` | 38 |
| 450 | [vdo/vdo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vdo/vdo.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 451 | [vim/vim.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vim/vim.spec) | `autoconf`, `automake`, `make` | 23 |
| 452 | [virt-what/virt-what.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/virt-what/virt-what.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 453 | [vorbis-tools/vorbis-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vorbis-tools/vorbis-tools.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 454 | [which/which.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/which/which.spec) | `autoconf`, `automake`, `libtool`, `make` | 21 |
| 455 | [whois/whois.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/whois/whois.spec) | `autoconf`, `automake`, `libtool` | 16 |
| 456 | [wireguard-tools/wireguard-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wireguard-tools/wireguard-tools.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 457 | [wpa_supplicant/wpa_supplicant.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wpa_supplicant/wpa_supplicant.spec) | `autoconf`, `automake`, `libtool` | 21 |
| 458 | [xapian/xapian.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xapian/xapian.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 459 | [xcb-proto/xcb-proto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-proto/xcb-proto.spec) | `libtool` | 19 |
| 460 | [xcb-util/xcb-util.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-util/xcb-util.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 461 | [xcb-util-cursor/xcb-util-cursor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-util-cursor/xcb-util-cursor.spec) | `make` | 18 |
| 462 | [xcb-util-image/xcb-util-image.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-util-image/xcb-util-image.spec) | `make` | 17 |
| 463 | [xcb-util-keysyms/xcb-util-keysyms.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-util-keysyms/xcb-util-keysyms.spec) | `autoconf`, `automake`, `libtool`, `make` | 18 |
| 464 | [xcb-util-renderutil/xcb-util-renderutil.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-util-renderutil/xcb-util-renderutil.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 465 | [xcb-util-wm/xcb-util-wm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcb-util-wm/xcb-util-wm.spec) | `autoconf`, `automake`, `libtool`, `make` | 17 |
| 466 | [xcursor-themes/xcursor-themes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcursor-themes/xcursor-themes.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 467 | [xcursorgen/xcursorgen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xcursorgen/xcursorgen.spec) | `autoconf` | 15 |
| 468 | [xdg-user-dirs/xdg-user-dirs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xdg-user-dirs/xdg-user-dirs.spec) | `libtool` | 16 |
| 469 | [xdg-utils/xdg-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xdg-utils/xdg-utils.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 470 | [xfsprogs/xfsprogs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xfsprogs/xfsprogs.spec) | `autoconf`, `automake`, `make` | 19 |
| 471 | [xinetd/xinetd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xinetd/xinetd.spec) | `make` | 17 |
| 472 | [xkbcomp/xkbcomp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xkbcomp/xkbcomp.spec) | `autoconf`, `automake`, `libtool` | 15 |
| 473 | [xmlrpc-c/xmlrpc-c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xmlrpc-c/xmlrpc-c.spec) | `autoconf`, `automake`, `libtool`, `make` | 16 |
| 474 | [xmlto/xmlto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xmlto/xmlto.spec) | `libtool`, `make` | 18 |
| 475 | [xmltoman/xmltoman.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xmltoman/xmltoman.spec) | `autoconf`, `automake`, `libtool` | 17 |
| 476 | [xtrans/xtrans.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xtrans/xtrans.spec) | `autoconf`, `automake`, `libtool` | 19 |
| 477 | [xz/xz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xz/xz.spec) | `autoconf`, `automake`, `libtool`, `make` | 21 |
| 478 | [ypserv/ypserv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ypserv/ypserv.spec) | `libtool` | 20 |
| 479 | [zeromq/zeromq.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zeromq/zeromq.spec) | `make` | 16 |
| 480 | [zfs/zfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zfs/zfs.spec) | `autoconf`, `automake`, `libtool` | 31 |
| 481 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `autoconf`, `automake`, `libtool` | 18 |
| 482 | [zsh/zsh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zsh/zsh.spec) | `make` | 24 |

## 说明

- 规则仅适用于 `BuildSystem: autotools` 的 spec（共 675 个）：
  头部区域 `BuildRequires` 必须声明 `autoconf`、`automake`、`libtool`、
  `make` 四项依赖。`gcc` 在构建环境预装，可不显式声明，不纳入检查。
- 其余 4592 个非 autotools spec 不适用本规则，未计入统计。
- `%package` 子包段落内的 `BuildRequires`、宏展开值（如 `%{?foo}`）以及注释行不视为有效声明。
- 是否应在 `%conf` 前置运行 `autoreconf -fiv`、源码无 `configure` 脚本时是否应使用空 `%conf`：
  依赖源码树内容，无法静态判定，不在本规则范围内。

> 规则说明：[docs/check-spec-autotools.md](../docs/check-spec-autotools.md)
