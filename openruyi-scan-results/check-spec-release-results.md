# check-spec-release 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库的 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `master`）执行
`check-spec-release` 规则的扫描结果。

## 结果概览

| 项目 | 数量 |
| --- | --- |
| 扫描 spec 文件总数 | 5337 |
| 违规数量 | 0 |

## 分布统计

| Release 写法类别 | 数量 |
| --- | --- |
| `%autorelease`（含 `%{autorelease}`） | 5337 |
| 其它宏展开（如 `%{patchset_release}.%{config_version}_%autorelease`） | 0（计入上一行） |
| 纯数字整数修订（如 `3`） | 0 |
| 硬编码发行版后缀（如 `1.fc40`） | 0 |
| `0` 起始修订 | 0 |
| 覆盖 `dist` 宏（`%global dist` / `%define dist`） | 0 |
| 缺失 `Release` 字段 | 0 |

## 结论

扫描的 5337 个 spec 文件全部使用 `%autorelease` 作为 `Release` 值，
未发现硬编码发行版后缀、`0` 起始修订或覆盖 `dist` 宏的违规，规则
全部通过。

（仓库 spec 遵循官方规范程度很高，扫描无违规记录。）
