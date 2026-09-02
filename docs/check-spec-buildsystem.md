# check-spec-buildsystem

> 规则 ID：`check-spec-buildsystem`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-buildsystem-results.md](../openruyi-scan-results/check-spec-buildsystem-results.md)

## 原始需求

来源：[openRuyi 打包指南 · BuildSystem](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#buildsystem)

> 1. Spec 必须包含 `BuildSystem` 字段。
> 2. `BuildSystem` 的取值应当为以下之一（或其它新增的值）：
>    - `autotools`
>    - `cmake`
>    - `meson`
>    - `golang`
>    - `golangmodules`
>    - `pyproject`
> 3. 当软件包不适用上述类型或不需要配置阶段时，`BuildSystem` 可以为空，但必须以注释说明原因。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 取值合法 | `BuildSystem` 的取值应当为官方列出的构建系统之一（或其它新增的值） | 值不是已知构建系统即失败（提示可能是新增值） |
| 2 | 空值注释 | 当软件包不适用上述类型或不需要配置阶段时，`BuildSystem` 可以为空，但必须以注释说明原因 | 值为空且无说明原因的注释即失败 |

**跳过**（无法静态判定 / 由其它规则覆盖）：

- 字段缺失：`BuildSystem` 为必填字段，缺失由 `check-spec-structure` 规则覆盖，本规则不重复报告；
- 软件包是否真的需要配置阶段：需人工核对，不判定；
- `%package` 子包段落内的 `BuildSystem`：该字段声明的是子包构建系统，不属于本规则范围，不判定。

**注意**：检查点 1 为「应当」级要求（取值应当为已知构建系统或新增值），
检查点 2 为「必须」级要求（空值必须注释说明原因）。官方明确允许
「其它新增的值」，因此本规则将官方列出的 6 个构建系统与 openRuyi
仓库实际使用的 4 个扩展值（`perlbuild`、`perlmaker`、`rust`、
`rustcrates`）合并为已知值白名单；遇到白名单之外的值时报告，提示
维护者确认是否为新增构建系统。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.2.0   # 使用最新 tag
    hooks:
    -   id: check-spec-buildsystem
```

也可独立运行：`check-spec-buildsystem path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
BuildSystem:    autotools
```

```spec
BuildSystem:    pyproject
```

```spec
BuildSystem:    rustcrates
```

```spec
# 该软件包为纯数据包，不需要配置阶段
BuildSystem:
```

```spec
BuildSystem:    # 该软件包为纯数据包，不需要配置阶段
```

### 不通过 ❌

```spec
BuildSystem:
```
→ `BuildSystem is empty; the reason must be explained in a comment`

```spec
BuildSystem:    make
```
→ `BuildSystem must be one of the known build systems (...) or a newly added value (found "make")`
