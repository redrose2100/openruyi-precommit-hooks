# CHANGELOG

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
