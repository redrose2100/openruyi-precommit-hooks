# check-spec-patch 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库的 spec 文件（`SPECS/{pkg}/{pkg}.spec`）执行 `check-spec-patch` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| --- | ---: | ---: |
| 5267 | 5063 | 204 |

> 说明：问题数按 spec 文件去重统计（一个文件可能命中多条规则）。

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

| # | spec 文件 | 字段值 | 问题所在行数 | 问题类型 |
| --- | --- | --- | ---: | --- |
| 1 | [angelscript/angelscript.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/angelscript/angelscript.spec) | `2000-install-libraries-and-CMake-files-to-GNUInstallDirs....` | 18 | `Patch` 字段上方缺少注释行 |
| 2 | [arrow/arrow.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/arrow/arrow.spec) | `0002-test-use-approximate-comparison-for-quantile.patch` | 31 | `Patch` 字段上方缺少注释行 |
| 3 | [aspell/aspell.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aspell/aspell.spec) | `0002-aspell-quotes.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 4 | [attr/attr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/attr/attr.spec) | `0001-bypass-wrong-output-when-enabled-selinux.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 5 | [attr/attr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/attr/attr.spec) | `0002-dont-skip-security.evm-when-copy-xattr.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 6 | [audiofile/audiofile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/audiofile/audiofile.spec) | `0007-822b732fd31ffcb78f6920001e9b1fbd815fa712.patch` | 29 | `Patch` 字段上方缺少注释行 |
| 7 | [autoconf/autoconf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/autoconf/autoconf.spec) | `autoreconf-ltdl.diff` | 22 | `Patch` 字段上方缺少注释行 |
| 8 | [autofs/autofs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/autofs/autofs.spec) | `autofs-5.1.9-Fix-incompatible-function-pointer-types-in-c...` | 20 | `Patch` 字段上方缺少注释行 |
| 9 | [bash/bash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bash/bash.spec) | `0002-bash-5.3-patch-2.patch` | 28 | `Patch` 字段上方缺少注释行 |
| 10 | [bash/bash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bash/bash.spec) | `0003-bash-5.3-patch-3.patch` | 29 | `Patch` 字段上方缺少注释行 |
| 11 | [bdfresize/bdfresize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bdfresize/bdfresize.spec) | `020_minus-sign.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 12 | [bison/bison.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bison/bison.spec) | `glr2-cc-ensure-yylookaheadNeeds-is-same-size-as-yystates....` | 19 | `Patch` 字段上方缺少注释行 |
| 13 | [cgctl/cgctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cgctl/cgctl.spec) | `2000-cgroups-root-adapt-to-runtime-spec-1.3.patch` | 32 | `Patch` 字段上方缺少注释行 |
| 14 | [cgctl/cgctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cgctl/cgctl.spec) | `2001-cgroups-v3-adapt-to-runtime-spec-1.3.patch` | 33 | `Patch` 字段上方缺少注释行 |
| 15 | [cloud-init/cloud-init.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cloud-init/cloud-init.spec) | `2000-Add-openruyi-support.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 16 | [console-setup/console-setup.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/console-setup/console-setup.spec) | `0001-fix-makefile.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 17 | [crash/crash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crash/crash.spec) | `lzo_snappy_zstd.patch` | 26 | `Patch` 字段上方缺少注释行 |
| 18 | [crash/crash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crash/crash.spec) | `crash-9.0.1_build.patch` | 27 | `Patch` 字段上方缺少注释行 |
| 19 | [cunit/cunit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cunit/cunit.spec) | `0001-cunit-link-ncurses.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 20 | [cunit/cunit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cunit/cunit.spec) | `0002-cunit-ncurses6.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 21 | [cunit/cunit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cunit/cunit.spec) | `0003-avoid-Wformat-security-bug.patch` | 24 | `Patch` 字段上方缺少注释行 |
| 22 | [cyrus-sasl/cyrus-sasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cyrus-sasl/cyrus-sasl.spec) | `0001-cyrus-sasl-lfs.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 23 | [cyrus-sasl/cyrus-sasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cyrus-sasl/cyrus-sasl.spec) | `0002-fix_libpq-fe_include.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 24 | [cyrus-sasl/cyrus-sasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cyrus-sasl/cyrus-sasl.spec) | `0003-Fix-time.h-check.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 25 | [cyrus-sasl/cyrus-sasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cyrus-sasl/cyrus-sasl.spec) | `0004-cyrus-sasl-make-digestmd5-work-ssl3.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 26 | [dbus-broker/dbus-broker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dbus-broker/dbus-broker.spec) | `test-sockopt-loosen-verification-of-stale-pidfds.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 27 | [dejagnu/dejagnu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dejagnu/dejagnu.spec) | `testsuite-legacy.patch` | 25 | `Patch` 字段上方缺少注释行 |
| 28 | [desktop-file-utils/desktop-file-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/desktop-file-utils/desktop-file-utils.spec) | `0001-validate-Add-Phosh-to-list-of-valid-OnlyShowIn-envir...` | 20 | `Patch` 字段上方缺少注释行 |
| 29 | [dosfstools/dosfstools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dosfstools/dosfstools.spec) | `0001-Fix-vasprintf-implementation.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 30 | [doxygen/doxygen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/doxygen/doxygen.spec) | `doxygen-no-lowercase-man-names.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 31 | [doxygen/doxygen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/doxygen/doxygen.spec) | `reproducible.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 32 | [duktape/duktape.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/duktape/duktape.spec) | `0001-duktape-link-m.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 33 | [dwz/dwz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dwz/dwz.spec) | `remove-gold-tests.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 34 | [eigen3/eigen3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/eigen3/eigen3.spec) | `eigen3_libinstalldir.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 35 | [ethtool/ethtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ethtool/ethtool.spec) | `0001-netlink-fix-missing-headers-in-text-output.patch` | 24 | `Patch` 字段上方缺少注释行 |
| 36 | [ethtool/ethtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ethtool/ethtool.spec) | `0002-netlink-fix-print_string-when-the-value-is-NULL.patch` | 25 | `Patch` 字段上方缺少注释行 |
| 37 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `0001-expect.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 38 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `0002-expect-fixes.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 39 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `0003-expect-log.patch` | 24 | `Patch` 字段上方缺少注释行 |
| 40 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `0004-config-guess-sub-update.patch` | 25 | `Patch` 字段上方缺少注释行 |
| 41 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `0005-expect-errorfd.patch` | 26 | `Patch` 字段上方缺少注释行 |
| 42 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `0006-expect-5.45-format-security.patch` | 27 | `Patch` 字段上方缺少注释行 |
| 43 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `0007-expect-fix-implicit.patch` | 28 | `Patch` 字段上方缺少注释行 |
| 44 | [f2fs-tools/f2fs-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/f2fs-tools/f2fs-tools.spec) | `0001-f2fs-tools-1.16.0-c23.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 45 | [fakeroot/fakeroot.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fakeroot/fakeroot.spec) | `debian_fix-shell-in-fakeroot.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 46 | [fcoe-utils/fcoe-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fcoe-utils/fcoe-utils.spec) | `0001-fcoemon-add-snprintf-string-precision-modifiers-in-f...` | 24 | `Patch` 字段上方缺少注释行 |
| 47 | [fcoe-utils/fcoe-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fcoe-utils/fcoe-utils.spec) | `0002-Don-t-attempt-to-memcpy-zero-bytes.patch` | 25 | `Patch` 字段上方缺少注释行 |
| 48 | [fcoe-utils/fcoe-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fcoe-utils/fcoe-utils.spec) | `0003-Fix-build-against-glibc-2.43.patch` | 26 | `Patch` 字段上方缺少注释行 |
| 49 | [fscryptctl/fscryptctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fscryptctl/fscryptctl.spec) | `0001-disable-doc.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 50 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `gcc-add-defaultsspec.diff` | 152 | `Patch` 字段上方缺少注释行 |
| 51 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `gcc44-textdomain.patch` | 153 | `Patch` 字段上方缺少注释行 |
| 52 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `gcc44-rename-info-files.patch` | 154 | `Patch` 字段上方缺少注释行 |
| 53 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0002-RISC-V-Fix-missing-implied-Zicsr-from-Zve32x.patch` | 158 | `Patch` 字段上方缺少注释行 |
| 54 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0003-RISC-V-Add-new-option-param-gpr2vr-cost-for-rvv-insn...` | 159 | `Patch` 字段上方缺少注释行 |
| 55 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0004-PATCH-RISC-V-Recognized-svadu-and-svade-extension.patch` | 160 | `Patch` 字段上方缺少注释行 |
| 56 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0005-PATCH-RISC-V-Minimal-support-for-sdtrig-and-ssstrict...` | 161 | `Patch` 字段上方缺少注释行 |
| 57 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0006-PATCH-RISC-V-Minimal-support-for-zama16b-extension.p...` | 162 | `Patch` 字段上方缺少注释行 |
| 58 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0007-RISC-V-Support-RISC-V-Profiles-20-22.patch` | 163 | `Patch` 字段上方缺少注释行 |
| 59 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0008-RISC-V-Support-RISC-V-Profiles-23.patch` | 164 | `Patch` 字段上方缺少注释行 |
| 60 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0009-RISC-V-Support-for-zilsd-and-zclsd-extensions.patch` | 165 | `Patch` 字段上方缺少注释行 |
| 61 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0010-RISC-V-Minimal-support-for-ssnpm-smnpm-and-smmpm-ext...` | 166 | `Patch` 字段上方缺少注释行 |
| 62 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0011-RISC-V-Introduce-riscv-ext-.def-to-define-extensions...` | 167 | `Patch` 字段上方缺少注释行 |
| 63 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0012-RISC-V-Use-riscv-ext.def-to-generate-target-options-...` | 168 | `Patch` 字段上方缺少注释行 |
| 64 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0013-RISC-V-Generate-extension-table-in-documentation-fro...` | 169 | `Patch` 字段上方缺少注释行 |
| 65 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0014-RISC-V-Adjust-riscv_can_inline_p.patch` | 170 | `Patch` 字段上方缺少注释行 |
| 66 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0015-RISC-V-Introduce-riscv_ext_info_t-to-hold-extension-...` | 171 | `Patch` 字段上方缺少注释行 |
| 67 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0016-RISC-V-Drop-riscv_implied_info-and-riscv_combine_inf...` | 172 | `Patch` 字段上方缺少注释行 |
| 68 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0017-RISC-V-Drop-riscv_ext_version_table-in-favor-of-risc...` | 173 | `Patch` 字段上方缺少注释行 |
| 69 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0018-RISC-V-Drop-riscv_ext_flag_table-in-favor-of-riscv_e...` | 174 | `Patch` 字段上方缺少注释行 |
| 70 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0019-RISC-V-Add-augmented-hypervisor-series-extensions.patch` | 175 | `Patch` 字段上方缺少注释行 |
| 71 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0020-RISC-V-Support-CPUs-in-march.patch` | 176 | `Patch` 字段上方缺少注释行 |
| 72 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0021-RISC-V-Add-minimal-support-of-double-trap-extension-...` | 177 | `Patch` 字段上方缺少注释行 |
| 73 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0022-PATCH-RISC-V-Add-smcntrpmf-extension.patch` | 178 | `Patch` 字段上方缺少注释行 |
| 74 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0023-RISC-V-Add-Shlcofideleg-extension.patch` | 179 | `Patch` 字段上方缺少注释行 |
| 75 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0024-PATCH-v2-RISC-V-Add-svbare-extension.patch` | 180 | `Patch` 字段上方缺少注释行 |
| 76 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0025-PATCH-RISC-V-Imply-zicsr-for-svade-and-svadu-extensi...` | 181 | `Patch` 字段上方缺少注释行 |
| 77 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0026-RISC-V-Update-extension-defination.patch` | 182 | `Patch` 字段上方缺少注释行 |
| 78 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0027-RISC-V-Support-Sm-scsrind-extensions.patch` | 183 | `Patch` 字段上方缺少注释行 |
| 79 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0028-RISC-V-Support-Smrnmi-extension.patch` | 184 | `Patch` 字段上方缺少注释行 |
| 80 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0029-RISC-V-Support-Ssccptr-extension.patch` | 185 | `Patch` 字段上方缺少注释行 |
| 81 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0030-RISC-V-Support-Sscounterenw-extension.patch` | 186 | `Patch` 字段上方缺少注释行 |
| 82 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0031-RISC-V-Support-Sstvala-extension.patch` | 187 | `Patch` 字段上方缺少注释行 |
| 83 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0032-RISC-V-Support-Sstvecd-extension.patch` | 188 | `Patch` 字段上方缺少注释行 |
| 84 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0033-RISC-V-Support-Ssu64xl-extension.patch` | 189 | `Patch` 字段上方缺少注释行 |
| 85 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0034-RISC-V-Update-Profiles-string-in-RV23.patch` | 190 | `Patch` 字段上方缺少注释行 |
| 86 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0035-RISC-V-Add-Profiles-RVA-B23S64-support.patch` | 191 | `Patch` 字段上方缺少注释行 |
| 87 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `0036-RISC-V-check-if-we-can-vec_extract.patch` | 192 | `Patch` 字段上方缺少注释行 |
| 88 | [gcc16/gcc16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc16/gcc16.spec) | `2000-textdomain.patch` | 152 | `Patch` 字段上方缺少注释行 |
| 89 | [gcc16/gcc16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc16/gcc16.spec) | `2001-rename-info-files.patch` | 153 | `Patch` 字段上方缺少注释行 |
| 90 | [gdbm/gdbm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gdbm/gdbm.spec) | `gdbm-no-build-date.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 91 | [gflags/gflags.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gflags/gflags.spec) | `0001-gflags-fix_pkgconfig.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 92 | [giflib/giflib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/giflib/giflib.spec) | `0001-disable-doc.patch` | 17 | `Patch` 字段上方缺少注释行 |
| 93 | [glib/glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glib/glib.spec) | `meson.build-Avoid-linking-with-libatomic-when-unneed.patch` | 37 | `Patch` 字段上方缺少注释行 |
| 94 | [go-github-envoyproxy-protoc-gen-validate/go-github-envoyproxy-protoc-gen-validate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-envoyproxy-protoc-gen-validate/go-github-envoyproxy-protoc-gen-validate.spec) | `2000-fix-checker.go-error.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 95 | [go-gopkg-tomb.v1/go-gopkg-tomb.v1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-gopkg-tomb.v1/go-gopkg-tomb.v1.spec) | `2000-fix-killf-test-format-string.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 96 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `0001-some-headers.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 97 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `0002-gpm-1.20.6-multilib.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 98 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `0003-gpm-1.20.1-lib-silent.patch` | 24 | `Patch` 字段上方缺少注释行 |
| 99 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `0004-gpm-1.20.5-close-fds.patch` | 25 | `Patch` 字段上方缺少注释行 |
| 100 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `0005-gpm-1.20.1-weak-wgetch.patch` | 26 | `Patch` 字段上方缺少注释行 |
| 101 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `0006-gpm-1.20.7-rhbz-668480-gpm-types-7-manpage-fixes.patch` | 27 | `Patch` 字段上方缺少注释行 |
| 102 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `0007-src-daemon-remove-obvious-use-of-unitialized-data.patch` | 28 | `Patch` 字段上方缺少注释行 |
| 103 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `0008-src-daemon-reindent-switch-statement-to-avoid-compil...` | 29 | `Patch` 字段上方缺少注释行 |
| 104 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `0009-configure-drop-broken-configure-code.patch` | 30 | `Patch` 字段上方缺少注释行 |
| 105 | [gpsd/gpsd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpsd/gpsd.spec) | `2000-gpsd_hotplug_rules_disable.patch` | 17 | `Patch` 字段上方缺少注释行 |
| 106 | [gptfdisk/gptfdisk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gptfdisk/gptfdisk.spec) | `2000-fix-include-ncurses.h-unconditionally.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 107 | [grpc/grpc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grpc/grpc.spec) | `2000-force-system-libraries-in-isolated-environments.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 108 | [guile/guile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/guile/guile.spec) | `guile-fix-riscv64-jit.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 109 | [gzip/gzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gzip/gzip.spec) | `manpage-no-date.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 110 | [hipfft/hipfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipfft/hipfft.spec) | `0001-hipfft-hipfftw-soversion.patch` | 25 | `Patch` 字段上方缺少注释行 |
| 111 | [hipify/hipify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipify/hipify.spec) | `0001-prepare-hipify-cmake.patch` | 28 | `Patch` 字段上方缺少注释行 |
| 112 | [icu4c/icu4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/icu4c/icu4c.spec) | `0001-icu-fix-install-mode-files.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 113 | [icu4c/icu4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/icu4c/icu4c.spec) | `0002-icu-error-reporting.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 114 | [icu4c/icu4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/icu4c/icu4c.spec) | `0003-icu-avoid-x87-excess-precision.patch` | 24 | `Patch` 字段上方缺少注释行 |
| 115 | [icu4c/icu4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/icu4c/icu4c.spec) | `0004-locale.patch` | 25 | `Patch` 字段上方缺少注释行 |
| 116 | [icu4c/icu4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/icu4c/icu4c.spec) | `0005-nan-undefined-conversion.patch` | 26 | `Patch` 字段上方缺少注释行 |
| 117 | [itstool/itstool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/itstool/itstool.spec) | `0001-Fix-insufficiently-quoted-regular-expressions.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 118 | [itstool/itstool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/itstool/itstool.spec) | `0002-Switch-from-libxml2-to-lxml.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 119 | [kf6-ksvg/kf6-ksvg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-ksvg/kf6-ksvg.spec) | `0001-Revert-Support-for-fractional-scaling.patch` | 24 | `Patch` 字段上方缺少注释行 |
| 120 | [kiwi/kiwi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kiwi/kiwi.spec) | `2000-optional-manpage.patch` | 26 | `Patch` 字段上方缺少注释行 |
| 121 | [libburn/libburn.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libburn/libburn.spec) | `0001-libburn-1.5.6-c23.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 122 | [libdwarf/libdwarf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdwarf/libdwarf.spec) | `libdwarf-both.patch` | 17 | `Patch` 字段上方缺少注释行 |
| 123 | [libfaketime/libfaketime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfaketime/libfaketime.spec) | `0001-Add-const-qualifiers-to-fix-build-with-ISO-C23.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 124 | [libfaketime/libfaketime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libfaketime/libfaketime.spec) | `0002-tests-Silence-an-unused-but-set-variable-warning-wit...` | 23 | `Patch` 字段上方缺少注释行 |
| 125 | [libjpeg-turbo/libjpeg-turbo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libjpeg-turbo/libjpeg-turbo.spec) | `0001-libjpeg-turbo-cmake.patch` | 17 | `Patch` 字段上方缺少注释行 |
| 126 | [liblc3/liblc3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/liblc3/liblc3.spec) | `0001-Revert-build-fix-rpath-issue.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 127 | [liblognorm/liblognorm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/liblognorm/liblognorm.spec) | `0001-Port-pcre-dependency-to-pcre2.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 128 | [libmodulemd/libmodulemd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmodulemd/libmodulemd.spec) | `0001-tests-Adapt-to-glib-2.87.0.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 129 | [libmodulemd/libmodulemd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmodulemd/libmodulemd.spec) | `0002-tests-Adapt-to-pygobject-3.55.0.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 130 | [libosinfo/libosinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libosinfo/libosinfo.spec) | `0001-libosinfo-libxml2-2.14.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 131 | [libseccomp/libseccomp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libseccomp/libseccomp.spec) | `2000-make-python-build.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 132 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | `readv-proto.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 133 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | `skip_cycles.patch` | 24 | `Patch` 字段上方缺少注释行 |
| 134 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | `swig4_moduleimport.patch` | 27 | `Patch` 字段上方缺少注释行 |
| 135 | [libsquish/libsquish.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsquish/libsquish.spec) | `2000-OBCMake-Replace-hardcoded-cmake-install-paths-with-C...` | 21 | `Patch` 字段上方缺少注释行 |
| 136 | [libtiff/libtiff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtiff/libtiff.spec) | `libtiff-4.0.3-seek.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 137 | [libtiff/libtiff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtiff/libtiff.spec) | `libtiff-4.7.0-test_directory.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 138 | [libunwind/libunwind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libunwind/libunwind.spec) | `0001-Fix-bad-prototype-for-malloc-in-test.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 139 | [libutempter/libutempter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libutempter/libutempter.spec) | `0001-fix-install-path.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 140 | [libvdpau/libvdpau.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libvdpau/libvdpau.spec) | `0001-libvdpau-av1-trace.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 141 | [libwebp/libwebp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libwebp/libwebp.spec) | `0001-libwebp-cmakedir.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 142 | [libwebp/libwebp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libwebp/libwebp.spec) | `0002-libwebp-rpath.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 143 | [libyuv/libyuv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libyuv/libyuv.spec) | `0001-fix-install-dir.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 144 | [llvm-snapshot/llvm-snapshot.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvm-snapshot/llvm-snapshot.spec) | `2000-Add-riscv64-openruyi-linux-triple-and-set-it-to-rva2...` | 87 | `Patch` 字段上方缺少注释行 |
| 145 | [llvm-snapshot/llvm-snapshot.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvm-snapshot/llvm-snapshot.spec) | `2001-Add-openruyi-linux-to-X86_64Triples-and-RISCV64Tripl...` | 89 | `Patch` 字段上方缺少注释行 |
| 146 | [llvm22/llvm22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvm22/llvm22.spec) | `2000-Add-riscv64-openruyi-linux-triple-and-set-it-to-rva2...` | 86 | `Patch` 字段上方缺少注释行 |
| 147 | [llvm22/llvm22.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvm22/llvm22.spec) | `2001-Add-openruyi-linux-to-X86_64Triples-and-RISCV64Tripl...` | 88 | `Patch` 字段上方缺少注释行 |
| 148 | [lsof/lsof.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lsof/lsof.spec) | `2000-skip-LTlock-test-in-package-builds.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 149 | [lua/lua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua/lua.spec) | `0001-lua-5.4.6-idsize.patch` | 27 | `Patch` 字段上方缺少注释行 |
| 150 | [lua/lua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua/lua.spec) | `0002-lua-5.4.0-beta-autotoolize.patch` | 28 | `Patch` 字段上方缺少注释行 |
| 151 | [lua/lua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua/lua.spec) | `0003-lua-5.2.2-configure-linux.patch` | 29 | `Patch` 字段上方缺少注释行 |
| 152 | [lua/lua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua/lua.spec) | `0004-lua-5.3.0-configure-compat-module.patch` | 30 | `Patch` 字段上方缺少注释行 |
| 153 | [lua-json/lua-json.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua-json/lua-json.spec) | `0001-support-lpeg1.1.0.patch` | 17 | `Patch` 字段上方缺少注释行 |
| 154 | [lz4/lz4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lz4/lz4.spec) | `lz4-export.diff` | 19 | `Patch` 字段上方缺少注释行 |
| 155 | [mariadb/mariadb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mariadb/mariadb.spec) | `fix-pamdir.patch` | 42 | `Patch` 字段上方缺少注释行 |
| 156 | [mergerfs/mergerfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mergerfs/mergerfs.spec) | `0001-no_chown_during_install.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 157 | [mkosi/mkosi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mkosi/mkosi.spec) | `0001-Add-openruyi-support.patch` | 24 | `Patch` 字段上方缺少注释行 |
| 158 | [msgpack/msgpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/msgpack/msgpack.spec) | `0002-msgpack-cmake4.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 159 | [nghttp3/nghttp3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nghttp3/nghttp3.spec) | `0001-fix-install-path.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 160 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `v8-riscv-fix-trampoline.patch` | 43 | `Patch` 字段上方缺少注释行 |
| 161 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `v8-riscv-fix-trampoline-release.patch` | 44 | `Patch` 字段上方缺少注释行 |
| 162 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `60591.diff` | 49 | `Patch` 字段上方缺少注释行 |
| 163 | [nss/nss.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nss/nss.spec) | `2001-Make-dbtests-certutil-K-timeout-configurable.patch` | 29 | `Patch` 字段上方缺少注释行 |
| 164 | [numad/numad.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/numad/numad.spec) | `0001-recognize-m-option-correctly.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 165 | [numad/numad.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/numad/numad.spec) | `0002-numad_log-fix-buffer-overflow.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 166 | [numad/numad.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/numad/numad.spec) | `0003-avoid-array-index-out-of-bounds.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 167 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `0001-reproducible.patch` | 39 | `Patch` 字段上方缺少注释行 |
| 168 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `0002-LDAPI-socket-location.patch` | 40 | `Patch` 字段上方缺少注释行 |
| 169 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `0003-pie-compile.patch` | 41 | `Patch` 字段上方缺少注释行 |
| 170 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `0004-In-monitor-backend-do-not-return-Connection0-entries...` | 42 | `Patch` 字段上方缺少注释行 |
| 171 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `0005-Clear-shared-key-only-in-close-function.patch` | 43 | `Patch` 字段上方缺少注释行 |
| 172 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `0006-gcc14-v2.patch` | 44 | `Patch` 字段上方缺少注释行 |
| 173 | [openzl/openzl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openzl/openzl.spec) | `2000-add-install-rules-for-CLI-tools-and-parser-targets.p...` | 18 | `Patch` 字段上方缺少注释行 |
| 174 | [openzl/openzl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openzl/openzl.spec) | `2001-feat-prefer-system-installed-zstd-over-bundled-depen...` | 19 | `Patch` 字段上方缺少注释行 |
| 175 | [orbit2/orbit2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/orbit2/orbit2.spec) | `0001-ORBit2-2.14.3-multilib.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 176 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | `args.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 177 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | `freetype2.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 178 | [perl-Log-Any/perl-Log-Any.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Log-Any/perl-Log-Any.spec) | `2000-isolate-syslog-test-env.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 179 | [perl-rpm-packaging/perl-rpm-packaging.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-rpm-packaging/perl-rpm-packaging.spec) | `0001-fileattrs.diff` | 16 | `Patch` 字段上方缺少注释行 |
| 180 | [pesign/pesign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `0001-cms_common-Fixed-Segmentation-fault.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 181 | [pesign/pesign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `0002-Fix-reversed-calloc-arguments.patch` | 24 | `Patch` 字段上方缺少注释行 |
| 182 | [pesign/pesign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `0003-Work-around-OpenSC-changing-token-names-on-fedora-bu...` | 25 | `Patch` 字段上方缺少注释行 |
| 183 | [pesign/pesign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `0004-cms_common-skip-authentication-on-the-Friendly-slot....` | 26 | `Patch` 字段上方缺少注释行 |
| 184 | [pesign/pesign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `0005-pesum-strrchr-should-be-of-type-const.patch` | 27 | `Patch` 字段上方缺少注释行 |
| 185 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `0001-pinfo-0.6.9-infopath.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 186 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `0002-pinfo-0.6.9-xdg.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 187 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `0003-pinfo-0.6.10-man.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 188 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `0004-pinfo-0.6.13-fnocommon.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 189 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `0005-pinfo-0.6.13-gccwarn.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 190 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `0006-pinfo-0.6.13-nogroup.patch` | 24 | `Patch` 字段上方缺少注释行 |
| 191 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `0007-pinfo-0.6.13-stringop-overflow.patch` | 25 | `Patch` 字段上方缺少注释行 |
| 192 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `0008-pinfo-configure-c99.patch` | 26 | `Patch` 字段上方缺少注释行 |
| 193 | [plasma-desktop/plasma-desktop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/plasma-desktop/plasma-desktop.spec) | `2000-Apply-branding-to-default-favorites.patch` | 32 | `Patch` 字段上方缺少注释行 |
| 194 | [plasma-desktop/plasma-desktop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/plasma-desktop/plasma-desktop.spec) | `2001-Remove-discover-from-taskmanager-default-launchers.p...` | 33 | `Patch` 字段上方缺少注释行 |
| 195 | [popt/popt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/popt/popt.spec) | `0001-popt-libc-updates.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 196 | [postgresql/postgresql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postgresql/postgresql.spec) | `postgresql-var-run-socket.patch` | 36 | `Patch` 字段上方缺少注释行 |
| 197 | [postgresql/postgresql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postgresql/postgresql.spec) | `postgresql-no-libecpg.patch` | 37 | `Patch` 字段上方缺少注释行 |
| 198 | [powertop/powertop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/powertop/powertop.spec) | `powertop-2.7-always-create-params.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 199 | [python-cart/python-cart.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cart/python-cart.spec) | `0001-python-cart-1.2.2-cryptodomex.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 200 | [python-cppheaderparser/python-cppheaderparser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cppheaderparser/python-cppheaderparser.spec) | `0001-cppheaderparser-silence-invalid-escape-sequence.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 201 | [python-gcloud-aio-auth/python-gcloud-aio-auth.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gcloud-aio-auth/python-gcloud-aio-auth.spec) | `0001-chore-deps-bump-maximum-cryptography-version.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 202 | [python-optimum/python-optimum.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-optimum/python-optimum.spec) | `2000-fix-utils-use-default_factory-for-mutable-dataclass-...` | 20 | `Patch` 字段上方缺少注释行 |
| 203 | [python-optimum-benchmark/python-optimum-benchmark.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-optimum-benchmark/python-optimum-benchmark.spec) | `2000-fix-backends-handle-SpecialTokensMixin-import-for-tr...` | 21 | `Patch` 字段上方缺少注释行 |
| 204 | [python-propcache/python-propcache.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-propcache/python-propcache.spec) | `0001-Update-Cython-to-version-3.2.3.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 205 | [python-tokenizers/python-tokenizers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tokenizers/python-tokenizers.spec) | `2001-fix-bindings-cargo.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 206 | [python-torchvision/python-torchvision.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-torchvision/python-torchvision.spec) | `0001-python-torchvision-ffmpeg8.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 207 | [python-torchvision/python-torchvision.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-torchvision/python-torchvision.spec) | `2000-Add-HIP-detect-logic.patch` | 25 | `Patch` 字段上方缺少注释行 |
| 208 | [qt6-qtwebengine/qt6-qtwebengine.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtwebengine/qt6-qtwebengine.spec) | `0003-riscv-misc.patch` | 28 | `Patch` 字段上方缺少注释行 |
| 209 | [qt6-qtwebengine/qt6-qtwebengine.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtwebengine/qt6-qtwebengine.spec) | `0004-riscv-enable-v8-webasm.patch` | 29 | `Patch` 字段上方缺少注释行 |
| 210 | [quota/quota.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/quota/quota.spec) | `quota-4.06-warnquota-configuration-tunes.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 211 | [quota/quota.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/quota/quota.spec) | `quota-4.03-Validate-upper-bound-of-RPC-port.patch` | 24 | `Patch` 字段上方缺少注释行 |
| 212 | [readline/readline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/readline/readline.spec) | `0002-readline-8.3-patch-2.patch` | 22 | `Patch` 字段上方缺少注释行 |
| 213 | [readline/readline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/readline/readline.spec) | `0003-readline-8.3-patch-3.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 214 | [recutils/recutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/recutils/recutils.spec) | `0001-recutils-1.9-mdbtools-0.9.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 215 | [recutils/recutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/recutils/recutils.spec) | `0002-recutils-c99.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 216 | [rocblas/rocblas.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocblas/rocblas.spec) | `0001-fixup-install-of-tensile-output.patch` | 60 | `Patch` 字段上方缺少注释行 |
| 217 | [rocfft/rocfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocfft/rocfft.spec) | `0001-cmake-use-gnu-installdirs.patch` | 28 | `Patch` 字段上方缺少注释行 |
| 218 | [rocfft/rocfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocfft/rocfft.spec) | `2000-relax-sqlite-version-requirement.patch` | 29 | `Patch` 字段上方缺少注释行 |
| 219 | [rocksdb/rocksdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocksdb/rocksdb.spec) | `0001-no_rpath.patch` | 24 | `Patch` 字段上方缺少注释行 |
| 220 | [rocksdb/rocksdb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocksdb/rocksdb.spec) | `0002-disable_static.patch` | 25 | `Patch` 字段上方缺少注释行 |
| 221 | [rocminfo/rocminfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocminfo/rocminfo.spec) | `0001-adjust-CMAKE_CXX_FLAGS.patch` | 26 | `Patch` 字段上方缺少注释行 |
| 222 | [rocr-runtime/rocr-runtime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocr-runtime/rocr-runtime.spec) | `0001-Add-riscv64-support.patch` | 34 | `Patch` 字段上方缺少注释行 |
| 223 | [rocr-runtime/rocr-runtime.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocr-runtime/rocr-runtime.spec) | `0002-Replace-fence-instructions-for-riscv64.patch` | 35 | `Patch` 字段上方缺少注释行 |
| 224 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `checkfilesnoinfodir.diff` | 34 | `Patch` 字段上方缺少注释行 |
| 225 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `rpmpopt.diff` | 35 | `Patch` 字段上方缺少注释行 |
| 226 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `safeugid.diff` | 36 | `Patch` 字段上方缺少注释行 |
| 227 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `fileattrs.diff` | 37 | `Patch` 字段上方缺少注释行 |
| 228 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `brp-compress-no-img.patch` | 38 | `Patch` 字段上方缺少注释行 |
| 229 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `emptymanifest.diff` | 39 | `Patch` 字段上方缺少注释行 |
| 230 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `find-lang-qt-qm.patch` | 40 | `Patch` 字段上方缺少注释行 |
| 231 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `canongnu.diff` | 41 | `Patch` 字段上方缺少注释行 |
| 232 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `unshare.diff` | 42 | `Patch` 字段上方缺少注释行 |
| 233 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `buildroot-symlink.diff` | 43 | `Patch` 字段上方缺少注释行 |
| 234 | [rust-async-std-1/rust-async-std-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-async-std-1/rust-async-std-1.spec) | `0001-fix-range-dependencies.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 235 | [rust-dlib-0.5/rust-dlib-0.5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-dlib-0.5/rust-dlib-0.5.spec) | `0001-fix-range-dependencies.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 236 | [rust-generator-0.8/rust-generator-0.8.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-generator-0.8/rust-generator-0.8.spec) | `0001-fix-range-dependencies.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 237 | [rust-hyper-util-0.1/rust-hyper-util-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-hyper-util-0.1/rust-hyper-util-0.1.spec) | `0001-fix-range-dependencies.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 238 | [rust-malloc-buf-0.0.6/rust-malloc-buf-0.0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-malloc-buf-0.0.6/rust-malloc-buf-0.0.6.spec) | `0001-fix-range-dependencies.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 239 | [rust-nom-locate-5/rust-nom-locate-5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-nom-locate-5/rust-nom-locate-5.spec) | `0001-fix-range-dependencies.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 240 | [rust-objc-0.2/rust-objc-0.2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-objc-0.2/rust-objc-0.2.spec) | `0001-fix-range-dependencies.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 241 | [rust-pyo3-introspection-0.28/rust-pyo3-introspection-0.28.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-pyo3-introspection-0.28/rust-pyo3-introspection-0.28.spec) | `0001-fix-dependency-ranges.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 242 | [rust-python-pkginfo-0.6/rust-python-pkginfo-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-python-pkginfo-0.6/rust-python-pkginfo-0.6.spec) | `0001-fix-dependency-ranges.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 243 | [rust-reflink-copy-0.1/rust-reflink-copy-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-reflink-copy-0.1/rust-reflink-copy-0.1.spec) | `0001-fix-dependency-ranges.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 244 | [rust-shellexpand-3/rust-shellexpand-3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-shellexpand-3/rust-shellexpand-3.spec) | `0001-fix-range-dependencies.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 245 | [rust-signal-hook-registry-1/rust-signal-hook-registry-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-signal-hook-registry-1/rust-signal-hook-registry-1.spec) | `0001-fix-version.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 246 | [rust-system-deps-7/rust-system-deps-7.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-system-deps-7/rust-system-deps-7.spec) | `0001-fix-range-dependencies.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 247 | [rust-tracy-client-0.18/rust-tracy-client-0.18.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-tracy-client-0.18/rust-tracy-client-0.18.spec) | `0001-fix-range-dependencies.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 248 | [rust-v-frame-0.3/rust-v-frame-0.3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-v-frame-0.3/rust-v-frame-0.3.spec) | `0001-fix-cargo-requirements.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 249 | [rust-wasite-1/rust-wasite-1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-wasite-1/rust-wasite-1.spec) | `0001-fix-range-dependencies.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 250 | [scap-security-guide/scap-security-guide.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/scap-security-guide/scap-security-guide.spec) | `2000-add-support-for-openRuyi.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 251 | [sddm/sddm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sddm/sddm.spec) | `0001-CMake-Raise-required-version-to-3.5.patch` | 23 | `Patch` 字段上方缺少注释行 |
| 252 | [shadow/shadow.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/shadow/shadow.spec) | `2000-openruyi-disable-conflicting-tools.patch` | 26 | `Patch` 字段上方缺少注释行 |
| 253 | [shadow/shadow.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/shadow/shadow.spec) | `2001-openruyi-adapt-configs.patch` | 27 | `Patch` 字段上方缺少注释行 |
| 254 | [sharutils/sharutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sharutils/sharutils.spec) | `0001-backport-Fix-building-with-GCC-10.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 255 | [soxr/soxr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/soxr/soxr.spec) | `0001-soxr-cmake.patch` | 15 | `Patch` 字段上方缺少注释行 |
| 256 | [srt/srt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/srt/srt.spec) | `0001-build-Update-for-compatibility-with-CMake-4.x-3167.p...` | 19 | `Patch` 字段上方缺少注释行 |
| 257 | [startup-notification/startup-notification.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/startup-notification/startup-notification.spec) | `0001-fix-test-xmessage-atom-types.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 258 | [symlinks/symlinks.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/symlinks/symlinks.spec) | `0001-fix-makefile.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 259 | [tcsh/tcsh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tcsh/tcsh.spec) | `0001-fix-nice-case-fail-if-noroot.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 260 | [texlive/texlive.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/texlive/texlive.spec) | `2000-add-luajit-support-for-riscv64.patch` | 30 | `Patch` 字段上方缺少注释行 |
| 261 | [xdg-utils/xdg-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xdg-utils/xdg-utils.spec) | `0001-disable-docs.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 262 | [xevd/xevd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xevd/xevd.spec) | `0001-xevd-fix-build-on-non-x86.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 263 | [xevd/xevd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xevd/xevd.spec) | `0002-xevd-fix-neon-header.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 264 | [xevd/xevd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xevd/xevd.spec) | `0003-xevd-link-libm.patch` | 20 | `Patch` 字段上方缺少注释行 |
| 265 | [xeve/xeve.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xeve/xeve.spec) | `0001-xeve-fix-build-on-non-x86.patch` | 17 | `Patch` 字段上方缺少注释行 |
| 266 | [xeve/xeve.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xeve/xeve.spec) | `0002-xeve-link-libm.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 267 | [xinetd/xinetd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xinetd/xinetd.spec) | `0001-xinetd-service-sysconfig.patch` | 19 | `Patch` 字段上方缺少注释行 |
| 268 | [xtrans/xtrans.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xtrans/xtrans.spec) | `xtrans-1.0.3-avoid-gethostname.patch` | 21 | `Patch` 字段上方缺少注释行 |
| 269 | [yaml-cpp/yaml-cpp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/yaml-cpp/yaml-cpp.spec) | `0001-fix-include.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 270 | [zimg/zimg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zimg/zimg.spec) | `0001-fix-build.patch` | 18 | `Patch` 字段上方缺少注释行 |
| 271 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `0004-man.patch` | 28 | `Patch` 字段上方缺少注释行 |
| 272 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `0005-zip-3.0-format-security.patch` | 29 | `Patch` 字段上方缺少注释行 |
| 273 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `0006-zipnote.patch` | 30 | `Patch` 字段上方缺少注释行 |
| 274 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `0007-zip-gnu89-build.patch` | 31 | `Patch` 字段上方缺少注释行 |
| 275 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `0008-buffer_overflow.patch` | 32 | `Patch` 字段上方缺少注释行 |
| 276 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `0009-zip-3.0-man-strip-extra.patch` | 33 | `Patch` 字段上方缺少注释行 |
| 277 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `0001-cups-system-auth.patch` | 63 | `%patchlist` 条目上方缺少注释行 |
| 278 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `0002-cups-multilib.patch` | 64 | `%patchlist` 条目上方缺少注释行 |
| 279 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `0003-cups-banners.patch` | 65 | `%patchlist` 条目上方缺少注释行 |
| 280 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `0004-cups-direct-usb.patch` | 66 | `%patchlist` 条目上方缺少注释行 |
| 281 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `0005-cups-driverd-timeout.patch` | 67 | `%patchlist` 条目上方缺少注释行 |
| 282 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `0006-cups-usb-paperout.patch` | 68 | `%patchlist` 条目上方缺少注释行 |
| 283 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `0007-cups-uri-compat.patch` | 69 | `%patchlist` 条目上方缺少注释行 |
| 284 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `0008-cups-freebind.patch` | 70 | `%patchlist` 条目上方缺少注释行 |
| 285 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `0009-cups-ipp-multifile.patch` | 71 | `%patchlist` 条目上方缺少注释行 |
| 286 | [cups/cups.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cups/cups.spec) | `0010-cups-web-devices-timeout.patch` | 72 | `%patchlist` 条目上方缺少注释行 |
| 287 | [docbook-dtds/docbook-dtds.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-dtds/docbook-dtds.spec) | `0002-docbook-dtd31-sgml-1.0.catalog.patch` | 129 | `%patchlist` 条目上方缺少注释行 |
| 288 | [docbook-dtds/docbook-dtds.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-dtds/docbook-dtds.spec) | `0003-docbook-dtd40-sgml-1.0.catalog.patch` | 130 | `%patchlist` 条目上方缺少注释行 |
| 289 | [docbook-dtds/docbook-dtds.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-dtds/docbook-dtds.spec) | `0004-docbook-dtd41-sgml-1.0.catalog.patch` | 131 | `%patchlist` 条目上方缺少注释行 |
| 290 | [docbook-dtds/docbook-dtds.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-dtds/docbook-dtds.spec) | `0005-docbook-dtd42-sgml-1.0.catalog.patch` | 132 | `%patchlist` 条目上方缺少注释行 |
| 291 | [dpdk/dpdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dpdk/dpdk.spec) | `0002-lpm-lookup-with-RISC-V-vector-extension.patch` | 46 | `%patchlist` 条目上方缺少注释行 |
| 292 | [dpdk/dpdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dpdk/dpdk.spec) | `0003-fib-lookup-with-RISC-V-vector-extension.patch` | 47 | `%patchlist` 条目上方缺少注释行 |
| 293 | [dpdk/dpdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dpdk/dpdk.spec) | `0004-config-riscv-consider-specified-CPU.patch` | 48 | `%patchlist` 条目上方缺少注释行 |
| 294 | [dpdk/dpdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dpdk/dpdk.spec) | `0005-test-raise-fast-test-timeout-to-60s-on-RISC-V.patch` | 49 | `%patchlist` 条目上方缺少注释行 |
| 295 | [dpdk/dpdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dpdk/dpdk.spec) | `0006-config-riscv-add-rv64gcv-cross-compilation-target.patch` | 50 | `%patchlist` 条目上方缺少注释行 |
| 296 | [firefox/firefox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/firefox/firefox.spec) | `0001-add-GetSystemProxyDirect-to-libproxy-path.patch` | 302 | `%patchlist` 条目上方缺少注释行 |
| 297 | [firefox/firefox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/firefox/firefox.spec) | `2000-riscv64-Use-long-tail-jump-for-xptcall-stubs.patch` | 303 | `%patchlist` 条目上方缺少注释行 |
| 298 | [firefox/firefox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/firefox/firefox.spec) | `2003-blindly-set-rust-rva23-target-when-needed.patch` | 308 | `%patchlist` 条目上方缺少注释行 |
| 299 | [firefox/firefox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/firefox/firefox.spec) | `2005-add-riscv64-support-for-crash-context.patch` | 311 | `%patchlist` 条目上方缺少注释行 |
| 300 | [firefox/firefox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/firefox/firefox.spec) | `2006-enable-crashreporter-for-riscv64.patch` | 312 | `%patchlist` 条目上方缺少注释行 |
| 301 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `freetype-2.3.0-enable-spr.patch` | 54 | `%patchlist` 条目上方缺少注释行 |
| 302 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `freetype-2.2.1-enable-valid.patch` | 55 | `%patchlist` 条目上方缺少注释行 |
| 303 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `freetype-2.6.5-libtool.patch` | 56 | `%patchlist` 条目上方缺少注释行 |
| 304 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `freetype-2.8-multilib.patch` | 57 | `%patchlist` 条目上方缺少注释行 |
| 305 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `freetype-2.10.0-internal-outline.patch` | 58 | `%patchlist` 条目上方缺少注释行 |
| 306 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `freetype-2.10.1-debughook.patch` | 59 | `%patchlist` 条目上方缺少注释行 |
| 307 | [i2c-tools/i2c-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/i2c-tools/i2c-tools.spec) | `0001-i2ctransfer-Don-t-link-with-libi2c.patch` | 40 | `%patchlist` 条目上方缺少注释行 |
| 308 | [i2c-tools/i2c-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/i2c-tools/i2c-tools.spec) | `0002-i2ctransfer-Don-t-free-memory-which-was-never-alloca...` | 41 | `%patchlist` 条目上方缺少注释行 |
| 309 | [i2c-tools/i2c-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/i2c-tools/i2c-tools.spec) | `0003-i2ctransfer-Prevent-msgs-overflow-with-many-paramete...` | 42 | `%patchlist` 条目上方缺少注释行 |
| 310 | [i2c-tools/i2c-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/i2c-tools/i2c-tools.spec) | `0004-i2ctransfer-Zero-out-memory-passed-to-ioctl.patch` | 43 | `%patchlist` 条目上方缺少注释行 |
| 311 | [isa-l_crypto/isa-l_crypto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/isa-l_crypto/isa-l_crypto.spec) | `0005-aes-riscv64-add-RISC-V-Zvk-AES-implementation-for-AE...` | 46 | `%patchlist` 条目上方缺少注释行 |
| 312 | [miopen/miopen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/miopen/miopen.spec) | `2001-disable-clang-tidy.patch` | 79 | `%patchlist` 条目上方缺少注释行 |
| 313 | [miopen/miopen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/miopen/miopen.spec) | `2002-workaround-half-float-expr-deduction.patch` | 80 | `%patchlist` 条目上方缺少注释行 |
| 314 | [miopen/miopen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/miopen/miopen.spec) | `2003-disable-fno-offload-uniform-block.patch` | 81 | `%patchlist` 条目上方缺少注释行 |
| 315 | [miopen/miopen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/miopen/miopen.spec) | `2004-fix-clang-rel-path.patch` | 82 | `%patchlist` 条目上方缺少注释行 |
| 316 | [python-pytest-xdist/python-pytest-xdist.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-xdist/python-pytest-xdist.spec) | `0001-python-pytest-xdist-3.8.0-fix-for-pytest-9.0+.patch` | 48 | `%patchlist` 条目上方缺少注释行 |
| 317 | [python-pytest-xdist/python-pytest-xdist.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-xdist/python-pytest-xdist.spec) | `0002-python-pytest-xdist-3.8.0-update-biapp.patch` | 49 | `%patchlist` 条目上方缺少注释行 |
| 318 | [python-tensile/python-tensile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tensile/python-tensile.spec) | `0001-fix-python-shebang.patch` | 38 | `%patchlist` 条目上方缺少注释行 |
| 319 | [python-tensile/python-tensile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tensile/python-tensile.spec) | `0002-fix-tensile-get-path.patch` | 39 | `%patchlist` 条目上方缺少注释行 |
| 320 | [python-tensile/python-tensile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tensile/python-tensile.spec) | `0004-ignore-asm-cap-cache.patch` | 42 | `%patchlist` 条目上方缺少注释行 |
| 321 | [rocclr/rocclr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocclr/rocclr.spec) | `2002-add-lp64d-target-to-llvm-mc.patch` | 75 | `%patchlist` 条目上方缺少注释行 |
| 322 | [rrdtool/rrdtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | `Fix-compatibility-with-Tcl-9.0.patch` | 48 | `%patchlist` 条目上方缺少注释行 |
| 323 | [rrdtool/rrdtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | `correctly-link-ruby-bindings.patch` | 49 | `%patchlist` 条目上方缺少注释行 |
| 324 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `0015-unzip-6.0-alt-iconv-utf8-print.patch` | 54 | `%patchlist` 条目上方缺少注释行 |
| 325 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `0016-Fix-CVE-2016-9844-rhbz-1404283.patch` | 55 | `%patchlist` 条目上方缺少注释行 |
| 326 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `0022-unzip-zipbomb-part2.patch` | 66 | `%patchlist` 条目上方缺少注释行 |
| 327 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `0023-unzip-zipbomb-part3.patch` | 67 | `%patchlist` 条目上方缺少注释行 |
| 328 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `0024-unzip-zipbomb-manpage.patch` | 68 | `%patchlist` 条目上方缺少注释行 |
| 329 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `0025-unzip-zipbomb-part4.patch` | 69 | `%patchlist` 条目上方缺少注释行 |
| 330 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `0026-unzip-zipbomb-part5.patch` | 70 | `%patchlist` 条目上方缺少注释行 |
| 331 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `0027-unzip-zipbomb-part6.patch` | 71 | `%patchlist` 条目上方缺少注释行 |
| 332 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `0028-unzip-zipbomb-part7.patch` | 72 | `%patchlist` 条目上方缺少注释行 |
| 333 | [unzip/unzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unzip/unzip.spec) | `0029-unzip-zipbomb-switch.patch` | 73 | `%patchlist` 条目上方缺少注释行 |
| 334 | [autoconf/autoconf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/autoconf/autoconf.spec) | `autoreconf-ltdl.diff` | 22 | 补丁文件名未以四位数字开头 |
| 335 | [autofs/autofs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/autofs/autofs.spec) | `autofs-5.1.9-Fix-incompatible-function-pointer-types-in-c...` | 20 | 补丁文件名未以四位数字开头 |
| 336 | [bdfresize/bdfresize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bdfresize/bdfresize.spec) | `010_ftbfs-gcc4.patch` | 20 | 补丁文件名未以四位数字开头 |
| 337 | [bdfresize/bdfresize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bdfresize/bdfresize.spec) | `020_minus-sign.patch` | 21 | 补丁文件名未以四位数字开头 |
| 338 | [bison/bison.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bison/bison.spec) | `glr2-cc-ensure-yylookaheadNeeds-is-same-size-as-yystates....` | 19 | 补丁文件名未以四位数字开头 |
| 339 | [blake3/blake3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/blake3/blake3.spec) | `riscv-v.patch` | 22 | 补丁文件名未以四位数字开头 |
| 340 | [busybox/busybox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/busybox/busybox.spec) | `busybox-1.36.1-no-cbq.patch` | 23 | 补丁文件名未以四位数字开头 |
| 341 | [busybox/busybox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/busybox/busybox.spec) | `busybox-1.37.0-fix-conditional-for-sha1_process_block64_s...` | 25 | 补丁文件名未以四位数字开头 |
| 342 | [compsize/compsize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/compsize/compsize.spec) | `compsize-1.5-fix-build-btrfsprogs-0.6.1.patch` | 16 | 补丁文件名未以四位数字开头 |
| 343 | [crash/crash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crash/crash.spec) | `lzo_snappy_zstd.patch` | 26 | 补丁文件名未以四位数字开头 |
| 344 | [crash/crash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crash/crash.spec) | `crash-9.0.1_build.patch` | 27 | 补丁文件名未以四位数字开头 |
| 345 | [dblatex/dblatex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dblatex/dblatex.spec) | `dblatex-0.3.12-replace-imp-by-importlib.patch` | 20 | 补丁文件名未以四位数字开头 |
| 346 | [dblatex/dblatex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dblatex/dblatex.spec) | `dblatex-0.3.12-adjust-submodule-imports.patch` | 22 | 补丁文件名未以四位数字开头 |
| 347 | [dblatex/dblatex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dblatex/dblatex.spec) | `dblatex-0.3.4-disable-debian.patch` | 24 | 补丁文件名未以四位数字开头 |
| 348 | [dbus-broker/dbus-broker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dbus-broker/dbus-broker.spec) | `test-sockopt-loosen-verification-of-stale-pidfds.patch` | 21 | 补丁文件名未以四位数字开头 |
| 349 | [dejagnu/dejagnu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dejagnu/dejagnu.spec) | `testsuite-legacy.patch` | 25 | 补丁文件名未以四位数字开头 |
| 350 | [dotnet10.0/dotnet10.0.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dotnet10.0/dotnet10.0.spec) | `runtime-disable-fortify-on-ilasm-parser.patch` | 91 | 补丁文件名未以四位数字开头 |
| 351 | [doxygen/doxygen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/doxygen/doxygen.spec) | `doxygen-no-lowercase-man-names.patch` | 19 | 补丁文件名未以四位数字开头 |
| 352 | [doxygen/doxygen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/doxygen/doxygen.spec) | `reproducible.patch` | 20 | 补丁文件名未以四位数字开头 |
| 353 | [dwz/dwz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dwz/dwz.spec) | `remove-gold-tests.patch` | 19 | 补丁文件名未以四位数字开头 |
| 354 | [efivar/efivar.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/efivar/efivar.spec) | `fix-build-failure-with-glibc-2.43.patch` | 23 | 补丁文件名未以四位数字开头 |
| 355 | [eigen3/eigen3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/eigen3/eigen3.spec) | `eigen3_libinstalldir.patch` | 18 | 补丁文件名未以四位数字开头 |
| 356 | [fakeroot/fakeroot.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fakeroot/fakeroot.spec) | `debian_fix-shell-in-fakeroot.patch` | 19 | 补丁文件名未以四位数字开头 |
| 357 | [findutils/findutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/findutils/findutils.spec) | `findutils-xautofs.patch` | 24 | 补丁文件名未以四位数字开头 |
| 358 | [findutils/findutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/findutils/findutils.spec) | `findutils-avoid-crash-system-loop.patch` | 26 | 补丁文件名未以四位数字开头 |
| 359 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `freetype-2.3.0-enable-spr.patch` | 54 | 补丁文件名未以四位数字开头 |
| 360 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `freetype-2.2.1-enable-valid.patch` | 55 | 补丁文件名未以四位数字开头 |
| 361 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `freetype-2.6.5-libtool.patch` | 56 | 补丁文件名未以四位数字开头 |
| 362 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `freetype-2.8-multilib.patch` | 57 | 补丁文件名未以四位数字开头 |
| 363 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `freetype-2.10.0-internal-outline.patch` | 58 | 补丁文件名未以四位数字开头 |
| 364 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | `freetype-2.10.1-debughook.patch` | 59 | 补丁文件名未以四位数字开头 |
| 365 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `gcc-add-defaultsspec.diff` | 152 | 补丁文件名未以四位数字开头 |
| 366 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `gcc44-textdomain.patch` | 153 | 补丁文件名未以四位数字开头 |
| 367 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `gcc44-rename-info-files.patch` | 154 | 补丁文件名未以四位数字开头 |
| 368 | [gdbm/gdbm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gdbm/gdbm.spec) | `gdbm-no-build-date.patch` | 21 | 补丁文件名未以四位数字开头 |
| 369 | [glib/glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glib/glib.spec) | `meson.build-Avoid-linking-with-libatomic-when-unneed.patch` | 37 | 补丁文件名未以四位数字开头 |
| 370 | [glibc/glibc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glibc/glibc.spec) | `glibc-2.4-china.diff` | 39 | 补丁文件名未以四位数字开头 |
| 371 | [glmark2/glmark2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glmark2/glmark2.spec) | `glmark2-2023.01-backport-visual-config-match.patch` | 18 | 补丁文件名未以四位数字开头 |
| 372 | [grub/grub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grub/grub.spec) | `skip-efi_uga.patch` | 29 | 补丁文件名未以四位数字开头 |
| 373 | [grub/grub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grub/grub.spec) | `blsuki-append-version.patch` | 32 | 补丁文件名未以四位数字开头 |
| 374 | [grub/grub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grub/grub.spec) | `grub-c23-string-func-handling-updates.patch` | 35 | 补丁文件名未以四位数字开头 |
| 375 | [grub/grub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grub/grub.spec) | `conditionally-apply-regparm-attr.patch` | 38 | 补丁文件名未以四位数字开头 |
| 376 | [gtk-doc/gtk-doc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gtk-doc/gtk-doc.spec) | `gtk-doc-mkhtml-test-fix.patch` | 19 | 补丁文件名未以四位数字开头 |
| 377 | [guile/guile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/guile/guile.spec) | `guile-fix-riscv64-jit.patch` | 23 | 补丁文件名未以四位数字开头 |
| 378 | [gzip/gzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gzip/gzip.spec) | `manpage-no-date.patch` | 21 | 补丁文件名未以四位数字开头 |
| 379 | [keybinder/keybinder.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/keybinder/keybinder.spec) | `fix-empty-gobject.patch` | 17 | 补丁文件名未以四位数字开头 |
| 380 | [krb5/krb5.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/krb5/krb5.spec) | `Fix-strchr-conformance-to-C23.patch` | 27 | 补丁文件名未以四位数字开头 |
| 381 | [libaio/libaio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libaio/libaio.spec) | `libaio-fix-test-off64_t.patch` | 20 | 补丁文件名未以四位数字开头 |
| 382 | [libdwarf/libdwarf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdwarf/libdwarf.spec) | `libdwarf-both.patch` | 17 | 补丁文件名未以四位数字开头 |
| 383 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | `readv-proto.patch` | 23 | 补丁文件名未以四位数字开头 |
| 384 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | `skip_cycles.patch` | 24 | 补丁文件名未以四位数字开头 |
| 385 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | `python3.8-compat.patch` | 26 | 补丁文件名未以四位数字开头 |
| 386 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | `swig4_moduleimport.patch` | 27 | 补丁文件名未以四位数字开头 |
| 387 | [libsemanage/libsemanage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsemanage/libsemanage.spec) | `fix-test-failure-with-secilc.patch` | 24 | 补丁文件名未以四位数字开头 |
| 388 | [libtiff/libtiff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtiff/libtiff.spec) | `libtiff-4.0.3-seek.patch` | 20 | 补丁文件名未以四位数字开头 |
| 389 | [libtiff/libtiff.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtiff/libtiff.spec) | `libtiff-4.7.0-test_directory.patch` | 21 | 补丁文件名未以四位数字开头 |
| 390 | [libxcrypt/libxcrypt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxcrypt/libxcrypt.spec) | `fix-werror-discarded-qualifiers.patch` | 19 | 补丁文件名未以四位数字开头 |
| 391 | [libxkbcommon/libxkbcommon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxkbcommon/libxkbcommon.spec) | `libxkbcommon-1.13.1-mask-x11-test.patch` | 22 | 补丁文件名未以四位数字开头 |
| 392 | [lz4/lz4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lz4/lz4.spec) | `lz4-export.diff` | 19 | 补丁文件名未以四位数字开头 |
| 393 | [lz4/lz4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lz4/lz4.spec) | `Enable-LZ4_FAST_DEC_LOOP-for-RISC-V.patch` | 21 | 补丁文件名未以四位数字开头 |
| 394 | [mariadb/mariadb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mariadb/mariadb.spec) | `fix-pamdir.patch` | 42 | 补丁文件名未以四位数字开头 |
| 395 | [mdevd/mdevd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mdevd/mdevd.spec) | `some-libcs-have-a-char-const-strchr-need-to-investigate.p...` | 19 | 补丁文件名未以四位数字开头 |
| 396 | [mesa/mesa.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mesa/mesa.spec) | `mesa-26.1.1-zink-kmsro-for-img-blob.patch` | 28 | 补丁文件名未以四位数字开头 |
| 397 | [mesa/mesa.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mesa/mesa.spec) | `mesa-26.1.1-pvr-conformance.patch` | 30 | 补丁文件名未以四位数字开头 |
| 398 | [mesa-demos/mesa-demos.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mesa-demos/mesa-demos.spec) | `mesa-demos-8.5.0-legal.patch` | 20 | 补丁文件名未以四位数字开头 |
| 399 | [mesa-demos/mesa-demos.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mesa-demos/mesa-demos.spec) | `mesa-demos-system-data.patch` | 22 | 补丁文件名未以四位数字开头 |
| 400 | [multipath-tools/multipath-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/multipath-tools/multipath-tools.spec) | `multipath-tools-fix-c23-errors-with-strchr.patch` | 22 | 补丁文件名未以四位数字开头 |
| 401 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | `nmap-4.03-mktemp.patch` | 71 | 补丁文件名未以四位数字开头 |
| 402 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | `nmap-4.52-noms.patch` | 73 | 补丁文件名未以四位数字开头 |
| 403 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | `ncat_reg_stdin.diff` | 75 | 补丁文件名未以四位数字开头 |
| 404 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | `nmap_resolve_config.patch` | 77 | 补丁文件名未以四位数字开头 |
| 405 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | `nmap-pcre2.patch` | 79 | 补丁文件名未以四位数字开头 |
| 406 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | `nmap-ems-ssl-enum-ciphers.patch` | 81 | 补丁文件名未以四位数字开头 |
| 407 | [nmap/nmap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nmap/nmap.spec) | `nmap-libpcap.patch` | 83 | 补丁文件名未以四位数字开头 |
| 408 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `hwy-broken-rvv.diff` | 42 | 补丁文件名未以四位数字开头 |
| 409 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `v8-riscv-fix-trampoline.patch` | 43 | 补丁文件名未以四位数字开头 |
| 410 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `v8-riscv-fix-trampoline-release.patch` | 44 | 补丁文件名未以四位数字开头 |
| 411 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `v8-riscv-fix-sp.patch` | 46 | 补丁文件名未以四位数字开头 |
| 412 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | `mkinstalldirs.patch` | 21 | 补丁文件名未以四位数字开头 |
| 413 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | `args.patch` | 22 | 补丁文件名未以四位数字开头 |
| 414 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | `freetype2.patch` | 23 | 补丁文件名未以四位数字开头 |
| 415 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | `Makefile-Add-DESTDIR.patch` | 25 | 补丁文件名未以四位数字开头 |
| 416 | [patch/patch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/patch/patch.spec) | `CVE-2019-20633.patch` | 22 | 补丁文件名未以四位数字开头 |
| 417 | [policycoreutils/policycoreutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/policycoreutils/policycoreutils.spec) | `fix-discarded-qualifiers-warning-with-glib-2.43.patch` | 43 | 补丁文件名未以四位数字开头 |
| 418 | [postgresql/postgresql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postgresql/postgresql.spec) | `rpm-pgsql.patch` | 35 | 补丁文件名未以四位数字开头 |
| 419 | [postgresql/postgresql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postgresql/postgresql.spec) | `postgresql-var-run-socket.patch` | 36 | 补丁文件名未以四位数字开头 |
| 420 | [postgresql/postgresql.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/postgresql/postgresql.spec) | `postgresql-no-libecpg.patch` | 37 | 补丁文件名未以四位数字开头 |
| 421 | [powertop/powertop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/powertop/powertop.spec) | `powertop-2.7-always-create-params.patch` | 18 | 补丁文件名未以四位数字开头 |
| 422 | [quota/quota.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/quota/quota.spec) | `quota-4.06-warnquota-configuration-tunes.patch` | 23 | 补丁文件名未以四位数字开头 |
| 423 | [quota/quota.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/quota/quota.spec) | `quota-4.03-Validate-upper-bound-of-RPC-port.patch` | 24 | 补丁文件名未以四位数字开头 |
| 424 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `brpcompress.diff` | 33 | 补丁文件名未以四位数字开头 |
| 425 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `checkfilesnoinfodir.diff` | 34 | 补丁文件名未以四位数字开头 |
| 426 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `rpmpopt.diff` | 35 | 补丁文件名未以四位数字开头 |
| 427 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `safeugid.diff` | 36 | 补丁文件名未以四位数字开头 |
| 428 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `fileattrs.diff` | 37 | 补丁文件名未以四位数字开头 |
| 429 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `brp-compress-no-img.patch` | 38 | 补丁文件名未以四位数字开头 |
| 430 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `emptymanifest.diff` | 39 | 补丁文件名未以四位数字开头 |
| 431 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `find-lang-qt-qm.patch` | 40 | 补丁文件名未以四位数字开头 |
| 432 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `canongnu.diff` | 41 | 补丁文件名未以四位数字开头 |
| 433 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `unshare.diff` | 42 | 补丁文件名未以四位数字开头 |
| 434 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `buildroot-symlink.diff` | 43 | 补丁文件名未以四位数字开头 |
| 435 | [rrdtool/rrdtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | `rrdtool-1.6.0-ruby-2-fix.patch` | 45 | 补丁文件名未以四位数字开头 |
| 436 | [rrdtool/rrdtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | `rrdtool-zero_vs_nothing.patch` | 47 | 补丁文件名未以四位数字开头 |
| 437 | [rrdtool/rrdtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | `Fix-compatibility-with-Tcl-9.0.patch` | 48 | 补丁文件名未以四位数字开头 |
| 438 | [rrdtool/rrdtool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | `correctly-link-ruby-bindings.patch` | 49 | 补丁文件名未以四位数字开头 |
| 439 | [utf8cpp/utf8cpp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/utf8cpp/utf8cpp.spec) | `utf8cpp-cmake.patch` | 19 | 补丁文件名未以四位数字开头 |
| 440 | [util-linux/util-linux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/util-linux/util-linux.spec) | `login-lastlog-create.patch` | 29 | 补丁文件名未以四位数字开头 |
| 441 | [util-linux/util-linux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/util-linux/util-linux.spec) | `login-default-motd-file.patch` | 31 | 补丁文件名未以四位数字开头 |
| 442 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | `uuid-1.6.1-ossp.patch` | 34 | 补丁文件名未以四位数字开头 |
| 443 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | `uuid-1.6.1-mkdir.patch` | 36 | 补丁文件名未以四位数字开头 |
| 444 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | `uuid-1.6.2-php54.patch` | 38 | 补丁文件名未以四位数字开头 |
| 445 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | `uuid-1.6.2-hwaddr.patch` | 40 | 补丁文件名未以四位数字开头 |
| 446 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | `uuid-1.6.2-nostrip.patch` | 42 | 补丁文件名未以四位数字开头 |
| 447 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | `uuid-1.6.2-manfix.patch` | 44 | 补丁文件名未以四位数字开头 |
| 448 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | `uuid-1.6.2-ldflags.patch` | 46 | 补丁文件名未以四位数字开头 |
| 449 | [valkey/valkey.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/valkey/valkey.spec) | `valkey-conf.patch` | 41 | 补丁文件名未以四位数字开头 |
| 450 | [valkey/valkey.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/valkey/valkey.spec) | `valkey-loadmod.patch` | 43 | 补丁文件名未以四位数字开头 |
| 451 | [xtrans/xtrans.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xtrans/xtrans.spec) | `xtrans-1.0.3-avoid-gethostname.patch` | 21 | 补丁文件名未以四位数字开头 |
| 452 | [xxhash/xxhash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xxhash/xxhash.spec) | `xxhash-fix-non-x86-dispatch.patch` | 23 | 补丁文件名未以四位数字开头 |
| 453 | [xxhash/xxhash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xxhash/xxhash.spec) | `xxhash-test-respect-cflags.patch` | 25 | 补丁文件名未以四位数字开头 |
| 454 | [zlib-ng/zlib-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zlib-ng/zlib-ng.spec) | `zlib-ng-2.3.2-riscv-hwprobe.patch` | 25 | 补丁文件名未以四位数字开头 |
| 455 | [libunwind/libunwind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libunwind/libunwind.spec) | `3000-libunwind-no-dl-iterate-phdr.patch` | 20 | 补丁文件名前缀不在 0001-2999 范围内 |
| 456 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `60588.diff` | 48 | 补丁文件名前缀不在 0001-2999 范围内 |
| 457 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `60591.diff` | 49 | 补丁文件名前缀不在 0001-2999 范围内 |
| 458 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `6464-auto-config-update.diff` | 50 | 补丁文件名前缀不在 0001-2999 范围内 |
| 459 | [audiofile/audiofile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/audiofile/audiofile.spec) | `11` | 18 | 补丁数量 > 3 未使用 `%patchlist` |
| 460 | [binutils/binutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/binutils/binutils.spec) | `5` | 29 | 补丁数量 > 3 未使用 `%patchlist` |
| 461 | [cyrus-sasl/cyrus-sasl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cyrus-sasl/cyrus-sasl.spec) | `4` | 20 | 补丁数量 > 3 未使用 `%patchlist` |
| 462 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `7` | 22 | 补丁数量 > 3 未使用 `%patchlist` |
| 463 | [gcc15/gcc15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc15/gcc15.spec) | `40` | 152 | 补丁数量 > 3 未使用 `%patchlist` |
| 464 | [gpm/gpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `9` | 22 | 补丁数量 > 3 未使用 `%patchlist` |
| 465 | [grub/grub.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/grub/grub.spec) | `4` | 29 | 补丁数量 > 3 未使用 `%patchlist` |
| 466 | [icu4c/icu4c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/icu4c/icu4c.spec) | `5` | 22 | 补丁数量 > 3 未使用 `%patchlist` |
| 467 | [indent/indent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/indent/indent.spec) | `4` | 20 | 补丁数量 > 3 未使用 `%patchlist` |
| 468 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | `4` | 23 | 补丁数量 > 3 未使用 `%patchlist` |
| 469 | [lua/lua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua/lua.spec) | `4` | 27 | 补丁数量 > 3 未使用 `%patchlist` |
| 470 | [ncurses/ncurses.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ncurses/ncurses.spec) | `4` | 22 | 补丁数量 > 3 未使用 `%patchlist` |
| 471 | [nodejs/nodejs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nodejs/nodejs.spec) | `6` | 42 | 补丁数量 > 3 未使用 `%patchlist` |
| 472 | [openjade/openjade.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openjade/openjade.spec) | `6` | 19 | 补丁数量 > 3 未使用 `%patchlist` |
| 473 | [openldap/openldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openldap/openldap.spec) | `6` | 39 | 补丁数量 > 3 未使用 `%patchlist` |
| 474 | [orbit2/orbit2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/orbit2/orbit2.spec) | `6` | 18 | 补丁数量 > 3 未使用 `%patchlist` |
| 475 | [otf2bdf/otf2bdf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/otf2bdf/otf2bdf.spec) | `4` | 21 | 补丁数量 > 3 未使用 `%patchlist` |
| 476 | [pesign/pesign.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `5` | 23 | 补丁数量 > 3 未使用 `%patchlist` |
| 477 | [pinfo/pinfo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pinfo/pinfo.spec) | `8` | 19 | 补丁数量 > 3 未使用 `%patchlist` |
| 478 | [procmail/procmail.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/procmail/procmail.spec) | `6` | 20 | 补丁数量 > 3 未使用 `%patchlist` |
| 479 | [qt6-qtbase/qt6-qtbase.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtbase/qt6-qtbase.spec) | `7` | 31 | 补丁数量 > 3 未使用 `%patchlist` |
| 480 | [qt6-qtwebengine/qt6-qtwebengine.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qt6-qtwebengine/qt6-qtwebengine.spec) | `5` | 23 | 补丁数量 > 3 未使用 `%patchlist` |
| 481 | [readline/readline.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/readline/readline.spec) | `4` | 21 | 补丁数量 > 3 未使用 `%patchlist` |
| 482 | [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `15` | 31 | 补丁数量 > 3 未使用 `%patchlist` |
| 483 | [zip/zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zip/zip.spec) | `9` | 23 | 补丁数量 > 3 未使用 `%patchlist` |
| 484 | [cdparanoia/cdparanoia.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cdparanoia/cdparanoia.spec) |  | 45 | `%patchlist` 位于 `%description` 之下 |
| 485 | [openssl/openssl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openssl/openssl.spec) |  | 48 | `%patchlist` 位于 `%description` 之下 |
| 486 | [python-torch/python-torch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-torch/python-torch.spec) |  | 221 | `%patchlist` 位于 `%description` 之下 |
| 487 | [spdk/spdk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/spdk/spdk.spec) |  | 56 | `%patchlist` 位于 `%description` 之下 |
| 488 | [aom/aom.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aom/aom.spec) |  | 28 | `Patch` 字段放置顺序错误 |
| 489 | [aspell/aspell.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aspell/aspell.spec) |  | 22 | `Patch` 字段放置顺序错误 |
| 490 | [cgctl/cgctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cgctl/cgctl.spec) |  | 32 | `Patch` 字段放置顺序错误 |
| 491 | [compsize/compsize.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/compsize/compsize.spec) |  | 16 | `Patch` 字段放置顺序错误 |
| 492 | [crash/crash.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crash/crash.spec) |  | 26 | `Patch` 字段放置顺序错误 |
| 493 | [dbus-broker/dbus-broker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dbus-broker/dbus-broker.spec) |  | 21 | `Patch` 字段放置顺序错误 |
| 494 | [eigen3/eigen3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/eigen3/eigen3.spec) |  | 18 | `Patch` 字段放置顺序错误 |
| 495 | [giflib/giflib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/giflib/giflib.spec) |  | 17 | `Patch` 字段放置顺序错误 |
| 496 | [guile/guile.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/guile/guile.spec) |  | 23 | `Patch` 字段放置顺序错误 |
| 497 | [hipfft/hipfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipfft/hipfft.spec) |  | 25 | `Patch` 字段放置顺序错误 |
| 498 | [hipify/hipify.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipify/hipify.spec) |  | 28 | `Patch` 字段放置顺序错误 |
| 499 | [hipsparselt/hipsparselt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipsparselt/hipsparselt.spec) |  | 38 | `Patch` 字段放置顺序错误 |
| 500 | [keybinder/keybinder.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/keybinder/keybinder.spec) |  | 17 | `Patch` 字段放置顺序错误 |
| 501 | [libaio/libaio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libaio/libaio.spec) |  | 20 | `Patch` 字段放置顺序错误 |
| 502 | [libdwarf/libdwarf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdwarf/libdwarf.spec) |  | 17 | `Patch` 字段放置顺序错误 |
| 503 | [libjpeg-turbo/libjpeg-turbo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libjpeg-turbo/libjpeg-turbo.spec) |  | 17 | `Patch` 字段放置顺序错误 |
| 504 | [libunwind/libunwind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libunwind/libunwind.spec) |  | 18 | `Patch` 字段放置顺序错误 |
| 505 | [lua-json/lua-json.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua-json/lua-json.spec) |  | 17 | `Patch` 字段放置顺序错误 |
| 506 | [msgpack/msgpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/msgpack/msgpack.spec) |  | 21 | `Patch` 字段放置顺序错误 |
| 507 | [powertop/powertop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/powertop/powertop.spec) |  | 18 | `Patch` 字段放置顺序错误 |
| 508 | [python-python-dateutil/python-python-dateutil.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-dateutil/python-python-dateutil.spec) |  | 29 | `Patch` 字段放置顺序错误 |
| 509 | [qhull/qhull.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qhull/qhull.spec) |  | 24 | `Patch` 字段放置顺序错误 |
| 510 | [rocblas/rocblas.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocblas/rocblas.spec) |  | 60 | `Patch` 字段放置顺序错误 |
| 511 | [rocsolver/rocsolver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocsolver/rocsolver.spec) |  | 44 | `Patch` 字段放置顺序错误 |
| 512 | [soxr/soxr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/soxr/soxr.spec) |  | 15 | `Patch` 字段放置顺序错误 |
| 513 | [vdo/vdo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vdo/vdo.spec) |  | 34 | `Patch` 字段放置顺序错误 |

## 说明

- 注释要求：规则要求每个 `Patch:` 字段（及 `%patchlist` 条目）上方必须有一行以 `#` 开头的注释，说明补丁用途或给出上游链接。openRuyi 仓库中大量 spec 未遵循此约定。
- 命名要求：补丁文件名应以四位数字开头（`0001-0999` 上游补丁、`1000-1999` CVE 修复或跨版本 backport、`2000-2999` openRuyi 特有补丁），用于控制补丁应用顺序。仓库中部分 spec 使用了 `60588.diff`、`3000-xxx.patch` 等不符合约定的命名。
- `%patchlist`：当补丁数量超过 3 个时，建议使用 `%patchlist` 统一管理，避免逐个 `%patch` 应用。仓库中 `gcc15`（40 个补丁）、`audiofile`（11 个补丁）等 spec 未使用 `%patchlist`。
- 放置顺序：`Patch` 字段应位于 `BuildSystem` 与 `BuildOption`（或 `BuildRequires`）之间，与 `Source` 字段类似。
- 本规则仅扫描 spec 头部区域（`%description`/`%package` 等段落之前），`%patchlist` 位置检查除外（在整个文件中查找）。

> 规则说明：[docs/check-spec-patch.md](../docs/check-spec-patch.md)
