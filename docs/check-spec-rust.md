# check-spec-rust

> 规则 ID：`check-spec-rust`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-rust-results.md](../openruyi-scan-results/check-spec-rust-results.md)

## 原始需求

来源：[openRuyi 打包指南 · 构建系统 · Rust](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems/rust)

> 使用 `rust` 或 `rustcrates` 构建系统时，通常需要添加：
>
> ```spec
> BuildRequires:   rust
> BuildRequires:   rust-rpm-macros
> ```

> 如果软件包依赖其他 Rust crate，应通过 `crate(...)` 能力声明对应的构建依赖，
> 例如：
>
> ```spec
> BuildRequires:  crate(clap-4/default) >= 4.5.0
> ```

> ### `rustcrates`
>
> `rustcrates` 构建系统的构建阶段不执行 Cargo build。它会运行动态 specpart
> 生成脚本，根据 crate provider 的 feature 子包生成对应的 `%files` 片段。
> **因此，请不要覆盖此阶段。**

> ### `rust`
>
> `rust` 构建系统提供默认测试阶段。它会执行 Cargo test 流程。
> 可以通过 `BuildOption(check)` 向测试阶段传递参数。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 声明必需依赖 | `BuildSystem: rustcrates` 的 spec 必须在头部 `BuildRequires` 中声明 `rust-rpm-macros`；`BuildSystem: rust` 的 spec 必须声明 `rust` 与 `rust-rpm-macros` | 头部区域 `BuildRequires` 缺失对应依赖，即失败 |
| 2 | `rustcrates` 不覆盖构建阶段 | `BuildSystem: rustcrates` 的 spec 不得使用 `BuildOption(build)` | 头部区域出现 `BuildOption(build)`，即失败 |
| 3 | `BuildOption(check)` 须写明原因 | `BuildSystem: rust` 的 spec 使用 `BuildOption(check)` 跳过测试时，须在上方以注释写明跳过原因 | 连续的 `BuildOption(check)` 块首行上方最近的非空行不是注释，即失败 |

**说明**：

- 检查点 1 按构建系统区分必需依赖：crate provider 包（`rustcrates`）不执行
  Cargo 编译，只需要 `rust-rpm-macros`（`%rust_setup_registry`、
  `%rust_install_crate` 等宏的提供方）；应用包（`rust`）还需要编译器
  `rust`。只要求**存在声明**，不限制声明顺序、是否带版本约束；
- 检查点 2 对应文档「构建阶段 · `rustcrates`」的明确要求；`rust` 应用包
  允许使用 `BuildOption(build)` 向 Cargo 构建传递参数，不受此限制；
- 检查点 3 的"注释在上方"指**紧邻的上一非空行**为注释；连续多行
  `BuildOption(check)`（中间无空行）视为同一块，仅块首行上方需要注释。

**跳过**（无法静态判定 / 由其它规则覆盖 / 建议性要求）：

- `BuildSystem` 字段缺失、`rust` 与 `rustcrates` 的选型：依赖上游源码树
  （应用包还是 crate provider 包），spec 内无法静态判定；字段缺失由
  `check-spec-structure` 规则覆盖；
- `crate(...)` 虚拟依赖声明：软件包是否依赖其他 crate 需要分析上游
  `Cargo.toml`，spec 内无法静态判定是否存在依赖，故不强制声明；
- 三宏声明（`crate_name`/`full_version`/`pkgname`）：文档说明「一般不需
  手动修改」，由 crate provider 生成工具（tako）负责；
- `rust` 应用包的 `%install`：文档「安装阶段 · `rust`」说明无默认安装动作，
  但 `%install -p/-a` 扩展为合法写法，无法用"必须有 `%install`"静态约束；
- `rustcrates` 的 `%check` 覆盖、`%prep -p/-a`、`%build -p/-a` 等扩展机制：
  由其它规则覆盖或非强制；
- `BuildOption` 的格式规则（双空格、顺序、位置）：由
  `check-spec-buildoption` 规则覆盖；
- `BuildRequires: crate(...)` 的依赖语法：由 `check-spec-requires` 规则覆盖。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.2.0   # 使用最新 tag
    hooks:
    -   id: check-spec-rust
```

也可独立运行：`check-spec-rust path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
BuildSystem:    rust
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
```

```spec
BuildSystem:    rustcrates
BuildRequires:  rust-rpm-macros
```

```spec
BuildSystem:    rust
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
# test_body requires network access unavailable in the build environment
BuildOption(check):  -- --skip test_body
```

### 失败 ❌

```spec
BuildSystem:    rust
BuildRequires:  rust-rpm-macros
```

```spec
BuildSystem:    rustcrates
BuildRequires:  rust
```

```spec
BuildSystem:    rustcrates
BuildRequires:  rust-rpm-macros
BuildOption(build):  --features "foo"
```

```spec
BuildSystem:    rust
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildOption(check):  -- --skip test_body
```
