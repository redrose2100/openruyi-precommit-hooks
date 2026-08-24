# check-spec-version 扫描结果

> 扫描仓库：[openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) `main` 分支
> 扫描时间：2026-08-24
> 扫描文件数：5337 个 `.spec` 文件
> 不合规：**6 个**

## 结果

| openRuyi 仓库文件链接 | `Version` 值 | 问题原因简述 |
| --- | --- | --- |
| [go-github-stefanberger-go-pkcs11uri/go-github-stefanberger-go-pkcs11uri.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/go-github-stefanberger-go-pkcs11uri/go-github-stefanberger-go-pkcs11uri.spec) | `0+git202608018.7828495` | 快照版本应以 `<version>+<scm><YYYYMMDD>.<revision>` 结尾 |
| [iozone/iozone.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iozone/iozone.spec) | `3_508` | 版本号中的 `_` 应替换为 `.` |
| [libcaca/libcaca.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcaca/libcaca.spec) | `0.99.beta20` | 预发布标记应转为小写并在字母前加 `~` |
| [libcdio-paranoia/libcdio-paranoia.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcdio-paranoia/libcdio-paranoia.spec) | `10.2+2.0.2` | 快照版本应以 `<version>+<scm><YYYYMMDD>.<revision>` 结尾 |
| [libftdi/libftdi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libftdi/libftdi.spec) | `1.6rc1` | 预发布标记应转为小写并在字母前加 `~` |
| [lmbench/lmbench.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lmbench/lmbench.spec) | `3.0_a9` | 版本号中的 `_` 应替换为 `.` |
