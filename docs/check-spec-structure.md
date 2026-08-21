# check-spec-structure

> 规则 ID：`check-spec-structure`

## 规则说明

Spec 文件（RPM `.spec`）的主包头部字段与段落布局必须保持规范的结构，便于
维护与自动化解析。

本规则包含两个检查点：

1. **检查点 1**：Spec **必须**包含以下字段与段落，且应当按如下顺序出现；
2. **检查点 2**：段落（`%description` / `%files` / `%changelog` / `%package` /
   `%prep` / `%build` / `%install` / `%check`）之间必须用空行隔开。

## 检查点 1：头部字段顺序

主包头部（第一个 `%description` 段落之前）中，以下字段**若出现则必须按此顺序**
排列：

```spec
Name:
Version:
Release:
Summary:
License:
URL:
VCS:
Source:
BuildSystem:
BuildRequires:
Requires:
```

| 字段 | 说明 |
| --- | --- |
| `Name` / `Version` / `Release` / `Summary` / `License` | 基本标识字段，通常全部出现 |
| `URL` / `VCS` / `Source` | 上游与源代码来源；`VCS` 仅在使用版本控制仓库作为源码来源时出现 |
| `BuildSystem` | 构建系统，openRuyi 扩展字段 |
| `BuildRequires` / `Requires` | 构建与运行时依赖，可有多行（多行视为同一字段的延续） |

校验规则：

- 每个字段**允许缺失**——例如不通过 VCS 获取源码的包可以没有 `VCS` 字段
  （openRuyi 中约 82% 的 spec 没有 `VCS`，属正常情况）；
- 字段**若出现则必须按上述顺序**，出现顺序违反则报错；
- `Source` 匹配 `Source`/`Source0`/`Source1`/`SourceN` 等所有变体；
- `BuildRequires` 与 `Requires` 允许多行，以首次出现位置参与顺序比较。

违反示例：`Version` 出现在 `Summary` 之后、或 `Summary` 出现在 `License` 之后。

## 检查点 2：段落之间的空行

以下段落之间必须用**至少一个空行**隔开：

```spec
%description
%package
%prep
%build
%install
%check
%files
%changelog
```

校验规则：

- 段落标签可携带参数（如 `%description devel`、`%package -n foo`、
  `%files -f %{name}.lang`），同样参与检查；
- 段落标签**前一非注释行**必须是空行或另一结构指令（`%if`/`%else`/`%endif`
  等条件指令或另一段落标签）；
- `%if`/`%endif` 条件块后紧跟段落是 RPM 合法写法，不判违规；
- `%{...}` 宏展开与 `%find_lang` 等宏调用是内容行，段落前必须有空行。

## 检查内容

对每个 `.spec` 文件，本规则检查：

1. 主包头部（第一个 `%description` 之前）中出现的字段是否按
   `Name → Version → Release → Summary → License → URL → VCS → Source →
   BuildSystem → BuildRequires → Requires` 顺序排列。
2. 每行段落标签（`%description`/`%package`/`%prep`/`%build`/`%install`/
   `%check`/`%files`/`%changelog` 及其带参数变体）之前是否有空行分隔。

以下情况会被判定为**失败**：

- 出现字段乱序；
- 段落前缺少空行（前一行是字段内容、文件列表或脚本内容）；
- 文件不是 UTF-8 编码；
- 文件为空。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-structure
```

也可以作为独立命令使用：

```console
$ check-spec-structure path/to/foo.spec
```

返回码为 1 表示有文件不满足要求，0 表示全部通过。

## 示例

### 通过 ✅

```spec
Name:           foo
Version:        1.0.0
Release:        %autorelease
Summary:        A test package
License:        MIT
URL:            https://example.com
VCS:            git:https://github.com/example/foo
Source0:        https://example.com/foo-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc

Requires:       glibc

%description
This is a test package.

%prep
%autosetup

%build
%make_build

%install
%make_install

%check
%make_test

%files
%{_bindir}/foo

%changelog
%autochangelog
```

### 不通过 ❌（字段乱序）

```spec
Name:           foo
Summary:        A test package
Version:        1.0.0
Release:        %autorelease
License:        MIT

%description
This is a test package.

%files
%{_bindir}/foo

%changelog
%autochangelog
```

`Version` 出现在 `Summary` 之后，违反字段顺序。

### 不通过 ❌（段落前缺少空行）

```spec
Name:           foo
Version:        1.0.0
Release:        %autorelease
Summary:        A test package
License:        MIT

BuildRequires:  gcc
%description
This is a test package.

%files
%{_bindir}/foo

%changelog
%autochangelog
```

`%description` 前一行是 `BuildRequires:` 内容而非空行，违反段落空行要求。

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) `main`
分支的扫描结果见 [check-spec-structure-results](../openruyi-scan-results/check-spec-structure-results.md)。
