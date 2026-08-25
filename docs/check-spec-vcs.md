# check-spec-vcs

> 规则 ID：`check-spec-vcs`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-vcs-results.md](../openruyi-scan-results/check-spec-vcs-results.md)

## 原始需求

来源：[openRuyi 打包指南 · VCS](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#vcs)

> `VCS` 字段用于指向源码版本控制仓库，帮助定位源码并支持自动化构建与追溯。

补充说明：若 `URL:` 字段已经完整地指向源码仓库，则在某些情况下 `VCS:` 可以省略；但通常 `VCS:` 应明确给出指向源码仓库的可克隆地址或显式说明无 VCS。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | `VCS` 字段存在性 | 当 `URL` 未指向源码仓库时，应在 Spec 中提供 `VCS:` 字段指向源码仓库 | 缺少 `VCS:` 且 `URL` 不指向源码仓库时报告 |
| 2 | 允许的占位 | 若确实无仓库可用，应在 `VCS` 字段处以注释形式保留前缀 `# VCS:` 并写 `No VCS link available` | 非注释或注释内容不匹配 `# VCS: No VCS link available` 时报告 |
| 3 | Git 可克隆链接形式建议 | 对于 Git 托管，建议使用可克隆形式（例如 `git:https://.../.git`）或标准 HTTPS/SCP 可克隆地址 | 明显的非仓库 URL（如指向 release 页面或文件 blob 链接）时报错 |
| 4 | 宏展开跳过 | 含 `%{...}` 宏展开的 `VCS` 值跳过检查以避免误报 | 含宏的值不判定、不报告 |
| 5 | 格式健全性 | 基本的 URL/SCHEME 校验（例如不得只写 `blob/` 或 `tree/` 等引用） | 明显非仓库引用（包含 `blob/`、`tree/`、`raw` 等路径）即报告 |

**跳过**（无法静态判定或由其它规则覆盖）：

- 含宏展开的 `VCS` 值（如 `%{vcs}`）不参与判定；
- 字段缺失或文件结构问题由 `check-spec-structure` 规则检测，本规则不重复报告；

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-vcs
```

也可独立运行：`check-spec-vcs path/to/foo.spec`。
返回码：0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
VCS:            git:https://git.example.org/project.git
```

```spec
# VCS: No VCS link available
```

```spec
URL:            https://github.com/example/project
# VCS 可省略（当 URL 明确指向源码仓库时）
```

### 不通过 ❌

```spec
VCS:            https://github.com/example/project/blob/main/SPECS/foo/foo.spec
```
→ `VCS must point to a repository clone URL, not a blob/tree reference`。

```spec
VCS:            http://example.com/downloads/release-1.2.tar.gz
```
→ `VCS should point to a VCS repository, not an archive or release download`。

```spec
VCS:            %{vcs}
```
→ `Skipped (macro-expanded value)`。

## 实现

规则实现位于 `openruyi_precommit_hooks/check_spec_vcs.py`，在含有 `SPECS/` 工作树的环境中可运行：

```bash
python -m openruyi_precommit_hooks.check_spec_vcs SPECS/**/*.spec
```

当把规则集成到 `pre-commit` 时，请在 `.pre-commit-hooks.yaml` 中声明对应 hook 元数据并在 `README.md` 的 Hooks 列表中同步更新链接。
