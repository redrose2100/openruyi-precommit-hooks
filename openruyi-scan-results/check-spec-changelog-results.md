# check-spec-changelog 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-changelog` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| --- | ---: | ---: |
| 5267 | 5267 | 0 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| `%changelog` 段使用手写 changelog 条目（应使用 `%autochangelog`） | 0 |
| `%changelog` 段为空或仅含注释（应使用 `%autochangelog`） | 0 |

## 说明

- 全部 5267 个 spec 的 `%changelog` 段均合规，其中：
  - 4436 个使用直接宏形式 `%autochangelog`；
  - 831 个使用条件宏形式 `%{?autochangelog}`（仅在定义了 `%autochangelog`
    时展开，语义等价）。
- openRuyi 仓库严格执行自身打包指南：未发现手写 changelog、空段或仅注释
  段的违规情形。
