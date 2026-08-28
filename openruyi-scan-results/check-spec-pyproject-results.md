# check-spec-pyproject 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-pyproject` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | pyproject | 通过 | 问题 |
| --- | ---: | ---: | ---: |
| 5267 | 852 | 785 | 67 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | ---: |
| 缺失 `pyproject-rpm-macros` | 6 |
| `BuildOption(install)` 为空 | 0 |
| `BuildOption(check)` 上方无原因注释 | 61 |

## 问题清单（67 条）

### `BuildRequires` 未声明 `pyproject-rpm-macros`（6 条）

| # | spec 文件 | 行号 | 问题 |
| --- | --- | ---: | --- |
| 1 | `python-curl-cffi/python-curl-cffi.spec` | — | `BuildSystem is pyproject; BuildRequires must declare pyproject-rpm-macros` |
| 2 | `python-linux-procfs/python-linux-procfs.spec` | — | `BuildSystem is pyproject; BuildRequires must declare pyproject-rpm-macros` |
| 3 | `python-pytest-xdist/python-pytest-xdist.spec` | — | `BuildSystem is pyproject; BuildRequires must declare pyproject-rpm-macros` |
| 4 | `python-setuptools-gettext/python-setuptools-gettext.spec` | — | `BuildSystem is pyproject; BuildRequires must declare pyproject-rpm-macros` |
| 5 | `python-tabulate/python-tabulate.spec` | — | `BuildSystem is pyproject; BuildRequires must declare pyproject-rpm-macros` |
| 6 | `python-torchvision/python-torchvision.spec` | — | `BuildSystem is pyproject; BuildRequires must declare pyproject-rpm-macros` |

### `BuildOption(check)` 上方无原因注释（61 条）

| # | spec 文件 | 行号 | 问题 |
| --- | --- | ---: | --- |
| 1 | `python-Whoosh/python-Whoosh.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 2 | `python-accelerate/python-accelerate.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 3 | `python-alembic/python-alembic.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 4 | `python-argon2-cffi-bindings/python-argon2-cffi-bindings.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 5 | `python-beaker/python-beaker.spec` | 26 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 6 | `python-botocore/python-botocore.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 7 | `python-cython/python-cython.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 8 | `python-datasets/python-datasets.spec` | 26 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 9 | `python-depyf/python-depyf.spec` | 25 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 10 | `python-docstring-parser/python-docstring-parser.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 11 | `python-email-validator/python-email-validator.spec` | 23 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 12 | `python-ffmpy/python-ffmpy.spec` | 29 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 13 | `python-fonttools/python-fonttools.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 14 | `python-fsspec/python-fsspec.spec` | 23 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 15 | `python-gevent/python-gevent.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 16 | `python-gguf/python-gguf.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 17 | `python-glyphslib/python-glyphslib.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 18 | `python-greenlet/python-greenlet.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 19 | `python-gssapi/python-gssapi.spec` | 20 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 20 | `python-gunicorn/python-gunicorn.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 21 | `python-httpx-sse/python-httpx-sse.spec` | 26 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 22 | `python-id/python-id.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 23 | `python-kernels-data/python-kernels-data.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 24 | `python-kernels/python-kernels.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 25 | `python-lm-format-enforcer/python-lm-format-enforcer.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 26 | `python-matplotlib/python-matplotlib.spec` | 25 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 27 | `python-mcp/python-mcp.spec` | 25 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 28 | `python-multipart/python-multipart.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 29 | `python-multiprocess/python-multiprocess.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 30 | `python-nltk/python-nltk.spec` | 23 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 31 | `python-passlib/python-passlib.spec` | 24 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 32 | `python-peft/python-peft.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 33 | `python-plac/python-plac.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 34 | `python-portalocker/python-portalocker.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 35 | `python-progressbar2/python-progressbar2.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 36 | `python-prometheus-client/python-prometheus-client.spec` | 23 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 37 | `python-pyfakefs/python-pyfakefs.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 38 | `python-pygments/python-pygments.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 39 | `python-pyroute2/python-pyroute2.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 40 | `python-python-json-logger/python-python-json-logger.spec` | 23 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 41 | `python-pyvex/python-pyvex.spec` | 23 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 42 | `python-pyyaml-ft/python-pyyaml-ft.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 43 | `python-redis/python-redis.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 44 | `python-rfc3161-client/python-rfc3161-client.spec` | 26 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 45 | `python-rfc8785/python-rfc8785.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 46 | `python-rouge-score/python-rouge-score.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 47 | `python-sacremoses/python-sacremoses.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 48 | `python-schedulefree/python-schedulefree.spec` | 23 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 49 | `python-scikit-learn/python-scikit-learn.spec` | 25 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 50 | `python-securesystemslib/python-securesystemslib.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 51 | `python-sigstore-models/python-sigstore-models.spec` | 23 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 52 | `python-sigstore-rekor-types/python-sigstore-rekor-types.spec` | 23 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 53 | `python-sigstore/python-sigstore.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 54 | `python-sqlalchemy/python-sqlalchemy.spec` | 21 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 55 | `python-sse-starlette/python-sse-starlette.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 56 | `python-transformers/python-transformers.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 57 | `python-triton/python-triton.spec` | 23 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 58 | `python-tuf/python-tuf.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 59 | `python-unidic-lite/python-unidic-lite.spec` | 20 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 60 | `python-uvicorn/python-uvicorn.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |
| 61 | `python-zope-interface/python-zope-interface.spec` | 22 | `BuildOption(check) must be preceded by a comment explaining why the modules are skipped` |


## 说明

- 规则仅适用于 `BuildSystem: pyproject` 的 spec（共 852 个）：
  1. 头部区域 `BuildRequires` 必须声明 `pyproject-rpm-macros`；
  2. `BuildOption(install)` 必须携带模块名（非空）；
  3. 每个 `BuildOption(check)` 块首行上方必须有原因注释。
- 其中 851 个 spec 存在 `BuildOption(install)`，
  671 个以 `-l` 开头（`-l` 为建议性参数，不作为检查点）。
- 其余 spec 不适用本规则，未计入统计。
- `%package` 子包段落内的 `BuildRequires`、宏展开值（如
  `%{?foo}`）以及注释行不视为有效声明。
- `pkgconfig(python3)`、`-l` 参数、`%generate_buildrequires`、
  置空 `%check` 等为建议性/条件性要求，未纳入强检查点。

> 规则说明：[docs/check-spec-pyproject.md](../docs/check-spec-pyproject.md)
