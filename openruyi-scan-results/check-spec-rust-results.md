# check-spec-rust 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-rust` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | rust | rustcrates | 通过 | 问题 |
| --- | ---: | ---: | ---: | ---: |
| 5267 | 13 | 1884 | 1896 | 1 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | ---: |
| 缺失 `rust-rpm-macros` | 0 |
| 缺失 `rust`（应用包） | 0 |
| `rustcrates` 使用 `BuildOption(build)` | 0 |
| `BuildOption(check)` 上方无原因注释 | 1 |

## 问题清单（1）

### `BuildOption(check)` 上方无原因注释（1 条）

| # | spec 文件 | 行号 | 问题 |
| --- | --- | ---: | --- |
| 1 | [cbindgen/cbindgen.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cbindgen/cbindgen.spec) | [20](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cbindgen/cbindgen.spec#L20) | `BuildOption(check)` 上方缺少原因注释（跳过测试须写明理由） |


## 说明

- 规则适用于 `BuildSystem: rust`（应用包）与 `BuildSystem: rustcrates`（crate provider 包）的 spec（共 1897 个）：
  1. 头部区域 `BuildRequires` 必须声明 `rust-rpm-macros`（两种系统）；
  2. `rust` 应用包还必须声明 `rust`（编译器）；
  3. `rustcrates` 不得使用 `BuildOption(build)`（不可覆盖构建阶段）；
  4. `rust` 应用包每个 `BuildOption(check)` 块首行上方必须有原因注释。
- 其中 rust 应用包 13 个，crate provider 包 1884 个。
- 其余 spec 不适用本规则，未计入统计。
- `%package` 子包段落内的 `BuildRequires`、宏展开值（如
  `%{?foo}`）以及注释行不视为有效声明。
- `crate(...)` 虚拟依赖、三宏声明（`crate_name`/`full_version`/
  `pkgname`）、`rust` 应用包的 `%install` 编写等为建议性/
  条件性要求，未纳入强检查点。

> 规则说明：[docs/check-spec-rust.md](../docs/check-spec-rust.md)
