# check-spec-version 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库的 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-version` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 违规 |
| --- | ---: | ---: |
| 5337 | 5331 | 6 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| 版本号中的 `_` 应替换为 `.` | 2 |
| 预发布标记应转为小写并在字母前加 `~` | 2 |
| 快照版本应以 `<version>+<scm><YYYYMMDD>.<revision>` 结尾 | 2 |

## 问题清单（6 条）

| # | spec 文件 | `Version` 值 | 问题类型 |
| --- | --- | --- | --- |
| 1 | [go-github-stefanberger-go-pkcs11uri/go-github-stefanberger-go-pkcs11uri.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-stefanberger-go-pkcs11uri/go-github-stefanberger-go-pkcs11uri.spec) | `0+git202608018.7828495` | 快照版本应以 `<version>+<scm><YYYYMMDD>.<revision>` 结尾 |
| 2 | [iozone/iozone.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iozone/iozone.spec) | `3_508` | 版本号中的 `_` 应替换为 `.` |
| 3 | [libcaca/libcaca.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcaca/libcaca.spec) | `0.99.beta20` | 预发布标记应转为小写并在字母前加 `~` |
| 4 | [libcdio-paranoia/libcdio-paranoia.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcdio-paranoia/libcdio-paranoia.spec) | `10.2+2.0.2` | 快照版本应以 `<version>+<scm><YYYYMMDD>.<revision>` 结尾 |
| 5 | [libftdi/libftdi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libftdi/libftdi.spec) | `1.6rc1` | 预发布标记应转为小写并在字母前加 `~` |
| 6 | [lmbench/lmbench.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lmbench/lmbench.spec) | `3.0_a9` | 版本号中的 `_` 应替换为 `.` |
