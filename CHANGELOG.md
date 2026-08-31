# CHANGELOG

## 未发布

### 新增

- 规则 hook `check-spec-autotools`：校验 `BuildSystem: autotools` 的
  spec 文件必须在头部 `BuildRequires` 声明 `autoconf`、`automake`、
  `libtool`、`make` 四项构建依赖（gcc 预装豁免）。静态检查：截取头部
  （首个 `%description`/`%package` 之前）收集 `BuildSystem` 与
  `BuildRequires`，剥离 `%{...}` 宏并按空白/逗号/括号拆分依赖名，
  仅匹配 `^[A-Za-z0-9_.+/]+(?:-[A-Za-z0-9_.+/]+)*$` 的视为有效声明
  （允许 `go-rpm-macros` 等带连字符的包名）；`BuildSystem` 值为
  `autotools` 时缺失任意一项即报错，非 autotools 构建系统直接跳过。
  新增规则文档 `docs/check-spec-autotools.md` 与扫描结果
  `openruyi-scan-results/check-spec-autotools-results.md`（675 个
  autotools spec 中 193 个通过、482 个缺失依赖）。
- 规则 hook `check-spec-cmake`：校验 `BuildSystem: cmake` 的 spec
  文件必须在头部 `BuildRequires` 声明 `cmake` 构建依赖（gcc 预装
  豁免）。静态检查逻辑同 `check-spec-autotools`（截取头部收集
  `BuildSystem` 与 `BuildRequires`、剥离 `%{...}` 宏后按
  空白/逗号/括号拆分依赖名、匹配`^[A-Za-z0-9_.+/]+(?:-[A-Za-z0-9_.+/]+)*$`
  的视为有效声明）；`BuildSystem` 值为 `cmake` 时缺失即报错，非 cmake
  构建系统直接跳过。新增规则文档 `docs/check-spec-cmake.md` 与
  扫描结果 `openruyi-scan-results/check-spec-cmake-results.md`
  （422 个 cmake spec 中 421 个通过、1 个缺失依赖）。
- 规则 hook `check-spec-golang`：校验 `BuildSystem: golang` 或
  `BuildSystem: golangmodules` 的 spec 文件必须在头部
  `BuildRequires` 声明 `go`、`go-rpm-macros` 两项构建依赖
  （golang 指南未提及预装工具豁免，两项均为必需）。静态检查逻辑
  同 `check-spec-autotools`；`BuildSystem` 值为 `golang` 或
  `golangmodules` 时缺失任意一项即报错，其它构建系统直接跳过。
  新增规则文档 `docs/check-spec-golang.md` 与扫描结果
  `openruyi-scan-results/check-spec-golang-results.md`
  （730 个 golang/golangmodules spec 全部通过、0 个缺失依赖）。
- 规则 hook `check-spec-golang` 新增检查点（依据「编程语言 ·
  Golang」指南依赖关系章节「库软件包本身必须要显式在 RPM Spec
  内写出自己提供的导入路径和版本」）：`BuildSystem: golangmodules`
  （纯库打包构建系统）必须在头部或 `%package` 子包块内声明至少
  一条 `Provides: go(<import path>)`；每条 `Provides: go(...)`
  必须带显式版本约束（`= <version>`，如 `= %{version}`）。
  静态检查：`Provides` 字段在头部区域与全部 `%package` 子包块内
  收集，`golangmodules` 无任何 `go()` 虚拟提供即报错；`go(...)`
  提供行内未写出 `= <version>` 即报错（`%files`/`%description`/
  `%changelog` 与脚本段内容不检查）。更新规则文档
  `docs/check-spec-golang.md` 与扫描结果
  `openruyi-scan-results/check-spec-golang-results.md`
  （730 个 golang/golangmodules spec 中 725 个通过、5 个问题：
  gofakeit 缺 `Provides: go(...)`；fatih-color、shortuuid、
  blackfriday、blackfriday-v2 四个包的 `Provides: go(...)`
  缺版本约束）。
- 规则 hook `check-spec-meson`：校验 `BuildSystem: meson` 的 spec
  文件必须在头部 `BuildRequires` 声明 `meson` 构建依赖
  （meson 指南未提及预装工具豁免，`meson` 为必需声明）。静态检查
  逻辑同 `check-spec-autotools`；`BuildSystem` 值为 `meson` 时
  缺失即报错，其它构建系统直接跳过。新增规则文档
  `docs/check-spec-meson.md` 与扫描结果
  `openruyi-scan-results/check-spec-meson-results.md`
  （178 个 meson spec 全部通过、0 个缺失依赖）。
- 规则 hook `check-spec-perl`：校验 `BuildSystem: perlbuild` 或
  `BuildSystem: perlmaker` 的 spec 文件必须在头部
  `BuildRequires` 声明 `perl-rpm-packaging`、`perl-rpm-macros`、
  `perl-macros` 三项构建依赖（perl 指南未提及预装工具豁免，
  三项均为必需）。静态检查逻辑同 `check-spec-autotools`；
  `BuildSystem` 值为 `perlbuild` 或 `perlmaker` 时缺失任意一项
  即报错，其它构建系统直接跳过。新增规则文档
  `docs/check-spec-perl.md` 与扫描结果
  `openruyi-scan-results/check-spec-perl-results.md`
  （394 个 perlbuild/perlmaker spec 全部通过、0 个缺失依赖）。
- 规则 hook `check-spec-perl` 新增检查点（依据「编程语言 ·
  Perl」指南 Requires 和 Provides 标签章节「应使用 `perl(MODULE)`
  格式，而不是直接依赖包名」）：`Requires:`/`Provides:` 字段
  中出现 `perl-CPANDIST` 包名（`perl-[A-Z]\S*`）时，必须改写成
  `perl(MODULE)` 虚拟依赖格式；仅当 spec 内声明了同名
  `%package perl-X` 子包（如 `git.spec` 的 `%package perl-Git`）
  时才允许使用包名。静态检查：收集全部 `%package` 子包名，
  逐行匹配 `Requires:`/`Provides:` 值并按空白/逗号拆分 token、
  剥离 `=<>~` 版本约束符号，命中 `perl-[A-Z]...` 且不在子包集合
  内即报错。本检查点适用于全部 spec（不限于 perlbuild/perlmaker）。
  更新规则文档 `docs/check-spec-perl.md` 与扫描结果
  `openruyi-scan-results/check-spec-perl-results.md`
  （5267 个 spec 中 5265 个通过、2 个问题：docbook-utils 的
  `Requires: perl-SGMLSpm`、help2man 的
  `Requires: perl-Locale-gettext`，应分别改写为
  `perl(SGMLSpm)`、`perl(Gettext)`）。
- 规则 hook `check-spec-pyproject`：校验 `BuildSystem: pyproject`
  的 spec 文件必须满足三项静态检查点（pyproject 指南的
  「至少需要」依赖、install 模块名、check 原因注释）。静态检查：
  截取头部（首个 `%description`/`%package` 之前）收集
  `BuildSystem` 与 `BuildRequires`，剥离 `%{...}` 宏后按
空白/逗号/括号拆分依赖名，`BuildRequires` 缺失
  `pyproject-rpm-macros` 即报错；`BuildOption(install)` 值为空
  （未携带模块名）即报错；`BuildOption(check)` 块首行上方最近
  非空行不是注释（未写明跳过原因）即报错。`BuildSystem` 值非
  `pyproject` 直接跳过。新增规则文档
  `docs/check-spec-pyproject.md` 与扫描结果
  `openruyi-scan-results/check-spec-pyproject-results.md`
  （852 个 pyproject spec 中 785 个通过、67 个问题：6 个缺失
  `pyproject-rpm-macros` + 61 个 `BuildOption(check)` 无原因注释）。
- 规则 hook `check-spec-rust`：校验 `BuildSystem: rust` / `BuildSystem:
  rustcrates` 的 spec 文件必须满足四项静态检查点（Rust 指南的
  「通常需要」依赖、rustcrates 不可覆盖构建阶段、check 原因注释）。
  静态检查：截取头部（首个 `%description`/`%package` 之前）收集
  `BuildSystem` 与 `BuildRequires`，剥离 `%{...}` 宏后按
  空白/逗号/括号拆分依赖名，`BuildRequires` 缺失
  `rust-rpm-macros` 即报错（两种系统）；`rust` 应用包缺失 `rust`
  （编译器）即报错；`BuildSystem: rustcrates` 出现
  `BuildOption(build)` 即报错（构建阶段运行 specpart 脚本，文档
  明确不可覆盖）；`BuildOption(check)` 块首行上方最近非空行不是
  注释（未写明跳过原因）即报错。`BuildSystem` 值非 `rust`/
  `rustcrates` 直接跳过。新增规则文档 `docs/check-spec-rust.md`
  与扫描结果 `openruyi-scan-results/check-spec-rust-results.md`
  （1897 个 rust/rustcrates spec 中 1896 个通过、1 个问题：
  `cbindgen` 的 `BuildOption(check)` 无原因注释）。
- 规则 hook `check-spec-subpackage`：校验 `%package` 子包块内
  `Requires` 若引用主包（`%{name}` 或主包字面名）必须带严格版本
  比较符（SplitPackage 指南「需要主包的子包必须严格指定版本地依赖
  主包」，推荐 `Requires: %{name}%{?_isa} = %{version}-%{release}`）。
  静态检查：提取 `Name` 字段，遍历 `%package` 子包块（跳过主包块
  与宏展开的主包名），匹配裸 `Requires:`（`Requires(pre):` 等
  scriptlet 变体天然不匹配被跳过）；豁免整值虚拟能力
  （`go(...)`/`pkgconfig(...)`/`perl(...)`/`python3dist(...)` 等）、
  子包引用（`%{name}-devel`/`<主包名>-<功能>`）、宏续接包名
  （`gcc%{gcc_version}-c++` 展开为另一包）；命中主包引用且无版本
  比较符即报错。适用于全部 spec。新增规则文档
  `docs/check-spec-subpackage.md` 与扫描结果
  `openruyi-scan-results/check-spec-subpackage-results.md`
  （5267 个 spec 中 5262 个通过、5 个问题：e2fsprogs 的
  `e2fsprogs-scrub` → e2fsprogs、libmodulemd 的 `devel` →
  libmodulemd、swig 的 `ccache-swig` → swig、obs-build 的
  `mkdrpms` → %{name}、perl 的 `macros` → perl）。

### 变更

- `check-spec-subpackage` 的错误消息与扫描结果补充行号：错误消息
  改为 `文件:行号:` 前缀（如 `foo.spec:56: subpackage ...`，与
  `check-spec-bcond` 一致），扫描结果
  `openruyi-scan-results/check-spec-subpackage-results.md` 的问题
  清单新增「行号」列（e2fsprogs:56、libmodulemd:58、obs-build:61、
  perl:86、swig:78）。规则文档 `docs/check-spec-subpackage.md` 的
  失败示例同步更新，并新增 swig（ccache-swig）形态的测试用例。

## 0.1.0 (2026-08-26)

### 变更

- 扫描结果文档 `openruyi-scan-results/` 统一为三段式格式：
  「结果概览」（扫描/通过/违规）、「问题类型分布」（问题类型与
  数量）、「问题清单」（带序号的问题明细）。涉及
  `check-spdx-header`、`check-spec-name`、`check-spec-release`、
  `check-spec-summary`、`check-spec-version`、`check-spec-structure`
  六个结果文件；`check-spec-structure` 由生成脚本
  `scripts/regenerate_structure_results.py` 重新生成（问题清单按
  缺少必填字段 / 头部字段乱序 / 段落前缺少空行分组并编号）。
- 规则文档 `docs/check-spdx-header.md` 重构为「原始需求 / 检查点 /
  用法 / 示例」四个部分：原始需求引用官方打包指南的 SPDX 版权与
  许可声明原文，检查点以表格形式逐项列出（位置、版权声明、分隔
  空行、许可证标识等），用法与示例保持原实现方式。
- 规则文档 `docs/check-spec-structure.md` 同样重构为「原始需求 /
  检查点 / 用法 / 示例」：原始需求引用官方打包指南的 基础字段与段落
  原文，检查点以表格形式分头部字段（完整性、顺序、变体与延续）与
  段落空行（分隔、带参数、条件块）两组列出。
- 规则文档 `docs/check-spec-name.md` 同样重构为「原始需求 / 检查点 /
  用法 / 示例」：原始需求引用官方打包指南的 Name 规则原文，检查点以
  表格形式逐项列出（字段存在、全小写、分隔符、版本编码、上游别名）
  并保留跳过与注意说明。
- 规则 `check-spec-structure` 检查标准更新：当 `URL` 已为源代码仓库
  链接时，`VCS` 字段可以省略（不再判为缺失违规）；判定依据为
  `git:` 前缀、`.git` 结尾或已知源码托管平台域名（github.com、
  gitlab.com、codeberg.org、bitbucket.org、git.sr.ht 等）。规则文档
  `docs/check-spec-structure.md` 增加 `VCS` 豁免规则说明与示例，扫描
  结果 `openruyi-scan-results/check-spec-structure-results.md` 重新
  生成：缺 `VCS` 文件数由 4363 降至 772（其余 3591 个 URL 为源码仓库
  链接获豁免），不合规总数由 4066 降至 3474。

### 新增

- 规则 hook `check-spec-changelog`：校验 spec 文件 `%changelog` 段落符合
  openRuyi Changelog 规则（`%changelog` 段内容必须为 `%autochangelog`，
  不得手写更新日志）。静态检查：段内不含 `%autochangelog` 且含手写
  changelog 条目报错；段为空或仅含注释报错。`%autochangelog` 的两种
  合法写法（直接宏 `%autochangelog` 与条件宏 `%{?autochangelog}`）均
  通过；段内注释允许，但仅注释不足以满足要求。
- 规则 hook `check-spec-bcond`：校验 spec 文件条件构建开关符合 openRuyi
  条件构建规则（定义可选构建开关应当使用 `%bcond <name> <0|1>`，应当
  尽量避免 `%bcond_with` / `%bcond_without`）。静态检查：`%bcond_with` /
  `%bcond_without` 旧式宏出现即报错；`%{with ...}` / `%{without ...}`
  引用未在文件中声明的开关即报错（构建期展开为空、`%if` 恒假）。旧式
  下划线形态 `%define with_xxx` + `%{with_xxx}` 不属于 `%bcond` 体系，
  不检查；注释行忽略。扫描结果：5267 个 spec 中 10 个违规（curl、
  make、pkgconf 使用旧式宏 3 处；cronie、firewalld、gtk3、kmod、
  libXfixes、libXt、plasma-desktop 引用未声明开关 11 处）。
- 规则文档 `docs/check-spec-bcond.md`，README 增加 Hooks 列表项
  （共 19 个）、扫描结果 `openruyi-scan-results/check-spec-bcond-results.md`。
- 规则文档 `docs/check-spec-changelog.md`，README 增加 Hooks 列表项
  （共 18 个）。
- 扫描结果 `openruyi-scan-results/check-spec-changelog-results.md`：
  5267 个 spec 文件的 `%changelog` 段全部合规（0 违规），其中 4436 个
  使用直接宏 `%autochangelog`、831 个使用条件宏 `%{?autochangelog}`；
  未发现手写 changelog、空段或仅注释段的违规情形。
- 规则 hook `check-spec-requires`：校验 spec 文件 `Requires` 字段符合
  openRuyi Requires 规则（`Requires` 用于列出运行期依赖；依赖项必须按
  "一行一个依赖包"的形式书写；排版与可读性要求 `BuildRequires` 与
  `Requires` 必须采用"一行一个依赖"的形式）。静态检查：一行仅允许一个
  依赖包（逗号分隔 `a, b` 或空格分隔 `a b` 报错），值不得为空
  （`Requires:` 报错）；富依赖表达式（`(foo >= 1 with foo < 2)`）、带
  版本约束（`foo >= 1.2` / `foo = 1.29`）及含宏的值视为单个依赖。
  `%package` 子包内的 `Requires` 声明的是子包运行期依赖，同样按规则
  检查；`Requires(pre):` / `Requires(post):` 等 scriptlet 变体声明的是
  特定脚本段依赖，不属于本规则范围；字段缺失交由 `check-spec-structure`
  覆盖。
- 规则文档 `docs/check-spec-requires.md`，README 增加 Hooks 列表项
  （共 16 个）。
- 扫描结果 `openruyi-scan-results/check-spec-requires-results.md`：
  5267 个 spec 文件中仅 1 个文件违规（`cloud-utils` 子包内 3 条：
  `Requires: file gzip e2fsprogs gawk tar` 一行声明 5 个包、
  `Requires: gawk util-linux` 两行各声明 2 个包）；
  `cronie` 的 `Requires(post): coreutils sed` 与 `e2fsprogs` 的
  `Requires(post): /usr/bin/mkdir /usr/bin/touch` 为 scriptlet 变体，
  不属于本规则范围。
- 规则 hook `check-spec-files`：校验 spec 文件 `%files` 段落符合 openRuyi
  Files 规则（许可证文本文件必须使用 `%license` 标记，文档文件应当使用
  `%doc` 标记；`%files` 列表不得重复列出同一文件（允许的特定情形除外）；
  软件包不得包含 `.la`（libtool archive）文件，若构建过程产生该类文件
  Spec 必须移除；本地化文件必须在 `%install` 段落内使用 `%find_lang`
  机制处理，不得直接在 `%files` 中通配包含 `%{_datadir}/locale/*`）。
  静态检查：`%doc` 中列出许可证文本文件（`license`/`licence`/`copying`
  开头的文件名或其中文、`license.terms` 等）报错；许可证文本裸列未加
  `%license` 报错；文档类文件（`readme`/`news`/`authors`/`changelog`/
  `changes`/`history` 等）裸列未加 `%doc` 报错；同一字面文件路径在段顶层
  重复列出报错（宏路径、条件块内、`%dir`/`%ghost`/`%doc` 指令项、含通配
  符路径跳过）；含 `.la` 后缀条目报错；`%{_datadir}/locale/*` 通配报错。
- 规则文档 `docs/check-spec-files.md`，README 增加 Hooks 列表项
  （共 17 个）。
- 扫描结果 `openruyi-scan-results/check-spec-files-results.md`：5267 个
  spec 文件中 93 个文件违规共 105 条（`%doc` 中列出许可证文本文件 91 条、
  `%files` 中直接通配 `%{_datadir}/locale/*` 14 条）；重复列出与
  `.la` 归档 0 条。234 个 spec 正确使用 `%find_lang` 处理本地化；全部
  12 个 KF6 locale 违规包中仅 `kf6-kconfigwidgets` 使用了 `%find_lang`。
- 规则 hook `check-spec-buildoption`：校验 spec 文件 `BuildOption` 字段
  符合 openRuyi BuildOption 规则（当需要为特定构建阶段声明额外参数时可
  使用 `BuildOption(<stage>):` 字段；`BuildOption(<stage>):` 与参数之间
  必须以两个空格分隔；多个参数必须按行分别声明；若使用 `BuildOption`，
  其位置应当位于 `BuildSystem` 与 `BuildRequires` 之间；书写顺序应当与
  RPM 构建过程一致，即 `build` → `install` → `check`）。补充文档（声明式
  构建系统）要求阶段名称必须写明（虽然语法上可以省略）。静态检查：阶段
  名称必须写明（`BuildOption:` 或 `BuildOption():` 报错）；冒号后必须为
  双空格分隔；位置须在 `BuildSystem` 与 `BuildRequires` 之间；`build`/
  `install`/`check` 三个阶段的相对顺序须符合 `build` → `install` →
  `check`（其它阶段如 `conf`/`prep`/`generate_buildrequires` 不参与顺序
  判定）；字段缺失交由 `check-spec-structure` 覆盖，`%package` 子包内的
  `BuildOption` 不判定。
- 规则文档 `docs/check-spec-buildoption.md`，README 增加 Hooks 列表项。
- 扫描结果 `openruyi-scan-results/check-spec-buildoption-results.md`：
  5267 个 spec 文件中 27 个 `BuildOption` 字段违规（共 34 条：冒号后
  单空格分隔 18 条、位置不在 `BuildSystem` 与 `BuildRequires` 之间 9 条、
  阶段顺序不符合 `build` → `install` → `check` 7 条）。
- 规则 hook `check-spec-buildrequires`：校验 spec 文件 `BuildRequires`
  字段符合 openRuyi BuildRequires 规则（`BuildRequires` 必须列出构建期
  依赖；依赖项必须按"一行一个依赖包"的形式书写；对于 C 程序通常不需要
  显式声明 `gcc`；当依赖通过 `pkg-config` 发现时应当优先使用
  `pkgconfig(xxx)` 形式声明而不是直接依赖 `xxx-devel`；必须确保构建依赖
  完整）。静态检查：一行仅允许一个依赖包（逗号分隔 `a, b` 或空格分隔
  `a b` 报错），值不得为空（`BuildRequires:` 报错）；富依赖表达式
  （`(foo >= 1 with foo < 2)`）、带版本约束（`foo >= 1.2` / `foo = 1.29`）
  及含宏的值视为单个依赖。依赖完整性、`gcc` 是否必需、`pkgconfig(xxx)`
  与 `xxx-devel` 的选择需人工核对，不静态判定；字段缺失交由
  `check-spec-structure` 覆盖，`%package` 子包内的 `BuildRequires`
  不判定。
- 规则文档 `docs/check-spec-buildrequires.md`，README 增加 Hooks 列表项
  （共 15 个）。
- 扫描结果 `openruyi-scan-results/check-spec-buildrequires-results.md`：
  5267 个 spec 文件中仅 1 个文件违规（`valgrind` 的
  `BuildRequires:  automake autoconf` 一行声明了 `automake` 与
  `autoconf` 两个包）；`groff` 子包（`%package x11`）内的
  `libXaw-devel, libXmu-devel` 位于子包段落内，不属于本规则范围。
- 规则 hook `check-spec-patch`：校验 spec 文件 `Patch` 字段符合 openRuyi
  Patch 规则（每个 `Patch:` 字段上方须有一行注释说明补丁用途；补丁文件
  名须以四位数字开头且前缀在 `0001-2999` 范围内；补丁数量超过 3 个时应
  使用 `%patchlist` 统一管理；`%patchlist` 须位于 `%description` 之上；
  `Patch` 字段应位于 `BuildSystem` 与 `BuildOption`（或 `BuildRequires`）
  之间）。静态检查：仅扫描 spec 头部区域（`%description`/`%package` 等
  段落之前），`%patchlist` 位置检查在整个文件中查找；`%patch` 应用阶段
  的补丁顺序由 `%patchlist` 或 `%patch` 行号决定，不静态判定。
- 规则文档 `docs/check-spec-patch.md`，README 增加 Hooks 列表项。
- 扫描结果 `openruyi-scan-results/check-spec-patch-results.md`：5267 个
  spec 文件中 204 个违规（共 513 条：`Patch` 上方无注释 276 条、
  `%patchlist` 条目无注释 57 条、文件名非四位数字开头 121 条、放置
  顺序错误 26 条、>3 补丁未用 `%patchlist` 25 条、前缀不在
  `0001-2999` 4 条、`%patchlist` 位于 `%description` 之下 4 条）。
- 规则 hook `check-spec-buildsystem`：校验 spec 文件 `BuildSystem` 字段
  符合 openRuyi BuildSystem 规则（Spec 必须包含 `BuildSystem` 字段；取值
  应当为官方列出的构建系统之一或其它新增的值；当软件包不适用上述类型或
  不需要配置阶段时可以为空，但必须以注释说明原因）。静态检查：值须为
  已知构建系统（官方 6 种 + openRuyi 仓库扩展的 `perlbuild`/`perlmaker`/
  `rust`/`rustcrates` 4 种），未知值报告提示确认是否为新增值；值为空时
  须在同行或上一行以注释说明原因；字段缺失交由 `check-spec-structure`
  覆盖，`%package` 子包内的 `BuildSystem` 不判定。
- 规则文档 `docs/check-spec-buildsystem.md`，README 增加 Hooks 列表项。
- 扫描结果 `openruyi-scan-results/check-spec-buildsystem-results.md`：
  5267 个 spec 文件全部通过（10 种取值均在已知白名单内，无空值）。
- 规则 hook `check-spec-buildarch`：校验 spec 文件 `BuildArch` 字段
  符合 openRuyi BuildArch 规则（`BuildArch` 用于声明目标架构；字段
  应当位于最后一个 `Source` 字段与 `BuildSystem` 字段之间；若为
  `noarch` 表示软件包与 CPU 架构无关）。静态检查：值不得为空、须为
  `noarch`（openRuyi 仓库唯一使用的取值）、位置须在最后一个 `Source`
  与 `BuildSystem` 之间；字段缺失交由 `check-spec-structure` 覆盖，
  `%package` 子包内的 `BuildArch` 不判定。
- 规则文档 `docs/check-spec-buildarch.md`，README 增加 Hooks 列表项。
- 扫描结果 `openruyi-scan-results/check-spec-buildarch-results.md`：
  5267 个 spec 文件中 2 个 `BuildArch` 字段位置违规（均位于 `Source0`
  之前，值均为 `noarch`）。
- 规则 hook `check-spec-vcs`：校验 spec 文件 `VCS` 字段符合 openRuyi
  VCS 规则（`VCS` 应当为源代码仓库链接；若 `URL` 已为源码仓库链接则
  `VCS` 可以省略；不存在可用链接时必须在 `VCS` 字段位置写入精确的
  `# VCS: No VCS link available` 注释；Git 仓库应使用 `git:` 可克隆
  链接）。静态检查：`VCS` 值须为 `git:` 前缀或指向已知源码托管平台
  的 http(s) 链接、不得用 `%{name}` 等宏拼接、`# VCS:` 注释必须精确
  匹配；字段缺失交由 `check-spec-structure` 覆盖。
- 规则文档 `docs/check-spec-vcs.md`，README 增加 Hooks 列表项。
- 扫描结果 `openruyi-scan-results/check-spec-vcs-results.md`：
  5267 个 spec 文件中 23 个 `VCS` 字段违规（13 个 `# VCS:` 注释不
  精确、10 个非 `git:` 可克隆链接如 `hg:`/`svn:` 前缀）。
- 规则 hook `check-spec-summary`：校验 spec 文件 `Summary` 字段符合
  openRuyi Summary 规则（不得以英文句号 `.` 结尾、应当仅包含必要的英文
  介绍）；含宏展开的 `Summary` 值跳过静态检查，「简短描述」为定性要求
  无法静态判定，字段缺失交由 `check-spec-structure` 覆盖。
- 规则文档 `docs/check-spec-summary.md`，README 增加 Hooks 列表项。
- 扫描结果 `openruyi-scan-results/check-spec-summary-results.md`：
  5337 个 spec 文件中 113 个 `Summary` 以英文句号结尾（违规），
  未发现含 CJK/全角字符的非英文 `Summary`。
- 规则 hook `check-spec-release`：校验 spec 文件 `Release` 字段符合
  openRuyi Release 规则（应当使用 `%autorelease`、修订序号为从 `1` 开始
  的整数且不为 `0`、不得硬编码发行版后缀如 `1.fc40`、不得覆盖 `dist` 宏）；
  宏展开值跳过静态检查，递增/复位规则需版本历史无法静态判定，字段缺失
  交由 `check-spec-structure` 覆盖。
- 规则文档 `docs/check-spec-release.md`，README 增加 Hooks 列表项。
- 规则 hook `check-spec-license`：校验 spec 文件 `License` 字段使用
  SPDX License Identifier 或表达式（连接符必须大写 `AND`/`OR`/`WITH`、
  不得用逗号分隔、不得用老式 `+` 后缀、括号须配对）；标识符准确性
  与 `%files` 中 `%license` 标记为定性/跨段落要求无法静态判定，字段缺失
  交由 `check-spec-structure` 覆盖。
- 规则文档 `docs/check-spec-license.md`，README 增加 Hooks 列表项。
- 扫描结果 `openruyi-scan-results/check-spec-license-results.md`：
  5337 个 spec 文件中 21 个 `License` 字段违规（15 个小写连接符、
  1 个逗号分隔、5 个老式 `+` 后缀）。
- 规则 hook `check-spec-source`：校验 spec 文件 `Source` 字段符合
  openRuyi Source 规则（网络来源 `Source` 行前必须紧跟
  `#!RemoteAsset` 注释且携带 sha256 校验值；SourceForge 下载链接
  必须使用 `downloads.sourceforge.net` 主机）；本地文件与 `git+`/
  `git:` 来源跳过静态检查，字段缺失交由 `check-spec-structure` 覆盖。
- 规则文档 `docs/check-spec-source.md`，README 增加 Hooks 列表项。
- 扫描结果 `openruyi-scan-results/check-spec-source-results.md`：
  5337 个 spec 文件中 725 个违规（852 条 `#!RemoteAsset` 注释为空
  缺少 sha256 校验值、11 条 SourceForge 域名不合规：
  3 条 `download.sourceforge.net`、2 条 `prdownloads.sourceforge.net`、
  6 条 `sourceforge.net/projects/...`）；违规清单与既有规则文档一致，
  `Source 值` 列后标注违规类型。
- 规则 hook `check-spec-url`：校验 spec 文件 `URL` 字段必须为软件包
  官方网站或源码仓库链接（以 `http://`/`https://` 开头），且不得使用
  `%{name}` 等宏进行拼接；链接是否为真实官网/仓库需人工核对无法静态
  判定，字段缺失交由 `check-spec-structure` 覆盖。
- 规则文档 `docs/check-spec-url.md`，README 增加 Hooks 列表项。
- 扫描结果 `openruyi-scan-results/check-spec-url-results.md`：5337 个
  spec 文件中 7 个 `URL` 字段违规（4 个宏拼接、3 个 `FIXME` 占位符
  非 http(s) 链接）。
- 扫描结果 `openruyi-scan-results/check-spec-release-results.md`：
  5337 个 spec 文件全部使用 `%autorelease`，扫描无违规记录。
- 规则 hook `check-spec-version`：校验 spec 文件 `Version` 字段符合
  openRuyi 版本号规范化规则（点号/日期版本直用、预发布标记小写加 `~`、
  `-`/`_` 替换为 `.`、提交哈希转换为快照格式）；宏展开版本跳过静态检查，
  字段缺失交由 `check-spec-structure` 覆盖。
- 规则文档 `docs/check-spec-version.md`，README 增加 Hooks 列表项。
- 扫描结果 `openruyi-scan-results/check-spec-version-results.md`：
  5337 个 spec 文件中 6 个存在版本规范化问题（2 个含下划线、
  2 个预发布标记未规范化、2 个快照格式不合规）。
- 规则 hook `check-spec-name`：校验 spec 文件 `Name` 字段符合
  openRuyi 命名规则（必须存在、全小写、优先短横线分隔、不编码
  ABI/主版本号）；`perl-*` 模块豁免小写检查，宏展开名称跳过静态检查。
- 规则文档 `docs/check-spec-name.md`，README 增加 Hooks 列表项。
- 扫描结果 `openruyi-scan-results/check-spec-name-results.md`：
  5337 个 spec 文件中 65 个存在命名违规（33 个非全小写、24 个含
  下划线、8 个编码 ABI/主版本号）。
- 项目框架：`setup.cfg` / `setup.py` 打包配置，`.pre-commit-hooks.yaml`
  对外 hooks 清单，`.pre-commit-config.yaml` 自举配置。
- 测试基础设施：`tests/`、`testing/`（`get_resource_path` / `git_commit`）、
  `resources/`，以及 `tox.ini`、`requirements-dev.txt`、GitHub Actions CI。
- 公共工具 `openruyi_precommit_hooks/util.py`：
  `cmd_output` / `added_files` / `zsplit` / `CalledProcessError`。
- 首个规则 hook `check-spdx-header`：校验 spec 文件起始位置包含
  SPDX 版权与许可证声明（ISCAS + openRuyi Project Contributors +
  `SPDX-License-Identifier: MulanPSL-2.0`），contributor 行为可选；
  版权行与许可证行之间必须有且仅有一行 `#` 空注释行。
- 规则 hook `check-spec-structure`：校验 spec 文件主包头部**必须包含**
  `Name → Version → Release → Summary → License → URL → VCS → Source →
  BuildSystem → BuildRequires → Requires` 全部字段且按此顺序出现（字段
  缺一即报错），且 `%description` / `%files` / `%changelog` /
  `%package` / `%prep` / `%build` / `%install` / `%check` 段落之间
  必须用空行隔开（`%if` 条件块后紧跟段落属合法写法）。
- 规则文档 `docs/check-spdx-header.md`，README 增加 Hooks 列表。
- 规则文档 `docs/check-spec-structure.md`。
- 扫描结果目录 `openruyi-scan-results/`，存放对 openRuyi 仓库的
  各规则扫描结果（`check-spdx-header-results.md`、
  `check-spec-structure-results.md`）。

### 移除

- 首批 hooks 及其注册、测试与文档已移除，规则列表暂为空：
  - `check-ast` / `check-yaml` / `check-executables-have-shebangs` /
    `trailing-whitespace` / `require-ascii`。
