# check-spec-summary

> 规则 ID：`check-spec-summary`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-summary-results.md](../openruyi-scan-results/check-spec-summary-results.md)

## 原始需求

来源：[openRuyi 打包指南 · Summary](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#summary)

> 1. `Summary` 必须为软件包功能的简短描述。
> 2. `Summary` 应当仅包含必要的英文介绍。
> 3. `Summary` 不得以英文句号 `.` 结尾。

相关：[排版与可读性](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#typesetting-and-readability)
要求 spec 中的说明性文字（如 `Summary`、注释与 `%description`）应当使用美式英语。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 不得以英文句号结尾 | `Summary` 不得以英文句号 `.` 结尾 | 值去除首尾空白后以 `.` 结尾即失败 |
| 2 | 仅包含必要的英文介绍 | `Summary` 应当仅包含必要的英文介绍 | 值含 CJK/全角字符（汉字、假名、谚文、全角符号、CJK 标点）即失败 |
| 3 | 简短描述 | `Summary` 必须为软件包功能的简短描述 | 定性要求，需语义判断，单个文件无法静态判定，不参与判定 |

**跳过**（无法静态判定）：

- 含宏展开的 `Summary` 值（如 `%{name}`、`%{pkg_desc}`）不做判定；
- 字段缺失或为空：由 `check-spec-structure` 规则覆盖，本规则不重复报告；
- 装饰性符号（如 en-dash `–`、emoji）不判定为「非英文介绍」，避免误报。

**注意**：检查点 2 为「应当」的推荐性表述，含 CJK/全角字符（即非英文
语言文字）的 `Summary` 会报告；检查点 3（简短描述）需要语义理解，静态
单文件检查无法覆盖，由包维护者自行斟酌描述长度。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.2.0   # 使用最新 tag
    hooks:
    -   id: check-spec-summary
```

也可独立运行：`check-spec-summary path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
Summary:        A tool for building packages
```

```spec
Summary:        Version 1.5.7 of the example tool
```

```spec
Summary:        %{name} library
```

```spec
Summary:        A fast tool — no fluff
```

### 不通过 ❌

```spec
Summary:        A tool for building packages.
```
→ `Summary must not end with a period (found "A tool for building packages.")`

```spec
Summary:        软件包功能描述
```
→ `Summary should contain only English text (found "软件包功能描述")`

```spec
Summary:        软件包功能描述。
```
→ `Summary should contain only English text (found "软件包功能描述。")`
（全角句号 `。` 属于 CJK 标点，同时触发非英文检查）
