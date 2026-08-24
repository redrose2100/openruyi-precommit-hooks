# check-spec-license

> 规则 ID：`check-spec-license`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-license-results.md](../openruyi-scan-results/check-spec-license-results.md)

## 原始需求

来源：[openRuyi 打包指南 · License](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#license)

> 1. `License` 必须使用 SPDX License Identifier 或 SPDX License Expression。
> 2. 当存在多个许可证时，表达式中许可证之间必须使用 `AND` / `OR` 等 SPDX 连接符。
> 3. 若源代码中存在许可证文本文件，Spec 必须在 `%files` 中使用 `%license` 将其标记并打包；若子包的许可证与主包不符，则必须在子包内写明对应的许可证信息。

补充规范：[许可证](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/Licenses)

> 每个 spec 文件都必须包含一个 `License` 字段，在填写 `License` 字段时必须尽一切可能做到准确。
> `License` 字段必须使用适当的 [SPDX 许可证标识符](https://spdx.org/licenses/)或表达式来填写。
> 如果碰到 Public Domain 也就是公有领域的软件包，可以这样编写 `License` 字段：
> `License:        LicenseRef-openRuyi-Public-Domain`

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | SPDX 连接符大小写 | 多个许可证必须使用 `AND` / `OR`（以及 `WITH` 例外）等 SPDX 连接符 | 值中出现空格/括号包围的小写 `and`、`or`、`with` 即失败 |
| 2 | 不得使用逗号分隔 | 连接符必须是 SPDX 操作符，逗号不是合法分隔符 | 值中含逗号 `,` 即失败 |
| 3 | 不得使用 `+` 后缀 | 老式 Fedora 风格 `GPLv3+`、`MPL-2.0+` 无 SPDX 含义，须用 `-or-later` 后缀 | 值中 token 以 `+` 结尾即失败（如 `GPLv3+`、`MPL-2.0+`） |
| 4 | 括号配对 | SPDX 表达式的括号分组必须配对 | 值中 `(` 与 `)` 数量不等即失败 |
| 5 | 标识符准确性 | `License` 必须使用合适的 SPDX 标识符或表达式 | 需要知识库与语义判断，静态单文件检查无法覆盖，不参与判定 |
| 6 | `%files` 中 `%license` 标记 | 源码含许可证文本时必须在 `%files` 中标记 | 需跨段落上下文与上游源码比对，不参与判定 |

**跳过**（无法静态判定）：

- 含宏展开的 `License` 值（如 `%{license}`）不做判定；
- 字段缺失或为空：由 `check-spec-structure` 规则覆盖，本规则不重复报告；
- `LicenseRef-openRuyi-Public-Domain`、`LicenseRef-*` 等 SPDX 扩展标识符视为合法，不判定；
- 括号内嵌 `-or-later` / `-with-` 等标识符片段：属于 SPDX 标识符的一部分（如 `GPL-3.0-or-later`、`Apache-2.0 WITH LLVM-exception`），不误报。

**注意**：检查点 1 为「必须」的强制性要求。小写 `and`/`or`/`with`
不符合 SPDX 表达式语法（SPDX 规定操作符必须大写），会报告。标识符本身
的准确性（检查点 5）需要许可证知识库，静态单文件检查无法覆盖，由包
维护者自行核对 SPDX License List。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-license
```

也可独立运行：`check-spec-license path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
License:        MIT
```

```spec
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND CC0-1.0
```

```spec
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
```

```spec
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
```

```spec
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause
```

```spec
License:        LicenseRef-openRuyi-Public-Domain
```

```spec
License:        %{license}
```

### 不通过 ❌

```spec
License:        BSD and MIT and zlib
```
→ `License must use uppercase SPDX operators AND/OR/WITH (found "BSD and MIT and zlib")`

```spec
License:        MIT, BSD-3-Clause
```
→ `License must not use a comma as a separator; use AND (found "MIT, BSD-3-Clause")`

```spec
License:        GPLv3+
```
→ `License must not use a legacy "+" suffix; use the "-or-later" suffix (found "GPLv3+")`