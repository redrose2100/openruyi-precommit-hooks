# check-spec-requires

> 规则 ID：`check-spec-requires`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-requires-results.md](../openruyi-scan-results/check-spec-requires-results.md)

## 原始需求

来源：[openRuyi 打包指南 · Requires / Provides / Conflicts / Obsoletes](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#requires--provides--conflicts--obsoletes-%E5%8F%AF%E9%80%89)

> 1. `Requires` 用于列出运行期依赖；依赖项必须按"一行一个依赖包"的形式书写。

排版与可读性：

> `BuildRequires` 与 `Requires` 必须采用"一行一个依赖"的形式。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 一行一个依赖 | `Requires` 依赖项必须按"一行一个依赖包"的形式书写 | 一行中出现多个依赖包（如逗号分隔 `a, b` 或空格分隔 `a b`）即失败 |
| 2 | 值非空 | `Requires` 必须列出运行期依赖 | 写成 `Requires:`（空值）即失败 |

**跳过**（无法静态判定或不属于本规则）：

- 字段缺失：`Requires` 为必填头部字段，缺失由 `check-spec-structure` 规则覆盖，本规则不重复报告；
- 子包段落：`%package` 子包内的 `Requires` 声明的是该子包的运行期依赖，同样按"一行一个依赖"检查（与 `BuildRequires` 不同，后者在子包内声明的是子包构建依赖，属于其它范围，不判定）；
- scriptlet 变体：`Requires(pre):` / `Requires(post):` / `Requires(preun):` / `Requires(postun):`（以及罕见的 `Requires(meta):` / `Requires(posttrans):`）声明的是特定脚本段或元数据角色的依赖，不属于 `Requires` 运行期依赖规则，不判定；
- 富依赖表达式：`(foo >= 1 with foo < 2)`、`foo with bar` 等写法声明的是单个依赖，属合法形式，不判定；
- 版本比较：`foo >= 1.2`、`foo = 1.29` 等带版本约束的写法仍为单个依赖，不判定；
- 宏展开：`%{...}` 等宏展开的依赖值无法静态解析，不判定。

**注意**：检查点 1、2 均为「必须」级要求（一行一个依赖、必须列出运行期
依赖）。任一违反即报告。富依赖表达式（`( ... )` 或 `with`/`without`）、
带版本约束的单个依赖、以及含宏的依赖值均视为单个依赖，不报告。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-requires
```

也可独立运行：`check-spec-requires path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
BuildSystem:    autotools
Requires:       gcc
Requires:       make
Requires:       pkgconfig(zlib)
```

```spec
BuildSystem:    cmake
Requires:       cmake >= 3.4.3
Requires:       python3dist(hatchling) = 1.29
Requires:       (cmake(LLVM) >= 22 with cmake(LLVM) < 23)
```

```spec
%package        devel
Summary:        Development files for %{name}
Requires:       libfoo-devel
Requires:       libbar-devel
```

### 不通过 ❌

```spec
BuildSystem:    autotools
Requires:       automake autoconf
```
→ `Requires must declare exactly one dependency per line (found "automake autoconf")`

```spec
BuildSystem:    autotools
Requires:       libXaw-devel, libXmu-devel
```
→ `Requires must declare exactly one dependency per line (found "libXaw-devel, libXmu-devel")`

```spec
BuildSystem:    autotools
Requires:
```
→ `Requires must list a runtime dependency (found empty value)`
