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

当前规则列表为空，仓库仅保留了框架（打包配置、测试基础设施、CI）。
后续新增规则时，将在此处补充文档。

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
