# check-spec-files

> 规则 ID：`check-spec-files`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-files-results.md](../openruyi-scan-results/check-spec-files-results.md)

## 原始需求

来源：[openRuyi 打包指南 · Files (%files)](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#files)

> 1. `%files` 列表中的许可证文件必须使用 `%license` 标记；文档文件应当使用 `%doc` 标记。
> 2. `%files` 列表不得重复列出同一文件（允许的特定情形除外）。
> 3. 软件包不得包含 `.la` (libtool archive) 文件；若构建过程产生该类文件，Spec 必须移除。
> 4. 本地化文件必须在 `%install` 段落内使用 `%find_lang` 机制处理；不得直接在 `%files`
>    中通配包含 `%{_datadir}/locale/*`。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 许可证文件标记 | 许可证文本文件必须使用 `%license` 标记 | 许可证文件名（`LICENSE`/`COPYING`/`LICENCE` 及其变体）出现在 `%doc` 中或以裸文件名列出（未加任何标记）即失败 |
| 2 | 文档文件标记 | 文档文件应当使用 `%doc` 标记 | 文档文件名（`README`/`NEWS`/`AUTHORS`/`CHANGELOG`/`CHANGES`/`HISTORY` 及其变体）以裸文件名列出（未加 `%doc`）即失败 |
| 3 | 文件不重复 | `%files` 列表不得重复列出同一文件 | 同一字面路径在同一 `%files` 段内出现 2 次及以上即失败 |
| 4 | 无 `.la` 文件 | 软件包不得包含 libtool archive 文件 | `%files` 列表中出现 `.la` 结尾的路径即失败 |
| 5 | 本地化处理 | 本地化文件必须用 `%find_lang` 处理，不得直接通配 `%{_datadir}/locale/*` | `%files` 列表中出现 `%{_datadir}/locale/*` 通配符即失败 |

**跳过**（无法静态判定）：

- `%exclude` 行：属于排除操作而非软件包内容，不参与检查（如
  `%exclude %{_libdir}/libexpat.la` 表示构建后排除该文件，不判 `.la` 违规）；
- `%dir` / `%ghost`：仅声明目录或幽灵文件，不安装文件内容，不参与许可
  证/文档/重复判定；
- 条件块（`%if`/`%ifarch`/`%ifnarch`/`%ifos`/`%ifnos`/`%else`/`%endif`）内
  的条目：不同条件分支可能互斥，同一路径出现在不同分支不算重复；
- 宏路径（`%{...}` 开头）：宏展开值无法静态求值，重复判定仅在字面路径
  上进行；
- 带目录组件的路径（如 `%{_docdir}/foo/README`、`%{_sysconfdir}/ssl/README`）：
  属于安装的数据文件而非文档/许可证标记对象，不参与判定；
- `%files -f` 引用的文件清单（由 `%find_lang` 等生成）：文件清单内容在
  构建期生成，静态不可见；`-f` 段内直接书写的条目仍照常检查；
- `%lang(x)` 指令：按语言标记的翻译文件，不参与重复/通配判定；
- 许可证文本是否真的对应声明的 `License` 字段、`.la` 文件是否由构建
  过程产生、`%find_lang` 实际生成了哪些文件等语义问题需人工核对。

**注意**：检查点 1、3、4、5 为「必须」级要求（许可证必须 `%license`、文件不得
重复、不得含 `.la`、本地化必须 `%find_lang`），违反即报告；检查点 2 为
「应当」级要求（文档应当 `%doc`），裸列即报告。许可证文件名判断按
`LICENSE`/`LICENCE`/`COPYING` 前缀（大小写不敏感，含扩展名与通配），
如 `license.terms`（tcl）也视为许可证文件。同一文件若同时出现在 `%license`
与 `%doc` 行中，`%doc` 一侧仍会报告（httpd 的 `%files tools` 段内
`%license LICENSE NOTICE` 与 `%doc LICENSE NOTICE` 并存即被报告）：
许可证文本以文档身份安装属于多余的重复标记，应仅保留 `%license`。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.2.0   # 使用最新 tag
    hooks:
    -   id: check-spec-files
```

也可独立运行：`check-spec-files path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
%install
%find_lang %{name}
...

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/foo
```

```spec
%files
%license LICENSE NOTICE
%doc README
%{_libdir}/libfoo.so.*
```

```spec
%files
%if 0%{?rhel}
%{_bindir}/foo
%else
%{_bindir}/foo
%endif
```

### 不通过 ❌

```spec
%files
%doc LICENSE
```

```text
→ foo.spec: license file "LICENSE" in %files must be marked with %license (found in %doc)
```

```spec
%files
README
```

```text
→ foo.spec: documentation file "README" in %files should be marked with %doc
```

```spec
%files
%{_libdir}/libfoo.la
```

```text
→ foo.spec: %files must not contain libtool archive ".la" files (found "%{_libdir}/libfoo.la")
```

```spec
%files
%{_datadir}/locale/*
```

```text
→ foo.spec: localized files must be handled with %find_lang in the %install section, not wildcarded as %{_datadir}/locale/* (found "%{_datadir}/locale/*")
```

```spec
%files
/usr/share/foo/bar
/usr/share/foo/bar
```

```text
→ foo.spec: %files must not list the same file twice (found "/usr/share/foo/bar" 2 times in %files)
```
