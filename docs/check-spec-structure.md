# check-spec-structure

> 规则 ID：`check-spec-structure`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-structure-results.md](../openruyi-scan-results/check-spec-structure-results.md)

## 规则

### 1. 头部字段

主包头部（第一个 `%description` 之前）**必须**包含以下全部字段，且按此顺序出现。
任一字段缺失或顺序不对即失败：

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

> `Source` 匹配 `Source0` / `Source1` 等变体；`BuildRequires` / `Requires`
> 允许多行延续，以首次出现位置参与顺序比较。

### 2. 段落空行

`%description` / `%package` / `%prep` / `%build` / `%install` / `%check` /
`%files` / `%changelog` 段落之间必须用空行隔开。段落标签可带参数
（如 `%description devel`、`%files -f %{name}.lang`），同样参与检查；
`%if` / `%endif` 条件块后紧跟段落是 RPM 合法写法，不判违规。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-structure
```

也可独立运行：`check-spec-structure path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

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

%files
%{_bindir}/foo

%changelog
%autochangelog
```

### 不通过 ❌

以此通过示例为基础，以下任一改动都会失败：

- 缺少 `VCS`（11 个字段缺一不可）→ `missing required header field(s): VCS`
- 字段乱序（如 `Summary` 与 `Release` 颠倒）→ `header fields out of order`
- `Requires:` 后直接跟 `%description`（段落前无空行）→ 段落空行检查失败
- 文件为空或非 UTF-8 编码 → 失败
