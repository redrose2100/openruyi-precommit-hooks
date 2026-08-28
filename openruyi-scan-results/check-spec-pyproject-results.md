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
| 1 | [python-curl-cffi/python-curl-cffi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-curl-cffi/python-curl-cffi.spec) | — | 头部 `BuildRequires` 未声明 `pyproject-rpm-macros`（构建宏的提供者，缺少将导致 `%pyproject_buildrequires` 等宏不可用） |
| 2 | [python-linux-procfs/python-linux-procfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-linux-procfs/python-linux-procfs.spec) | — | 头部 `BuildRequires` 未声明 `pyproject-rpm-macros`（构建宏的提供者，缺少将导致 `%pyproject_buildrequires` 等宏不可用） |
| 3 | [python-pytest-xdist/python-pytest-xdist.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-xdist/python-pytest-xdist.spec) | — | 头部 `BuildRequires` 未声明 `pyproject-rpm-macros`（构建宏的提供者，缺少将导致 `%pyproject_buildrequires` 等宏不可用） |
| 4 | [python-setuptools-gettext/python-setuptools-gettext.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-setuptools-gettext/python-setuptools-gettext.spec) | — | 头部 `BuildRequires` 未声明 `pyproject-rpm-macros`（构建宏的提供者，缺少将导致 `%pyproject_buildrequires` 等宏不可用） |
| 5 | [python-tabulate/python-tabulate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tabulate/python-tabulate.spec) | — | 头部 `BuildRequires` 未声明 `pyproject-rpm-macros`（构建宏的提供者，缺少将导致 `%pyproject_buildrequires` 等宏不可用） |
| 6 | [python-torchvision/python-torchvision.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-torchvision/python-torchvision.spec) | — | 头部 `BuildRequires` 未声明 `pyproject-rpm-macros`（构建宏的提供者，缺少将导致 `%pyproject_buildrequires` 等宏不可用） |

### `BuildOption(check)` 上方无原因注释（61 条）

| # | spec 文件 | 行号 | 问题 |
| --- | --- | ---: | --- |
| 1 | [python-Whoosh/python-Whoosh.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-Whoosh/python-Whoosh.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-Whoosh/python-Whoosh.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 2 | [python-accelerate/python-accelerate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-accelerate/python-accelerate.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-accelerate/python-accelerate.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 3 | [python-alembic/python-alembic.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-alembic/python-alembic.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-alembic/python-alembic.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 4 | [python-argon2-cffi-bindings/python-argon2-cffi-bindings.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-argon2-cffi-bindings/python-argon2-cffi-bindings.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-argon2-cffi-bindings/python-argon2-cffi-bindings.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 5 | [python-beaker/python-beaker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-beaker/python-beaker.spec) | [26](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-beaker/python-beaker.spec#L26) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 6 | [python-botocore/python-botocore.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-botocore/python-botocore.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-botocore/python-botocore.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 7 | [python-cython/python-cython.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cython/python-cython.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-cython/python-cython.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 8 | [python-datasets/python-datasets.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-datasets/python-datasets.spec) | [26](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-datasets/python-datasets.spec#L26) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 9 | [python-depyf/python-depyf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-depyf/python-depyf.spec) | [25](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-depyf/python-depyf.spec#L25) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 10 | [python-docstring-parser/python-docstring-parser.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-docstring-parser/python-docstring-parser.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-docstring-parser/python-docstring-parser.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 11 | [python-email-validator/python-email-validator.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-email-validator/python-email-validator.spec) | [23](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-email-validator/python-email-validator.spec#L23) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 12 | [python-ffmpy/python-ffmpy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ffmpy/python-ffmpy.spec) | [29](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-ffmpy/python-ffmpy.spec#L29) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 13 | [python-fonttools/python-fonttools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fonttools/python-fonttools.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fonttools/python-fonttools.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 14 | [python-fsspec/python-fsspec.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fsspec/python-fsspec.spec) | [23](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-fsspec/python-fsspec.spec#L23) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 15 | [python-gevent/python-gevent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gevent/python-gevent.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gevent/python-gevent.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 16 | [python-gguf/python-gguf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gguf/python-gguf.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gguf/python-gguf.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 17 | [python-glyphslib/python-glyphslib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-glyphslib/python-glyphslib.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-glyphslib/python-glyphslib.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 18 | [python-greenlet/python-greenlet.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-greenlet/python-greenlet.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-greenlet/python-greenlet.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 19 | [python-gssapi/python-gssapi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gssapi/python-gssapi.spec) | [20](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gssapi/python-gssapi.spec#L20) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 20 | [python-gunicorn/python-gunicorn.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gunicorn/python-gunicorn.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-gunicorn/python-gunicorn.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 21 | [python-httpx-sse/python-httpx-sse.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-httpx-sse/python-httpx-sse.spec) | [26](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-httpx-sse/python-httpx-sse.spec#L26) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 22 | [python-id/python-id.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-id/python-id.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-id/python-id.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 23 | [python-kernels-data/python-kernels-data.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-kernels-data/python-kernels-data.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-kernels-data/python-kernels-data.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 24 | [python-kernels/python-kernels.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-kernels/python-kernels.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-kernels/python-kernels.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 25 | [python-lm-format-enforcer/python-lm-format-enforcer.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-lm-format-enforcer/python-lm-format-enforcer.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-lm-format-enforcer/python-lm-format-enforcer.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 26 | [python-matplotlib/python-matplotlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-matplotlib/python-matplotlib.spec) | [25](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-matplotlib/python-matplotlib.spec#L25) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 27 | [python-mcp/python-mcp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mcp/python-mcp.spec) | [25](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-mcp/python-mcp.spec#L25) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 28 | [python-multipart/python-multipart.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-multipart/python-multipart.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-multipart/python-multipart.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 29 | [python-multiprocess/python-multiprocess.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-multiprocess/python-multiprocess.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-multiprocess/python-multiprocess.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 30 | [python-nltk/python-nltk.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-nltk/python-nltk.spec) | [23](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-nltk/python-nltk.spec#L23) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 31 | [python-passlib/python-passlib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-passlib/python-passlib.spec) | [24](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-passlib/python-passlib.spec#L24) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 32 | [python-peft/python-peft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-peft/python-peft.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-peft/python-peft.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 33 | [python-plac/python-plac.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-plac/python-plac.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-plac/python-plac.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 34 | [python-portalocker/python-portalocker.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-portalocker/python-portalocker.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-portalocker/python-portalocker.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 35 | [python-progressbar2/python-progressbar2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-progressbar2/python-progressbar2.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-progressbar2/python-progressbar2.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 36 | [python-prometheus-client/python-prometheus-client.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-prometheus-client/python-prometheus-client.spec) | [23](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-prometheus-client/python-prometheus-client.spec#L23) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 37 | [python-pyfakefs/python-pyfakefs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyfakefs/python-pyfakefs.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyfakefs/python-pyfakefs.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 38 | [python-pygments/python-pygments.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pygments/python-pygments.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pygments/python-pygments.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 39 | [python-pyroute2/python-pyroute2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyroute2/python-pyroute2.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyroute2/python-pyroute2.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 40 | [python-python-json-logger/python-python-json-logger.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-json-logger/python-python-json-logger.spec) | [23](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-json-logger/python-python-json-logger.spec#L23) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 41 | [python-pyvex/python-pyvex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyvex/python-pyvex.spec) | [23](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyvex/python-pyvex.spec#L23) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 42 | [python-pyyaml-ft/python-pyyaml-ft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyyaml-ft/python-pyyaml-ft.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyyaml-ft/python-pyyaml-ft.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 43 | [python-redis/python-redis.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-redis/python-redis.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-redis/python-redis.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 44 | [python-rfc3161-client/python-rfc3161-client.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rfc3161-client/python-rfc3161-client.spec) | [26](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rfc3161-client/python-rfc3161-client.spec#L26) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 45 | [python-rfc8785/python-rfc8785.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rfc8785/python-rfc8785.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rfc8785/python-rfc8785.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 46 | [python-rouge-score/python-rouge-score.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rouge-score/python-rouge-score.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-rouge-score/python-rouge-score.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 47 | [python-sacremoses/python-sacremoses.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sacremoses/python-sacremoses.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sacremoses/python-sacremoses.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 48 | [python-schedulefree/python-schedulefree.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-schedulefree/python-schedulefree.spec) | [23](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-schedulefree/python-schedulefree.spec#L23) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 49 | [python-scikit-learn/python-scikit-learn.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-scikit-learn/python-scikit-learn.spec) | [25](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-scikit-learn/python-scikit-learn.spec#L25) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 50 | [python-securesystemslib/python-securesystemslib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-securesystemslib/python-securesystemslib.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-securesystemslib/python-securesystemslib.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 51 | [python-sigstore-models/python-sigstore-models.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sigstore-models/python-sigstore-models.spec) | [23](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sigstore-models/python-sigstore-models.spec#L23) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 52 | [python-sigstore-rekor-types/python-sigstore-rekor-types.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sigstore-rekor-types/python-sigstore-rekor-types.spec) | [23](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sigstore-rekor-types/python-sigstore-rekor-types.spec#L23) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 53 | [python-sigstore/python-sigstore.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sigstore/python-sigstore.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sigstore/python-sigstore.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 54 | [python-sqlalchemy/python-sqlalchemy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sqlalchemy/python-sqlalchemy.spec) | [21](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sqlalchemy/python-sqlalchemy.spec#L21) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 55 | [python-sse-starlette/python-sse-starlette.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sse-starlette/python-sse-starlette.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-sse-starlette/python-sse-starlette.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 56 | [python-transformers/python-transformers.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-transformers/python-transformers.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-transformers/python-transformers.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 57 | [python-triton/python-triton.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-triton/python-triton.spec) | [23](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-triton/python-triton.spec#L23) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 58 | [python-tuf/python-tuf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tuf/python-tuf.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-tuf/python-tuf.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 59 | [python-unidic-lite/python-unidic-lite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-unidic-lite/python-unidic-lite.spec) | [20](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-unidic-lite/python-unidic-lite.spec#L20) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 60 | [python-uvicorn/python-uvicorn.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-uvicorn/python-uvicorn.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-uvicorn/python-uvicorn.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |
| 61 | [python-zope-interface/python-zope-interface.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-zope-interface/python-zope-interface.spec) | [22](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-zope-interface/python-zope-interface.spec#L22) | `BuildOption(check)` 上方缺少原因注释（跳过模块须写明理由） |


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
