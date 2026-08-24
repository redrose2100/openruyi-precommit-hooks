# check-spec-release

> 规则 ID：`check-spec-release`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-release-results.md](../openruyi-scan-results/check-spec-release-results.md)

## 原始需求

来源：[openRuyi 打包指南 · Release](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#release)

> 1. `Release` 应当使用 `%autorelease`。
> 2. `Release` 中不得硬编码发行版后缀或覆盖 `%{dist}` 的值。
> 3. 在同一 `Version` 下，`Release` 对应的修订序号必须递增。
> 4. 当 `Version` 更新时，`Release` 对应的修订序号必须复位为 `1`。

补充规范 [版本号（Versioning）](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/Versioning)
对 `Release` 的补充说明：

> `Release` 字段默认值应使用一个从 `1` 开始的整数（不是 `0`），并且在每次
> 修订软件包（即下游重新打包）时递增；当 `Version` 字段被更改时，应该将
> 数字复位为 `1`。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 使用 `%autorelease` | `Release` 应当使用 `%autorelease` | 字面整数（如 `3`）未使用 `%autorelease` 时给出建议性提示（应当级）；`%autorelease` / `%{autorelease}` 直接通过 |
| 2 | 修订序号从 `1` 开始 | `Release` 的修订序号应为从 `1` 开始的整数（不是 `0`） | 字面 `0` 或 `0%{?dist}` 等 `0` 前缀即失败 |
| 3 | 不得硬编码发行版后缀 | `Release` 中不得硬编码发行版后缀 | 字面值含非数字尾部（如 `1.fc40`、`2.el9`）即失败；宏展开值在宏前出现非数字（如 `1.fc40%{?dist}`）即失败 |
| 4 | 不得覆盖 `%{dist}` | 不得覆盖 `%{dist}` 的值 | 头部存在 `%global dist ...` / `%define dist ...` 即失败 |
| 5 | 修订序号递增 | 同一 `Version` 下 `Release` 修订序号必须递增 | 需要跨版本历史，单个文件无法静态判定，不参与判定 |
| 6 | `Version` 更新复位 | `Version` 更新时修订序号必须复位为 `1` | 需要版本历史，单个文件无法静态判定，不参与判定 |

**跳过**（无法静态判定）：

- 含其它宏展开的 `Release` 值（如 `%{release}`、`1%{?dist}`），除 `0` 前缀
  与硬编码后缀外不做判定；
- 字段缺失：由 `check-spec-structure` 规则覆盖，本规则不重复报告。

**注意**：检查点 1 为「应当」的推荐性表述，字面整数修订（如 `3`）会报告
建议性提示；检查点 5、6 需要版本历史信息，静态单文件检查无法覆盖，由包
维护者在升级 `Version` 时自行复位修订序号。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-release
```

也可独立运行：`check-spec-release path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
Release:        %autorelease
```

```spec
Release:        %{autorelease}
```

```spec
Release:        %{patchset_release}.%{config_version}_%autorelease
```

```spec
Release:        1%{?dist}
```

### 不通过 ❌

```spec
Release:        3
```
→ `Release should use "%autorelease" instead of a fixed revision (found "3")`

```spec
Release:        0
```
→ `Release revision must start at 1 (found "0")`

```spec
Release:        1.fc40
```
→ `Release must not hardcode a dist suffix (found "1.fc40")`

```spec
Release:        2.el9
```
→ `Release must not hardcode a dist suffix (found "2.el9")`

```spec
Release:        0%{?dist}
```
→ `Release revision must start at 1 (found "0%{?dist}")`

```spec
Release:        %autorelease
%global dist foo
```
→ `the "dist" macro must not be overridden (%global dist foo)`