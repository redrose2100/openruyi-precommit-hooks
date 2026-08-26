# check-spec-bcond

> 规则 ID：`check-spec-bcond`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-bcond-results.md](../openruyi-scan-results/check-spec-bcond-results.md)

## 原始需求

来源：[openRuyi 打包指南 · 条件构建](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#条件构建)

> 当需要定义可选构建开关时，Spec 应当使用 `%bcond`；
> Spec 应当尽量避免使用 `%bcond_with` 与 `%bcond_without`。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 不使用旧式宏 | Spec 应当使用 `%bcond <name> <0\|1>` 定义可选构建开关，尽量避免 `%bcond_with` / `%bcond_without` | 出现 `%bcond_with` 或 `%bcond_without` 宏（行首宏、非注释行），即失败 |
| 2 | 引用须有声明 | 每个 `%{with <name>}` / `%{without <name>}` 引用都应有一个对应的 `%bcond <name> <0\|1>` 声明 | 引用的开关名在本文件任何位置（含 `%bcond_with` / `%bcond_without` 声明）都找不到声明，即失败 |

**说明**：

- 旧式宏 `%bcond_with`（默认关闭）与 `%bcond_without`（默认开启）
  会把开关的默认方向写死；`%bcond <name> <0|1>` 默认值写在声明里，
  `--with=` / `--without=` 可以在两个方向上覆盖，语义更完整。
- 检查点 2 只要求开关被**声明**，不限制默认值；构建方仍可用
  `--with=...` / `--without=...` 从命令行覆盖任意已声明开关。
- `%{with <name>}` 未声明时构建期通常展开为空、`%if` 恒假，分支
  永远不参与构建（除非恰好以参数注入），故按 error 处理。
- 被注释掉的行（`#` 开头）不参与检查；旧式下划线形态
  `%define with_xxx` + `%{with_xxx}`（如 `mariadb.spec`）不属于
  `%bcond` 体系，不在本规则范围。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-bcond
```

也可独立运行：`check-spec-bcond path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
%bcond bootstrap 0

%if %{with bootstrap}
# 跳过 bootstrap 阶段的测试
%endif
```

```spec
%bcond tests 0
%bcond docs 1

%if %{with tests}
BuildRequires:  pytest
%endif

%if %{without docs}
# docs 被强制关闭
%endif
```

### 违规 ❌

```spec
# 旧式宏：默认值方向写死，应改用 %bcond
%bcond_with openssl

%if %{with openssl}
BuildRequires:  openssl-devel
%endif
```

```spec
# %{with gui} 未声明：构建期恒假，分支永不参与构建
%if %{with gui}
BuildRequires:  gtk3-devel
%endif
```
