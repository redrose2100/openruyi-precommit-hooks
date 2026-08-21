# check-spdx-header

> 规则 ID：`check-spdx-header`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spdx-header-results.md](../openruyi-scan-results/check-spdx-header-results.md)

## 规则说明

Spec 文件（RPM `.spec`）的**起始位置**必须包含 SPDX 形式的版权与许可证声明。

openRuyi 发行版中的每个软件包 spec 文件都必须声明版权归属与许可证，便于版权审计与合规检查。

## 格式要求

spec 文件开头的连续注释块中，必须按以下顺序出现（仅允许文件最前面有少量空行）：

```spec
# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Your Name <your.email@example.com>
#
# SPDX-License-Identifier: MulanPSL-2.0
```

| 行 | 必选/可选 | 说明 |
| --- | --- | --- |
| `# SPDX-FileCopyrightText: (C) <年份> Institute of Software, Chinese Academy of Sciences (ISCAS)` | **必选** | 中国科学院软件研究所（ISCAS）版权声明 |
| `# SPDX-FileCopyrightText: (C) <年份> openRuyi Project Contributors` | **必选** | openRuyi 项目贡献者版权声明 |
| `# SPDX-FileContributor: ...` | 可选 | 贡献者署名，可有多行或没有 |
| `#` | **必选** | 版权块与许可证之间的空注释行，**且恰好只有一行** |
| `# SPDX-License-Identifier: MulanPSL-2.0` | **必选** | 许可证标识，必须为 `MulanPSL-2.0` |

### 年份写法

两个版权声明行中的 `<年份>` 支持以下写法（正则形式：`\d{4}((,|-) \d{4})*`）：

| 写法 | 示例 |
| --- | --- |
| 单个年份 | `2026` |
| 逗号分隔多个年份 | `2025, 2026` |
| 连字符年份区间 | `2025-2026` |

正则校验示例：`SPDX-FileCopyrightText: (C) \d{4}((,|-) \d{4})* <组织名>`

## 检查内容

对每个 `.spec` 文件，本规则检查：

1. 文件开头（允许空行后）是否是注释块（`#` 开头）。
2. 注释块中是否包含 ISCAS 的 `SPDX-FileCopyrightText` 行。
3. 注释块中是否包含 openRuyi Project Contributors 的 `SPDX-FileCopyrightText` 行。
4. 版权两行与许可证行之间是否存在**恰好一行** `#` 空注释行。
5. 注释块中是否包含 `# SPDX-License-Identifier: MulanPSL-2.0` 行。

以下情况会被判定为**失败**：

- 缺少任一必选行；
- 版权块与许可证之间缺少 `#` 空注释行，或空注释行超过一行；
- `SPDX-License-Identifier` 不是 `MulanPSL-2.0`；
- 文件不是 UTF-8 编码；
- 文件为空或不是以注释开头。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spdx-header
```

也可以作为独立命令使用：

```console
$ check-spdx-header path/to/foo.spec
```

返回码为 1 表示有文件不满足要求，0 表示全部通过。

## 示例

### 通过 ✅

```spec
# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           foo
```

### 不通过 ❌（缺少 openRuyi 版权声明）

```spec
# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           foo
```

### 不通过 ❌（许可证不是 MulanPSL-2.0）

```spec
# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MIT

Name:           foo
```
