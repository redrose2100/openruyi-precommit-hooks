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
    -   id: check-ast
    -   id: check-yaml
    # -   id: ...
```

## 可用的 Hooks

### `check-ast`
简单地检查文件是否能够被解析为合法的 Python。

### `check-executables-have-shebangs`
确保（非二进制）可执行文件带有 shebang。

### `check-yaml`
尝试加载所有 yaml 文件以验证语法。
  - `--allow-multiple-documents` / `-m` - 允许使用
    [多文档语法](http://www.yaml.org/spec/1.2/spec.html#YAML) 的 yaml 文件。
  - `--unsafe` - 只做语法解析而不是加载文件。语法级检查允许扩展与不安全的
    构造，但会失去跨 yaml 实现的移植性保证，同时隐含
    `--allow-multiple-documents`。

### `require-ascii`
确保文件只包含 ASCII 字符。

### `trailing-whitespace`
去除行尾空白。
  - `--markdown-linebreak-ext EXT|*` - Markdown 文件保留行尾两空格（换行语义），
    可多次指定或以 `*` 表示所有文件。
  - `--chars CHARS` - 自定义需要从行尾剥离的字符集合。

## 新增一个 Hook

1. 在 `openruyi_precommit_hooks/` 下新建 `your_hook.py`，实现
   `main(argv=None) -> int`，返回非 0 表示检查失败。
2. 在 `setup.cfg` 的 `[options.entry_points] console_scripts` 中注册命令行入口。
3. 在 `.pre-commit-hooks.yaml` 中声明新的 hook 元数据。
4. 在 `tests/` 下新建对应测试，测试资源放在 `testing/resources/`。
5. 更新 `README.md` 的 Hooks 列表与 `CHANGELOG.md`。

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
