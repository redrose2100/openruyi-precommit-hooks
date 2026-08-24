# openruyi-precommit-hooks

Some out-of-the-box hooks for [pre-commit](https://pre-commit.com).

本项目参考 [pre-commit/pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
的组织方式，为 openruyi 相关仓库提供开箱即用的 git hooks。

## 使用方式

在你的 `.pre-commit-config.yaml` 中添加本仓库：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0  # 填写你要引用的版本
    hooks:
    # -   id: ...
```

## 可用的 Hooks

| Hook ID | 说明 | 文档 |
| --- | --- | --- |
| `check-spdx-header` | 校验 spec 文件起始位置包含 SPDX 版权与许可证声明（ISCAS + openRuyi Contributors + MulanPSL-2.0） | [docs/check-spdx-header.md](docs/check-spdx-header.md) |
| `check-spec-structure` | 校验 spec 文件必填头部字段（全字段必填 + 顺序）与段落之间空行分隔 | [docs/check-spec-structure.md](docs/check-spec-structure.md) |
| `check-spec-name` | 校验 spec 文件 `Name` 字段符合命名规则（小写、短横线分隔、不编码 ABI/版本号） | [docs/check-spec-name.md](docs/check-spec-name.md) |
| `check-spec-version` | 校验 spec 文件 `Version` 字段按官方规则规范化（点号/日期直用、`~` 预发布、`-`/`_` 换点、哈希转快照格式） | [docs/check-spec-version.md](docs/check-spec-version.md) |
| `check-spec-release` | 校验 spec 文件 `Release` 字段符合官方 Release 规则（使用 `%autorelease`、修订序号从 `1` 开始的整数、不硬编码发行版后缀、不覆盖 `dist` 宏） | [docs/check-spec-release.md](docs/check-spec-release.md) |
| `check-spec-summary` | 校验 spec 文件 `Summary` 字段符合官方 Summary 规则（简短英文描述、不以英文句号 `.` 结尾） | [docs/check-spec-summary.md](docs/check-spec-summary.md) |
| `check-spec-license` | 校验 spec 文件 `License` 字段使用合法 SPDX 标识符或表达式（大写 `AND`/`OR`/`WITH` 连接符、不用逗号分隔、不用老式 `+` 后缀） | [docs/check-spec-license.md](docs/check-spec-license.md) |

## 新增一个 Hook

1. 在 `openruyi_precommit_hooks/` 下新建 `your_hook.py`，实现
   `main(argv=None) -> int`，返回非 0 表示检查失败。
2. 在 `setup.cfg` 的 `[options.entry_points] console_scripts` 中注册命令行入口。
3. 在 `.pre-commit-hooks.yaml` 中声明新的 hook 元数据。
4. 在 `tests/` 下新建对应测试，测试资源放在 `testing/resources/`。
5. 更新 `README.md` 的 Hooks 列表与 `CHANGELOG.md`。

## 提交规范

本仓库的提交信息遵循 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/)
规范，格式为：

```
<type>(<scope>): <description>
```

常见的 `type`（完整列表，参考 Angular Commit Convention）：

| type | 用途 |
|------|------|
| `feat` | 新增功能（如新增一个 hook / 新特性） |
| `fix` | 修复 Bug |
| `docs` | 文档改动 |
| `style` | 不影响逻辑的格式改动（空格、分号、缩进等） |
| `refactor` | 重构，不改变外部行为 |
| `perf` | 性能优化 |
| `test` | 新增或修改测试 |
| `build` | 构建系统或外部依赖的改动（如 `setup.cfg`、`requirements-dev.txt`） |
| `ci` | CI 配置或脚本的改动（`ci.yml`、`.github/` 等） |
| `chore` | 其他维护性改动，不修改源码或测试（如 `.gitignore`、工具配置） |
| `revert` | 回滚之前的提交 |

补充说明：

- **scope**（可选）：用于缩小影响范围，如 `feat(check-yaml): ...`。
- **破坏性变更**：在 `type` 后加 `!`（如 `feat!: ...`），并在正文中写明
  `BREAKING CHANGE:` 说明。

示例：

```
feat: add check-commit-msg hook
fix: handle empty stdin in check-yaml
perf: cache added_files results across invocations
style: format code with autopep8
chore: bump pre-commit-hooks to v6.0.0
docs: add commit message conventions
```

## 开发

```sh
# 安装开发依赖
pip install -r requirements-dev.txt
pip install -e .

# 运行测试
python -m pytest tests

# 运行本项目自身的 pre-commit
pre-commit run --all-files

# 或使用 tox
tox
```

## License

MIT
