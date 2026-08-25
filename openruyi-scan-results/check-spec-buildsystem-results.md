# check-spec-buildsystem 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-buildsystem` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| --- | ---: | ---: |
| 5267 | 5267 | 0 |

## 问题类型分布

无问题。

## 问题清单

无问题。

## 说明

- 取值分布：openRuyi 仓库中 `BuildSystem` 字段共使用 10 种取值，全部
  在已知值白名单内（官方列出的 6 种 + 仓库扩展的 4 种）：

  | 取值 | 数量 |
  | --- | ---: |
  | `rustcrates` | 1884 |
  | `pyproject` | 852 |
  | `golangmodules` | 718 |
  | `autotools` | 684 |
  | `cmake` | 422 |
  | `perlmaker` | 350 |
  | `meson` | 178 |
  | `perlbuild` | 44 |
  | `rust` | 13 |
  | `golang` | 12 |

- 空值：未发现空 `BuildSystem` 字段（官方允许为空但须以注释说明原因，
  仓库中暂无此写法）。
- 字段缺失（5267 个 spec 中缺 `BuildSystem` 字段的 110 个文件）由
  `check-spec-structure` 规则覆盖（`BuildSystem` 为必填字段），本规则
  不重复报告。

> 规则说明：[docs/check-spec-buildsystem.md](../docs/check-spec-buildsystem.md)
