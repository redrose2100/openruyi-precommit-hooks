# check-spec-bcond 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-bcond` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| --- | ---: | ---: |
| 5267 | 5257 | 10 |

## 问题类型分布

| 问题类型 | 涉及 spec 数 | 问题处数 |
| --- | ---: | ---: |
| 使用旧式宏 `%bcond_with` / `%bcond_without`（应改用 `%bcond <name> <0\|1>`） | 3 | 3 |
| `%{with ...}` / `%{without ...}` 引用未声明的开关（应补 `%bcond <name> <0\|1>`） | 7 | 11 |

## 问题清单

### 旧式宏 `%bcond_with` / `%bcond_without`（3 处，3 个 spec）

| # | 文件 | 行号 | 问题 |
| --- | --- | ---: | --- |
| 1 | `curl/curl.spec` | 12 | `%bcond_with openssl` 应改为 `%bcond openssl <0\|1>` |
| 2 | `make/make.spec` | 8 | `%bcond_with guile` 应改为 `%bcond guile <0\|1>` |
| 3 | `pkgconf/pkgconf.spec` | 10 | `%bcond_without pkgconfig_compat` 应改为 `%bcond pkgconfig_compat <0\|1>` |

### `%{with ...}` / `%{without ...}` 引用未声明开关（11 处，7 个 spec）

| # | 文件 | 行号 | 问题 |
| --- | --- | ---: | --- |
| 1 | `cronie/cronie.spec` | 52 | `%{with systemd}` 未声明 |
| 2 | `firewalld/firewalld.spec` | 80 | `%{with gui}` 未声明 |
| 3 | `gtk3/gtk3.spec` | 144 | `%{with broadway}` 未声明 |
| 4 | `kmod/kmod.spec` | 85 | `%{with weak_modules}` 未声明 |
| 5 | `kmod/kmod.spec` | 91 | `%{with dist_conf}` 未声明 |
| 6 | `libXfixes/libXfixes.spec` | 48 | `%{with static}` 未声明 |
| 7 | `libXt/libXt.spec` | 62 | `%{with static}` 未声明 |
| 8 | `plasma-desktop/plasma-desktop.spec` | 114 | `%{with scim}` 未声明 |
| 9 | `plasma-desktop/plasma-desktop.spec` | 163 | `%{with scim}` 未声明 |
| 10 | `plasma-desktop/plasma-desktop.spec` | 189 | `%{with scim}` 未声明 |
| 11 | `plasma-desktop/plasma-desktop.spec` | 349 | `%{with scim}` 未声明 |

## 说明

- 旧式宏默认只允许一个方向的命令行覆盖（`%bcond_with` 默认关闭、
  `%bcond_without` 默认开启），而 `%bcond <name> <0|1>` 许可
  `--with=` / `--without=` 双向覆盖，语义更完整，是打包指南推荐的
  写法。
- `%{with ...}` 引用未声明的开关在构建时通常展开为空、`%if` 恒假，
  开关意图被隐藏；除非构建方恰好以参数注入同名开关，否则该分支
  永远不参与构建，是真实隐患。
- 10 个违规均出现于 openRuyi 仓库真实 spec 中，建议修复后本规则可
  达到 0 违规。