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

## 可用的 Hooks（共 26 个）

| # | Hook ID | 说明 | 文档 |
| --- | --- | --- | --- |
| 1 | `check-spdx-header` | 校验 spec 文件起始位置包含 SPDX 版权与许可证声明（ISCAS + openRuyi Contributors + MulanPSL-2.0） | [docs/check-spdx-header.md](docs/check-spdx-header.md) |
| 2 | `check-spec-structure` | 校验 spec 文件必填头部字段（全字段必填 + 顺序）与段落之间空行分隔 | [docs/check-spec-structure.md](docs/check-spec-structure.md) |
| 3 | `check-spec-name` | 校验 spec 文件 `Name` 字段符合命名规则（小写、短横线分隔、不编码 ABI/版本号） | [docs/check-spec-name.md](docs/check-spec-name.md) |
| 4 | `check-spec-version` | 校验 spec 文件 `Version` 字段按官方规则规范化（点号/日期直用、`~` 预发布、`-`/`_` 换点、哈希转快照格式） | [docs/check-spec-version.md](docs/check-spec-version.md) |
| 5 | `check-spec-release` | 校验 spec 文件 `Release` 字段符合官方 Release 规则（使用 `%autorelease`、修订序号从 `1` 开始的整数、不硬编码发行版后缀、不覆盖 `dist` 宏） | [docs/check-spec-release.md](docs/check-spec-release.md) |
| 6 | `check-spec-summary` | 校验 spec 文件 `Summary` 字段符合官方 Summary 规则（简短英文描述、不以英文句号 `.` 结尾） | [docs/check-spec-summary.md](docs/check-spec-summary.md) |
| 7 | `check-spec-license` | 校验 spec 文件 `License` 字段使用合法 SPDX 标识符或表达式（大写 `AND`/`OR`/`WITH` 连接符、不用逗号分隔、不用老式 `+` 后缀） | [docs/check-spec-license.md](docs/check-spec-license.md) |
| 8 | `check-spec-url` | 校验 spec 文件 `URL` 字段为合法的 http(s) 官网或源码仓库链接（不用 `%{name}` 等宏拼接） | [docs/check-spec-url.md](docs/check-spec-url.md) |
| 9 | `check-spec-source` | 校验 spec 文件网络来源 `Source` 行前有 `#!RemoteAsset` 注释并携带 sha256 校验值（SourceForge 链接须用 `downloads.sourceforge.net`） | [docs/check-spec-source.md](docs/check-spec-source.md) |
| 10 | `check-spec-vcs` | 校验 spec 文件 `VCS` 字段为可克隆的源码仓库链接（`git:` 前缀或指向源码托管平台的 http(s) 链接），无可用链接时须写 `# VCS: No VCS link available` 注释 | [docs/check-spec-vcs.md](docs/check-spec-vcs.md) |
| 11 | `check-spec-buildarch` | 校验 spec 文件 `BuildArch` 字段声明目标架构（`noarch`）、位于最后一个 `Source` 与 `BuildSystem` 之间且不为空 | [docs/check-spec-buildarch.md](docs/check-spec-buildarch.md) |
| 12 | `check-spec-buildsystem` | 校验 spec 文件 `BuildSystem` 字段取值合法（官方列出的构建系统或新增值），为空时须以注释说明原因 | [docs/check-spec-buildsystem.md](docs/check-spec-buildsystem.md) |
| 13 | `check-spec-buildoption` | 校验 spec 文件 `BuildOption` 字段符合官方 BuildOption 规则（阶段名称必须写明、冒号后双空格分隔、位于 `BuildSystem` 与 `BuildRequires` 之间、按 `build`/`install`/`check` 顺序书写） | [docs/check-spec-buildoption.md](docs/check-spec-buildoption.md) |
| 14 | `check-spec-buildrequires` | 校验 spec 文件 `BuildRequires` 字段符合官方 BuildRequires 规则（依赖项按"一行一个依赖包"书写、值非空） | [docs/check-spec-buildrequires.md](docs/check-spec-buildrequires.md) |
| 15 | `check-spec-requires` | 校验 spec 文件 `Requires` 字段符合官方 Requires 规则（运行期依赖按"一行一个依赖包"书写、值非空；`%package` 子包内同样检查） | [docs/check-spec-requires.md](docs/check-spec-requires.md) |
| 16 | `check-spec-patch` | 校验 spec 文件 `Patch` 字段符合官方 Patch 规则（每个 `Patch` 上方须有注释、文件名以四位数字开头且前缀在 `0001-2999` 范围、补丁数 > 3 时用 `%patchlist`、位于 `BuildSystem` 与 `BuildOption`/`BuildRequires` 之间） | [docs/check-spec-patch.md](docs/check-spec-patch.md) |
| 17 | `check-spec-files` | 校验 spec 文件 `%files` 段落符合官方 Files 规则（许可证文本必须 `%license`、文档应当 `%doc`、不得重复列出同一文件、不得含 `.la` 归档、本地化必须用 `%find_lang` 而非通配 `%{_datadir}/locale/*`） | [docs/check-spec-files.md](docs/check-spec-files.md) |
| 18 | `check-spec-changelog` | 校验 spec 文件 `%changelog` 段落内容必须为 `%autochangelog`（不得手写更新日志；`%{?autochangelog}` 条件宏同样合规） | [docs/check-spec-changelog.md](docs/check-spec-changelog.md) |
| 19 | `check-spec-bcond` | 校验 spec 文件条件构建开关符合官方规则（用 `%bcond <name> <0\|1>` 声明、不用旧式 `%bcond_with`/`%bcond_without`、`%{with}/%{without}` 引用不得指向未声明开关） | [docs/check-spec-bcond.md](docs/check-spec-bcond.md) |
| 20 | `check-spec-autotools` | 校验 `BuildSystem: autotools` 的 spec 文件必须在头部 `BuildRequires` 声明 `autoconf`、`automake`、`libtool`、`make` 四项依赖（gcc 预装豁免） | [docs/check-spec-autotools.md](docs/check-spec-autotools.md) |
| 21 | `check-spec-cmake` | 校验 `BuildSystem: cmake` 的 spec 文件必须在头部 `BuildRequires` 声明 `cmake` 依赖（gcc 预装豁免） | [docs/check-spec-cmake.md](docs/check-spec-cmake.md) |
| 22 | `check-spec-golang` | 校验 `BuildSystem: golang`/`golangmodules` 的 spec 文件必须在头部 `BuildRequires` 声明 `go`、`go-rpm-macros` 两项依赖（无预装豁免）；`golangmodules`（纯库）必须声明 `Provides: go(<import path>)`，且每条 `Provides: go(...)` 必须带 `= <version>` 版本约束 | [docs/check-spec-golang.md](docs/check-spec-golang.md) |
| 23 | `check-spec-meson` | 校验 `BuildSystem: meson` 的 spec 文件必须在头部 `BuildRequires` 声明 `meson` 依赖（无预装豁免） | [docs/check-spec-meson.md](docs/check-spec-meson.md) |
| 24 | `check-spec-perl` | 校验 `BuildSystem: perlbuild`/`perlmaker` 的 spec 文件必须在头部 `BuildRequires` 声明 `perl-rpm-packaging`、`perl-rpm-macros`、`perl-macros` 三项依赖（无预装豁免）；`Requires:`/`Provides:` 必须使用 `perl(MODULE)` 虚拟依赖格式，不得直接写 `perl-CPANDIST` 包名（同名 `%package` 子包除外） | [docs/check-spec-perl.md](docs/check-spec-perl.md) |
| 25 | `check-spec-pyproject` | 校验 `BuildSystem: pyproject` 的 spec 文件必须在头部 `BuildRequires` 声明 `pyproject-rpm-macros`、`BuildOption(install)` 必须携带模块名、`BuildOption(check)` 上方必须写明跳过原因注释 | [docs/check-spec-pyproject.md](docs/check-spec-pyproject.md) |
| 26 | `check-spec-rust` | 校验 `BuildSystem: rust`/`rustcrates` 的 spec 文件在头部 `BuildRequires` 声明对应必需依赖（`rust`+`rust-rpm-macros` 或仅 `rust-rpm-macros`）、`rustcrates` 不得用 `BuildOption(build)` 覆盖构建阶段、`BuildOption(check)` 上方必须写明跳过原因注释 | [docs/check-spec-rust.md](docs/check-spec-rust.md) |

## 新增一个 Hook

1. 在 `openruyi_precommit_hooks/` 下新建 `your_hook.py`，实现
   `main(argv=None) -> int`，返回非 0 表示检查失败。
2. 在 `setup.cfg` 的 `[options.entry_points] console_scripts` 中注册命令行入口。
3. 在 `.pre-commit-hooks.yaml` 中声明新的 hook 元数据。
4. 在 `tests/` 下新建对应测试，测试资源放在 `testing/resources/`。
5. 更新 `README.md` 的 Hooks 列表与标题「可用的 Hooks（共 N 个）」
   中的总数（每新增一个 hook 数量 +1），并更新 `CHANGELOG.md`。

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
