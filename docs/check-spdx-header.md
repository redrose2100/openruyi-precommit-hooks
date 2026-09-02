# check-spdx-header

> 规则 ID：`check-spdx-header`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spdx-header-results.md](../openruyi-scan-results/check-spdx-header-results.md)

## 原始需求

来源：[openRuyi 打包指南 · SPDX 版权与许可声明](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#spdx-%E7%89%88%E6%9D%83%E4%B8%8E%E8%AE%B8%E5%8F%AF%E8%AF%81%E5%A3%B0%E6%98%8E)

> Spec 文件起始位置必须包含 SPDX 形式的版权与许可证声明，格式如下
> （其中 `SPDX-FileContributor` 为可选项）：
>
> ```spec
> # SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
> # SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
> # SPDX-FileContributor: Your Name <your.email@example.com>
> #
> # SPDX-License-Identifier: MulanPSL-2.0
> ```

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 声明位置 | 文件起始位置（允许文件最前面有少量空行）必须是注释块（`#` 开头） | 文件为空、不是 UTF-8 编码或不是以注释开头 |
| 2 | ISCAS 版权声明 | 包含 `# SPDX-FileCopyrightText: (C) <年份> Institute of Software, Chinese Academy of Sciences (ISCAS)`（必选） | 缺失即失败 |
| 3 | openRuyi 版权声明 | 包含 `# SPDX-FileCopyrightText: (C) <年份> openRuyi Project Contributors`（必选） | 缺失即失败 |
| 4 | 贡献者署名 | `# SPDX-FileContributor: ...`（可选，可有多行或没有） | 不参与判定 |
| 5 | 分隔空行 | 版权块与许可证行之间**恰好一行** `#` 空注释行（必选） | 缺少或超过一行即失败 |
| 6 | 许可证标识 | 包含 `# SPDX-License-Identifier: MulanPSL-2.0`（必选） | 缺失或不是 `MulanPSL-2.0` 即失败 |

### 年份写法

两个版权声明行中的 `<年份>` 支持以下写法（正则形式：`\d{4}((,|-) \d{4})*`）：

| 写法 | 示例 |
| --- | --- |
| 单个年份 | `2026` |
| 逗号分隔多个年份 | `2025, 2026` |
| 连字符年份区间 | `2025-2026` |

正则校验示例：`SPDX-FileCopyrightText: (C) \d{4}((,|-) \d{4})* <组织名>`

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.2.0   # 使用最新 tag
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
