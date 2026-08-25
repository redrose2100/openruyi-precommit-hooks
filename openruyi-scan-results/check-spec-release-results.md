# check-spec-release 扫描结果

�?[openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库�?spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分�?`main`）执�?`check-spec-release` 规则的扫描结果�?
## 结果概览

## 结果概览

| 扫描 spec 文件数 | 通过 | 违规 |
| --- | ---: | ---: |
| 5337 | 5337 | 0 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| 硬编码发行版后缀（如 `1.fc40`�?| 0 |
| `0` 起始修订 | 0 |
| 覆盖 `dist` 宏（`%global dist` / `%define dist`�?| 0 |
| 缺失 `Release` 字段 | 0 |

## 问题清单

扫描�?5337 �?spec 文件全部使用 `%autorelease` 作为 `Release` 值，
未发现硬编码发行版后缀、`0` 起始修订或覆�?`dist` 宏的违规，规�?全部通过，无违规记录�?
（仓�?spec 遵循官方规范程度很高，扫描无违规记录。）
