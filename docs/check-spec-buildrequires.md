# check-spec-buildrequires

> 规则 ID：`check-spec-buildrequires`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-buildrequires-results.md](../openruyi-scan-results/check-spec-buildrequires-results.md)

## 原始需求

来源：[openRuyi 打包指南 · BuildRequires](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#buildrequires)
与 [排版与可读性](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#%E6%8E%92%E7%89%88%E4%B8%8E%E5%8F%AF%E8%AF%BB%E6%80%A7)

> 1. `BuildRequires` 必须列出构建期依赖。
> 2. 依赖项必须按"一行一个依赖包"的形式书写。
> 3. 对于 C 程序，通常不需要显式声明 `gcc`。
> 4. 当依赖通过 `pkg-config` 发现时，`BuildRequires` 应当优先使用 `pkgconfig(xxx)` 形式声明，而不是直接依赖 `xxx-devel`。
> 5. Spec 必须确保构建依赖完整；不得依赖构建环境偶然预装而省略必要依赖。

排版与可读性：

> `BuildRequires` 与 `Requires` 必须采用"一行一个依赖"的形式。

补充文档（[使用 pkgconfig(xxx)](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/PkgConfigBuildRequires)）：

> 当某库 `foo` 通过 pkg-config 被发现时，`BuildRequires` 应当声明为 `pkgconfig(foo)`。
> 在不通过 pkg-config 发现（或包名含义更直接）的情况下，也可以按包名 `foo` 声明。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 一行一个依赖 | `BuildRequires` 依赖项必须按"一行一个依赖包"的形式书写 | 一行中出现多个依赖包（如逗号分隔 `a, b` 或空格分隔 `a b`）即失败 |
| 2 | 值非空 | `BuildRequires` 必须列出构建期依赖 | 写成 `BuildRequires:`（空值）即失败 |

**跳过**（无法静态判定）：

- 字段缺失：`BuildRequires` 为必填字段，缺失由 `check-spec-structure` 规则覆盖，本规则不重复报告；
- 依赖完整性：是否遗漏了构建环境偶然预装而未声明的依赖，需人工核对，不判定；
- `gcc` 显式声明：是否 C 程序需结合 `%build` 等内容判断，规范为"通常不需要"，不判定；
- `pkgconfig(xxx)` 优先：依赖是否通过 `pkg-config` 发现需人工核对，且直接依赖 `xxx-devel` 并非违规（规范为"应当优先"），不判定；
- 富依赖表达式：`(foo >= 1 with foo < 2)`、`foo with bar` 等写法声明的是单个依赖，属合法形式，不判定；
- 版本比较：`foo >= 1.2`、`foo = 1.29` 等带版本约束的写法仍为单个依赖，不判定；
- 宏展开：`%{...}` 等宏展开的依赖值无法静态解析，不判定；
- `%package` 子包段落内的 `BuildRequires`：该字段声明的是子包构建依赖，不属于本规则范围，不判定；
- 尾部空行分隔：各 `BuildRequires` 行之间、以及之后接 `Requirements` 等的空行，由其它规则覆盖，不判定。

**注意**：检查点 1、2 均为「必须」级要求（一行一个依赖、必须列出构建期
依赖）。任一违反即报告。富依赖表达式（`( ... )` 或 `with`/`without`）、
带版本约束的单个依赖、以及含宏的依赖值均视为单个依赖，不报告。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-buildrequires
```

也可独立运行：`check-spec-buildrequires path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
BuildSystem:    autotools
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(zlib)
```

```spec
BuildSystem:    cmake
BuildRequires:  cmake >= 3.4.3
BuildRequires:  python3dist(hatchling) = 1.29
BuildRequires:  (cmake(LLVM) >= 22 with cmake(LLVM) < 23)
```

### 不通过 ❌

```spec
BuildSystem:    autotools
BuildRequires:  automake autoconf
```
→ `BuildRequires must declare exactly one dependency per line (found "automake autoconf")`

```spec
BuildSystem:    autotools
BuildRequires:  libXaw-devel, libXmu-devel
```
→ `BuildRequires must declare exactly one dependency per line (found "libXaw-devel, libXmu-devel")`

```spec
BuildSystem:    autotools
BuildRequires:
```
→ `BuildRequires must list a build-time dependency (found empty value)`
