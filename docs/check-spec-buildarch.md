# check-spec-buildarch

> 规则 ID：`check-spec-buildarch`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-buildarch-results.md](../openruyi-scan-results/check-spec-buildarch-results.md)

## 原始需求

来源：[openRuyi 打包指南 · BuildArch (可选)](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#buildarch-%E5%8F%AF%E9%80%89)

> 1. `BuildArch` 用于声明目标架构。
> 2. `BuildArch` 字段应当位于最后一个 `Source` 字段与 `BuildSystem` 字段之间。
> 3. 若 `BuildArch` 为 `noarch`，表示该软件包与 CPU 架构无关。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 声明目标架构 | `BuildArch` 用于声明目标架构，值不得为空 | 值为空即失败 |
| 2 | 字段位置 | `BuildArch` 字段应当位于最后一个 `Source` 字段与 `BuildSystem` 字段之间 | 位于最后一个 `Source` 之前、或位于 `BuildSystem` 之后即失败 |
| 3 | noarch 取值 | 若 `BuildArch` 为 `noarch`，表示该软件包与 CPU 架构无关 | 值不是 `noarch` 即失败（openRuyi 仓库中仅使用 `noarch`） |

**跳过**（无法静态判定）：

- 字段缺失：`BuildArch` 为可选字段，缺失由 `check-spec-structure` 规则覆盖，本规则不重复报告；
- 软件包是否真的与 CPU 架构无关：需人工核对，不判定；
- `%package` 子包段落内的 `BuildArch`：该字段声明的是子包架构，不属于本规则范围，不判定；
- 缺少 `Source` 或 `BuildSystem` 锚点时：位置无法判定，仅校验取值。

**注意**：检查点 1、3 为「必须」级要求（值非空且为 `noarch`），
检查点 2 为「应当」级要求（位置在最后一个 `Source` 与 `BuildSystem`
之间）。三者任一违反即报告。`BuildArch` 是否与软件包实际架构一致等
语义问题不在本规则静态检查范围内。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-buildarch
```

也可独立运行：`check-spec-buildarch path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
Source0:        https://example.com/foo-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools
```

```spec
Source0:        https://example.com/foo-%{version}.tar.gz
Source1:        https://example.com/foo-%{version}-extra.tar.gz
BuildArch:      noarch
BuildSystem:    autotools
```

### 不通过 ❌

```spec
BuildArch:      noarch
Source0:        https://example.com/foo-%{version}.tar.gz
BuildSystem:    autotools
```
→ `BuildArch must be located between the last Source field and the BuildSystem field`

```spec
Source0:        https://example.com/foo-%{version}.tar.gz
BuildSystem:    autotools
BuildArch:      noarch
```
→ `BuildArch must be located between the last Source field and the BuildSystem field`

```spec
Source0:        https://example.com/foo-%{version}.tar.gz
BuildArch:      x86_64
BuildSystem:    autotools
```
→ `BuildArch must be "noarch" (the only architecture value used by the openRuyi repository) (found "x86_64")`

```spec
Source0:        https://example.com/foo-%{version}.tar.gz
BuildArch:
BuildSystem:    autotools
```
→ `BuildArch must declare a target architecture (found empty value)`
