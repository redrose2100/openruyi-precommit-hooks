# check-spdx-header 扫描结果

�?[openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库�?spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分�?`main`）执�?
`check-spdx-header` 规则的扫描结果�?

## 结果概览

## 结果概览

| 扫描 spec 文件数 | 通过 | 违规 |
| --- | ---: | ---: |
| 5337 | 5333 | 4 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| `SPDX-License-Identifier` �?`MulanPSL-2.0` | 4 |

## 问题清单�? 条）

| # | spec 文件 | 问题原因 |
| --- | --- | --- |
| 1 | [SPECS/go-github-google-certtostore/go-github-google-certtostore.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-google-certtostore/go-github-google-certtostore.spec) | `SPDX-License-Identifier` �?`Apache-2.0`，应�?`MulanPSL-2.0` |
| 2 | [SPECS/go-github-opencontainers-runtime-tools/go-github-opencontainers-runtime-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-opencontainers-runtime-tools/go-github-opencontainers-runtime-tools.spec) | `SPDX-License-Identifier` �?`Apache-2.0`，应�?`MulanPSL-2.0` |
| 3 | [SPECS/go-github-stefanberger-go-pkcs11uri/go-github-stefanberger-go-pkcs11uri.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-stefanberger-go-pkcs11uri/go-github-stefanberger-go-pkcs11uri.spec) | `SPDX-License-Identifier` �?`Apache-2.0`，应�?`MulanPSL-2.0` |
| 4 | [SPECS/llvmir-converter/llvmir-converter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvmir-converter/llvmir-converter.spec) | `SPDX-License-Identifier` �?`Apache-2.0`，应�?`MulanPSL-2.0` |

## 说明

本次扫描基于 [check-spdx-header](../docs/check-spdx-header.md) 规则的校验逻辑�?

- 头部必须包含 ISCAS �?openRuyi 两条 `SPDX-FileCopyrightText` 声明�?
- 尾部必须包含 `SPDX-License-Identifier: MulanPSL-2.0`�?

5331 个文件（99.9%）头部完全合规；唯一问题集中�?4 �?Go 相关包（`go-github-*` �?`llvmir-converter`）使用了 `Apache-2.0` 许可证标识�?
