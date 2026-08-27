# check-spec-perl 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-perl` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | perlbuild | perlmaker | 适用小计 | 通过 | 问题 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 5267 | 44 | 350 | 394 | 394 | 0 |

## 问题类型分布

未发现缺失依赖的情况（0 条）。

## 问题清单（0 条）

未发现违规 spec。

## 说明

- 规则仅适用于 `BuildSystem: perlbuild` 或 `BuildSystem: perlmaker`
  的 spec（共 394 个）：
  头部区域 `BuildRequires` 必须声明 `perl-rpm-packaging`、
  `perl-rpm-macros`、`perl-macros` 三项依赖。
  （与 cmake/autotools 指南不同，perl 页面未提及预装工具豁免，
  因此三项均为必需声明。）
- 其余 spec 不适用本规则，未计入统计。
- `%package` 子包段落内的 `BuildRequires`、宏展开值（如
  `%{?foo}`）以及注释行不视为有效声明。
- `perl(Module::Build)`/`perl(ExtUtils::MakeMaker)`/
  `perl(Test::More)` 等虚拟依赖：文档措辞为「通常需要」，
  且取决于上游构建脚本，未纳入强检查点。
- `BuildOption(build)`/`BuildOption(install)`/
  `BuildOption(check)` 示例由 `check-spec-buildoption` 覆盖，
  不在本规则范围内。

> 规则说明：[docs/check-spec-perl.md](../docs/check-spec-perl.md)
