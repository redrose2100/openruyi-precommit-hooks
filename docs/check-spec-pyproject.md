# check-spec-pyproject

> 规则 ID：`check-spec-pyproject`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-pyproject-results.md](../openruyi-scan-results/check-spec-pyproject-results.md)

## 原始需求

来源：[openRuyi 打包指南 · 构建系统 · Pyproject](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems/pyproject)

> 如需要使用 `pyproject` 构建系统，那么通常至少需要添加这些 `BuildRequires`。
>
> ```spec
> BuildRequires:  pyproject-rpm-macros
> BuildRequires:  pkgconfig(python3)
> ```

> 在使用 `pyproject` 声明式构建系统时，**一定要**在 `BuildOption(install)`
> 处传入对应的模块名。由于该选项会作为参数传递给 `%pyproject_save_files`，
> 因此通常建议默认添加 `-l` 参数。

> 如果在这个过程中需要排除某些模块，可以通过 `BuildOption(check)` 向
> `%pyproject_check_import` 传递参数，**并且在上方写明跳过的原因**。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 声明必需依赖 | `BuildSystem: pyproject` 的 spec 必须在头部 `BuildRequires` 中声明 `pyproject-rpm-macros` | 头部区域 `BuildRequires` 缺失 `pyproject-rpm-macros`，即失败 |
| 2 | `BuildOption(install)` 非空 | `BuildSystem: pyproject` 的 spec 使用 `BuildOption(install)` 时必须传入对应的模块名 | `BuildOption(install)` 后为空值（无参数），即失败 |
| 3 | `BuildOption(check)` 须写明原因 | `BuildSystem: pyproject` 的 spec 使用 `BuildOption(check)` 排除模块时，须在上方以注释写明跳过原因 | 连续的 `BuildOption(check)` 块首行上方最近的非空行不是注释，即失败 |

**说明**：

- 检查点 1 只要求**存在声明**，不限制声明顺序、是否带版本约束；
  "一行一个依赖包"的书写格式由 `check-spec-buildrequires` 规则覆盖；
- 检查点 2 只要求 `BuildOption(install)` **非空**（模块名可以是
  `-l %{srcname}`、`%{srcname}`、`-l %{srcname} +auto` 等形态），
  无法静态验证模块名是否真实存在于上游源码树；
- 检查点 3 的"注释在上方"指**紧邻的上一非空行**为注释；连续多行
  `BuildOption(check)`（中间无空行）视为同一块，仅块首行上方需要
  注释。

**跳过**（无法静态判定 / 由其它规则覆盖 / 建议性要求）：

- `BuildSystem` 字段缺失：为必填字段，由 `check-spec-structure` 规则覆盖；
- 非 `pyproject` 构建系统的 spec：本规则不适用，不检查；
- `pkgconfig(python3)`：文档措辞为「通常至少需要」，且由
  `%pyproject_buildrequires` 自动生成（`pyproject-rpm-macros` 是
  `%pyproject_*` 宏的提供方，缺失会导致构建失败，故作为必需声明）；
- `BuildOption(install)` 的 `-l` 参数：文档措辞为「通常建议」，且依赖
  上游 PEP 639 License-File 声明（"如果构建时报出 `No License-File`
  错误，则去掉该参数"），无法静态判定；
- `%generate_buildrequires` / `%pyproject_buildrequires` 自动生成依赖：
  文档为推荐做法，非强制；
- 置空 `%check`：文档措辞为「通常来说，不应」，属建议性要求，且声明式
  构建系统仍会执行默认冒烟测试；
- 适用性（上游存在 `pyproject.toml` 且遵循 PEP 517）：依赖上游源码树，
  spec 内无法静态判定；
- `BuildOption` 的格式规则（双空格、顺序、位置）：由
  `check-spec-buildoption` 规则覆盖。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.2.0   # 使用最新 tag
    hooks:
    -   id: check-spec-pyproject
```

也可独立运行：`check-spec-pyproject path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
BuildSystem:    pyproject
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

BuildOption(install):  -l example_pkg
```

```spec
BuildSystem:    pyproject
BuildRequires:  pyproject-rpm-macros
# No module named 'marray'
BuildOption(check):  -e 'example_pkg.tests*'
```

### 失败 ❌

```spec
BuildSystem:    pyproject
BuildRequires:  pkgconfig(python3)
```

```spec
BuildSystem:    pyproject
BuildOption(install):
BuildRequires:  pyproject-rpm-macros
```

```spec
BuildSystem:    pyproject
BuildOption(check):  -e example_pkg.tests*
BuildRequires:  pyproject-rpm-macros
```
