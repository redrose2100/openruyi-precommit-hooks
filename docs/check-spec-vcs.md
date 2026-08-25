# check-spec-vcs

校验 Spec 文件的 `VCS` 字段是否符合 openRuyi 打包规范中的 VCS 要求。

主要检查点：

- `VCS:` 字段应指向源码仓库，用于定位源代码；当 `URL:` 字段已指向源码仓库时，`VCS:` 可省略。
- 如果仓库不可用或确实没有源代码仓库，必须在 `VCS` 字段位置写注释，且注释行**保留前缀** `# VCS:`，内容为 `No VCS link available`，例如：

  `# VCS: No VCS link available`

- 当源码托管于 Git 时，建议使用可克隆链接形式（带 `git:` 前缀），例如：

  `VCS:            git:https://git.example.org/project.git`

- 对包含宏展开（`%{...}`）的值，静态检查器将跳过以避免误报。

实现与运行：

- 规则实现位于 `openruyi_precommit_hooks/check_spec_vcs.py`。
- 在含有 `SPECS/` 工作树的环境中，可按如下方式运行：

```bash
python -m openruyi_precommit_hooks.check_spec_vcs SPECS/**/*.spec
```

如果需要将检查集成到 `pre-commit`，请在 `.pre-commit-hooks.yaml` 中声明对应 hook 元数据并在 `README.md` 中同步更新 Hooks 列表。
