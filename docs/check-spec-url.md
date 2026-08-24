# check-spec-url

> 规则 ID：`check-spec-url`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-url-results.md](../openruyi-scan-results/check-spec-url-results.md)

## 原始需求

来源：[openRuyi 打包指南 · URL](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#url)

> 1. `URL` 必须为软件包官方网站链接；若无官方网站，可以使用源代码仓库链接。
> 2. `URL` 字段中不得使用 `%{name}` 等宏进行拼接。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 不使用宏拼接 | `URL` 是固定的永久链接，不得用 `%{name}` 等宏在构建期拼接 | 值中出现 `%{...}` 宏即失败 |
| 2 | 合法链接形式 | 必须是 `http://` 或 `https://` 开头的官网或源码仓库链接 | 值不以 `http(s)://` 开头即失败（如 `FIXME` 占位符、裸主机名） |
| 3 | 官网/仓库判定 | 值应为软件包官方网站；无官网时可用源代码仓库链接 | 需联网验证与人工判断，静态单文件检查无法覆盖，不参与判定 |

**跳过**（无法静态判定）：

- 字段缺失或为空：由 `check-spec-structure` 规则覆盖，本规则不重复报告；
- `# URL:` 注释行：视为说明性文字，不判定；
- 链接是否确实是上游官网/规范源码仓库：需人工核对，不判定。

**注意**：检查点 1 为「不得」的强制性禁止，检查点 2 为 URL
字段的最基本合法性。两者均为「必须/不得」级要求，任一违反即报告。
`URL` 是否与 `Source` 前缀一致、是否指向真实可达的站点等语义问题
不在本规则静态检查范围内。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-url
```

也可独立运行：`check-spec-url path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
URL:            https://www.example.org/
```

```spec
URL:            https://github.com/foo/bar
```

```spec
URL:            http://example.org/project
```

```spec
# URL:            https://www.example.org/
```

### 不通过 ❌

```spec
URL:            https://github.com/mreineck/%{name}
```
→ `URL must not be built with macros such as %{name} (found "https://github.com/mreineck/%{name}")`

```spec
URL:            FIXME
```
→ `URL must be a valid http(s) website or source repository link (found "FIXME")`

```spec
URL:            www.example.org
```
→ `URL must be a valid http(s) website or source repository link (found "www.example.org")`