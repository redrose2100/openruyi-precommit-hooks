# check-spec-summary 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库的 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `master`）执行
`check-spec-summary` 规则的扫描结果。

## 结果概览

| 项目 | 数量 |
| --- | --- |
| 扫描 spec 文件总数 | 5337 |
| 通过 | 5224 |
| 违规数量 | 113 |

## 分布统计

| Summary 写法类别 | 数量 |
| --- | --- |
| 正常（简短英文描述，不以句号结尾） | 5224 |
| 以英文句号 `.` 结尾 | 113 |
| 含 CJK / 全角字符（非英文介绍） | 0 |
| 含宏展开（如 `%{name}`、`%{pkg_desc}`） | 8（跳过判定） |
| 缺失 / 空 `Summary` 字段 | 0 |

## 违规示例（截取）

| spec 文件 | 违规类型 |
| --- | --- |
| `Xwayland.spec` | Summary 以英文句号结尾 |
| `autofs.spec` | Summary 以英文句号结尾 |
| `dblatex.spec` | Summary 以英文句号结尾 |
| `go-aead-dev-mem.spec` | Summary 以英文句号结尾 |
| `go-aead-dev-minisign.spec` | Summary 以英文句号结尾 |

## 结论

扫描的 5337 个 spec 文件中，113 个的 `Summary` 以英文句号 `.` 结尾，
违反「`Summary` 不得以英文句号 `.` 结尾」的禁止性规定；未发现含 CJK /
全角字符的非英文 `Summary`。建议将违规文件的 `Summary` 结尾句号删除。
