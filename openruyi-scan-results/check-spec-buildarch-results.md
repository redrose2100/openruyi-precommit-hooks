# check-spec-buildarch 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-buildarch` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| --- | ---: | ---: |
| 5267 | 5265 | 2 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| `BuildArch` 字段位置不在最后一个 `Source` 与 `BuildSystem` 之间 | 2 |

## 问题清单（2 条）

| # | spec 文件 | `BuildArch` 值 | 问题所在行数 | 问题类型 |
| --- | --- | --- | ---: | --- |
| 1 | [go-github-azure-azure-sdk-for-go/go-github-azure-azure-sdk-for-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-azure-azure-sdk-for-go/go-github-azure-azure-sdk-for-go.spec) | `noarch` | 46 | 位置错误（位于 `Source0` 之前） |
| 2 | [go-github-moby-sys/go-github-moby-sys.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-moby-sys/go-github-moby-sys.spec) | `noarch` | 33 | 位置错误（位于 `Source0` 之前） |

## 说明

- 位置错误：规则要求 `BuildArch` 字段应当位于最后一个 `Source` 字段
  与 `BuildSystem` 字段之间。上述 2 个 spec 的 `BuildArch: noarch`
  均位于 `Source0` 之前，应移动到最后一个 `Source` 字段之后、
  `BuildSystem` 字段之前。
- 取值：openRuyi 仓库中所有 `BuildArch` 字段值均为 `noarch`（表示
  软件包与 CPU 架构无关），未发现其它取值。
- 字段缺失（5267 个 spec 中缺 `BuildArch` 字段的文件）由
  `check-spec-structure` 规则覆盖（`BuildArch` 为可选字段），本规则
  不重复报告。

> 规则说明：[docs/check-spec-buildarch.md](../docs/check-spec-buildarch.md)
