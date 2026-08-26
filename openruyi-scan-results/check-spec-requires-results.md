# check-spec-requires 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-requires` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| --- | ---: | ---: |
| 5267 | 5266 | 1 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| `Requires` 一行声明多个依赖包 | 3 |

## 问题清单（1 文件 3 条）

| # | spec 文件 | 字段值 | 问题所在行数 | 问题类型 |
| --- | --- | --- | ---: | --- |
| 1 | [cloud-utils/cloud-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cloud-utils/cloud-utils.spec) | `file gzip e2fsprogs gawk tar` | 53 | 一行多个依赖包（空格分隔） |
| 2 | [cloud-utils/cloud-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cloud-utils/cloud-utils.spec) | `gawk util-linux` | 60 | 一行多个依赖包（空格分隔） |
| 3 | [cloud-utils/cloud-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cloud-utils/cloud-utils.spec) | `gawk util-linux` | 74 | 一行多个依赖包（空格分隔） |

## 说明

- 一行一个依赖：规则要求 `Requires` 运行期依赖必须按"一行一个依赖包"
  的形式书写。问题均在 `cloud-utils` 子包（`%package` 段落）内：
  第 53 行 `Requires: file gzip e2fsprogs gawk tar` 一行声明了 5 个包，
  第 60 行（`mount-image-callback` 子包）与第 74 行（`growpart` 子包）的
  `Requires: gawk util-linux` 各声明了 2 个包，应各自拆成多行。
- 富依赖表达式（`(foo >= 1 with foo < 2)` 等）、带版本约束的单个依赖
  （`foo >= 1.2` / `foo = 1.29`）以及含宏的依赖值均视为单个依赖，
  未计入问题。
- `Requires` 的 scriptlet 变体 `Requires(pre):` / `Requires(post):` /
  `Requires(preun):` / `Requires(postun):`（以及罕见的 `Requires(meta):` /
  `Requires(posttrans):`）声明的是特定脚本段或元数据角色的依赖，不属于
  本规则检查范围，未计入问题。
- 字段缺失（5267 个 spec 中缺 `Requires` 字段的文件）由
  `check-spec-structure` 规则覆盖（`Requires` 为必填头部字段），本规则
  不重复报告。

> 规则说明：[docs/check-spec-requires.md](../docs/check-spec-requires.md)
