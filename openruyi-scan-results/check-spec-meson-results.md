# check-spec-meson 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-meson` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | meson | 适用小计 | 通过 | 问题 |
| --- | ---: | ---: | ---: | ---: |
| 5267 | 178 | 178 | 178 | 0 |

## 问题类型分布

未发现缺失依赖的情况（0 条）。

## 问题清单（0 条）

未发现违规 spec。

## 说明

- 规则仅适用于 `BuildSystem: meson` 的 spec（共 178 个）：
  头部区域 `BuildRequires` 必须声明 `meson` 依赖。
  （与 cmake/autotools 指南不同，meson 页面未提及预装工具豁免，
  因此 `meson` 为必需声明。）
- 其余 spec 不适用本规则，未计入统计。
- `%package` 子包段落内的 `BuildRequires`、宏展开值（如
  `%{?foo}`）以及注释行不视为有效声明。
- `BuildOption(conf)`/`BuildOption(build)` 配置项迁移
  （`%build` → `%conf`、`%install -a`）由
  `check-spec-buildoption` 覆盖，不在本规则范围内。
- `ninja-build` 为 meson 的构建后端，指南未要求 spec 声明，
  不纳入本规则。

> 规则说明：[docs/check-spec-meson.md](../docs/check-spec-meson.md)
