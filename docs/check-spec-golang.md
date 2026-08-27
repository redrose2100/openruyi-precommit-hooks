# check-spec-golang

> 规则 ID：`check-spec-golang`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-golang-results.md](../openruyi-scan-results/check-spec-golang-results.md)

## 原始需求

来源：[openRuyi 打包指南 · 构建系统 · Golang](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems/golang)

> 如需要使用 `golang` 或 `golangmodules` 构建系统，那么需要添加这些 `BuildRequires`。
>
> ```spec
> BuildRequires:  go
> BuildRequires:  go-rpm-macros
> ```

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 声明必需依赖 | `BuildSystem: golang` 或 `BuildSystem: golangmodules` 的 spec 必须在 `BuildRequires` 中声明 `go`、`go-rpm-macros` | 头部区域 `BuildRequires` 缺失其中任意一项，即失败 |

**说明**：

- 本规则同时覆盖 `golang` 与 `golangmodules` 两个构建系统值；
- 与 cmake/autotools 指南不同，golang 页面**未提及** `gcc` 等
  预装工具豁免，因此 `go` 与 `go-rpm-macros` 均为必需声明；
- 检查点只要求**存在声明**，不限制声明顺序、是否带版本约束；
  "一行一个依赖包"的书写格式由 `check-spec-buildrequires` 规则覆盖。

**跳过**（无法静态判定 / 由其它规则覆盖 / 建议性要求）：

- `BuildSystem` 字段缺失：为必填字段，由 `check-spec-structure` 规则覆盖；
- 非 `golang` / `golangmodules` 构建系统的 spec：本规则不适用，不检查；
- 头部定义 `_name` 与 `go_import_path` 宏：文档措辞为「至少应该」，
  属建议性要求，未纳入强检查点；
- 跨构建系统宏调用（`%go_common`、`%buildsystem_golangmodules_install`、
  `%install -a`）：取决于最终产物形态（二进制/库），无法静态判定，
  不在本规则范围内；
- `BuildOption(prep)` / `BuildOption(check)` 示例：由
  `check-spec-buildoption` 规则覆盖。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
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
