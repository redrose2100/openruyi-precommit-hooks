# check-spec-perl 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-perl` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | perlbuild | perlmaker | 适用小计 | 通过 | 问题 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 5267 | 44 | 350 | 5267 | 5265 | 2 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | ---: |
| Requires/Provides 使用 `perl-包名` 而非 `perl(MODULE)` 格式 | 2 |

## 问题清单（2 条）

| spec | 问题 |
| --- | --- |
| `docbook-utils/docbook-utils.spec` | `Requires: perl-SGMLSpm` 应改写为 `perl(SGMLSpm)` 虚拟依赖格式 |
| `help2man/help2man.spec` | `Requires: perl-Locale-gettext` 应改写为 `perl(Gettext)` 虚拟依赖格式 |

## 说明

- 规则一（构建依赖）：仅适用于 `BuildSystem: perlbuild` 或
  `BuildSystem: perlmaker` 的 spec（共 394 个）：头部区域
  `BuildRequires` 必须声明 `perl-rpm-packaging`、`perl-rpm-macros`、
  `perl-macros` 三项依赖。
  （与 cmake/autotools 指南不同，perl 页面未提及预装工具豁免，
  因此三项均为必需声明。）该规则扫描结果：394/394 全部通过。
- 规则二（虚拟依赖格式）：适用于全部 5267 个 spec：
  `Requires:`/`Provides:` 中出现的 `perl-CPANDIST` 包名依赖应改写为
  `perl(MODULE)` 虚拟依赖格式；仅当 spec 内声明了同名
  `%package perl-X` 子包时（如 `git.spec` 的
  `%package perl-Git`）才允许使用包名。真实违规 2 个：
  `docbook-utils`（`perl-SGMLSpm`）、`help2man`（`perl-Locale-gettext`）。
- `%package` 子包段落内的 `BuildRequires`、宏展开值（如
  `%{?foo}`）以及注释行不视为有效声明。
- `perl(Module::Build)`/`perl(ExtUtils::MakeMaker)`/
  `perl(Test::More)` 等虚拟依赖：文档措辞为「通常需要」，
  且取决于上游构建脚本，未纳入强检查点。
- `BuildOption(build)`/`BuildOption(install)`/
  `BuildOption(check)` 示例由 `check-spec-buildoption` 覆盖，
  不在本规则范围内。

> 规则说明：[docs/check-spec-perl.md](../docs/check-spec-perl.md)
