# check-spec-version

> 规则 ID：`check-spec-version`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-version-results.md](../openruyi-scan-results/check-spec-version-results.md)

## 原始需求

来源：[openRuyi 打包指南 · Version](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#version)

> `Version` 字段用来定义软件包的版本。上游版本号需要按以下规则规范化后才
> 能写入 `Version` 字段：
>
> 1. 版本号只带有半角句号（`.`）时，可直接使用上游的版本号（如
>    `1.5.7` → `1.5.7`）。
> 2. 版本号带有发布阶段标记（`alpha`、`beta`、`rc`）时，将字母转为小写，
>    并在字母前加波浪号（`~`）（如 `v3.5.0-rc1` → `3.5.0~rc1`）。
> 3. 版本号本身带有短横线（`-`）时，将短横线替换为小数点（`.`）
>    （如 `7.1.1-44` → `7.1.1.44`）。
> 4. 版本号本身带有下划线（`_`）时，将下划线替换为小数点（`.`）
>    （如 `17_6` → `17.6`）。
> 5. 版本号为格式化后带有半角句号的日期时，可直接使用上游的版本号
>    （如 `2025.07` → `2025.07`）。
> 6. 版本号为基于版本控制系统的提交哈希值时，由数字 `0` 作为开头，而后接上
>    `+`、版本控制器名称、打包日期（`YYYYMMDD`），及哈希值的前 7 位
>    （如 `ee5b7e32b961a9da1933e9f46a018ba6cac8ef60` →
>    `0+git20250808.ee5b7e3`）。
>
> 快速参考表见原始需求文档中的速查表；版本号规范化、快照版本、预发布版本
> 与 `Epoch`/`Release` 的完整策略，请见补充规范
> [版本号（Versioning）](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/Versioning)。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 点号版本 | 版本号仅含半角句号时可直接使用上游版本号 | 无直接违规判定 |
| 2 | 日期版本 | 格式化后带半角句号的日期（如 `2025.07`）可直接使用 | 无直接违规判定 |
| 3 | 预发布标记 | `alpha` / `beta` / `rc` 应转为小写，并在字母前加 `~` | 标记未小写或字母前无 `~` 即失败（如 `3.5.0-rc1`、`1.6RC1`） |
| 4 | 短横线 | 版本号中的 `-` 应替换为 `.` | 版本含 `-` 且非预发布标记所在即失败（如 `7.1.1-44`） |
| 5 | 下划线 | 版本号中的 `_` 应替换为 `.` | 版本含 `_` 即失败（如 `17_6`） |
| 6 | VCS 提交哈希 | 基于提交哈希的版本应转换为快照格式 `0+<scm><YYYYMMDD>.<hash7>`（上游从未发布）；上游曾发布、之后仅发布快照时保留最后发布版本并追加 `+<scm><YYYYMMDD>.<revision>` | 纯 40 位哈希直接用作版本即失败；`+` 后的快照信息不符合 `<scm><YYYYMMDD>.<revision>` 即失败 |

**跳过**（无法静态判定）：

- `Version` 值含宏展开（如 `%{version}`）；
- 字段缺失：由 `check-spec-structure` 规则覆盖，本规则不重复报告。

**注意**：规则多为「应当/可」的推荐性表述，若某个版本确实无法按上述规则
规范化（如 `Epoch` 场景），由打包者按补充规范决定最终写法；
版本组件允许包含 ASCII 字母（如 `5.02c`），此类版本不违规。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-version
```

也可独立运行：`check-spec-version path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
Version:        1.5.7
```

```spec
Version:        2025.07
```

```spec
Version:        3.5.0~rc1
```

```spec
Version:        5.02c
```

```spec
Version:        0+git20250808.ee5b7e3
```

```spec
Version:        4.3.1+git20260616.55a9409
```

```spec
Version:        %{version}
```

### 不通过 ❌

```spec
Version:        7.1.1-44
```
→ `"-" in version should be replaced with "." (found "7.1.1-44")`

```spec
Version:        17_6
```
→ `"_" in version should be replaced with "." (found "17_6")`

```spec
Version:        3.5.0-RC1
```
→ `prerelease marker should be lowercased and prefixed with "~" (found "3.5.0-RC1")`

```spec
Version:        ee5b7e32b961a9da1933e9f46a018ba6cac8ef60
```
→ `VCS commit hash versions should use the snapshot format "0+<scm><YYYYMMDD>.<hash7>" (found "ee5b7e32b961a9da1933e9f46a018ba6cac8ef60")`

```spec
Version:        10.2+2.0.2
```
→ `snapshot versions should end with "+<scm><YYYYMMDD>.<revision>" after the released version (found "10.2+2.0.2")`

```spec
Version:        0+git202608018.7828495
```
→ `snapshot versions should end with "+<scm><YYYYMMDD>.<revision>" after the released version (found "0+git202608018.7828495")`

```spec
Version:        0.99.beta20
```
→ `prerelease marker should be lowercased and prefixed with "~" (found "0.99.beta20")`
