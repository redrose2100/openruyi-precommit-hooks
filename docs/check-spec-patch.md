# check-spec-patch

> 规则 ID：`check-spec-patch`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-patch-results.md](../openruyi-scan-results/check-spec-patch-results.md)

## 原始需求

来源：[openRuyi 打包指南 · Patch and %patchlist (可选)](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#patch-and-patchlist-%E5%8F%AF%E9%80%89)

> 1. Spec 中引用的每个补丁必须在其上方提供至少一行注释，说明补丁用途或给出上游链接；补丁内已经说明的除外。
> 2. 补丁文件名必须以四位数字开头，并按以下范围表达补丁类型：
>    - `0001–0999`: 同一版本 upstream 补丁
>    - `1000–1999`: CVE 修复或跨版本 backport 补丁
>    - `2000–2999`: openRuyi 特有补丁 (预期不进入 upstream)
> 3. 当 patch 数量大于 3 时，Spec 应当使用 `%patchlist`，且列表必须放置于 `%description` 之上。
> 4. Patch 的放置顺序：
>    - 当 Spec 含 `BuildOption` 字段时，Patch 应当位于 `BuildSystem` 与 `BuildOption` 之间。
>    - 当 Spec 不含 `BuildOption` 字段时，Patch 应当位于 `BuildSystem` 与 `BuildRequires` 之间。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 补丁上方注释 | 每个补丁上方必须提供至少一行注释，说明用途或给出上游链接 | `Patch:` 字段或 `%patchlist` 条目上方无注释行即失败 |
| 2 | 补丁文件名前缀 | 补丁文件名必须以四位数字开头，且范围表达补丁类型（`0001–0999` upstream、`1000–1999` CVE/backport、`2000–2999` openRuyi 特有） | 文件名不以四位数字开头、或前缀不在 `0001–2999` 范围内即失败 |
| 3 | `%patchlist` 使用 | 当 patch 数量大于 3 时，应当使用 `%patchlist` | 存在 4 个及以上 `Patch:` 字段但未使用 `%patchlist` 即失败 |
| 4 | `%patchlist` 位置 | `%patchlist` 列表必须放置于 `%description` 之上 | `%patchlist` 位于 `%description` 之下即失败 |
| 5 | Patch 放置顺序 | 含 `BuildOption` 时 Patch 位于 `BuildSystem` 与 `BuildOption` 之间；不含时位于 `BuildSystem` 与 `BuildRequires` 之间 | `Patch:` 字段位于 `BuildSystem` 之前、或位于锚点字段（`BuildOption`/`BuildRequires`）之后即失败 |

**跳过**（无法静态判定）：

- 字段缺失：`Patch` 与 `%patchlist` 为可选字段，缺失不报告；
- 补丁用途是否已在补丁文件内部说明：需人工核对，不判定；
- `%package` 子包段落内的 `Patch`：该字段属于子包上下文，不属于本规则范围，不判定；
- 缺少 `BuildSystem` 或锚点字段（`BuildOption`/`BuildRequires`）时：放置顺序无法判定，仅校验其它检查点。

**注意**：检查点 1、2 为「必须」级要求（补丁上方必须有注释、文件名必须四位数字前缀），
检查点 3、4、5 为「应当」级要求（>3 个补丁用 `%patchlist`、`%patchlist` 在
`%description` 之上、Patch 位于 `BuildSystem` 与锚点之间）。任一违反即报告。
补丁内容是否真的与用途一致等语义问题不在本规则静态检查范围内。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-patch
```

也可独立运行：`check-spec-patch path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
BuildSystem:    autotools
# Fix build with gcc 16
Patch0:         0001-fix-build.patch
# https://github.com/foo/foo/pull/123
Patch1:         0002-upstream-fix.patch
BuildRequires:  gcc
```

```spec
BuildSystem:    autotools
%patchlist
# Fix build with gcc 16
0001-fix-build.patch
# https://github.com/foo/foo/pull/123
0002-upstream-fix.patch

%description
A test package.
```

### 不通过 ❌

```spec
BuildSystem:    autotools
Patch0:         0001-fix-build.patch
BuildRequires:  gcc
```
→ `Patch "0001-fix-build.patch" must have a comment line above it explaining its purpose or giving an upstream link`

```spec
BuildSystem:    autotools
# Fix build
Patch0:         fix-build.patch
BuildRequires:  gcc
```
→ `patch file name "fix-build.patch" must start with a four digit number (0001-0999, 1000-1999, 2000-2999)`

```spec
BuildSystem:    autotools
# Fix build
Patch0:         3000-fix-build.patch
BuildRequires:  gcc
```
→ `patch file name "3000-fix-build.patch" must start with a four digit number in one of the ranges (0001-0999, 1000-1999, 2000-2999)`

```spec
BuildSystem:    autotools
# c1
Patch0:         0001-a.patch
# c2
Patch1:         0002-b.patch
# c3
Patch2:         0003-c.patch
# c4
Patch3:         0004-d.patch
BuildRequires:  gcc
```
→ `more than 3 patches should use %patchlist (found 4 Patch fields)`

```spec
BuildSystem:    autotools
BuildRequires:  gcc

%description
A test package.

%patchlist
# Fix build
0001-fix-build.patch
```
→ `%patchlist must be placed above %description`

```spec
BuildSystem:    autotools
BuildOption(build):  OPT="%{optflags}"
# Fix build
Patch0:         0001-fix-build.patch
BuildRequires:  gcc
```
→ `Patch must be located between BuildSystem and BuildOption`
