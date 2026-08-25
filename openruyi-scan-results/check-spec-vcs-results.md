# check-spec-vcs 扫描结果（占位）

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库的 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-vcs` 规则的扫描结果（本次占位，规则实现已添加）。

## 结果概览

| 项目 | 数量 |
| --- | --- |
| 扫描 spec 文件数 | 0 |
| 通过 | 0 |
| 违规 | 0 |

## 说明

该规则已在 `openruyi_precommit_hooks/check_spec_vcs.py` 中实现，但本仓库中未包含上游 `SPECS/` 源文件，因而未在本地执行完整扫描。

要在有完整 `SPECS/` 工作树的环境中生成真实结果，请运行：

```bash
python -m openruyi_precommit_hooks.check_spec_vcs SPECS/**/*.spec
```

执行后请将生成的统计数替换本文件的概览表格并补充违规清单。
