# check-spec-vcs

> 规则 ID：`check-spec-vcs`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-vcs-results.md](../openruyi-scan-results/check-spec-vcs-results.md)

## 原始需求

来源：[openRuyi 打包指南 · VCS](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#vcs)

> 1. `VCS` 应当为源代码仓库链接，用于定位源代码位置。
> 2. 若 `URL` 已为源代码仓库链接，则 `VCS` 可以省略。
> 3. 若不存在可用的源代码仓库链接，则必须在 `VCS` 字段位置写入以下注释（`# VCS:` 前缀必须保留）：
>
>    ```spec
>    # VCS: No VCS link available
>    ```
>
> 4. 当源代码托管于 Git 仓库时，`VCS` 应当使用可克隆链接，例如：
>
>    ```spec
>    VCS:            git:https://git.example.org/project.git
>    ```

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 可克隆链接 | `VCS` 为源代码仓库链接，用于定位源代码位置；Git 仓库应使用可克隆链接（`git:` 前缀，或指向已知源码托管平台的 http(s) 链接） | 值不以 `git:` 开头、也不是指向已知源码托管平台（github.com、gitlab.*、git.*、codeberg.org 等）的 http(s) 链接即失败（如 `FIXME` 占位符、裸主机名、`ftp://` 链接） |
| 2 | 无链接注释 | 不存在可用源码仓库链接时，必须在 `VCS` 字段位置写入 `# VCS: No VCS link available`（`# VCS:` 前缀必须保留） | `# VCS:` 注释内容不是精确的 `No VCS link available` 即失败 |
| 3 | 不使用宏拼接 | `VCS` 是固定的永久链接，不得用 `%{name}` 等宏在构建期拼接 | 值中出现 `%{...}` 宏即失败 |
| 4 | URL 已为仓库时省略 | 若 `URL` 已为源代码仓库链接，则 `VCS` 可以省略 | 由 `check-spec-structure` 规则覆盖，本规则不重复报告 |

**跳过**（无法静态判定）：

- 字段缺失或为空：由 `check-spec-structure` 规则覆盖，本规则不重复报告（`URL` 已为源码仓库链接时 `VCS` 可省略）；
- 链接是否确实是上游规范源码仓库：需人工核对，不判定；
- 链接是否真实可达、可克隆：需联网验证，不判定。

**注意**：检查点 1 为「应当」级要求，检查点 2 为「必须」级要求。
检查点 2 是强制性禁止（`# VCS:` 注释必须精确匹配），检查点 1 是
推荐性要求（Git 仓库应使用可克隆链接）。两者任一违反即报告。
`VCS` 是否与 `Source` 前缀一致、是否指向真实可达的仓库等语义问题
不在本规则静态检查范围内。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.2.0   # 使用最新 tag
    hooks:
    -   id: check-spec-vcs
```

也可独立运行：`check-spec-vcs path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
VCS:            git:https://git.example.org/project.git
```

```spec
VCS:            https://github.com/foo/bar
```

```spec
# VCS: No VCS link available
```

### 不通过 ❌

```spec
VCS:            FIXME
```
→ `VCS must be a cloneable source repository link (git: scheme or http(s) link to a source-code hosting platform) (found "FIXME")`

```spec
VCS:            git.example.org/project.git
```
→ `VCS must be a cloneable source repository link (git: scheme or http(s) link to a source-code hosting platform) (found "git.example.org/project.git")`

```spec
VCS:            git:https://git.example.org/%{name}.git
```
→ `VCS must not be built with macros such as %{name} (found "git:https://git.example.org/%{name}.git")`

```spec
# VCS: no repository available
```
→ `VCS comment must be exactly "# VCS: No VCS link available" (found "# VCS: no repository available")`
