# check-spec-source

> 规则 ID：`check-spec-source`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-source-results.md](../openruyi-scan-results/check-spec-source-results.md)

## 原始需求

来源：[openRuyi 打包指南 · Source](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#source)

> 1. `Source` 必须提供上游源码（或等价可重现的源码归档）的获取位置。
> 2. 若 `URL` 可以复用为 `Source` 的前缀，`Source` 可以使用 `%{url}` 复用 `URL`。
> 3. 对于网络来源的 `Source`，其行前必须添加
>    `#!RemoteAsset` 注释；存在多条网络来源 `Source`
>    时，每条均必须标识。
> 4. 对于 HTTP 和 HTTPS 协议来源的 `Source`，在
>    `#!RemoteAsset` 注释后，必须添加来源文件的 sha256
>    值（可用 remoteassetify 自动生成）。
> 5. 对于无法从 URL 解析出 tarball 文件名的情形，
>    `Source` 应当使用 URL 片段显式给出 tarball 名称。
> 6. `Source` 编号规则：默认编号为 `0`，每增加一条递增
>    1；若仅有一条源代码文件，编号可以省略。

补充：[openRuyi 打包指南 · SourceURL 规范](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/SourceURL)

> - SourceForge 项目必须使用 `downloads.sourceforge.net`
>   下载域名（不能使用 `download.sourceforge.net` 或任意
>   镜像），否则会触发任意重定向。
> - `#!RemoteAsset` 前缀 + `#!CreateArchive` 注释。
> - 复用 URL 示例：`Source: %{url}/archive/refs/tags/%{version}.tar.gz`。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 网络来源标记 | 以 `http://` / `https://` / `%{url}` 开头的网络来源 `Source`，其紧邻上一行必须为 `#!RemoteAsset` 注释 | 网络来源缺前置 `#!RemoteAsset` 注释即失败 |
| 2 | sha256 校验值 | HTTP(S) 来源的 `#!RemoteAsset` 注释必须携带 `sha256:...` 校验值（64 位十六进制） | `#!RemoteAsset` 无校验值、或校验值不是合法的 64 位 `sha256:` 格式即失败 |
| 3 | SourceForge 域名 | SourceForge 下载链接必须使用 `downloads.sourceforge.net` 主机 | 使用 `download.sourceforge.net` / `prdownloads.sourceforge.net` / `sourceforge.net/projects/...` 即失败 |
| 4 | 本地文件来源 | 本地文件（非网络）`Source` 不需要 `#!RemoteAsset` 注释 | 本地文件来源无注释合法，不判定 |
| 5 | URL 片段命名 | 无法从 URL 解析 tarball 文件名时，`Source` 应使用 URL 片段显式给出名称 | 需人工核对 URL 与实际 tarball 名称，静态不判定 |
| 6 | 编号规则 | 默认编号 `0` 起递增；仅一条时可省略 | 需完整解析条件块与宏，静态不判定 |

**跳过**（无法静态判定）：

- 字段缺失或为空：由 `check-spec-structure` 规则覆盖，本规则不重复报告；
- 本地文件 `Source`（不以 `http(s)://` 或 `%{url}` 开头）：不要求 `#!RemoteAsset`；
- `git+` / `git:` 形式：在 `#!RemoteAsset` 中记录仓库与 commit 引用，不要求 sha256；
- `# Source:` 注释行：视为说明性文字，不判定；
- 检查点 5、6 的语义判断（tarball 名称解析、条件块内编号）：静态无法可靠覆盖。

**注意**：检查点 1 为「必须」级强制要求，检查点 2 为「必须携带 sha256」
的强制要求，检查点 3 为 SourceForge 域名的强制要求。三者任一违反即报告。
`#!RemoteAsset` 注释必须紧跟在该 `Source` 行上一行，中间插入空行或其它
注释视为缺失。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-source
```

也可独立运行：`check-spec-source path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
#!RemoteAsset:  sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Source:         https://www.apache.org/dist/apr/%{name}-%{version}.tar.bz2
```

```spec
#!RemoteAsset:  sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Source0:        https://ftpmirror.gnu.org/gnu/autoconf/autoconf-%{version}.tar.xz
#!RemoteAsset:  sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Source1:        https://ftpmirror.gnu.org/gnu/autoconf/autoconf-%{version}.tar.xz.sig
```

```spec
Source:         %{name}-%{version}.tar.gz
```

```spec
#!RemoteAsset:  git+https://aomedia.googlesource.com/aom#v%{version}
#!CreateArchive
Source:         %{name}-%{version}.tar.gz
```

```spec
#!RemoteAsset:  sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Source:         %{url}/archive/refs/tags/%{version}.tar.gz
```

### 不通过 ❌

```spec
#!RemoteAsset
Source:         https://www.apache.org/dist/apr/%{name}-%{version}.tar.bz2
```
→ `#!RemoteAsset comment of an http(s) Source must carry a sha256 checksum (found "https://www.apache.org/dist/apr/%{name}-%{version}.tar.bz2")`

```spec
Source:         http://audiofile.68k.org/audiofile-%{version}.tar.gz
```
→ `Source obtained over the network must be preceded by a #!RemoteAsset comment (found "http://audiofile.68k.org/audiofile-%{version}.tar.gz")`

```spec
#!RemoteAsset:  sha256:1234
Source:         https://example.org/foo-%{version}.tar.gz
```
→ `#!RemoteAsset comment of an http(s) Source must carry a sha256 checksum (found "https://example.org/foo-%{version}.tar.gz")`

```spec
#!RemoteAsset:  sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Source:         http://download.sourceforge.net/openjade/openjade-%{version}.tar.gz
```
→ `Source with a sourceforge.net link must use downloads.sourceforge.net (found "http://download.sourceforge.net/openjade/openjade-%{version}.tar.gz")`
