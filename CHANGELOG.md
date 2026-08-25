# CHANGELOG

## 未发布

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

## 0.1.0 (2026-08-20)

### 新增

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
