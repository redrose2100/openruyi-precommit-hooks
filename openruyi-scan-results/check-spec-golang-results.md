# check-spec-golang 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-golang` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | golang | golangmodules | 适用小计 | 通过 | 问题 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 5267 | 12 | 718 | 730 | 730 | 0 |

## 问题类型分布

未发现缺失依赖的情况（0 条）。

## 问题清单（0 条）

未发现违规 spec。

## 说明

- 规则仅适用于 `BuildSystem: golang` 或 `BuildSystem: golangmodules`
  的 spec（共 730 个）：
  头部区域 `BuildRequires` 必须声明 `go` 与 `go-rpm-macros`
  两项依赖。
  （与 cmake/autotools 指南不同，golang 页面未提及预装工具豁免，
  因此两项均为必需声明。）
- 其余 4537 个非 golang/golangmodules spec 不适用本规则，未计入统计。
- `%package` 子包段落内的 `BuildRequires`、宏展开值（如 `%{?foo}`）以及注释行不视为有效声明。
- 头部定义 `_name` 与 `go_import_path` 宏（"至少应该"）：属建议性要求，未纳入强检查点。
- 跨构建系统宏调用（`%go_common`、`%buildsystem_golangmodules_install`
 等）取决于最终产物形态（二进制/库），无法静态判定，
  不在本规则范围内。

> 规则说明：[docs/check-spec-golang.md](../docs/check-spec-golang.md)
