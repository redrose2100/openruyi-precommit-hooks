# check-spec-structure

> 规则 ID：`check-spec-structure`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-structure-results.md](../openruyi-scan-results/check-spec-structure-results.md)

## 原始需求

来源：[openRuyi 打包指南 · 基础字段与段落](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#%E5%9F%BA%E7%A1%80%E5%AD%97%E6%AE%B5%E4%B8%8E%E6%AE%B5%E8%90%BD)

> Spec 必须包含以下字段与段落，且应当按如下顺序出现：
>
> ```specfile
> Name:
> Version:
> Release:
> Summary:
> License:
> URL:
> VCS:
> Source:
> BuildSystem:
>
> BuildRequires:
>
> Requires:
>
> %description
>
> %files
>
> %changelog
> ```
>
> 其他情况可以按照 A-Z 的顺序排列。
>
> 段落与段落之间必须用空行隔开。

## 检查点

### 1. 头部字段

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 字段完整性 | 主包头部（第一个 `%description` 之前）必须包含 `Name` / `Version` / `Release` / `Summary` / `License` / `URL` / `VCS` / `Source` / `BuildSystem` / `BuildRequires` / `Requires` 全部 11 个字段；**例外**：若 `URL` 已为源代码仓库链接，则 `VCS` 可以省略 | 任一字段缺失即失败（`VCS` 在 `URL` 为源码仓库链接时可豁免） |
| 2 | 字段顺序 | 上述字段必须按上述顺序出现（其他情况可以按照 A-Z 的顺序排列） | 字段顺序不对即失败 |
| 3 | 变体与延续 | `Source` 匹配 `Source0` / `Source1` 等变体；`BuildRequires` / `Requires` 允许多行延续，以首次出现位置参与顺序比较 | 不参与判定 |

> **`VCS` 豁免规则**：当 `URL` 字段的值指向源代码仓库时，`VCS` 可以省略（见[打包指南 · VCS](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#vcs)）。判定为"源代码仓库链接"的情形：
>
> - 以 `git:` 协议前缀开头（如 `git:https://example.org/foo.git`）；
> - 以 `.git` 结尾（可克隆链接）；
> - 托管在已知源码托管平台：`github.com`、`gitlab.com`、`gitlab.*`、`git.*`、`codeberg.org`、`bitbucket.org`、`git.sr.ht`、`hg.sr.ht`、`invent.kde.org`、`salsa.debian.org`、`pagure.io`、`code.videolan.org`、`src.fedoraproject.org` 等。
>
> 若 `URL` 为普通官方网站（如 `https://example.com`、`https://metacpan.org/dist/foo`），则 `VCS` 仍为必填。

### 2. 段落空行

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 段落分隔 | `%description` / `%package` / `%prep` / `%build` / `%install` / `%check` / `%files` / `%changelog` 段落之间必须用空行隔开 | 段落之间无空行即失败 |
| 2 | 段落带参数 | 段落标签可带参数（如 `%description devel`、`%files -f %{name}.lang`），同样参与检查 | 与序号 1 相同 |
| 3 | 条件块 | `%if` / `%endif` 条件块后紧跟段落是 RPM 合法写法 | 不判违规 |

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.2.0   # 使用最新 tag
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

### 通过 ✅（`URL` 为源码仓库链接，`VCS` 可省略）

```spec
Name:           foo
Version:        1.0.0
Release:        %autorelease
Summary:        A test package
License:        MIT
URL:            https://github.com/example/foo
Source0:        https://github.com/example/foo/archive/refs/tags/v%{version}.tar.gz
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

- 缺少 `VCS` 且 `URL` 为普通官方网站（如 `https://example.com`）→ `missing required header field(s): VCS`
- 字段乱序（如 `Summary` 与 `Release` 颠倒）→ `header fields out of order`
- `Requires:` 后直接跟 `%description`（段落前无空行）→ 段落空行检查失败
- 文件为空或非 UTF-8 编码 → 失败
