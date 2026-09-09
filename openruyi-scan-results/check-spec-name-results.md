# check-spec-name 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库的 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-name` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| --- | ---: | ---: |
| 5337 | 5280 | 57 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| 包名非全小写 | 33 |
| 使用下划线 `_`，应优先用短横线 `-` | 24 |

## 问题清单（57 条）

| # | spec 文件 | `Name` 值 | 问题所在行数 | 问题类型 |
| --- | --- | --- | ---: | --- |
| 1 | [Catch2/Catch2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/Catch2/Catch2.spec) | `Catch2` | 9 | 包名非全小写 |
| 2 | [ModemManager/ModemManager.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ModemManager/ModemManager.spec) | `ModemManager` | 7 | 包名非全小写 |
| 3 | [NetworkManager/NetworkManager.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/NetworkManager/NetworkManager.spec) | `NetworkManager` | 12 | 包名非全小写 |
| 4 | [PackageKit-Qt/PackageKit-Qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/PackageKit-Qt/PackageKit-Qt.spec) | `PackageKit-Qt` | 7 | 包名非全小写 |
| 5 | [PackageKit/PackageKit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/PackageKit/PackageKit.spec) | `PackageKit` | 9 | 包名非全小写 |
| 6 | [SDL2/SDL2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/SDL2/SDL2.spec) | `SDL2` | 10 | 包名非全小写 |
| 7 | [SDL3/SDL3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/SDL3/SDL3.spec) | `SDL3` | 11 | 包名非全小写 |
| 8 | [Xwayland/Xwayland.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/Xwayland/Xwayland.spec) | `Xwayland` | 8 | 包名非全小写 |
| 9 | [libICE/libICE.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libICE/libICE.spec) | `libICE` | 9 | 包名非全小写 |
| 10 | [libSM/libSM.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libSM/libSM.spec) | `libSM` | 9 | 包名非全小写 |
| 11 | [libX11/libX11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libX11/libX11.spec) | `libX11` | 9 | 包名非全小写 |
| 12 | [libXScrnSaver/libXScrnSaver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXScrnSaver/libXScrnSaver.spec) | `libXScrnSaver` | 7 | 包名非全小写 |
| 13 | [libXau/libXau.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXau/libXau.spec) | `libXau` | 9 | 包名非全小写 |
| 14 | [libXcomposite/libXcomposite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXcomposite/libXcomposite.spec) | `libXcomposite` | 7 | 包名非全小写 |
| 15 | [libXcursor/libXcursor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXcursor/libXcursor.spec) | `libXcursor` | 7 | 包名非全小写 |
| 16 | [libXdamage/libXdamage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXdamage/libXdamage.spec) | `libXdamage` | 7 | 包名非全小写 |
| 17 | [libXdmcp/libXdmcp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXdmcp/libXdmcp.spec) | `libXdmcp` | 8 | 包名非全小写 |
| 18 | [libXext/libXext.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXext/libXext.spec) | `libXext` | 9 | 包名非全小写 |
| 19 | [libXfixes/libXfixes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXfixes/libXfixes.spec) | `libXfixes` | 9 | 包名非全小写 |
| 20 | [libXfont2/libXfont2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXfont2/libXfont2.spec) | `libXfont2` | 7 | 包名非全小写 |
| 21 | [libXft/libXft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXft/libXft.spec) | `libXft` | 8 | 包名非全小写 |
| 22 | [libXi/libXi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXi/libXi.spec) | `libXi` | 11 | 包名非全小写 |
| 23 | [libXinerama/libXinerama.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXinerama/libXinerama.spec) | `libXinerama` | 7 | 包名非全小写 |
| 24 | [libXmu/libXmu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXmu/libXmu.spec) | `libXmu` | 8 | 包名非全小写 |
| 25 | [libXpresent/libXpresent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXpresent/libXpresent.spec) | `libXpresent` | 7 | 包名非全小写 |
| 26 | [libXrandr/libXrandr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXrandr/libXrandr.spec) | `libXrandr` | 9 | 包名非全小写 |
| 27 | [libXrender/libXrender.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXrender/libXrender.spec) | `libXrender` | 9 | 包名非全小写 |
| 28 | [libXres/libXres.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXres/libXres.spec) | `libXres` | 8 | 包名非全小写 |
| 29 | [libXt/libXt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXt/libXt.spec) | `libXt` | 9 | 包名非全小写 |
| 30 | [libXtst/libXtst.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXtst/libXtst.spec) | `libXtst` | 9 | 包名非全小写 |
| 31 | [libXv/libXv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXv/libXv.spec) | `libXv` | 7 | 包名非全小写 |
| 32 | [libXxf86vm/libXxf86vm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXxf86vm/libXxf86vm.spec) | `libXxf86vm` | 9 | 包名非全小写 |
| 33 | [unixODBC/unixODBC.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unixODBC/unixODBC.spec) | `unixODBC` | 11 | 包名非全小写 |
| 34 | [createrepo_c/createrepo_c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/createrepo_c/createrepo_c.spec) | `createrepo_c` | 8 | 使用下划线 `_`，应优先用短横线 `-` |
| 35 | [fast_float/fast_float.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fast_float/fast_float.spec) | `fast_float` | 7 | 使用下划线 `_`，应优先用短横线 `-` |
| 36 | [isa-l_crypto/isa-l_crypto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/isa-l_crypto/isa-l_crypto.spec) | `isa-l_crypto` | 15 | 使用下划线 `_`，应优先用短横线 `-` |
| 37 | [libatomic_ops/libatomic_ops.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libatomic_ops/libatomic_ops.spec) | `libatomic_ops` | 9 | 使用下划线 `_`，应优先用短横线 `-` |
| 38 | [libnetfilter_acct/libnetfilter_acct.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_acct/libnetfilter_acct.spec) | `libnetfilter_acct` | 7 | 使用下划线 `_`，应优先用短横线 `-` |
| 39 | [libnetfilter_conntrack/libnetfilter_conntrack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_conntrack/libnetfilter_conntrack.spec) | `libnetfilter_conntrack` | 8 | 使用下划线 `_`，应优先用短横线 `-` |
| 40 | [libnetfilter_cthelper/libnetfilter_cthelper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_cthelper/libnetfilter_cthelper.spec) | `libnetfilter_cthelper` | 9 | 使用下划线 `_`，应优先用短横线 `-` |
| 41 | [libnetfilter_cttimeout/libnetfilter_cttimeout.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_cttimeout/libnetfilter_cttimeout.spec) | `libnetfilter_cttimeout` | 9 | 使用下划线 `_`，应优先用短横线 `-` |
| 42 | [libnetfilter_log/libnetfilter_log.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_log/libnetfilter_log.spec) | `libnetfilter_log` | 9 | 使用下划线 `_`，应优先用短横线 `-` |
| 43 | [libnetfilter_queue/libnetfilter_queue.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_queue/libnetfilter_queue.spec) | `libnetfilter_queue` | 9 | 使用下划线 `_`，应优先用短横线 `-` |
| 44 | [lm_sensors/lm_sensors.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lm_sensors/lm_sensors.spec) | `lm_sensors` | 12 | 使用下划线 `_`，应优先用短横线 `-` |
| 45 | [magic_enum/magic_enum.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/magic_enum/magic_enum.spec) | `magic_enum` | 7 | 使用下划线 `_`，应优先用短横线 `-` |
| 46 | [mod_http2/mod_http2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mod_http2/mod_http2.spec) | `mod_http2` | 9 | 使用下划线 `_`，应优先用短横线 `-` |
| 47 | [nss_wrapper/nss_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nss_wrapper/nss_wrapper.spec) | `nss_wrapper` | 8 | 使用下划线 `_`，应优先用短横线 `-` |
| 48 | [pam_wrapper/pam_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pam_wrapper/pam_wrapper.spec) | `pam_wrapper` | 8 | 使用下划线 `_`，应优先用短横线 `-` |
| 49 | [perl-OLE-Storage_Lite/perl-OLE-Storage_Lite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-OLE-Storage_Lite/perl-OLE-Storage_Lite.spec) | `perl-OLE-Storage_Lite` | 8 | 使用下划线 `_`，应优先用短横线 `-` |
| 50 | [perl-PerlIO-utf8_strict/perl-PerlIO-utf8_strict.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-PerlIO-utf8_strict/perl-PerlIO-utf8_strict.spec) | `perl-PerlIO-utf8_strict` | 8 | 使用下划线 `_`，应优先用短横线 `-` |
| 51 | [perl-Text-CSV_XS/perl-Text-CSV_XS.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Text-CSV_XS/perl-Text-CSV_XS.spec) | `perl-Text-CSV_XS` | 8 | 使用下划线 `_`，应优先用短横线 `-` |
| 52 | [priv_wrapper/priv_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/priv_wrapper/priv_wrapper.spec) | `priv_wrapper` | 8 | 使用下划线 `_`，应优先用短横线 `-` |
| 53 | [sg3_utils/sg3_utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sg3_utils/sg3_utils.spec) | `sg3_utils` | 8 | 使用下划线 `_`，应优先用短横线 `-` |
| 54 | [socket_wrapper/socket_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/socket_wrapper/socket_wrapper.spec) | `socket_wrapper` | 8 | 使用下划线 `_`，应优先用短横线 `-` |
| 55 | [uid_wrapper/uid_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uid_wrapper/uid_wrapper.spec) | `uid_wrapper` | 8 | 使用下划线 `_`，应优先用短横线 `-` |
| 56 | [volume_key/volume_key.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/volume_key/volume_key.spec) | `volume_key` | 7 | 使用下划线 `_`，应优先用短横线 `-` |
| 57 | [wpa_supplicant/wpa_supplicant.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wpa_supplicant/wpa_supplicant.spec) | `wpa_supplicant` | 8 | 使用下划线 `_`，应优先用短横线 `-` |

## 说明

本次扫描基于 [check-spec-name](../docs/check-spec-name.md) 规则的校验逻辑：

- 名称必须全小写（`perl-*` 模块豁免，CPAN 分发组名需大写）；
- 分隔符优先用短横线 `-`，下划线 `_` 仅限补充规范允许的例外；
- 名称不得编码 ABI/主版本号（`libfoo2` 形式）；若该名称本身是
  上游项目名（`URL`/`VCS`/`Source` 中出现同名标识符，如 `libxml2`）则豁免；
- 名称含宏展开（如 `python-%{pypi_name}`）时跳过静态检查。

5280 个文件（98.9%）命名合规；57 个文件存在 1 类以上问题：

- **非全小写（33 个）**：`SDL2`/`SDL3`、X11 库系列 `libX*`（上游惯例）、
  `NetworkManager`、`PackageKit`、`Catch2`、`unixODBC` 等；
- **含下划线（24 个）**：多为上游名称自然含下划线（`*_wrapper` 系列、
  `libnetfilter_*`、`wpa_supplicant`、`sg3_utils` 等）——是否豁免由
  打包者按补充规范判断。

原先报告的 8 个「编码 ABI/主版本号」名称（`libxml2`、`libssh2`、
`libgit2`、`libp11`、`libtasn1` 等）经
[openRuyi-Project/openRuyi#1232](https://github.com/openRuyi-Project/openRuyi/issues/1232)
评审确认为上游源名称（`URL`/`VCS`/`Source` 中出现同名标识符），
本次更新后豁免，不再报告。
