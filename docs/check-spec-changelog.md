# check-spec-changelog

> 规则 ID：`check-spec-changelog`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-changelog-results.md](../openruyi-scan-results/check-spec-changelog-results.md)

## 原始需求

来源：[openRuyi 打包指南 · %changelog](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#changelog)

> `%changelog` 段内容必须为 `%autochangelog`，不得手写更新日志。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 使用 `%autochangelog` | `%changelog` 段内容必须为 `%autochangelog`，不得手写更新日志 | 段内不存在 `%autochangelog`（或其条件宏形式 `%{?autochangelog}`），而是手写 changelog 条目、仅注释、或空段，即失败 |
| 2 | 移除手写条目 | 段内不得包含任何手写 changelog 条目 | 段内同时存在手写条目与 `%autochangelog` 宏，即失败 |

**说明**：

- `%autochangelog` 的两种合法写法均通过检查：
  - 直接宏形式：`%autochangelog`
  - 条件宏形式：`%{?autochangelog}`（仅在定义了 `%autochangelog` 时展开；openRuyi 仓库中 831 个包采用此写法）
- 段内注释（`#` 开头）允许存在，但仅注释不足以满足「段内容必须为
  `%autochangelog`」的要求——空段或仅注释段仍判定为违规。
- `%changelog` 段缺失：`%changelog` 是打包指南「基础字段与段落」中列出的
  必填段落，缺失由 `check-spec-structure` 规则覆盖，本规则不重复报告。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.2.0   # 使用最新 tag
    hooks:
    -   id: check-spec-changelog
```

也可独立运行：`check-spec-changelog path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
%changelog
%autochangelog
```

```spec
%changelog
%{?autochangelog}
```

### 不通过 ❌

```spec
%changelog
* Tue Aug 26 2026 Jane Doe <jane@example.org> - 1.0-1
- initial package
```

```spec
%changelog
%{?autochangelog}
* Tue Aug 26 2026 Jane Doe <jane@example.org> - 1.0-1
- initial package
```
