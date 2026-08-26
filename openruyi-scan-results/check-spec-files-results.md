# check-spec-files 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-files` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| --- | ---: | ---: |
| 5267 | 5174 | 93 |

> 说明：问题数按 spec 文件去重统计（同一文件多条违规计为 1 个文件）。

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） | 91 |
| `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） | 14 |
| `%files` 列表重复列出同一文件 | 0 |
| `%files` 中包含 `.la`（libtool archive）文件 | 0 |
| 文档文件未用 `%doc` 标记（应使用 `%doc`） | 0 |

## 问题清单（93 文件 105 条）

### `%doc` 中列出许可证文本文件（应使用 `%license` 标记）（91 条）

| # | spec 文件 | 字段值 | 问题所在行数 | 问题类型 |
| --- | --- | --- | ---: | --- |
| 1 | [apr](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/apr/apr.spec) | `LICENSE` | 85 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 2 | [apr-util](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/apr-util/apr-util.spec) | `LICENSE` | 147 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 3 | [aspell](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aspell/aspell.spec) | `COPYING` | 64 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 4 | [blktrace](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/blktrace/blktrace.spec) | `COPYING` | 49 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 5 | [cdparanoia](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cdparanoia/cdparanoia.spec) | `COPYING*` | 78 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 6 | [conntrack-tools](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/conntrack-tools/conntrack-tools.spec) | `COPYING` | 73 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 7 | [ding-libs](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ding-libs/ding-libs.spec) | `COPYING` | 42 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 8 | [ding-libs](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ding-libs/ding-libs.spec) | `COPYING.LESSER` | 42 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 9 | [ding-libs](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ding-libs/ding-libs.spec) | `COPYING` | 47 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 10 | [ding-libs](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ding-libs/ding-libs.spec) | `COPYING.LESSER` | 47 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 11 | [docbook-utils](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-utils/docbook-utils.spec) | `COPYING` | 85 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 12 | [docbook-xsl](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-xsl/docbook-xsl.spec) | `COPYING` | 158 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 13 | [docbook2x](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook2x/docbook2x.spec) | `COPYING` | 49 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 14 | [fakeroot](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fakeroot/fakeroot.spec) | `COPYING` | 114 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 15 | [fcoe-utils](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fcoe-utils/fcoe-utils.spec) | `COPYING` | 67 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 16 | [fio](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fio/fio.spec) | `COPYING` | 56 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 17 | [firewalld](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/firewalld/firewalld.spec) | `COPYING` | 104 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 18 | [foot](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/foot/foot.spec) | `LICENSE` | 63 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 19 | [glog](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glog/glog.spec) | `COPYING` | 46 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 20 | [gpm](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `COPYING` | 88 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 21 | [httpd](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/httpd/httpd.spec) | `LICENSE` | 319 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 22 | [hwdata](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hwdata/hwdata.spec) | `LICENSE` | 35 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 23 | [iptraf-ng](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iptraf-ng/iptraf-ng.spec) | `LICENSE` | 49 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 24 | [irqbalance](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/irqbalance/irqbalance.spec) | `COPYING` | 56 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 25 | [jbig2dec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jbig2dec/jbig2dec.spec) | `COPYING` | 44 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 26 | [jbig2dec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jbig2dec/jbig2dec.spec) | `LICENSE` | 44 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 27 | [jbig2dec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jbig2dec/jbig2dec.spec) | `COPYING` | 50 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 28 | [jbig2dec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jbig2dec/jbig2dec.spec) | `LICENSE` | 50 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 29 | [jose](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jose/jose.spec) | `COPYING` | 52 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 30 | [ledmon](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ledmon/ledmon.spec) | `COPYING` | 68 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 31 | [libdvdread](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdvdread/libdvdread.spec) | `COPYING` | 40 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 32 | [libICE](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libICE/libICE.spec) | `COPYING` | 44 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 33 | [libinput](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libinput/libinput.spec) | `COPYING` | 74 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 34 | [libmng](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmng/libmng.spec) | `LICENSE` | 52 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 35 | [libndp](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libndp/libndp.spec) | `COPYING` | 38 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 36 | [libnetfilter_cttimeout](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_cttimeout/libnetfilter_cttimeout.spec) | `COPYING` | 43 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 37 | [libnftnl](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnftnl/libnftnl.spec) | `COPYING` | 39 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 38 | [libotf](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libotf/libotf.spec) | `COPYING` | 45 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 39 | [libstoragemgmt](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libstoragemgmt/libstoragemgmt.spec) | `COPYING.LIB` | 160 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 40 | [libthai](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libthai/libthai.spec) | `COPYING` | 43 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 41 | [libvirt-glib](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libvirt-glib/libvirt-glib.spec) | `COPYING` | 52 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 42 | [libwacom](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libwacom/libwacom.spec) | `COPYING` | 83 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 43 | [libXau](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXau/libXau.spec) | `COPYING` | 44 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 44 | [libXcomposite](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXcomposite/libXcomposite.spec) | `COPYING` | 45 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 45 | [libXcursor](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXcursor/libXcursor.spec) | `COPYING` | 52 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 46 | [libxcvt](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxcvt/libxcvt.spec) | `COPYING` | 34 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 47 | [libXdamage](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXdamage/libXdamage.spec) | `COPYING` | 43 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 48 | [libXft](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXft/libXft.spec) | `COPYING` | 47 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 49 | [libXinerama](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXinerama/libXinerama.spec) | `COPYING` | 44 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 50 | [libxkbfile](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxkbfile/libxkbfile.spec) | `COPYING` | 37 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 51 | [libXmu](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXmu/libXmu.spec) | `COPYING` | 44 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 52 | [libXres](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXres/libXres.spec) | `COPYING` | 43 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 53 | [libXScrnSaver](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXScrnSaver/libXScrnSaver.spec) | `COPYING` | 46 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 54 | [libXv](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXv/libXv.spec) | `COPYING` | 42 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 55 | [lldpad](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lldpad/lldpad.spec) | `COPYING` | 69 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 56 | [ltrace](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ltrace/ltrace.spec) | `COPYING` | 45 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 57 | [lua-json](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua-json/lua-json.spec) | `LICENSE` | 40 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 58 | [memcached](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/memcached/memcached.spec) | `COPYING` | 70 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 59 | [nfs4-acl-tools](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nfs4-acl-tools/nfs4-acl-tools.spec) | `COPYING` | 33 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 60 | [oath-toolkit](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/oath-toolkit/oath-toolkit.spec) | `COPYING` | 74 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 61 | [oath-toolkit](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/oath-toolkit/oath-toolkit.spec) | `COPYING` | 88 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 62 | [openjade](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openjade/openjade.spec) | `COPYING` | 91 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 63 | [opensc](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/opensc/opensc.spec) | `COPYING` | 99 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 64 | [opensp](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/opensp/opensp.spec) | `COPYING` | 75 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 65 | [orbit2](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/orbit2/orbit2.spec) | `COPYING` | 72 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 66 | [pacemaker](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pacemaker/pacemaker.spec) | `COPYING` | 131 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 67 | [perl-DateTime-Locale](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DateTime-Locale/perl-DateTime-Locale.spec) | `LICENSE.cldr` | 75 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 68 | [pesign](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `COPYING` | 93 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 69 | [phoronix-test-suite](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/phoronix-test-suite/phoronix-test-suite.spec) | `COPYING` | 58 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 70 | [potrace](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/potrace/potrace.spec) | `COPYING` | 53 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 71 | [procmail](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/procmail/procmail.spec) | `COPYING` | 54 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 72 | [python-blinker](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-blinker/python-blinker.spec) | `LICENSE.txt` | 36 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 73 | [python-meh](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-meh/python-meh.spec) | `COPYING` | 45 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 74 | [python-pyserial](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyserial/python-pyserial.spec) | `LICENSE.txt` | 47 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 75 | [qemu](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qemu/qemu.spec) | `COPYING` | 1226 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 76 | [rrdtool](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | `bindings/python/COPYING` | 255 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 77 | [rtkit](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rtkit/rtkit.spec) | `LICENSE` | 68 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 78 | [sgml-common](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sgml-common/sgml-common.spec) | `COPYING` | 168 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 79 | [sgml-common](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sgml-common/sgml-common.spec) | `COPYING` | 185 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 80 | [softhsm](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/softhsm/softhsm.spec) | `LICENSE` | 120 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 81 | [sshpass](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sshpass/sshpass.spec) | `COPYING` | 28 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 82 | [tcl](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tcl/tcl.spec) | `license.terms` | 156 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 83 | [tuned](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tuned/tuned.spec) | `COPYING` | 231 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 84 | [tuned](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tuned/tuned.spec) | `COPYING` | 238 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 85 | [utf8proc](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/utf8proc/utf8proc.spec) | `LICENSE.md` | 62 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 86 | [volume_key](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/volume_key/volume_key.spec) | `COPYING` | 68 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 87 | [xfsdump](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xfsdump/xfsdump.spec) | `doc/COPYING` | 66 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 88 | [xkeyboard-config](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xkeyboard-config/xkeyboard-config.spec) | `COPYING` | 56 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 89 | [ypserv](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ypserv/ypserv.spec) | `COPYING` | 83 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 90 | [zfs](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zfs/zfs.spec) | `LICENSE` | 259 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |
| 91 | [zsh](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zsh/zsh.spec) | `LICENCE` | 124 | 许可证文本文件在 `%doc` 中列出（应使用 `%license` 标记） |

### `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`）（14 条）

| # | spec 文件 | 字段值 | 问题所在行数 | 问题类型 |
| --- | --- | --- | ---: | --- |
| 1 | [kf6-kconfig](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kconfig/kf6-kconfig.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kconfig6_qt.qm` | 93 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |
| 2 | [kf6-kcoreaddons](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kcoreaddons/kf6-kcoreaddons.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kcoreaddons6_qt.qm` | 88 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |
| 3 | [kf6-kdbusaddons](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kdbusaddons/kf6-kdbusaddons.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kdbusaddons6_qt.qm` | 65 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |
| 4 | [kf6-kjobwidgets](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kjobwidgets/kf6-kjobwidgets.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kjobwidgets6_qt.qm` | 62 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |
| 5 | [kf6-knotifications](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-knotifications/kf6-knotifications.spec) | `%{_datadir}/locale/*/LC_MESSAGES/knotifications6_qt.qm` | 82 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |
| 6 | [kf6-kwindowsystem](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kwindowsystem/kf6-kwindowsystem.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kwindowsystem6_qt.qm` | 87 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |
| 7 | [kpmcore](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kpmcore/kpmcore.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kpmcore.mo` | 58 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |
| 8 | [kpmcore](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kpmcore/kpmcore.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kpmcore._policy_.mo` | 59 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |
| 9 | [krb5](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/krb5/krb5.spec) | `%{_datadir}/locale/*/LC_MESSAGES/mit-krb5.mo` | 148 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |
| 10 | [kwin](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kwin/kwin.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kwin*.mo` | 247 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |
| 11 | [kwin](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kwin/kwin.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kcm*.mo` | 248 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |
| 12 | [samba](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/samba/samba.spec) | `%{_datadir}/locale/*/LC_MESSAGES/net.mo` | 439 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |
| 13 | [samba](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/samba/samba.spec) | `%{_datadir}/locale/*/LC_MESSAGES/pam_winbind.mo` | 849 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |
| 14 | [texinfo](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/texinfo/texinfo.spec) | `%{_datadir}/locale/*` | 66 | `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） |

## 说明

- 许可证文本文件必须使用 `%license` 标记、本地化文件必须在 `%install`
  段落内用 `%find_lang` 处理。93 个违规文件集中在两类：91 条为许可证
  文本文件出现在 `%doc` 行中（未用 `%license` 标记），14 条为
  `%files` 中直接通配 `%{_datadir}/locale/*`。
- 许可证文件名判定按 `LICENSE`/`LICENCE`/`COPYING` 前缀（大小写不敏感，
  含扩展名与通配）：如 `tcl` 的 `license.terms`、`rrdtool` 的
  `bindings/python/COPYING`、`xfsdump` 的 `doc/COPYING` 均计入问题。
- `%files -f` 段内直接书写的条目同样参与检查（如 `aspell`、`fakeroot`、
  `firewalld`、`libvirt-glib`、`perl-DateTime-Locale`、`python-blinker`、
  `python-pyserial`、`volume_key`、`xfsdump`、`xkeyboard-config` 的
  `COPYING`/`LICENSE.txt` 等）；`-f` 引用的文件清单本身在构建期生成，
  静态不可见，不参与判定。
- 12 个 locale 违规的 KF6 软件包（`kf6-kconfig` 等）中仅
  `kf6-kconfigwidgets` 使用了 `%find_lang`；其余软件包在整个仓库
  共有 234 个 spec 正确使用 `%find_lang` 机制。
- 重复列出（检查点 3）与 `.la` 文件（检查点 4）在扫描中均为 0：
  `%exclude` 行（如 `expat` 的 `%exclude %{_libdir}/libexpat.la`）属于
  排除操作而非包内容，不判违规；同一字面路径重复仅出现在条件块互斥
  分支内（如多个软件包的 `%if 0%{?arch}` 双份列表），静态无法确认为
  同一文件的重复安装，不判违规。

> 规则说明：[docs/check-spec-files.md](../docs/check-spec-files.md)
