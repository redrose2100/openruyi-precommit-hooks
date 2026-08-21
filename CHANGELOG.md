# CHANGELOG

## 0.2.0 (2026-08-21)

### 新增

- 首个规则 hook `check-spdx-header`：校验 spec 文件起始位置包含
  SPDX 版权与许可证声明（ISCAS + openRuyi Project Contributors +
  `SPDX-License-Identifier: MulanPSL-2.0`），contributor 行为可选。
- 规则文档 `docs/check-spdx-header.md`，README 增加 Hooks 列表。
- 扫描结果目录 `openruyi-scan-results/`，存放对 openRuyi 仓库的
  各规则扫描结果（`check-spdx-header-results.md`）。

## 0.1.0 (2026-08-20)

### 新增

- 项目框架：`setup.cfg` / `setup.py` 打包配置，`.pre-commit-hooks.yaml`
  对外 hooks 清单，`.pre-commit-config.yaml` 自举配置。
- 测试基础设施：`tests/`、`testing/`（`get_resource_path` / `git_commit`）、
  `resources/`，以及 `tox.ini`、`requirements-dev.txt`、GitHub Actions CI。
- 公共工具 `openruyi_precommit_hooks/util.py`：
  `cmd_output` / `added_files` / `zsplit` / `CalledProcessError`。

### 移除

- 首批 hooks 及其注册、测试与文档已移除，规则列表暂为空：
  - `check-ast` / `check-yaml` / `check-executables-have-shebangs` /
    `trailing-whitespace` / `require-ascii`。
