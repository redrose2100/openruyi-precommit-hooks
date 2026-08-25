# check-spec-patch 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库的 spec 文件（`SPECS/{pkg}/{pkg}.spec`）执行 `check-spec-patch` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 违规 |
| --- | ---: | ---: |
| 5267 | 5063 | 204 |

> 说明：违规数按 spec 文件去重统计（一个文件可能命中多条规则）。

## 问题类型分布

| 问题类型 | 数量 |
| --- | ---: |
| `Patch` 字段上方缺少注释行 | 276 |
| `%patchlist` 条目上方缺少注释行 | 57 |
| 补丁文件名未以四位数字开头 | 121 |
| 补丁文件名前缀不在 `0001-2999` 范围内 | 4 |
| 补丁数量 > 3 未使用 `%patchlist` | 25 |
| `%patchlist` 位于 `%description` 之下 | 4 |
| `Patch` 字段放置顺序错误 | 26 |

## 问题清单（513 条）

| # | spec 文件 | 详情 |
| --- | --- | --- |
| 1 | [angelscript/angelscript.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/angelscript/angelscript.spec) | `Patch` 字段 `2000-install-libraries-and-CMake-files-to-GNUInstallDirs....` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 2 | [arrow/arrow.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/arrow/arrow.spec) | `Patch` 字段 `0002-test-use-approximate-comparison-for-quantile.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 3 | [aspell/aspell.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aspell/aspell.spec) | `Patch` 字段 `0002-aspell-quotes.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 4 | [attr/attr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/attr/attr.spec) | `Patch` 字段 `0001-bypass-wrong-output-when-enabled-selinux.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 5 | [attr/attr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/attr/attr.spec) | `Patch` 字段 `0002-dont-skip-security.evm-when-copy-xattr.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 6 | [audiofile/audiofile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/audiofile/audiofile.spec) | `Patch` 字段 `0007-822b732fd31ffcb78f6920001e9b1fbd815fa712.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 7 | [autoconf/autoconf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/autoconf/autoconf.spec) | `Patch` 字段 `autoreconf-ltdl.diff` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 8 | [autofs/autofs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/autofs/autofs.spec) | `Patch` 字段 `autofs-5.1.9-Fix-incompatible-function-pointer-types-in-c...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 9 | [bash/bash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bash/bash.spec) | `Patch` 字段 `0002-bash-5.3-patch-2.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 10 | [bash/bash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bash/bash.spec) | `Patch` 字段 `0003-bash-5.3-patch-3.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 11 | [bdfresize/bdfresize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bdfresize/bdfresize.spec) | `Patch` 字段 `020_minus-sign.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 12 | [bison/bison.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bison/bison.spec) | `Patch` 字段 `glr2-cc-ensure-yylookaheadNeeds-is-same-size-as-yystates....` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 13 | [cgctl/cgctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cgctl/cgctl.spec) | `Patch` 字段 `2000-cgroups-root-adapt-to-runtime-spec-1.3.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 14 | [cgctl/cgctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cgctl/cgctl.spec) | `Patch` 字段 `2001-cgroups-v3-adapt-to-runtime-spec-1.3.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 15 | [cloud-init/cloud-init.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cloud-init/cloud-init.spec) | `Patch` 字段 `2000-Add-openruyi-support.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 16 | [console-setup/console-setup.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/console-setup/console-setup.spec) | `Patch` 字段 `0001-fix-makefile.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 17 | [crash/crash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crash/crash.spec) | `Patch` 字段 `lzo_snappy_zstd.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 18 | [crash/crash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crash/crash.spec) | `Patch` 字段 `crash-9.0.1_build.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 19 | [cunit/cunit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cunit/cunit.spec) | `Patch` 字段 `0001-cunit-link-ncurses.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 20 | [cunit/cunit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cunit/cunit.spec) | `Patch` 字段 `0002-cunit-ncurses6.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 21 | [cunit/cunit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cunit/cunit.spec) | `Patch` 字段 `0003-avoid-Wformat-security-bug.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 22 | [cyrus-sasl/cyrus-sasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cyrus-sasl/cyrus-sasl.spec) | `Patch` 字段 `0001-cyrus-sasl-lfs.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 23 | [cyrus-sasl/cyrus-sasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cyrus-sasl/cyrus-sasl.spec) | `Patch` 字段 `0002-fix_libpq-fe_include.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 24 | [cyrus-sasl/cyrus-sasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cyrus-sasl/cyrus-sasl.spec) | `Patch` 字段 `0003-Fix-time.h-check.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 25 | [cyrus-sasl/cyrus-sasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cyrus-sasl/cyrus-sasl.spec) | `Patch` 字段 `0004-cyrus-sasl-make-digestmd5-work-ssl3.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 26 | [dbus-broker/dbus-broker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dbus-broker/dbus-broker.spec) | `Patch` 字段 `test-sockopt-loosen-verification-of-stale-pidfds.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 27 | [dejagnu/dejagnu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dejagnu/dejagnu.spec) | `Patch` 字段 `testsuite-legacy.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 28 | [desktop-file-utils/desktop-file-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/desktop-file-utils/desktop-file-utils.spec) | `Patch` 字段 `0001-validate-Add-Phosh-to-list-of-valid-OnlyShowIn-envir...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 29 | [dosfstools/dosfstools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dosfstools/dosfstools.spec) | `Patch` 字段 `0001-Fix-vasprintf-implementation.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 30 | [doxygen/doxygen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/doxygen/doxygen.spec) | `Patch` 字段 `doxygen-no-lowercase-man-names.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 31 | [doxygen/doxygen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/doxygen/doxygen.spec) | `Patch` 字段 `reproducible.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 32 | [duktape/duktape.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/duktape/duktape.spec) | `Patch` 字段 `0001-duktape-link-m.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 33 | [dwz/dwz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dwz/dwz.spec) | `Patch` 字段 `remove-gold-tests.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 34 | [eigen3/eigen3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/eigen3/eigen3.spec) | `Patch` 字段 `eigen3_libinstalldir.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 35 | [ethtool/ethtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ethtool/ethtool.spec) | `Patch` 字段 `0001-netlink-fix-missing-headers-in-text-output.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 36 | [ethtool/ethtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ethtool/ethtool.spec) | `Patch` 字段 `0002-netlink-fix-print_string-when-the-value-is-NULL.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 37 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `Patch` 字段 `0001-expect.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 38 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `Patch` 字段 `0002-expect-fixes.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 39 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `Patch` 字段 `0003-expect-log.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 40 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `Patch` 字段 `0004-config-guess-sub-update.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 41 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `Patch` 字段 `0005-expect-errorfd.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 42 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `Patch` 字段 `0006-expect-5.45-format-security.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 43 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `Patch` 字段 `0007-expect-fix-implicit.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 44 | [f2fs-tools/f2fs-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/f2fs-tools/f2fs-tools.spec) | `Patch` 字段 `0001-f2fs-tools-1.16.0-c23.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 45 | [fakeroot/fakeroot.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fakeroot/fakeroot.spec) | `Patch` 字段 `debian_fix-shell-in-fakeroot.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 46 | [fcoe-utils/fcoe-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fcoe-utils/fcoe-utils.spec) | `Patch` 字段 `0001-fcoemon-add-snprintf-string-precision-modifiers-in-f...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 47 | [fcoe-utils/fcoe-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fcoe-utils/fcoe-utils.spec) | `Patch` 字段 `0002-Don-t-attempt-to-memcpy-zero-bytes.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 48 | [fcoe-utils/fcoe-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fcoe-utils/fcoe-utils.spec) | `Patch` 字段 `0003-Fix-build-against-glibc-2.43.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 49 | [fscryptctl/fscryptctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fscryptctl/fscryptctl.spec) | `Patch` 字段 `0001-disable-doc.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 50 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `gcc-add-defaultsspec.diff` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 51 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `gcc44-textdomain.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 52 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `gcc44-rename-info-files.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 53 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0002-RISC-V-Fix-missing-implied-Zicsr-from-Zve32x.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 54 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0003-RISC-V-Add-new-option-param-gpr2vr-cost-for-rvv-insn...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 55 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0004-PATCH-RISC-V-Recognized-svadu-and-svade-extension.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 56 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0005-PATCH-RISC-V-Minimal-support-for-sdtrig-and-ssstrict...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 57 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0006-PATCH-RISC-V-Minimal-support-for-zama16b-extension.p...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 58 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0007-RISC-V-Support-RISC-V-Profiles-20-22.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 59 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0008-RISC-V-Support-RISC-V-Profiles-23.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 60 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0009-RISC-V-Support-for-zilsd-and-zclsd-extensions.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 61 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0010-RISC-V-Minimal-support-for-ssnpm-smnpm-and-smmpm-ext...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 62 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0011-RISC-V-Introduce-riscv-ext-.def-to-define-extensions...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 63 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0012-RISC-V-Use-riscv-ext.def-to-generate-target-options-...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 64 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0013-RISC-V-Generate-extension-table-in-documentation-fro...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 65 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0014-RISC-V-Adjust-riscv_can_inline_p.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 66 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0015-RISC-V-Introduce-riscv_ext_info_t-to-hold-extension-...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 67 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0016-RISC-V-Drop-riscv_implied_info-and-riscv_combine_inf...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 68 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0017-RISC-V-Drop-riscv_ext_version_table-in-favor-of-risc...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 69 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0018-RISC-V-Drop-riscv_ext_flag_table-in-favor-of-riscv_e...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 70 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0019-RISC-V-Add-augmented-hypervisor-series-extensions.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 71 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0020-RISC-V-Support-CPUs-in-march.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 72 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0021-RISC-V-Add-minimal-support-of-double-trap-extension-...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 73 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0022-PATCH-RISC-V-Add-smcntrpmf-extension.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 74 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0023-RISC-V-Add-Shlcofideleg-extension.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 75 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0024-PATCH-v2-RISC-V-Add-svbare-extension.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 76 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0025-PATCH-RISC-V-Imply-zicsr-for-svade-and-svadu-extensi...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 77 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0026-RISC-V-Update-extension-defination.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 78 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0027-RISC-V-Support-Sm-scsrind-extensions.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 79 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0028-RISC-V-Support-Smrnmi-extension.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 80 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0029-RISC-V-Support-Ssccptr-extension.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 81 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0030-RISC-V-Support-Sscounterenw-extension.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 82 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0031-RISC-V-Support-Sstvala-extension.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 83 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0032-RISC-V-Support-Sstvecd-extension.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 84 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0033-RISC-V-Support-Ssu64xl-extension.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 85 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0034-RISC-V-Update-Profiles-string-in-RV23.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 86 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0035-RISC-V-Add-Profiles-RVA-B23S64-support.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 87 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `Patch` 字段 `0036-RISC-V-check-if-we-can-vec_extract.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 88 | [gcc16/gcc16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc16/gcc16.spec) | `Patch` 字段 `2000-textdomain.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 89 | [gcc16/gcc16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc16/gcc16.spec) | `Patch` 字段 `2001-rename-info-files.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 90 | [gdbm/gdbm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gdbm/gdbm.spec) | `Patch` 字段 `gdbm-no-build-date.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 91 | [gflags/gflags.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gflags/gflags.spec) | `Patch` 字段 `0001-gflags-fix_pkgconfig.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 92 | [giflib/giflib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/giflib/giflib.spec) | `Patch` 字段 `0001-disable-doc.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 93 | [glib/glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glib/glib.spec) | `Patch` 字段 `meson.build-Avoid-linking-with-libatomic-when-unneed.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 94 | [go-github-envoyproxy-protoc-gen-validate/go-github-envoyproxy-protoc-gen-validate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-envoyproxy-protoc-gen-validate/go-github-envoyproxy-protoc-gen-validate.spec) | `Patch` 字段 `2000-fix-checker.go-error.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 95 | [go-gopkg-tomb.v1/go-gopkg-tomb.v1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-gopkg-tomb.v1/go-gopkg-tomb.v1.spec) | `Patch` 字段 `2000-fix-killf-test-format-string.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 96 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `Patch` 字段 `0001-some-headers.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 97 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `Patch` 字段 `0002-gpm-1.20.6-multilib.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 98 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `Patch` 字段 `0003-gpm-1.20.1-lib-silent.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 99 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `Patch` 字段 `0004-gpm-1.20.5-close-fds.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 100 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `Patch` 字段 `0005-gpm-1.20.1-weak-wgetch.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 101 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `Patch` 字段 `0006-gpm-1.20.7-rhbz-668480-gpm-types-7-manpage-fixes.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 102 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `Patch` 字段 `0007-src-daemon-remove-obvious-use-of-unitialized-data.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 103 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `Patch` 字段 `0008-src-daemon-reindent-switch-statement-to-avoid-compil...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 104 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `Patch` 字段 `0009-configure-drop-broken-configure-code.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 105 | [gpsd/gpsd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpsd/gpsd.spec) | `Patch` 字段 `2000-gpsd_hotplug_rules_disable.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 106 | [gptfdisk/gptfdisk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gptfdisk/gptfdisk.spec) | `Patch` 字段 `2000-fix-include-ncurses.h-unconditionally.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 107 | [grpc/grpc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grpc/grpc.spec) | `Patch` 字段 `2000-force-system-libraries-in-isolated-environments.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 108 | [guile/guile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/guile/guile.spec) | `Patch` 字段 `guile-fix-riscv64-jit.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 109 | [gzip/gzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gzip/gzip.spec) | `Patch` 字段 `manpage-no-date.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 110 | [hipfft/hipfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipfft/hipfft.spec) | `Patch` 字段 `0001-hipfft-hipfftw-soversion.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 111 | [hipify/hipify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipify/hipify.spec) | `Patch` 字段 `0001-prepare-hipify-cmake.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 112 | [icu4c/icu4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/icu4c/icu4c.spec) | `Patch` 字段 `0001-icu-fix-install-mode-files.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 113 | [icu4c/icu4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/icu4c/icu4c.spec) | `Patch` 字段 `0002-icu-error-reporting.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 114 | [icu4c/icu4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/icu4c/icu4c.spec) | `Patch` 字段 `0003-icu-avoid-x87-excess-precision.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 115 | [icu4c/icu4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/icu4c/icu4c.spec) | `Patch` 字段 `0004-locale.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 116 | [icu4c/icu4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/icu4c/icu4c.spec) | `Patch` 字段 `0005-nan-undefined-conversion.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 117 | [itstool/itstool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/itstool/itstool.spec) | `Patch` 字段 `0001-Fix-insufficiently-quoted-regular-expressions.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 118 | [itstool/itstool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/itstool/itstool.spec) | `Patch` 字段 `0002-Switch-from-libxml2-to-lxml.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 119 | [kf6-ksvg/kf6-ksvg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-ksvg/kf6-ksvg.spec) | `Patch` 字段 `0001-Revert-Support-for-fractional-scaling.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 120 | [kiwi/kiwi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kiwi/kiwi.spec) | `Patch` 字段 `2000-optional-manpage.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 121 | [libburn/libburn.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libburn/libburn.spec) | `Patch` 字段 `0001-libburn-1.5.6-c23.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 122 | [libdwarf/libdwarf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdwarf/libdwarf.spec) | `Patch` 字段 `libdwarf-both.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 123 | [libfaketime/libfaketime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfaketime/libfaketime.spec) | `Patch` 字段 `0001-Add-const-qualifiers-to-fix-build-with-ISO-C23.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 124 | [libfaketime/libfaketime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfaketime/libfaketime.spec) | `Patch` 字段 `0002-tests-Silence-an-unused-but-set-variable-warning-wit...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 125 | [libjpeg-turbo/libjpeg-turbo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libjpeg-turbo/libjpeg-turbo.spec) | `Patch` 字段 `0001-libjpeg-turbo-cmake.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 126 | [liblc3/liblc3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/liblc3/liblc3.spec) | `Patch` 字段 `0001-Revert-build-fix-rpath-issue.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 127 | [liblognorm/liblognorm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/liblognorm/liblognorm.spec) | `Patch` 字段 `0001-Port-pcre-dependency-to-pcre2.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 128 | [libmodulemd/libmodulemd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmodulemd/libmodulemd.spec) | `Patch` 字段 `0001-tests-Adapt-to-glib-2.87.0.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 129 | [libmodulemd/libmodulemd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmodulemd/libmodulemd.spec) | `Patch` 字段 `0002-tests-Adapt-to-pygobject-3.55.0.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 130 | [libosinfo/libosinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libosinfo/libosinfo.spec) | `Patch` 字段 `0001-libosinfo-libxml2-2.14.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 131 | [libseccomp/libseccomp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libseccomp/libseccomp.spec) | `Patch` 字段 `2000-make-python-build.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 132 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | `Patch` 字段 `readv-proto.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 133 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | `Patch` 字段 `skip_cycles.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 134 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | `Patch` 字段 `swig4_moduleimport.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 135 | [libsquish/libsquish.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsquish/libsquish.spec) | `Patch` 字段 `2000-OBCMake-Replace-hardcoded-cmake-install-paths-with-C...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 136 | [libtiff/libtiff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtiff/libtiff.spec) | `Patch` 字段 `libtiff-4.0.3-seek.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 137 | [libtiff/libtiff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtiff/libtiff.spec) | `Patch` 字段 `libtiff-4.7.0-test_directory.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 138 | [libunwind/libunwind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libunwind/libunwind.spec) | `Patch` 字段 `0001-Fix-bad-prototype-for-malloc-in-test.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 139 | [libutempter/libutempter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libutempter/libutempter.spec) | `Patch` 字段 `0001-fix-install-path.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 140 | [libvdpau/libvdpau.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libvdpau/libvdpau.spec) | `Patch` 字段 `0001-libvdpau-av1-trace.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 141 | [libwebp/libwebp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libwebp/libwebp.spec) | `Patch` 字段 `0001-libwebp-cmakedir.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 142 | [libwebp/libwebp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libwebp/libwebp.spec) | `Patch` 字段 `0002-libwebp-rpath.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 143 | [libyuv/libyuv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libyuv/libyuv.spec) | `Patch` 字段 `0001-fix-install-dir.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 144 | [llvm-snapshot/llvm-snapshot.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvm-snapshot/llvm-snapshot.spec) | `Patch` 字段 `2000-Add-riscv64-openruyi-linux-triple-and-set-it-to-rva2...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 145 | [llvm-snapshot/llvm-snapshot.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvm-snapshot/llvm-snapshot.spec) | `Patch` 字段 `2001-Add-openruyi-linux-to-X86_64Triples-and-RISCV64Tripl...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 146 | [llvm22/llvm22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvm22/llvm22.spec) | `Patch` 字段 `2000-Add-riscv64-openruyi-linux-triple-and-set-it-to-rva2...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 147 | [llvm22/llvm22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvm22/llvm22.spec) | `Patch` 字段 `2001-Add-openruyi-linux-to-X86_64Triples-and-RISCV64Tripl...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 148 | [lsof/lsof.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lsof/lsof.spec) | `Patch` 字段 `2000-skip-LTlock-test-in-package-builds.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 149 | [lua/lua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua/lua.spec) | `Patch` 字段 `0001-lua-5.4.6-idsize.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 150 | [lua/lua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua/lua.spec) | `Patch` 字段 `0002-lua-5.4.0-beta-autotoolize.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 151 | [lua/lua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua/lua.spec) | `Patch` 字段 `0003-lua-5.2.2-configure-linux.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 152 | [lua/lua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua/lua.spec) | `Patch` 字段 `0004-lua-5.3.0-configure-compat-module.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 153 | [lua-json/lua-json.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua-json/lua-json.spec) | `Patch` 字段 `0001-support-lpeg1.1.0.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 154 | [lz4/lz4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lz4/lz4.spec) | `Patch` 字段 `lz4-export.diff` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 155 | [mariadb/mariadb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mariadb/mariadb.spec) | `Patch` 字段 `fix-pamdir.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 156 | [mergerfs/mergerfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mergerfs/mergerfs.spec) | `Patch` 字段 `0001-no_chown_during_install.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 157 | [mkosi/mkosi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mkosi/mkosi.spec) | `Patch` 字段 `0001-Add-openruyi-support.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 158 | [msgpack/msgpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/msgpack/msgpack.spec) | `Patch` 字段 `0002-msgpack-cmake4.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 159 | [nghttp3/nghttp3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nghttp3/nghttp3.spec) | `Patch` 字段 `0001-fix-install-path.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 160 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `Patch` 字段 `v8-riscv-fix-trampoline.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 161 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `Patch` 字段 `v8-riscv-fix-trampoline-release.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 162 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `Patch` 字段 `60591.diff` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 163 | [nss/nss.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nss/nss.spec) | `Patch` 字段 `2001-Make-dbtests-certutil-K-timeout-configurable.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 164 | [numad/numad.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/numad/numad.spec) | `Patch` 字段 `0001-recognize-m-option-correctly.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 165 | [numad/numad.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/numad/numad.spec) | `Patch` 字段 `0002-numad_log-fix-buffer-overflow.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 166 | [numad/numad.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/numad/numad.spec) | `Patch` 字段 `0003-avoid-array-index-out-of-bounds.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 167 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `Patch` 字段 `0001-reproducible.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 168 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `Patch` 字段 `0002-LDAPI-socket-location.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 169 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `Patch` 字段 `0003-pie-compile.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 170 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `Patch` 字段 `0004-In-monitor-backend-do-not-return-Connection0-entries...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 171 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `Patch` 字段 `0005-Clear-shared-key-only-in-close-function.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 172 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `Patch` 字段 `0006-gcc14-v2.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 173 | [openzl/openzl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openzl/openzl.spec) | `Patch` 字段 `2000-add-install-rules-for-CLI-tools-and-parser-targets.p...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 174 | [openzl/openzl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openzl/openzl.spec) | `Patch` 字段 `2001-feat-prefer-system-installed-zstd-over-bundled-depen...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 175 | [orbit2/orbit2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/orbit2/orbit2.spec) | `Patch` 字段 `0001-ORBit2-2.14.3-multilib.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 176 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | `Patch` 字段 `args.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 177 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | `Patch` 字段 `freetype2.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 178 | [perl-Log-Any/perl-Log-Any.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Log-Any/perl-Log-Any.spec) | `Patch` 字段 `2000-isolate-syslog-test-env.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 179 | [perl-rpm-packaging/perl-rpm-packaging.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-rpm-packaging/perl-rpm-packaging.spec) | `Patch` 字段 `0001-fileattrs.diff` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 180 | [pesign/pesign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `Patch` 字段 `0001-cms_common-Fixed-Segmentation-fault.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 181 | [pesign/pesign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `Patch` 字段 `0002-Fix-reversed-calloc-arguments.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 182 | [pesign/pesign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `Patch` 字段 `0003-Work-around-OpenSC-changing-token-names-on-fedora-bu...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 183 | [pesign/pesign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `Patch` 字段 `0004-cms_common-skip-authentication-on-the-Friendly-slot....` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 184 | [pesign/pesign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `Patch` 字段 `0005-pesum-strrchr-should-be-of-type-const.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 185 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `Patch` 字段 `0001-pinfo-0.6.9-infopath.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 186 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `Patch` 字段 `0002-pinfo-0.6.9-xdg.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 187 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `Patch` 字段 `0003-pinfo-0.6.10-man.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 188 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `Patch` 字段 `0004-pinfo-0.6.13-fnocommon.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 189 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `Patch` 字段 `0005-pinfo-0.6.13-gccwarn.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 190 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `Patch` 字段 `0006-pinfo-0.6.13-nogroup.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 191 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `Patch` 字段 `0007-pinfo-0.6.13-stringop-overflow.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 192 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `Patch` 字段 `0008-pinfo-configure-c99.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 193 | [plasma-desktop/plasma-desktop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/plasma-desktop/plasma-desktop.spec) | `Patch` 字段 `2000-Apply-branding-to-default-favorites.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 194 | [plasma-desktop/plasma-desktop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/plasma-desktop/plasma-desktop.spec) | `Patch` 字段 `2001-Remove-discover-from-taskmanager-default-launchers.p...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 195 | [popt/popt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/popt/popt.spec) | `Patch` 字段 `0001-popt-libc-updates.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 196 | [postgresql/postgresql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postgresql/postgresql.spec) | `Patch` 字段 `postgresql-var-run-socket.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 197 | [postgresql/postgresql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postgresql/postgresql.spec) | `Patch` 字段 `postgresql-no-libecpg.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 198 | [powertop/powertop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/powertop/powertop.spec) | `Patch` 字段 `powertop-2.7-always-create-params.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 199 | [python-cart/python-cart.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cart/python-cart.spec) | `Patch` 字段 `0001-python-cart-1.2.2-cryptodomex.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 200 | [python-cppheaderparser/python-cppheaderparser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cppheaderparser/python-cppheaderparser.spec) | `Patch` 字段 `0001-cppheaderparser-silence-invalid-escape-sequence.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 201 | [python-gcloud-aio-auth/python-gcloud-aio-auth.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gcloud-aio-auth/python-gcloud-aio-auth.spec) | `Patch` 字段 `0001-chore-deps-bump-maximum-cryptography-version.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 202 | [python-optimum/python-optimum.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-optimum/python-optimum.spec) | `Patch` 字段 `2000-fix-utils-use-default_factory-for-mutable-dataclass-...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 203 | [python-optimum-benchmark/python-optimum-benchmark.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-optimum-benchmark/python-optimum-benchmark.spec) | `Patch` 字段 `2000-fix-backends-handle-SpecialTokensMixin-import-for-tr...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 204 | [python-propcache/python-propcache.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-propcache/python-propcache.spec) | `Patch` 字段 `0001-Update-Cython-to-version-3.2.3.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 205 | [python-tokenizers/python-tokenizers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tokenizers/python-tokenizers.spec) | `Patch` 字段 `2001-fix-bindings-cargo.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 206 | [python-torchvision/python-torchvision.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-torchvision/python-torchvision.spec) | `Patch` 字段 `0001-python-torchvision-ffmpeg8.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 207 | [python-torchvision/python-torchvision.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-torchvision/python-torchvision.spec) | `Patch` 字段 `2000-Add-HIP-detect-logic.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 208 | [qt6-qtwebengine/qt6-qtwebengine.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtwebengine/qt6-qtwebengine.spec) | `Patch` 字段 `0003-riscv-misc.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 209 | [qt6-qtwebengine/qt6-qtwebengine.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtwebengine/qt6-qtwebengine.spec) | `Patch` 字段 `0004-riscv-enable-v8-webasm.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 210 | [quota/quota.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/quota/quota.spec) | `Patch` 字段 `quota-4.06-warnquota-configuration-tunes.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 211 | [quota/quota.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/quota/quota.spec) | `Patch` 字段 `quota-4.03-Validate-upper-bound-of-RPC-port.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 212 | [readline/readline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/readline/readline.spec) | `Patch` 字段 `0002-readline-8.3-patch-2.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 213 | [readline/readline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/readline/readline.spec) | `Patch` 字段 `0003-readline-8.3-patch-3.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 214 | [recutils/recutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/recutils/recutils.spec) | `Patch` 字段 `0001-recutils-1.9-mdbtools-0.9.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 215 | [recutils/recutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/recutils/recutils.spec) | `Patch` 字段 `0002-recutils-c99.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 216 | [rocblas/rocblas.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocblas/rocblas.spec) | `Patch` 字段 `0001-fixup-install-of-tensile-output.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 217 | [rocfft/rocfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocfft/rocfft.spec) | `Patch` 字段 `0001-cmake-use-gnu-installdirs.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 218 | [rocfft/rocfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocfft/rocfft.spec) | `Patch` 字段 `2000-relax-sqlite-version-requirement.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 219 | [rocksdb/rocksdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocksdb/rocksdb.spec) | `Patch` 字段 `0001-no_rpath.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 220 | [rocksdb/rocksdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocksdb/rocksdb.spec) | `Patch` 字段 `0002-disable_static.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 221 | [rocminfo/rocminfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocminfo/rocminfo.spec) | `Patch` 字段 `0001-adjust-CMAKE_CXX_FLAGS.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 222 | [rocr-runtime/rocr-runtime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocr-runtime/rocr-runtime.spec) | `Patch` 字段 `0001-Add-riscv64-support.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 223 | [rocr-runtime/rocr-runtime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocr-runtime/rocr-runtime.spec) | `Patch` 字段 `0002-Replace-fence-instructions-for-riscv64.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 224 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `Patch` 字段 `checkfilesnoinfodir.diff` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 225 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `Patch` 字段 `rpmpopt.diff` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 226 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `Patch` 字段 `safeugid.diff` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 227 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `Patch` 字段 `fileattrs.diff` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 228 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `Patch` 字段 `brp-compress-no-img.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 229 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `Patch` 字段 `emptymanifest.diff` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 230 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `Patch` 字段 `find-lang-qt-qm.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 231 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `Patch` 字段 `canongnu.diff` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 232 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `Patch` 字段 `unshare.diff` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 233 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `Patch` 字段 `buildroot-symlink.diff` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 234 | [rust-async-std-1/rust-async-std-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-async-std-1/rust-async-std-1.spec) | `Patch` 字段 `0001-fix-range-dependencies.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 235 | [rust-dlib-0.5/rust-dlib-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-dlib-0.5/rust-dlib-0.5.spec) | `Patch` 字段 `0001-fix-range-dependencies.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 236 | [rust-generator-0.8/rust-generator-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-generator-0.8/rust-generator-0.8.spec) | `Patch` 字段 `0001-fix-range-dependencies.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 237 | [rust-hyper-util-0.1/rust-hyper-util-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hyper-util-0.1/rust-hyper-util-0.1.spec) | `Patch` 字段 `0001-fix-range-dependencies.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 238 | [rust-malloc-buf-0.0.6/rust-malloc-buf-0.0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-malloc-buf-0.0.6/rust-malloc-buf-0.0.6.spec) | `Patch` 字段 `0001-fix-range-dependencies.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 239 | [rust-nom-locate-5/rust-nom-locate-5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-nom-locate-5/rust-nom-locate-5.spec) | `Patch` 字段 `0001-fix-range-dependencies.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 240 | [rust-objc-0.2/rust-objc-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-objc-0.2/rust-objc-0.2.spec) | `Patch` 字段 `0001-fix-range-dependencies.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 241 | [rust-pyo3-introspection-0.28/rust-pyo3-introspection-0.28.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pyo3-introspection-0.28/rust-pyo3-introspection-0.28.spec) | `Patch` 字段 `0001-fix-dependency-ranges.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 242 | [rust-python-pkginfo-0.6/rust-python-pkginfo-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-python-pkginfo-0.6/rust-python-pkginfo-0.6.spec) | `Patch` 字段 `0001-fix-dependency-ranges.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 243 | [rust-reflink-copy-0.1/rust-reflink-copy-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-reflink-copy-0.1/rust-reflink-copy-0.1.spec) | `Patch` 字段 `0001-fix-dependency-ranges.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 244 | [rust-shellexpand-3/rust-shellexpand-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-shellexpand-3/rust-shellexpand-3.spec) | `Patch` 字段 `0001-fix-range-dependencies.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 245 | [rust-signal-hook-registry-1/rust-signal-hook-registry-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-signal-hook-registry-1/rust-signal-hook-registry-1.spec) | `Patch` 字段 `0001-fix-version.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 246 | [rust-system-deps-7/rust-system-deps-7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-system-deps-7/rust-system-deps-7.spec) | `Patch` 字段 `0001-fix-range-dependencies.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 247 | [rust-tracy-client-0.18/rust-tracy-client-0.18.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tracy-client-0.18/rust-tracy-client-0.18.spec) | `Patch` 字段 `0001-fix-range-dependencies.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 248 | [rust-v-frame-0.3/rust-v-frame-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-v-frame-0.3/rust-v-frame-0.3.spec) | `Patch` 字段 `0001-fix-cargo-requirements.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 249 | [rust-wasite-1/rust-wasite-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-wasite-1/rust-wasite-1.spec) | `Patch` 字段 `0001-fix-range-dependencies.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 250 | [scap-security-guide/scap-security-guide.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/scap-security-guide/scap-security-guide.spec) | `Patch` 字段 `2000-add-support-for-openRuyi.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 251 | [sddm/sddm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sddm/sddm.spec) | `Patch` 字段 `0001-CMake-Raise-required-version-to-3.5.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 252 | [shadow/shadow.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/shadow/shadow.spec) | `Patch` 字段 `2000-openruyi-disable-conflicting-tools.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 253 | [shadow/shadow.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/shadow/shadow.spec) | `Patch` 字段 `2001-openruyi-adapt-configs.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 254 | [sharutils/sharutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sharutils/sharutils.spec) | `Patch` 字段 `0001-backport-Fix-building-with-GCC-10.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 255 | [soxr/soxr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/soxr/soxr.spec) | `Patch` 字段 `0001-soxr-cmake.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 256 | [srt/srt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/srt/srt.spec) | `Patch` 字段 `0001-build-Update-for-compatibility-with-CMake-4.x-3167.p...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 257 | [startup-notification/startup-notification.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/startup-notification/startup-notification.spec) | `Patch` 字段 `0001-fix-test-xmessage-atom-types.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 258 | [symlinks/symlinks.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/symlinks/symlinks.spec) | `Patch` 字段 `0001-fix-makefile.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 259 | [tcsh/tcsh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tcsh/tcsh.spec) | `Patch` 字段 `0001-fix-nice-case-fail-if-noroot.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 260 | [texlive/texlive.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/texlive/texlive.spec) | `Patch` 字段 `2000-add-luajit-support-for-riscv64.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 261 | [xdg-utils/xdg-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xdg-utils/xdg-utils.spec) | `Patch` 字段 `0001-disable-docs.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 262 | [xevd/xevd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xevd/xevd.spec) | `Patch` 字段 `0001-xevd-fix-build-on-non-x86.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 263 | [xevd/xevd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xevd/xevd.spec) | `Patch` 字段 `0002-xevd-fix-neon-header.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 264 | [xevd/xevd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xevd/xevd.spec) | `Patch` 字段 `0003-xevd-link-libm.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 265 | [xeve/xeve.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xeve/xeve.spec) | `Patch` 字段 `0001-xeve-fix-build-on-non-x86.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 266 | [xeve/xeve.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xeve/xeve.spec) | `Patch` 字段 `0002-xeve-link-libm.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 267 | [xinetd/xinetd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xinetd/xinetd.spec) | `Patch` 字段 `0001-xinetd-service-sysconfig.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 268 | [xtrans/xtrans.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xtrans/xtrans.spec) | `Patch` 字段 `xtrans-1.0.3-avoid-gethostname.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 269 | [yaml-cpp/yaml-cpp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/yaml-cpp/yaml-cpp.spec) | `Patch` 字段 `0001-fix-include.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 270 | [zimg/zimg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zimg/zimg.spec) | `Patch` 字段 `0001-fix-build.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 271 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `Patch` 字段 `0004-man.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 272 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `Patch` 字段 `0005-zip-3.0-format-security.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 273 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `Patch` 字段 `0006-zipnote.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 274 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `Patch` 字段 `0007-zip-gnu89-build.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 275 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `Patch` 字段 `0008-buffer_overflow.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 276 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `Patch` 字段 `0009-zip-3.0-man-strip-extra.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 277 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `%patchlist` 条目 `0001-cups-system-auth.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 278 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `%patchlist` 条目 `0002-cups-multilib.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 279 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `%patchlist` 条目 `0003-cups-banners.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 280 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `%patchlist` 条目 `0004-cups-direct-usb.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 281 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `%patchlist` 条目 `0005-cups-driverd-timeout.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 282 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `%patchlist` 条目 `0006-cups-usb-paperout.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 283 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `%patchlist` 条目 `0007-cups-uri-compat.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 284 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `%patchlist` 条目 `0008-cups-freebind.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 285 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `%patchlist` 条目 `0009-cups-ipp-multifile.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 286 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `%patchlist` 条目 `0010-cups-web-devices-timeout.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 287 | [docbook-dtds/docbook-dtds.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-dtds/docbook-dtds.spec) | `%patchlist` 条目 `0002-docbook-dtd31-sgml-1.0.catalog.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 288 | [docbook-dtds/docbook-dtds.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-dtds/docbook-dtds.spec) | `%patchlist` 条目 `0003-docbook-dtd40-sgml-1.0.catalog.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 289 | [docbook-dtds/docbook-dtds.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-dtds/docbook-dtds.spec) | `%patchlist` 条目 `0004-docbook-dtd41-sgml-1.0.catalog.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 290 | [docbook-dtds/docbook-dtds.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-dtds/docbook-dtds.spec) | `%patchlist` 条目 `0005-docbook-dtd42-sgml-1.0.catalog.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 291 | [dpdk/dpdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dpdk/dpdk.spec) | `%patchlist` 条目 `0002-lpm-lookup-with-RISC-V-vector-extension.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 292 | [dpdk/dpdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dpdk/dpdk.spec) | `%patchlist` 条目 `0003-fib-lookup-with-RISC-V-vector-extension.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 293 | [dpdk/dpdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dpdk/dpdk.spec) | `%patchlist` 条目 `0004-config-riscv-consider-specified-CPU.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 294 | [dpdk/dpdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dpdk/dpdk.spec) | `%patchlist` 条目 `0005-test-raise-fast-test-timeout-to-60s-on-RISC-V.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 295 | [dpdk/dpdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dpdk/dpdk.spec) | `%patchlist` 条目 `0006-config-riscv-add-rv64gcv-cross-compilation-target.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 296 | [firefox/firefox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/firefox/firefox.spec) | `%patchlist` 条目 `0001-add-GetSystemProxyDirect-to-libproxy-path.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 297 | [firefox/firefox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/firefox/firefox.spec) | `%patchlist` 条目 `2000-riscv64-Use-long-tail-jump-for-xptcall-stubs.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 298 | [firefox/firefox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/firefox/firefox.spec) | `%patchlist` 条目 `2003-blindly-set-rust-rva23-target-when-needed.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 299 | [firefox/firefox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/firefox/firefox.spec) | `%patchlist` 条目 `2005-add-riscv64-support-for-crash-context.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 300 | [firefox/firefox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/firefox/firefox.spec) | `%patchlist` 条目 `2006-enable-crashreporter-for-riscv64.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 301 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `%patchlist` 条目 `freetype-2.3.0-enable-spr.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 302 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `%patchlist` 条目 `freetype-2.2.1-enable-valid.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 303 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `%patchlist` 条目 `freetype-2.6.5-libtool.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 304 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `%patchlist` 条目 `freetype-2.8-multilib.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 305 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `%patchlist` 条目 `freetype-2.10.0-internal-outline.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 306 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `%patchlist` 条目 `freetype-2.10.1-debughook.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 307 | [i2c-tools/i2c-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/i2c-tools/i2c-tools.spec) | `%patchlist` 条目 `0001-i2ctransfer-Don-t-link-with-libi2c.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 308 | [i2c-tools/i2c-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/i2c-tools/i2c-tools.spec) | `%patchlist` 条目 `0002-i2ctransfer-Don-t-free-memory-which-was-never-alloca...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 309 | [i2c-tools/i2c-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/i2c-tools/i2c-tools.spec) | `%patchlist` 条目 `0003-i2ctransfer-Prevent-msgs-overflow-with-many-paramete...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 310 | [i2c-tools/i2c-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/i2c-tools/i2c-tools.spec) | `%patchlist` 条目 `0004-i2ctransfer-Zero-out-memory-passed-to-ioctl.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 311 | [isa-l_crypto/isa-l_crypto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/isa-l_crypto/isa-l_crypto.spec) | `%patchlist` 条目 `0005-aes-riscv64-add-RISC-V-Zvk-AES-implementation-for-AE...` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 312 | [miopen/miopen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/miopen/miopen.spec) | `%patchlist` 条目 `2001-disable-clang-tidy.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 313 | [miopen/miopen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/miopen/miopen.spec) | `%patchlist` 条目 `2002-workaround-half-float-expr-deduction.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 314 | [miopen/miopen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/miopen/miopen.spec) | `%patchlist` 条目 `2003-disable-fno-offload-uniform-block.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 315 | [miopen/miopen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/miopen/miopen.spec) | `%patchlist` 条目 `2004-fix-clang-rel-path.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 316 | [python-pytest-xdist/python-pytest-xdist.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-xdist/python-pytest-xdist.spec) | `%patchlist` 条目 `0001-python-pytest-xdist-3.8.0-fix-for-pytest-9.0+.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 317 | [python-pytest-xdist/python-pytest-xdist.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-xdist/python-pytest-xdist.spec) | `%patchlist` 条目 `0002-python-pytest-xdist-3.8.0-update-biapp.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 318 | [python-tensile/python-tensile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tensile/python-tensile.spec) | `%patchlist` 条目 `0001-fix-python-shebang.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 319 | [python-tensile/python-tensile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tensile/python-tensile.spec) | `%patchlist` 条目 `0002-fix-tensile-get-path.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 320 | [python-tensile/python-tensile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tensile/python-tensile.spec) | `%patchlist` 条目 `0004-ignore-asm-cap-cache.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 321 | [rocclr/rocclr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocclr/rocclr.spec) | `%patchlist` 条目 `2002-add-lp64d-target-to-llvm-mc.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 322 | [rrdtool/rrdtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | `%patchlist` 条目 `Fix-compatibility-with-Tcl-9.0.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 323 | [rrdtool/rrdtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | `%patchlist` 条目 `correctly-link-ruby-bindings.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 324 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `%patchlist` 条目 `0015-unzip-6.0-alt-iconv-utf8-print.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 325 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `%patchlist` 条目 `0016-Fix-CVE-2016-9844-rhbz-1404283.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 326 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `%patchlist` 条目 `0022-unzip-zipbomb-part2.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 327 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `%patchlist` 条目 `0023-unzip-zipbomb-part3.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 328 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `%patchlist` 条目 `0024-unzip-zipbomb-manpage.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 329 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `%patchlist` 条目 `0025-unzip-zipbomb-part4.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 330 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `%patchlist` 条目 `0026-unzip-zipbomb-part5.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 331 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `%patchlist` 条目 `0027-unzip-zipbomb-part6.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 332 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `%patchlist` 条目 `0028-unzip-zipbomb-part7.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 333 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `%patchlist` 条目 `0029-unzip-zipbomb-switch.patch` 上方缺少注释行，应添加一行以 `#` 开头的注释说明补丁用途或给出上游链接 |
| 334 | [autoconf/autoconf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/autoconf/autoconf.spec) | 补丁文件名 `autoreconf-ltdl.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 335 | [autofs/autofs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/autofs/autofs.spec) | 补丁文件名 `autofs-5.1.9-Fix-incompatible-function-pointer-types-in-c...` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 336 | [bdfresize/bdfresize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bdfresize/bdfresize.spec) | 补丁文件名 `010_ftbfs-gcc4.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 337 | [bdfresize/bdfresize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bdfresize/bdfresize.spec) | 补丁文件名 `020_minus-sign.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 338 | [bison/bison.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bison/bison.spec) | 补丁文件名 `glr2-cc-ensure-yylookaheadNeeds-is-same-size-as-yystates....` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 339 | [blake3/blake3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/blake3/blake3.spec) | 补丁文件名 `riscv-v.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 340 | [busybox/busybox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/busybox/busybox.spec) | 补丁文件名 `busybox-1.36.1-no-cbq.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 341 | [busybox/busybox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/busybox/busybox.spec) | 补丁文件名 `busybox-1.37.0-fix-conditional-for-sha1_process_block64_s...` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 342 | [compsize/compsize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/compsize/compsize.spec) | 补丁文件名 `compsize-1.5-fix-build-btrfsprogs-0.6.1.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 343 | [crash/crash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crash/crash.spec) | 补丁文件名 `lzo_snappy_zstd.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 344 | [crash/crash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crash/crash.spec) | 补丁文件名 `crash-9.0.1_build.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 345 | [dblatex/dblatex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dblatex/dblatex.spec) | 补丁文件名 `dblatex-0.3.12-replace-imp-by-importlib.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 346 | [dblatex/dblatex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dblatex/dblatex.spec) | 补丁文件名 `dblatex-0.3.12-adjust-submodule-imports.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 347 | [dblatex/dblatex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dblatex/dblatex.spec) | 补丁文件名 `dblatex-0.3.4-disable-debian.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 348 | [dbus-broker/dbus-broker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dbus-broker/dbus-broker.spec) | 补丁文件名 `test-sockopt-loosen-verification-of-stale-pidfds.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 349 | [dejagnu/dejagnu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dejagnu/dejagnu.spec) | 补丁文件名 `testsuite-legacy.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 350 | [dotnet10.0/dotnet10.0.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dotnet10.0/dotnet10.0.spec) | 补丁文件名 `runtime-disable-fortify-on-ilasm-parser.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 351 | [doxygen/doxygen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/doxygen/doxygen.spec) | 补丁文件名 `doxygen-no-lowercase-man-names.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 352 | [doxygen/doxygen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/doxygen/doxygen.spec) | 补丁文件名 `reproducible.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 353 | [dwz/dwz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dwz/dwz.spec) | 补丁文件名 `remove-gold-tests.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 354 | [efivar/efivar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/efivar/efivar.spec) | 补丁文件名 `fix-build-failure-with-glibc-2.43.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 355 | [eigen3/eigen3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/eigen3/eigen3.spec) | 补丁文件名 `eigen3_libinstalldir.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 356 | [fakeroot/fakeroot.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fakeroot/fakeroot.spec) | 补丁文件名 `debian_fix-shell-in-fakeroot.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 357 | [findutils/findutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/findutils/findutils.spec) | 补丁文件名 `findutils-xautofs.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 358 | [findutils/findutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/findutils/findutils.spec) | 补丁文件名 `findutils-avoid-crash-system-loop.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 359 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | 补丁文件名 `freetype-2.3.0-enable-spr.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 360 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | 补丁文件名 `freetype-2.2.1-enable-valid.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 361 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | 补丁文件名 `freetype-2.6.5-libtool.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 362 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | 补丁文件名 `freetype-2.8-multilib.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 363 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | 补丁文件名 `freetype-2.10.0-internal-outline.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 364 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | 补丁文件名 `freetype-2.10.1-debughook.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 365 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | 补丁文件名 `gcc-add-defaultsspec.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 366 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | 补丁文件名 `gcc44-textdomain.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 367 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | 补丁文件名 `gcc44-rename-info-files.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 368 | [gdbm/gdbm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gdbm/gdbm.spec) | 补丁文件名 `gdbm-no-build-date.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 369 | [glib/glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glib/glib.spec) | 补丁文件名 `meson.build-Avoid-linking-with-libatomic-when-unneed.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 370 | [glibc/glibc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glibc/glibc.spec) | 补丁文件名 `glibc-2.4-china.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 371 | [glmark2/glmark2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glmark2/glmark2.spec) | 补丁文件名 `glmark2-2023.01-backport-visual-config-match.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 372 | [grub/grub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grub/grub.spec) | 补丁文件名 `skip-efi_uga.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 373 | [grub/grub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grub/grub.spec) | 补丁文件名 `blsuki-append-version.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 374 | [grub/grub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grub/grub.spec) | 补丁文件名 `grub-c23-string-func-handling-updates.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 375 | [grub/grub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grub/grub.spec) | 补丁文件名 `conditionally-apply-regparm-attr.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 376 | [gtk-doc/gtk-doc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gtk-doc/gtk-doc.spec) | 补丁文件名 `gtk-doc-mkhtml-test-fix.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 377 | [guile/guile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/guile/guile.spec) | 补丁文件名 `guile-fix-riscv64-jit.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 378 | [gzip/gzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gzip/gzip.spec) | 补丁文件名 `manpage-no-date.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 379 | [keybinder/keybinder.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/keybinder/keybinder.spec) | 补丁文件名 `fix-empty-gobject.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 380 | [krb5/krb5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/krb5/krb5.spec) | 补丁文件名 `Fix-strchr-conformance-to-C23.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 381 | [libaio/libaio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libaio/libaio.spec) | 补丁文件名 `libaio-fix-test-off64_t.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 382 | [libdwarf/libdwarf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdwarf/libdwarf.spec) | 补丁文件名 `libdwarf-both.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 383 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | 补丁文件名 `readv-proto.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 384 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | 补丁文件名 `skip_cycles.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 385 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | 补丁文件名 `python3.8-compat.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 386 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | 补丁文件名 `swig4_moduleimport.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 387 | [libsemanage/libsemanage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsemanage/libsemanage.spec) | 补丁文件名 `fix-test-failure-with-secilc.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 388 | [libtiff/libtiff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtiff/libtiff.spec) | 补丁文件名 `libtiff-4.0.3-seek.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 389 | [libtiff/libtiff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtiff/libtiff.spec) | 补丁文件名 `libtiff-4.7.0-test_directory.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 390 | [libxcrypt/libxcrypt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxcrypt/libxcrypt.spec) | 补丁文件名 `fix-werror-discarded-qualifiers.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 391 | [libxkbcommon/libxkbcommon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxkbcommon/libxkbcommon.spec) | 补丁文件名 `libxkbcommon-1.13.1-mask-x11-test.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 392 | [lz4/lz4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lz4/lz4.spec) | 补丁文件名 `lz4-export.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 393 | [lz4/lz4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lz4/lz4.spec) | 补丁文件名 `Enable-LZ4_FAST_DEC_LOOP-for-RISC-V.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 394 | [mariadb/mariadb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mariadb/mariadb.spec) | 补丁文件名 `fix-pamdir.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 395 | [mdevd/mdevd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mdevd/mdevd.spec) | 补丁文件名 `some-libcs-have-a-char-const-strchr-need-to-investigate.p...` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 396 | [mesa/mesa.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mesa/mesa.spec) | 补丁文件名 `mesa-26.1.1-zink-kmsro-for-img-blob.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 397 | [mesa/mesa.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mesa/mesa.spec) | 补丁文件名 `mesa-26.1.1-pvr-conformance.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 398 | [mesa-demos/mesa-demos.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mesa-demos/mesa-demos.spec) | 补丁文件名 `mesa-demos-8.5.0-legal.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 399 | [mesa-demos/mesa-demos.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mesa-demos/mesa-demos.spec) | 补丁文件名 `mesa-demos-system-data.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 400 | [multipath-tools/multipath-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/multipath-tools/multipath-tools.spec) | 补丁文件名 `multipath-tools-fix-c23-errors-with-strchr.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 401 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | 补丁文件名 `nmap-4.03-mktemp.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 402 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | 补丁文件名 `nmap-4.52-noms.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 403 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | 补丁文件名 `ncat_reg_stdin.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 404 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | 补丁文件名 `nmap_resolve_config.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 405 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | 补丁文件名 `nmap-pcre2.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 406 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | 补丁文件名 `nmap-ems-ssl-enum-ciphers.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 407 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | 补丁文件名 `nmap-libpcap.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 408 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | 补丁文件名 `hwy-broken-rvv.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 409 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | 补丁文件名 `v8-riscv-fix-trampoline.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 410 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | 补丁文件名 `v8-riscv-fix-trampoline-release.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 411 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | 补丁文件名 `v8-riscv-fix-sp.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 412 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | 补丁文件名 `mkinstalldirs.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 413 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | 补丁文件名 `args.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 414 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | 补丁文件名 `freetype2.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 415 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | 补丁文件名 `Makefile-Add-DESTDIR.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 416 | [patch/patch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/patch/patch.spec) | 补丁文件名 `CVE-2019-20633.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 417 | [policycoreutils/policycoreutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/policycoreutils/policycoreutils.spec) | 补丁文件名 `fix-discarded-qualifiers-warning-with-glib-2.43.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 418 | [postgresql/postgresql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postgresql/postgresql.spec) | 补丁文件名 `rpm-pgsql.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 419 | [postgresql/postgresql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postgresql/postgresql.spec) | 补丁文件名 `postgresql-var-run-socket.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 420 | [postgresql/postgresql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postgresql/postgresql.spec) | 补丁文件名 `postgresql-no-libecpg.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 421 | [powertop/powertop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/powertop/powertop.spec) | 补丁文件名 `powertop-2.7-always-create-params.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 422 | [quota/quota.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/quota/quota.spec) | 补丁文件名 `quota-4.06-warnquota-configuration-tunes.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 423 | [quota/quota.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/quota/quota.spec) | 补丁文件名 `quota-4.03-Validate-upper-bound-of-RPC-port.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 424 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | 补丁文件名 `brpcompress.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 425 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | 补丁文件名 `checkfilesnoinfodir.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 426 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | 补丁文件名 `rpmpopt.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 427 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | 补丁文件名 `safeugid.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 428 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | 补丁文件名 `fileattrs.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 429 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | 补丁文件名 `brp-compress-no-img.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 430 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | 补丁文件名 `emptymanifest.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 431 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | 补丁文件名 `find-lang-qt-qm.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 432 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | 补丁文件名 `canongnu.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 433 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | 补丁文件名 `unshare.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 434 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | 补丁文件名 `buildroot-symlink.diff` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 435 | [rrdtool/rrdtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | 补丁文件名 `rrdtool-1.6.0-ruby-2-fix.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 436 | [rrdtool/rrdtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | 补丁文件名 `rrdtool-zero_vs_nothing.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 437 | [rrdtool/rrdtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | 补丁文件名 `Fix-compatibility-with-Tcl-9.0.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 438 | [rrdtool/rrdtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | 补丁文件名 `correctly-link-ruby-bindings.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 439 | [utf8cpp/utf8cpp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/utf8cpp/utf8cpp.spec) | 补丁文件名 `utf8cpp-cmake.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 440 | [util-linux/util-linux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/util-linux/util-linux.spec) | 补丁文件名 `login-lastlog-create.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 441 | [util-linux/util-linux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/util-linux/util-linux.spec) | 补丁文件名 `login-default-motd-file.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 442 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | 补丁文件名 `uuid-1.6.1-ossp.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 443 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | 补丁文件名 `uuid-1.6.1-mkdir.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 444 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | 补丁文件名 `uuid-1.6.2-php54.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 445 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | 补丁文件名 `uuid-1.6.2-hwaddr.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 446 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | 补丁文件名 `uuid-1.6.2-nostrip.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 447 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | 补丁文件名 `uuid-1.6.2-manfix.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 448 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | 补丁文件名 `uuid-1.6.2-ldflags.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 449 | [valkey/valkey.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/valkey/valkey.spec) | 补丁文件名 `valkey-conf.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 450 | [valkey/valkey.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/valkey/valkey.spec) | 补丁文件名 `valkey-loadmod.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 451 | [xtrans/xtrans.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xtrans/xtrans.spec) | 补丁文件名 `xtrans-1.0.3-avoid-gethostname.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 452 | [xxhash/xxhash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xxhash/xxhash.spec) | 补丁文件名 `xxhash-fix-non-x86-dispatch.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 453 | [xxhash/xxhash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xxhash/xxhash.spec) | 补丁文件名 `xxhash-test-respect-cflags.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 454 | [zlib-ng/zlib-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zlib-ng/zlib-ng.spec) | 补丁文件名 `zlib-ng-2.3.2-riscv-hwprobe.patch` 未以四位数字开头，应以 `0001-0999, 1000-1999, 2000-2999` 中的前缀开头以控制补丁应用顺序 |
| 455 | [libunwind/libunwind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libunwind/libunwind.spec) | 补丁文件名 `3000-libunwind-no-dl-iterate-phdr.patch` 的前缀不在 `0001-0999, 1000-1999, 2000-2999` 范围内，应使用该范围内的前缀以控制补丁应用顺序 |
| 456 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | 补丁文件名 `60588.diff` 的前缀不在 `0001-0999, 1000-1999, 2000-2999` 范围内，应使用该范围内的前缀以控制补丁应用顺序 |
| 457 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | 补丁文件名 `60591.diff` 的前缀不在 `0001-0999, 1000-1999, 2000-2999` 范围内，应使用该范围内的前缀以控制补丁应用顺序 |
| 458 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | 补丁文件名 `6464-auto-config-update.diff` 的前缀不在 `0001-0999, 1000-1999, 2000-2999` 范围内，应使用该范围内的前缀以控制补丁应用顺序 |
| 459 | [audiofile/audiofile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/audiofile/audiofile.spec) | 补丁数量超过 3 个（共 11 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 460 | [binutils/binutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/binutils/binutils.spec) | 补丁数量超过 3 个（共 5 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 461 | [cyrus-sasl/cyrus-sasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cyrus-sasl/cyrus-sasl.spec) | 补丁数量超过 3 个（共 4 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 462 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | 补丁数量超过 3 个（共 7 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 463 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | 补丁数量超过 3 个（共 40 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 464 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | 补丁数量超过 3 个（共 9 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 465 | [grub/grub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grub/grub.spec) | 补丁数量超过 3 个（共 4 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 466 | [icu4c/icu4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/icu4c/icu4c.spec) | 补丁数量超过 3 个（共 5 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 467 | [indent/indent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/indent/indent.spec) | 补丁数量超过 3 个（共 4 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 468 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | 补丁数量超过 3 个（共 4 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 469 | [lua/lua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua/lua.spec) | 补丁数量超过 3 个（共 4 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 470 | [ncurses/ncurses.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ncurses/ncurses.spec) | 补丁数量超过 3 个（共 4 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 471 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | 补丁数量超过 3 个（共 6 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 472 | [openjade/openjade.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openjade/openjade.spec) | 补丁数量超过 3 个（共 6 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 473 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | 补丁数量超过 3 个（共 6 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 474 | [orbit2/orbit2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/orbit2/orbit2.spec) | 补丁数量超过 3 个（共 6 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 475 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | 补丁数量超过 3 个（共 4 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 476 | [pesign/pesign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | 补丁数量超过 3 个（共 5 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 477 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | 补丁数量超过 3 个（共 8 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 478 | [procmail/procmail.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/procmail/procmail.spec) | 补丁数量超过 3 个（共 6 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 479 | [qt6-qtbase/qt6-qtbase.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtbase/qt6-qtbase.spec) | 补丁数量超过 3 个（共 7 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 480 | [qt6-qtwebengine/qt6-qtwebengine.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtwebengine/qt6-qtwebengine.spec) | 补丁数量超过 3 个（共 5 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 481 | [readline/readline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/readline/readline.spec) | 补丁数量超过 3 个（共 4 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 482 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | 补丁数量超过 3 个（共 15 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 483 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | 补丁数量超过 3 个（共 9 个 `Patch` 字段），应使用 `%patchlist` 统一管理 |
| 484 | [cdparanoia/cdparanoia.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cdparanoia/cdparanoia.spec) | `%patchlist` 应位于 `%description` 之上 |
| 485 | [openssl/openssl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openssl/openssl.spec) | `%patchlist` 应位于 `%description` 之上 |
| 486 | [python-torch/python-torch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-torch/python-torch.spec) | `%patchlist` 应位于 `%description` 之上 |
| 487 | [spdk/spdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/spdk/spdk.spec) | `%patchlist` 应位于 `%description` 之上 |
| 488 | [aom/aom.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aom/aom.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 489 | [aspell/aspell.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aspell/aspell.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 490 | [cgctl/cgctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cgctl/cgctl.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 491 | [compsize/compsize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/compsize/compsize.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildRequires` 之间，与 `Source` 字段的放置顺序类似 |
| 492 | [crash/crash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crash/crash.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 493 | [dbus-broker/dbus-broker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dbus-broker/dbus-broker.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 494 | [eigen3/eigen3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/eigen3/eigen3.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 495 | [giflib/giflib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/giflib/giflib.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 496 | [guile/guile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/guile/guile.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 497 | [hipfft/hipfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipfft/hipfft.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 498 | [hipify/hipify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipify/hipify.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 499 | [hipsparselt/hipsparselt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipsparselt/hipsparselt.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 500 | [keybinder/keybinder.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/keybinder/keybinder.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 501 | [libaio/libaio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libaio/libaio.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 502 | [libdwarf/libdwarf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdwarf/libdwarf.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 503 | [libjpeg-turbo/libjpeg-turbo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libjpeg-turbo/libjpeg-turbo.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 504 | [libunwind/libunwind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libunwind/libunwind.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 505 | [lua-json/lua-json.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua-json/lua-json.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildRequires` 之间，与 `Source` 字段的放置顺序类似 |
| 506 | [msgpack/msgpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/msgpack/msgpack.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 507 | [powertop/powertop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/powertop/powertop.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildRequires` 之间，与 `Source` 字段的放置顺序类似 |
| 508 | [python-python-dateutil/python-python-dateutil.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-dateutil/python-python-dateutil.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 509 | [qhull/qhull.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qhull/qhull.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 510 | [rocblas/rocblas.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocblas/rocblas.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 511 | [rocsolver/rocsolver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocsolver/rocsolver.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 512 | [soxr/soxr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/soxr/soxr.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |
| 513 | [vdo/vdo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vdo/vdo.spec) | `Patch` 字段应位于 `BuildSystem` 与 `BuildOption` 之间，与 `Source` 字段的放置顺序类似 |

## 说明

- 注释要求：规则要求每个 `Patch:` 字段（及 `%patchlist` 条目）上方必须有一行以 `#` 开头的注释，说明补丁用途或给出上游链接。openRuyi 仓库中大量 spec 未遵循此约定。
- 命名要求：补丁文件名应以四位数字开头（`0001-0999` 上游补丁、`1000-1999` CVE 修复或跨版本 backport、`2000-2999` openRuyi 特有补丁），用于控制补丁应用顺序。仓库中部分 spec 使用了 `60588.diff`、`3000-xxx.patch` 等不符合约定的命名。
- `%patchlist`：当补丁数量超过 3 个时，建议使用 `%patchlist` 统一管理，避免逐个 `%patch` 应用。仓库中 `gcc15`（40 个补丁）、`audiofile`（11 个补丁）等 spec 未使用 `%patchlist`。
- 放置顺序：`Patch` 字段应位于 `BuildSystem` 与 `BuildOption`（或 `BuildRequires`）之间，与 `Source` 字段类似。
- 本规则仅扫描 spec 头部区域（`%description`/`%package` 等段落之前），`%patchlist` 位置检查除外（在整个文件中查找）。

> 规则说明：[docs/check-spec-patch.md](../docs/check-spec-patch.md)
