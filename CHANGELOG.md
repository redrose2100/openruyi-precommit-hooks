# CHANGELOG

## 未发布

### 变更

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

### 新增

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
