# check-spec-license 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库的 spec 文件
执行 `check-spec-license` 规则扫描，结果如下。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| --- | ---: | ---: |
| 5337 | 5316 | 21 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| 小写 SPDX 连接符 | 15 |
| 逗号分隔 | 1 |
| 老式 "+" 后缀 | 5 |
| 括号不配对 | 0 |

## 问题清单（21 条）

| # | spec 文件 | License 值 | 问题类型 |
| --- | --- | --- | --- |
| 1 | [cmake/cmake.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cmake/cmake.spec) | `BSD and MIT and zlib` | 小写 SPDX 连接符 |
| 2 | [crontabs/crontabs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/crontabs/crontabs.spec) | `LicenseRef-openRuyi-Public-Domain and GPL-2.0-or-later` | 小写 SPDX 连接符 |
| 3 | [gtest/gtest.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gtest/gtest.spec) | `BSD-3-Clause and Apache-2.0` | 小写 SPDX 连接符 |
| 4 | [libheif/libheif.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libheif/libheif.spec) | `LGPL-3.0-or-later and MIT` | 小写 SPDX 连接符 |
| 5 | [libraw/libraw.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libraw/libraw.spec) | `BSD-3-Clause and (CDDL-1.0 or LGPL-2.1-only)` | 小写 SPDX 连接符 |
| 6 | [libwebsockets/libwebsockets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libwebsockets/libwebsockets.spec) | `LGPL-2.1-or-later and LicenseRef-openRuyi-Public-Domain a...` | 小写 SPDX 连接符 |
| 7 | [lmbench/lmbench.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lmbench/lmbench.spec) | `GPL with additional restrictions` | 小写 SPDX 连接符 |
| 8 | [lsof/lsof.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lsof/lsof.spec) | `Sendmail and LGPL-2.1-or-later and Zlib` | 小写 SPDX 连接符 |
| 9 | [mksh/mksh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mksh/mksh.spec) | `MirOS and ISC and BSD-3-Clause` | 小写 SPDX 连接符 |
| 10 | [p7zip/p7zip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/p7zip/p7zip.spec) | `LGPL-2.1-or-later and (LGPL-2.1-or-later or CPL-1.0)` | 小写 SPDX 连接符 |
| 11 | [python-exceptiongroup/python-exceptiongroup.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-exceptiongroup/python-exceptiongroup.spec) | `MIT or PSF-2.0` | 小写 SPDX 连接符 |
| 12 | [runc/runc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/runc/runc.spec) | `Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT` | 小写 SPDX 连接符 |
| 13 | [sof-firmware/sof-firmware.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sof-firmware/sof-firmware.spec) | `Intel-SOF-Firmware-Release-Licence or NXP-SOF-Firmware-Re...` | 小写 SPDX 连接符 |
| 14 | [util-linux/util-linux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/util-linux/util-linux.spec) | `GPL-2.0-or-later and others` | 小写 SPDX 连接符 |
| 15 | [weston/weston.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/weston/weston.spec) | `MIT and CC-BY-SA-3.0` | 小写 SPDX 连接符 |
| 16 | [go-github-klauspost-pgzip/go-github-klauspost-pgzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-klauspost-pgzip/go-github-klauspost-pgzip.spec) | `MIT, BSD-3-Clause` | 逗号分隔 |
| 17 | [parted/parted.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/parted/parted.spec) | `GPLv3+` | 老式 "+" 后缀 |
| 18 | [rust-bitmaps-2/rust-bitmaps-2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bitmaps-2/rust-bitmaps-2.spec) | `MPL-2.0+` | 老式 "+" 后缀 |
| 19 | [rust-im-rc-15/rust-im-rc-15.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-im-rc-15/rust-im-rc-15.spec) | `MPL-2.0+` | 老式 "+" 后缀 |
| 20 | [rust-sized-chunks-0.6/rust-sized-chunks-0.6.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-sized-chunks-0.6/rust-sized-chunks-0.6.spec) | `MPL-2.0+` | 老式 "+" 后缀 |
| 21 | [wolfssl/wolfssl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wolfssl/wolfssl.spec) | `GPLv3+` | 老式 "+" 后缀 |

## 说明

- 小写 SPDX 连接符（`and`/`or`/`with`）：SPDX 表达式语法要求连接符大写，
  例如 `BSD and MIT and zlib` 应写作 `BSD AND MIT AND Zlib`。
- 逗号分隔：SPDX 表达式中逗号不是合法连接符，`MIT, BSD-3-Clause` 应写作
  `MIT AND BSD-3-Clause`。
- 老式 `+` 后缀：`GPLv3+`、`MPL-2.0+` 是 Fedora 老式写法，SPDX 无此语法；
  应改用 `-or-later` 后缀，如 `GPL-3.0-or-later`、`MPL-2.0-or-later`。
- 合法但未标记的写法不报告：`-or-later` 内嵌的 `or`、`WITH` 大写的例外声明、
  `LicenseRef-*` 扩展标识符、括号分组、宏展开值，均不判定为问题。

> 规则说明见 [docs/check-spec-license.md](../docs/check-spec-license.md)。
