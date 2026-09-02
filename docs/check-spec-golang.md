# check-spec-golang

> 规则 ID：`check-spec-golang`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-golang-results.md](../openruyi-scan-results/check-spec-golang-results.md)

## 原始需求

来源 1：[openRuyi 打包指南 · 构建系统 · Golang](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems/golang)

> 如需要使用 `golang` 或 `golangmodules` 构建系统，那么需要添加这些 `BuildRequires`。
>
> ```spec
> BuildRequires:  go
> BuildRequires:  go-rpm-macros
> ```

来源 2：[openRuyi 打包指南 · 编程语言 · Golang](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/languages/Golang)（依赖关系章节）

> 库软件包本身必须要显式在 RPM Spec 内写出自己提供的导入路径和版本，例如：
>
> ```spec
> Provides:       go(github.com/clipperhouse/uax29/v2) = %{version}
> ```

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 声明必需依赖 | `BuildSystem: golang` 或 `BuildSystem: golangmodules` 的 spec 必须在 `BuildRequires` 中声明 `go`、`go-rpm-macros` | 头部区域 `BuildRequires` 缺失其中任意一项，即失败 |
| 2 | 库包声明自身导入路径 | `BuildSystem: golangmodules` 的纯库 spec 必须声明至少一条 `Provides: go(<import path>)` | 头部或 `%package` 子包块内没有任何 `Provides: go(...)`，即失败 |
| 3 | 提供了版本 | 每条 `Provides: go(<import path>)` 必须带显式版本约束 `= <version>` | 存在 `Provides: go(...)` 但未在行内写出 `= <version>`，即失败 |

**说明**：

- 本规则同时覆盖 `golang` 与 `golangmodules` 两个构建系统值；
- 与 cmake/autotools 指南不同，golang 页面**未提及** `gcc` 等
  预装工具豁免，因此 `go` 与 `go-rpm-macros` 均为必需声明；
- 检查点 1 只要求**存在声明**，不限制声明顺序、是否带版本约束；
  "一行一个依赖包"的书写格式由 `check-spec-buildrequires` 规则覆盖；
- 检查点 2 依据：`golangmodules` 构建系统文档描述为「仅打包库」
  （无需编译，内置 `%install`/`%check`），因此使用该构建系统的
  spec 即为库包，必须提供自身的 `go()` 虚拟依赖；
- 检查点 3 依据：指南原文「写出自己提供的导入路径**和版本**」，
  示例为 `Provides: go(...) = %{version}`；真实 SPECS 库中
  `%package` 子包块内的多版本 `Provides: go(...) = <version>`（如
  `go-golang-x-oauth2` 的 google 子包）同样带版本，均为合法；
- `Provides` 收集范围：头部区域与全部 `%package` 子包块
  （`%files`/`%description`/`%changelog`/脚本段等内容不检查）。

**跳过**（无法静态判定 / 由其它规则覆盖 / 建议性要求）：

- `BuildSystem` 字段缺失：为必填字段，由 `check-spec-structure` 规则覆盖；
- 非 `golang` / `golangmodules` 构建系统的 spec：本规则不适用，不检查；
- `golang` 构建系统且为纯二进制包（如 `ollama`）：不要求
  `Provides: go(...)`（仅 `golangmodules` 视为库包）；
- 头部定义 `_name` 与 `go_import_path` 宏：文档措辞为「至少应该」，
  属建议性要求，未纳入强检查点；
- 跨构建系统宏调用（`%go_common`、`%buildsystem_golangmodules_install`、
  `%install -a`）：取决于最终产物形态（二进制/库），无法静态判定，
  不在本规则范围内；
- 二进制包命名禁 `go-` 前缀、库文件装至 `/usr/share/gocode`、
  多版本 `Conflicts` 互斥：属建议性/需要上游知识，未纳入强检查点；
- `BuildOption(prep)` / `BuildOption(check)` 示例：由
  `check-spec-buildoption` 规则覆盖。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.2.0   # 使用最新 tag
    hooks:
    -   id: check-spec-golang
```

也可独立运行：`check-spec-golang path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
BuildSystem:    golang
BuildRequires:  go
BuildRequires:  go-rpm-macros
```

```spec
BuildSystem:    golangmodules
BuildRequires:  go >= 1.21
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
```

（`go(...)` 虚拟依赖等额外声明不影响判定）

### 不通过 ❌

```spec
BuildSystem:    golangmodules
BuildRequires:  go
```

→ `BuildSystem is golangmodules; BuildRequires must declare go-rpm-macros`

```spec
BuildSystem:    golang
BuildRequires:  zlib-devel
```

→ `BuildSystem is golang; BuildRequires must declare go, go-rpm-macros`
