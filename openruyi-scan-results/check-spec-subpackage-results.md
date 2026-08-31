# check-spec-subpackage 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-subpackage` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| ---: | ---: | ---: |
| 5267 | 5262 | 5 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | ---: |
| 子包 `Requires` 引用主包但无严格版本约束 | 5 |

## 问题清单（5 个文件）

| spec 文件 | 问题 |
| --- | --- |
| `e2fsprogs/e2fsprogs.spec` | 子包 `e2fsprogs-scrub` 的 `Requires` 引用主包但无严格版本（found "e2fsprogs"） |
| `libmodulemd/libmodulemd.spec` | 子包 `devel` 的 `Requires` 引用主包但无严格版本（found "libmodulemd"） |
| `obs-build/obs-build.spec` | 子包 `mkdrpms` 的 `Requires` 引用主包但无严格版本（found "%{name}"） |
| `perl/perl.spec` | 子包 `macros` 的 `Requires` 引用主包但无严格版本（found "perl"） |
| `swig/swig.spec` | 子包 `ccache-swig` 的 `Requires` 引用主包但无严格版本（found "swig"） |

## 说明

- 规则依据：openRuyi 打包指南「软件包拆分（SplitPackage）」开篇
  「以下是编写 RPM Spec 时必须要遵守的规则」：需要主包的子包必须
  严格指定版本地依赖主包，例如
  `Requires: %{name}%{?_isa} = %{version}-%{release}`。
- 本规则适用于全部 5267 个 spec 的 `%package` 子包块：子包内
  `Requires` 若引用主包（`%{name}` 或主包字面名）必须带版本比较符。
- 豁免：`%{name}-devel`/主包名-`<功能>` 等子包引用、
  `go(...)`/`pkgconfig(...)`/`perl(...)` 等虚拟能力、
  `gcc%{gcc_version}-c++` 等宏续接包名、
  `Requires(pre):` 等 scriptlet 变体、以及 `Name` 本身含宏
  无法静态解析的 spec。
- 真实违规 5 个：`e2fsprogs`（e2fsprogs-scrub → e2fsprogs）、
  `libmodulemd`（devel → libmodulemd）、`swig`（ccache-swig → swig）、
  `obs-build`（mkdrpms → %{name}）、`perl`（macros → perl）。
  同一 spec 内的其它子包（如 e2fsprogs 的 e2fsprogs-devel）均已正确
  使用 `Requires: %{name}%{?_isa} = %{version}-%{release}`，
  形成对照。

> 规则说明：[docs/check-spec-subpackage.md](../docs/check-spec-subpackage.md)
