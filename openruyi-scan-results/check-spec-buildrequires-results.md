# check-spec-buildrequires 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-buildrequires` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| --- | ---: | ---: |
| 5267 | 5266 | 1 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| `BuildRequires` 一行声明多个依赖包 | 1 |

## 问题清单（1 条）

| # | spec 文件 | 字段值 | 问题类型 |
| --- | --- | --- | --- |
| 1 | [valgrind/valgrind.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/valgrind/valgrind.spec) | `automake autoconf` | 一行多个依赖包（空格分隔） |

## 说明

- 一行一个依赖：规则要求 `BuildRequires` 依赖项必须按"一行一个依赖包"
  的形式书写。唯一问题为 `valgrind` 的 `BuildRequires:  automake autoconf`
  （一行声明了 `automake` 与 `autoconf` 两个包），应拆成两行。
- `groff` 子包（`%package x11`）内也存在
  `BuildRequires:  libXaw-devel, libXmu-devel` 的写法，但该行位于
  `%package` 子包段落内，声明的是子包构建依赖，不属于本规则范围
  （与 `check-spec-buildoption` 等规则对子包的处理一致），不计入问题。
- 富依赖表达式（`(foo >= 1 with foo < 2)` 等）、带版本约束的单个依赖
  （`foo >= 1.2` / `foo = 1.29`）以及含宏的依赖值均视为单个依赖，
  未计入问题。
- 字段缺失（5267 个 spec 中缺 `BuildRequires` 字段的文件）由
  `check-spec-structure` 规则覆盖（`BuildRequires` 为必填字段），本规则
  不重复报告。

> 规则说明：[docs/check-spec-buildrequires.md](../docs/check-spec-buildrequires.md)
