# CHANGELOG

## 0.1.0 (2026-08-20)

### 新增

- 项目框架：`setup.cfg` / `setup.py` 打包配置，`.pre-commit-hooks.yaml`
  对外 hooks 清单，`.pre-commit-config.yaml` 自举配置。
- 测试基础设施：`tests/`、`testing/`（`get_resource_path` / `git_commit`）、
  `resources/`，以及 `tox.ini`、`requirements-dev.txt`、GitHub Actions CI。
- 首批 hooks：
  - `check-ast`：检查 Python 语法。
  - `check-yaml`：校验 YAML 语法（支持 `--allow-multiple-documents`、
    `--unsafe`）。
  - `check-executables-have-shebangs`：检查可执行文件是否带有 shebang。
  - `trailing-whitespace`：去除行尾空白（支持 Markdown 行尾两空格保留）。
  - `require-ascii`：确保文件仅包含 ASCII 字符。
- 公共工具 `openruyi_precommit_hooks/util.py`：
  `cmd_output` / `added_files` / `zsplit` / `CalledProcessError`。