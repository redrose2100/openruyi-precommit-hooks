# check-spec-url 扫描结果

�?[openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库�?spec 文件
执行 `check-spec-url` 规则扫描，结果如下�?
## 结果概览

## 结果概览

| 扫描 spec 文件数 | 通过 | 违规 |
| --- | ---: | ---: |
| 5337 | 5330 | 7 |

## 违规类型分布

| 违规类型 | 数量 |
| --- | --- |
| 宏拼�?| 4 |
| �?http(s) 链接 | 3 |

## 违规清单�? 条）

| # | spec 文件 | URL �?| 违规类型 |
| --- | --- | --- | --- |
| 1 | [pocketfft/pocketfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pocketfft/pocketfft.spec) | `https://github.com/mreineck/%{name}` | 宏拼�?|
| 2 | [psutils/psutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/psutils/psutils.spec) | `https://github.com/rrthomas/%{name}` | 宏拼�?|
| 3 | [python-azure-storage-blob/python-azure-storage-blob.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-azure-storage-blob/python-azure-storage-blob.spec) | `https://pypi.org/project/%{srcname}/` | 宏拼�?|
| 4 | [xnnpack/xnnpack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xnnpack/xnnpack.spec) | `https://github.com/google/%{upstream_name}` | 宏拼�?|
| 5 | [rust-bssl-sys-0.1/rust-bssl-sys-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-bssl-sys-0.1/rust-bssl-sys-0.1.spec) | `FIXME` | �?http(s) 链接 |
| 6 | [rust-openssl-macros-0.1/rust-openssl-macros-0.1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-openssl-macros-0.1/rust-openssl-macros-0.1.spec) | `FIXME` | �?http(s) 链接 |
| 7 | [rust-spanned-0.4/rust-spanned-0.4.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rust-spanned-0.4/rust-spanned-0.4.spec) | `FIXME` | �?http(s) 链接 |

## 说明

- 宏拼接：`URL` 字段不得使用 `%{name}` 等宏进行拼接，应写成固定�?  永久链接，例�?`https://github.com/mreineck/%{name}` 应写�?  `https://github.com/mreineck/pocketfft`�?- �?http(s) 链接：`URL` 必须为软件包官方网站或源码仓库链接，�?  `http://` / `https://` 开头；`FIXME` 等占位符或裸主机名不是合法链接�?- 字段缺失�?7 �?spec �?`URL` 字段）由 `check-spec-structure` 规则覆盖�?  本规则不重复报告�?
> 规则说明�?[docs/check-spec-url.md](../docs/check-spec-url.md)�?
