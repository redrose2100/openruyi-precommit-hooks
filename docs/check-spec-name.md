# check-spec-name

> 规则 ID：`check-spec-name`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-name-results.md](../openruyi-scan-results/check-spec-name-results.md)

## 规则说明

Spec 文件的 `Name` 字段必须遵循
[openRuyi 打包指南·命名规则](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/Naming)：

1. `Name` 必须定义软件包名称。
2. 软件包名称应当为小写，并优先使用短横线（`-`）作为分隔符；
   下划线（`_`）仅在补充规范允许的例外情形下使用
   （如上游名称自然含下划线的 `nss_wrapper`）。
3. 软件包名称不得编码 ABI（如 SONAME major）或上游主版本号
   （例如不得为 `libfoo2` 之类命名）。
4. 当包名与上游常用名称不一致时，Spec 可以通过 `Provides:` 提供上游
   名称别名；是否提供由兼容性需求决定。

命名的完整策略（例如模块包、Perl/Python/字体包等专门规则），
请见补充规范[命名规则](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/Naming)。

## 检查内容

对每个 `.spec` 文件，本规则检查：

1. 是否存在 `Name:` 字段。
2. `Name` 值是否全小写 —— `perl-*` 模块例外（CPAN 分发组名需大写）。
3. `Name` 值中是否含下划线 `_`（应优先用短横线）。
4. `Name` 值是否形如 `lib<字母><数字>`（如 `libfoo2`，编码了 ABI/主版本号）。

以下情况会被**跳过**（无法静态判定）：

- `Name` 值含宏展开（如 `python-%{pypi_name}`）；
- `perl-*` 名称的大写检查。

**注意**：下划线检查会报告所有含 `_` 的名称（包括
`nss_wrapper` 这类规范允许的例外），是否采纳由打包者决定；
`perl-*` 模块整体豁免小写检查，但下划线/ABI 检查仍生效。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-name
```

也可独立运行：`check-spec-name path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
Name:           foo-bar
```

```spec
Name:           perl-Archive-Tar
```

```spec
Name:           python-%{pypi_name}
```

### 不通过 ❌

```spec
Name:           Catch2
```
→ `package name should be lowercase (found "Catch2")`

```spec
Name:           wpa_supplicant
```
→ `prefer "-" over "_" in package name (found "wpa_supplicant")`

```spec
Name:           libfoo2
```
→ `package name should not encode an ABI or major version (found "libfoo2")`

```spec
Version:        1.0
```
→ `missing required field "Name"`
