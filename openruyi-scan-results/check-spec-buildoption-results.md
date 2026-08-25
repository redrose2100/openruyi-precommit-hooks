# check-spec-buildoption 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-buildoption` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| --- | ---: | ---: |
| 5267 | 5240 | 27 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| `BuildOption(<stage>):` 与参数之间未用两个空格分隔 | 18 |
| `BuildOption` 位置不在 `BuildSystem` 与 `BuildRequires` 之间 | 9 |
| `BuildOption` 阶段书写顺序不符合 `build` → `install` → `check` | 7 |

## 问题清单（34 条）

| # | spec 文件 | 字段值 | 问题类型 |
| --- | --- | --- | --- |
| 1 | [abseil-cpp/abseil-cpp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/abseil-cpp/abseil-cpp.spec) | — | 位置错误（`BuildOption` 位于 `BuildRequires` 之后） |
| 2 | [asmjit/asmjit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/asmjit/asmjit.spec) | `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON` | 双空格分隔（冒号后为单个空格） |
| 3 | [asmjit/asmjit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/asmjit/asmjit.spec) | `-DASMJIT_STATIC=0` | 双空格分隔（冒号后为单个空格） |
| 4 | [asmjit/asmjit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/asmjit/asmjit.spec) | `-DASMJIT_TEST=1` | 双空格分隔（冒号后为单个空格） |
| 5 | [check/check.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/check/check.spec) | `--disable-option-checking MAKEINFO=true` | 双空格分隔（冒号后为单个空格） |
| 6 | [findutils/findutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/findutils/findutils.spec) | `--libexecdir=%{_libdir}/find` | 双空格分隔（冒号后为单个空格） |
| 7 | [findutils/findutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/findutils/findutils.spec) | `--localstatedir=%{_localstatedir}/lib` | 双空格分隔（冒号后为单个空格） |
| 8 | [freetype/freetype.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/freetype/freetype.spec) | — | 位置错误（`BuildOption` 位于 `BuildRequires` 之后） |
| 9 | [isomd5sum/isomd5sum.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/isomd5sum/isomd5sum.spec) | `install, build` | 顺序错误（`install` 在 `build` 之前） |
| 10 | [libbsd/libbsd.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libbsd/libbsd.spec) | — | 位置错误（`BuildOption` 位于 `BuildRequires` 之后） |
| 11 | [libgpg-error/libgpg-error.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libgpg-error/libgpg-error.spec) | `--enable-install-gpg-error-config` | 双空格分隔（冒号后为单个空格） |
| 12 | [libselinux/libselinux.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libselinux/libselinux.spec) | — | 位置错误（`BuildOption` 位于 `BuildRequires` 之后） |
| 13 | [libsquish/libsquish.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libsquish/libsquish.spec) | — | 位置错误（`BuildOption` 位于 `BuildRequires` 之后） |
| 14 | [lm_sensors/lm_sensors.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lm_sensors/lm_sensors.spec) | — | 位置错误（`BuildOption` 位于 `BuildRequires` 之后） |
| 15 | [lshw/lshw.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lshw/lshw.spec) | — | 位置错误（`BuildOption` 位于 `BuildRequires` 之后） |
| 16 | [lzo/lzo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lzo/lzo.spec) | `--enable-shared` | 双空格分隔（冒号后为单个空格） |
| 17 | [mkosi/mkosi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mkosi/mkosi.spec) | — | 位置错误（`BuildOption` 位于 `BuildRequires` 之后） |
| 18 | [mtd-utils/mtd-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mtd-utils/mtd-utils.spec) | `--without-tests` | 双空格分隔（冒号后为单个空格） |
| 19 | [mtd-utils/mtd-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mtd-utils/mtd-utils.spec) | `--disable-unit-tests` | 双空格分隔（冒号后为单个空格） |
| 20 | [python-dill/python-dill.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-dill/python-dill.spec) | `check, install` | 顺序错误（`check` 在 `install` 之前） |
| 21 | [python-fonttools/python-fonttools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fonttools/python-fonttools.spec) | `check, install` | 顺序错误（`check` 在 `install` 之前） |
| 22 | [python-ipython/python-ipython.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ipython/python-ipython.spec) | `check, install` | 顺序错误（`check` 在 `install` 之前） |
| 23 | [python-srsly/python-srsly.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-srsly/python-srsly.spec) | `check, install` | 顺序错误（`check` 在 `install` 之前） |
| 24 | [python-tox/python-tox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tox/python-tox.spec) | `check, install` | 顺序错误（`check` 在 `install` 之前） |
| 25 | [python-tox-current-env/python-tox-current-env.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tox-current-env/python-tox-current-env.spec) | `check, install` | 顺序错误（`check` 在 `install` 之前） |
| 26 | [pyxdg/pyxdg.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pyxdg/pyxdg.spec) | `-l xdg` | 双空格分隔（冒号后为单个空格） |
| 27 | [scons/scons.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/scons/scons.spec) | `-l SCons +auto` | 双空格分隔（冒号后为单个空格） |
| 28 | [soxr/soxr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/soxr/soxr.spec) | `-DWITH_CR32S=FALSE` | 双空格分隔（冒号后为单个空格） |
| 29 | [soxr/soxr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/soxr/soxr.spec) | `-DCMAKE_POLICY_VERSION_MINIMUM:STRING=3.5` | 双空格分隔（冒号后为单个空格） |
| 30 | [sqlcipher/sqlcipher.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sqlcipher/sqlcipher.spec) | — | 位置错误（`BuildOption` 位于 `BuildRequires` 之后） |
| 31 | [tcl/tcl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tcl/tcl.spec) | `--enable-man-symlinks` | 双空格分隔（冒号后为单个空格） |
| 32 | [tcl/tcl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tcl/tcl.spec) | `--enable-man-compression=gzip` | 双空格分隔（冒号后为单个空格） |
| 33 | [tcl/tcl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tcl/tcl.spec) | `--without-tzdata` | 双空格分隔（冒号后为单个空格） |
| 34 | [tunctl/tunctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tunctl/tunctl.spec) | `BIN_DIR=%{_sbindir}` | 双空格分隔（冒号后为单个空格） |

## 说明

- 双空格分隔：规则要求 `BuildOption(<stage>):` 与参数之间必须以两个空格
  分隔。上述 18 条均为冒号后只跟一个空格，应补足为两个空格。
- 位置错误：规则要求 `BuildOption` 应当位于 `BuildSystem` 与
  `BuildRequires` 之间。上述 9 个 spec 的 `BuildOption` 均位于
  `BuildRequires` 之后，应移动到 `BuildSystem` 之后、`BuildRequires`
  之前。
- 顺序错误：规则要求 `BuildOption` 的书写顺序应当与 RPM 构建过程一致
  （`build` → `install` → `check`）。上述 7 个 spec 中，6 个为 `check`
  写在 `install` 之前（Python 包常见写法），1 个为 `install` 写在
  `build` 之前，应调整顺序。
- 阶段名称：openRuyi 仓库中 `BuildOption` 阶段取值有 `conf`（4460 条）、
  `install`（1255 条）、`build`（738 条）、`check`（587 条）、`prep`
  （213 条）、`generate_buildrequires`（1 条），全部写明阶段名称，未发现
  省略阶段名称的写法。
- 字段缺失（5267 个 spec 中缺 `BuildOption` 字段的文件）由
  `check-spec-structure` 规则覆盖（`BuildOption` 为可选字段），本规则
  不重复报告。

> 规则说明：[docs/check-spec-buildoption.md](../docs/check-spec-buildoption.md)
