# check-spdx-header 扫描结果

> 扫描仓库：[openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) `main` 分支
> 扫描时间：2026-08-21
> 扫描文件数：5337 个 `.spec` 文件
> 不合规：**4 个**

## 结果

| openRuyi 仓库文件链接 | 问题原因简述 |
| --- | --- |
| [SPECS/go-github-google-certtostore/go-github-google-certtostore.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-google-certtostore/go-github-google-certtostore.spec) | `SPDX-License-Identifier` 为 `Apache-2.0`，应为 `MulanPSL-2.0` |
| [SPECS/go-github-opencontainers-runtime-tools/go-github-opencontainers-runtime-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-opencontainers-runtime-tools/go-github-opencontainers-runtime-tools.spec) | `SPDX-License-Identifier` 为 `Apache-2.0`，应为 `MulanPSL-2.0` |
| [SPECS/go-github-stefanberger-go-pkcs11uri/go-github-stefanberger-go-pkcs11uri.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-stefanberger-go-pkcs11uri/go-github-stefanberger-go-pkcs11uri.spec) | `SPDX-License-Identifier` 为 `Apache-2.0`，应为 `MulanPSL-2.0` |
| [SPECS/llvmir-converter/llvmir-converter.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/llvmir-converter/llvmir-converter.spec) | `SPDX-License-Identifier` 为 `Apache-2.0`，应为 `MulanPSL-2.0` |

## 说明

本次扫描基于 [check-spdx-header](../docs/check-spdx-header.md) 规则的校验逻辑：

- 头部必须包含 ISCAS 与 openRuyi 两条 `SPDX-FileCopyrightText` 声明；
- 尾部必须包含 `SPDX-License-Identifier: MulanPSL-2.0`。

5331 个文件（99.9%）头部完全合规；唯一问题集中在 4 个 Go 相关包（`go-github-*` 与 `llvmir-converter`）使用了 `Apache-2.0` 许可证标识。
