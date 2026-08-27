# check-spec-cmake 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-cmake` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | cmake | 通过 | 问题 |
| --- | ---: | ---: | ---: |
| 5267 | 422 | 421 | 1 |

## 问题类型分布

按缺失依赖统计：

| 缺失依赖 | 文件数 |
| --- | ---: |
| `cmake` | 1 |

按缺失组合统计：

| 缺失组合 | 文件数 |
| --- | ---: |
| 缺 1 项：`cmake` | 1 |

## 问题清单（1 条）

| # | spec 文件 | 缺失依赖 | BuildSystem 所在行数 |
| --- | --- | --- | ---: |
| 1 | [plasma-wayland-protocols/plasma-wayland-protocols.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/plasma-wayland-protocols/plasma-wayland-protocols.spec) | `cmake` | 16 |

## 说明

- 规则仅适用于 `BuildSystem: cmake` 的 spec（共 422 个）：
  头部区域 `BuildRequires` 必须声明 `cmake` 依赖。
  `gcc` 在构建环境预装，可不显式声明，不纳入检查。
- 其余 4845 个非 cmake spec 不适用本规则，未计入统计。
- `%package` 子包段落内的 `BuildRequires`、宏展开值（如 `%{?foo}`）以及注释行不视为有效声明。
- 是否应将 `%build`/`%install` 指令迁移为 `BuildOption`/`%build -p`/`%install -a`：
  由 `check-spec-buildoption` 规则覆盖与指南示例说明，
  不在本规则范围内。

> 规则说明：[docs/check-spec-cmake.md](../docs/check-spec-cmake.md)
