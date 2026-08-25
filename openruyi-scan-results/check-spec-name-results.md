# check-spec-name 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库的 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-name` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| --- | ---: | ---: |
| 5337 | 5272 | 65 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| 包名非全小写 | 33 |
| 使用下划线 `_`，应优先用短横线 `-` | 24 |
| 名称编码 ABI/主版本号（`libxxx2` 形式） | 8 |

## 问题清单（65 条）

| # | spec 文件 | `Name` 值 | 问题类型 |
| --- | --- | --- | --- |
| 1 | [Catch2/Catch2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/Catch2/Catch2.spec) | `Catch2` | 包名非全小写 |
| 2 | [ModemManager/ModemManager.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ModemManager/ModemManager.spec) | `ModemManager` | 包名非全小写 |
| 3 | [NetworkManager/NetworkManager.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/NetworkManager/NetworkManager.spec) | `NetworkManager` | 包名非全小写 |
| 4 | [PackageKit/PackageKit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/PackageKit/PackageKit.spec) | `PackageKit` | 包名非全小写 |
| 5 | [PackageKit-Qt/PackageKit-Qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/PackageKit-Qt/PackageKit-Qt.spec) | `PackageKit-Qt` | 包名非全小写 |
| 6 | [SDL2/SDL2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/SDL2/SDL2.spec) | `SDL2` | 包名非全小写 |
| 7 | [SDL3/SDL3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/SDL3/SDL3.spec) | `SDL3` | 包名非全小写 |
| 8 | [Xwayland/Xwayland.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/Xwayland/Xwayland.spec) | `Xwayland` | 包名非全小写 |
| 9 | [createrepo_c/createrepo_c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/createrepo_c/createrepo_c.spec) | `createrepo_c` | 使用下划线 `_`，应优先用短横线 `-` |
| 10 | [fast_float/fast_float.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fast_float/fast_float.spec) | `fast_float` | 使用下划线 `_`，应优先用短横线 `-` |
| 11 | [isa-l_crypto/isa-l_crypto.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/isa-l_crypto/isa-l_crypto.spec) | `isa-l_crypto` | 使用下划线 `_`，应优先用短横线 `-` |
| 12 | [libICE/libICE.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libICE/libICE.spec) | `libICE` | 包名非全小写 |
| 13 | [libSM/libSM.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libSM/libSM.spec) | `libSM` | 包名非全小写 |
| 14 | [libX11/libX11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libX11/libX11.spec) | `libX11` | 包名非全小写 |
| 15 | [libXScrnSaver/libXScrnSaver.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXScrnSaver/libXScrnSaver.spec) | `libXScrnSaver` | 包名非全小写 |
| 16 | [libXau/libXau.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXau/libXau.spec) | `libXau` | 包名非全小写 |
| 17 | [libXcomposite/libXcomposite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXcomposite/libXcomposite.spec) | `libXcomposite` | 包名非全小写 |
| 18 | [libXcursor/libXcursor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXcursor/libXcursor.spec) | `libXcursor` | 包名非全小写 |
| 19 | [libXdamage/libXdamage.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXdamage/libXdamage.spec) | `libXdamage` | 包名非全小写 |
| 20 | [libXdmcp/libXdmcp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXdmcp/libXdmcp.spec) | `libXdmcp` | 包名非全小写 |
| 21 | [libXext/libXext.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXext/libXext.spec) | `libXext` | 包名非全小写 |
| 22 | [libXfixes/libXfixes.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXfixes/libXfixes.spec) | `libXfixes` | 包名非全小写 |
| 23 | [libXfont2/libXfont2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXfont2/libXfont2.spec) | `libXfont2` | 包名非全小写 |
| 24 | [libXft/libXft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXft/libXft.spec) | `libXft` | 包名非全小写 |
| 25 | [libXi/libXi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXi/libXi.spec) | `libXi` | 包名非全小写 |
| 26 | [libXinerama/libXinerama.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXinerama/libXinerama.spec) | `libXinerama` | 包名非全小写 |
| 27 | [libXmu/libXmu.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXmu/libXmu.spec) | `libXmu` | 包名非全小写 |
| 28 | [libXpresent/libXpresent.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXpresent/libXpresent.spec) | `libXpresent` | 包名非全小写 |
| 29 | [libXrandr/libXrandr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXrandr/libXrandr.spec) | `libXrandr` | 包名非全小写 |
| 30 | [libXrender/libXrender.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXrender/libXrender.spec) | `libXrender` | 包名非全小写 |
| 31 | [libXres/libXres.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXres/libXres.spec) | `libXres` | 包名非全小写 |
| 32 | [libXt/libXt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXt/libXt.spec) | `libXt` | 包名非全小写 |
| 33 | [libXtst/libXtst.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXtst/libXtst.spec) | `libXtst` | 包名非全小写 |
| 34 | [libXv/libXv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXv/libXv.spec) | `libXv` | 包名非全小写 |
| 35 | [libXxf86vm/libXxf86vm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXxf86vm/libXxf86vm.spec) | `libXxf86vm` | 包名非全小写 |
| 36 | [libatomic_ops/libatomic_ops.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libatomic_ops/libatomic_ops.spec) | `libatomic_ops` | 使用下划线 `_`，应优先用短横线 `-` |
| 37 | [libgit2/libgit2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libgit2/libgit2.spec) | `libgit2` | 名称编码 ABI/主版本号（`libxxx2` 形式） |
| 38 | [libidn2/libidn2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libidn2/libidn2.spec) | `libidn2` | 名称编码 ABI/主版本号（`libxxx2` 形式） |
| 39 | [libkexiv2/libkexiv2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libkexiv2/libkexiv2.spec) | `libkexiv2` | 名称编码 ABI/主版本号（`libxxx2` 形式） |
| 40 | [liblc3/liblc3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/liblc3/liblc3.spec) | `liblc3` | 名称编码 ABI/主版本号（`libxxx2` 形式） |
| 41 | [libnetfilter_acct/libnetfilter_acct.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_acct/libnetfilter_acct.spec) | `libnetfilter_acct` | 使用下划线 `_`，应优先用短横线 `-` |
| 42 | [libnetfilter_conntrack/libnetfilter_conntrack.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_conntrack/libnetfilter_conntrack.spec) | `libnetfilter_conntrack` | 使用下划线 `_`，应优先用短横线 `-` |
| 43 | [libnetfilter_cthelper/libnetfilter_cthelper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_cthelper/libnetfilter_cthelper.spec) | `libnetfilter_cthelper` | 使用下划线 `_`，应优先用短横线 `-` |
| 44 | [libnetfilter_cttimeout/libnetfilter_cttimeout.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_cttimeout/libnetfilter_cttimeout.spec) | `libnetfilter_cttimeout` | 使用下划线 `_`，应优先用短横线 `-` |
| 45 | [libnetfilter_log/libnetfilter_log.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_log/libnetfilter_log.spec) | `libnetfilter_log` | 使用下划线 `_`，应优先用短横线 `-` |
| 46 | [libnetfilter_queue/libnetfilter_queue.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_queue/libnetfilter_queue.spec) | `libnetfilter_queue` | 使用下划线 `_`，应优先用短横线 `-` |
| 47 | [libp11/libp11.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libp11/libp11.spec) | `libp11` | 名称编码 ABI/主版本号（`libxxx2` 形式） |
| 48 | [libssh2/libssh2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libssh2/libssh2.spec) | `libssh2` | 名称编码 ABI/主版本号（`libxxx2` 形式） |
| 49 | [libtasn1/libtasn1.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libtasn1/libtasn1.spec) | `libtasn1` | 名称编码 ABI/主版本号（`libxxx2` 形式） |
| 50 | [libxml2/libxml2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxml2/libxml2.spec) | `libxml2` | 名称编码 ABI/主版本号（`libxxx2` 形式） |
| 51 | [lm_sensors/lm_sensors.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lm_sensors/lm_sensors.spec) | `lm_sensors` | 使用下划线 `_`，应优先用短横线 `-` |
| 52 | [magic_enum/magic_enum.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/magic_enum/magic_enum.spec) | `magic_enum` | 使用下划线 `_`，应优先用短横线 `-` |
| 53 | [mod_http2/mod_http2.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mod_http2/mod_http2.spec) | `mod_http2` | 使用下划线 `_`，应优先用短横线 `-` |
| 54 | [nss_wrapper/nss_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nss_wrapper/nss_wrapper.spec) | `nss_wrapper` | 使用下划线 `_`，应优先用短横线 `-` |
| 55 | [pam_wrapper/pam_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pam_wrapper/pam_wrapper.spec) | `pam_wrapper` | 使用下划线 `_`，应优先用短横线 `-` |
| 56 | [perl-OLE-Storage_Lite/perl-OLE-Storage_Lite.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-OLE-Storage_Lite/perl-OLE-Storage_Lite.spec) | `perl-OLE-Storage_Lite` | 使用下划线 `_`，应优先用短横线 `-` |
| 57 | [perl-PerlIO-utf8_strict/perl-PerlIO-utf8_strict.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-PerlIO-utf8_strict/perl-PerlIO-utf8_strict.spec) | `perl-PerlIO-utf8_strict` | 使用下划线 `_`，应优先用短横线 `-` |
| 58 | [perl-Text-CSV_XS/perl-Text-CSV_XS.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-Text-CSV_XS/perl-Text-CSV_XS.spec) | `perl-Text-CSV_XS` | 使用下划线 `_`，应优先用短横线 `-` |
| 59 | [priv_wrapper/priv_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/priv_wrapper/priv_wrapper.spec) | `priv_wrapper` | 使用下划线 `_`，应优先用短横线 `-` |
| 60 | [sg3_utils/sg3_utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sg3_utils/sg3_utils.spec) | `sg3_utils` | 使用下划线 `_`，应优先用短横线 `-` |
| 61 | [socket_wrapper/socket_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/socket_wrapper/socket_wrapper.spec) | `socket_wrapper` | 使用下划线 `_`，应优先用短横线 `-` |
| 62 | [uid_wrapper/uid_wrapper.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uid_wrapper/uid_wrapper.spec) | `uid_wrapper` | 使用下划线 `_`，应优先用短横线 `-` |
| 63 | [unixODBC/unixODBC.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/unixODBC/unixODBC.spec) | `unixODBC` | 包名非全小写 |
| 64 | [volume_key/volume_key.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/volume_key/volume_key.spec) | `volume_key` | 使用下划线 `_`，应优先用短横线 `-` |
| 65 | [wpa_supplicant/wpa_supplicant.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/wpa_supplicant/wpa_supplicant.spec) | `wpa_supplicant` | 使用下划线 `_`，应优先用短横线 `-` |

## 说明

本次扫描基于 [check-spec-name](../docs/check-spec-name.md) 规则的校验逻辑：

- 名称必须全小写（`perl-*` 模块豁免，CPAN 分发组名需大写）；
- 分隔符优先用短横线 `-`，下划线 `_` 仅限补充规范允许的例外；
- 名称不得编码 ABI/主版本号（`libfoo2` 形式）；
- 名称含宏展开（如 `python-%{pypi_name}`）时跳过静态检查。

5272 个文件（98.8%）命名合规；65 个文件存在 1 类以上问题：

- **非全小写（33 个）**：`SDL2`/`SDL3`、X11 库系列 `libX*`（上游惯例）、
  `NetworkManager`、`PackageKit`、`Catch2`、`unixODBC` 等；
- **含下划线（24 个）**：多为上游名称自然含下划线（`*_wrapper` 系列、
  `libnetfilter_*`、`wpa_supplicant`、`sg3_utils` 等）——是否豁免由
  打包者按补充规范判断；
- **编码 ABI/主版本号（8 个）**：`libxml2`、`libssh2`、`libgit2`、
  `libp11`、`libtasn1` 等。
