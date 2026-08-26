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
| 许可证文本文件在 `%doc` 中（未用 `%license` 标记） | 91 |
| `%files` 中直接通配 `%{_datadir}/locale/*`（未用 `%find_lang`） | 14 |
| `%files` 列表重复列出同一文件 | 0 |
| `%files` 中包含 `.la` (libtool archive) 文件 | 0 |
| 文档文件以裸文件名列出（未用 `%doc` 标记） | 0 |

## 问题清单（93 文件 105 条）

### `%doc` 中列出许可证文本文件（91 条）

| # | spec 文件 | 字段值 | 问题类型 |
| --- | --- | --- | --- |
| 1 | [apr](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/apr/apr.spec) | `LICENSE` | L1 license-in-doc |
| 2 | [apr-util](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/apr-util/apr-util.spec) | `LICENSE` | L1 license-in-doc |
| 3 | [aspell](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aspell/aspell.spec) | `COPYING` | L1 license-in-doc |
| 4 | [blktrace](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/blktrace/blktrace.spec) | `COPYING` | L1 license-in-doc |
| 5 | [cdparanoia](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cdparanoia/cdparanoia.spec) | `COPYING*` | L1 license-in-doc |
| 6 | [conntrack-tools](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/conntrack-tools/conntrack-tools.spec) | `COPYING` | L1 license-in-doc |
| 7 | [ding-libs](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ding-libs/ding-libs.spec) | `COPYING` | L1 license-in-doc |
| 8 | [ding-libs](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ding-libs/ding-libs.spec) | `COPYING.LESSER` | L1 license-in-doc |
| 9 | [ding-libs](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ding-libs/ding-libs.spec) | `COPYING` | L1 license-in-doc |
| 10 | [ding-libs](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ding-libs/ding-libs.spec) | `COPYING.LESSER` | L1 license-in-doc |
| 11 | [docbook-utils](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-utils/docbook-utils.spec) | `COPYING` | L1 license-in-doc |
| 12 | [docbook-xsl](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook-xsl/docbook-xsl.spec) | `COPYING` | L1 license-in-doc |
| 13 | [docbook2x](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/docbook2x/docbook2x.spec) | `COPYING` | L1 license-in-doc |
| 14 | [fakeroot](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fakeroot/fakeroot.spec) | `COPYING` | L1 license-in-doc |
| 15 | [fcoe-utils](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fcoe-utils/fcoe-utils.spec) | `COPYING` | L1 license-in-doc |
| 16 | [fio](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/fio/fio.spec) | `COPYING` | L1 license-in-doc |
| 17 | [firewalld](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/firewalld/firewalld.spec) | `COPYING` | L1 license-in-doc |
| 18 | [foot](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/foot/foot.spec) | `LICENSE` | L1 license-in-doc |
| 19 | [glog](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glog/glog.spec) | `COPYING` | L1 license-in-doc |
| 20 | [gpm](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gpm/gpm.spec) | `COPYING` | L1 license-in-doc |
| 21 | [httpd](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/httpd/httpd.spec) | `LICENSE` | L1 license-in-doc |
| 22 | [hwdata](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hwdata/hwdata.spec) | `LICENSE` | L1 license-in-doc |
| 23 | [iptraf-ng](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iptraf-ng/iptraf-ng.spec) | `LICENSE` | L1 license-in-doc |
| 24 | [irqbalance](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/irqbalance/irqbalance.spec) | `COPYING` | L1 license-in-doc |
| 25 | [jbig2dec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jbig2dec/jbig2dec.spec) | `COPYING` | L1 license-in-doc |
| 26 | [jbig2dec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jbig2dec/jbig2dec.spec) | `LICENSE` | L1 license-in-doc |
| 27 | [jbig2dec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jbig2dec/jbig2dec.spec) | `COPYING` | L1 license-in-doc |
| 28 | [jbig2dec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jbig2dec/jbig2dec.spec) | `LICENSE` | L1 license-in-doc |
| 29 | [jose](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jose/jose.spec) | `COPYING` | L1 license-in-doc |
| 30 | [ledmon](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ledmon/ledmon.spec) | `COPYING` | L1 license-in-doc |
| 31 | [libdvdread](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdvdread/libdvdread.spec) | `COPYING` | L1 license-in-doc |
| 32 | [libICE](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libICE/libICE.spec) | `COPYING` | L1 license-in-doc |
| 33 | [libinput](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libinput/libinput.spec) | `COPYING` | L1 license-in-doc |
| 34 | [libmng](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libmng/libmng.spec) | `LICENSE` | L1 license-in-doc |
| 35 | [libndp](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libndp/libndp.spec) | `COPYING` | L1 license-in-doc |
| 36 | [libnetfilter_cttimeout](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnetfilter_cttimeout/libnetfilter_cttimeout.spec) | `COPYING` | L1 license-in-doc |
| 37 | [libnftnl](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libnftnl/libnftnl.spec) | `COPYING` | L1 license-in-doc |
| 38 | [libotf](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libotf/libotf.spec) | `COPYING` | L1 license-in-doc |
| 39 | [libstoragemgmt](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libstoragemgmt/libstoragemgmt.spec) | `COPYING.LIB` | L1 license-in-doc |
| 40 | [libthai](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libthai/libthai.spec) | `COPYING` | L1 license-in-doc |
| 41 | [libvirt-glib](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libvirt-glib/libvirt-glib.spec) | `COPYING` | L1 license-in-doc |
| 42 | [libwacom](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libwacom/libwacom.spec) | `COPYING` | L1 license-in-doc |
| 43 | [libXau](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXau/libXau.spec) | `COPYING` | L1 license-in-doc |
| 44 | [libXcomposite](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXcomposite/libXcomposite.spec) | `COPYING` | L1 license-in-doc |
| 45 | [libXcursor](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXcursor/libXcursor.spec) | `COPYING` | L1 license-in-doc |
| 46 | [libxcvt](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxcvt/libxcvt.spec) | `COPYING` | L1 license-in-doc |
| 47 | [libXdamage](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXdamage/libXdamage.spec) | `COPYING` | L1 license-in-doc |
| 48 | [libXft](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXft/libXft.spec) | `COPYING` | L1 license-in-doc |
| 49 | [libXinerama](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXinerama/libXinerama.spec) | `COPYING` | L1 license-in-doc |
| 50 | [libxkbfile](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libxkbfile/libxkbfile.spec) | `COPYING` | L1 license-in-doc |
| 51 | [libXmu](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXmu/libXmu.spec) | `COPYING` | L1 license-in-doc |
| 52 | [libXres](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXres/libXres.spec) | `COPYING` | L1 license-in-doc |
| 53 | [libXScrnSaver](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXScrnSaver/libXScrnSaver.spec) | `COPYING` | L1 license-in-doc |
| 54 | [libXv](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libXv/libXv.spec) | `COPYING` | L1 license-in-doc |
| 55 | [lldpad](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lldpad/lldpad.spec) | `COPYING` | L1 license-in-doc |
| 56 | [ltrace](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ltrace/ltrace.spec) | `COPYING` | L1 license-in-doc |
| 57 | [lua-json](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua-json/lua-json.spec) | `LICENSE` | L1 license-in-doc |
| 58 | [memcached](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/memcached/memcached.spec) | `COPYING` | L1 license-in-doc |
| 59 | [nfs4-acl-tools](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nfs4-acl-tools/nfs4-acl-tools.spec) | `COPYING` | L1 license-in-doc |
| 60 | [oath-toolkit](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/oath-toolkit/oath-toolkit.spec) | `COPYING` | L1 license-in-doc |
| 61 | [oath-toolkit](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/oath-toolkit/oath-toolkit.spec) | `COPYING` | L1 license-in-doc |
| 62 | [openjade](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/openjade/openjade.spec) | `COPYING` | L1 license-in-doc |
| 63 | [opensc](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/opensc/opensc.spec) | `COPYING` | L1 license-in-doc |
| 64 | [opensp](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/opensp/opensp.spec) | `COPYING` | L1 license-in-doc |
| 65 | [orbit2](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/orbit2/orbit2.spec) | `COPYING` | L1 license-in-doc |
| 66 | [pacemaker](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pacemaker/pacemaker.spec) | `COPYING` | L1 license-in-doc |
| 67 | [perl-DateTime-Locale](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/perl-DateTime-Locale/perl-DateTime-Locale.spec) | `LICENSE.cldr` | L1 license-in-doc |
| 68 | [pesign](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pesign/pesign.spec) | `COPYING` | L1 license-in-doc |
| 69 | [phoronix-test-suite](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/phoronix-test-suite/phoronix-test-suite.spec) | `COPYING` | L1 license-in-doc |
| 70 | [potrace](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/potrace/potrace.spec) | `COPYING` | L1 license-in-doc |
| 71 | [procmail](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/procmail/procmail.spec) | `COPYING` | L1 license-in-doc |
| 72 | [python-blinker](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-blinker/python-blinker.spec) | `LICENSE.txt` | L1 license-in-doc |
| 73 | [python-meh](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-meh/python-meh.spec) | `COPYING` | L1 license-in-doc |
| 74 | [python-pyserial](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pyserial/python-pyserial.spec) | `LICENSE.txt` | L1 license-in-doc |
| 75 | [qemu](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qemu/qemu.spec) | `COPYING` | L1 license-in-doc |
| 76 | [rrdtool](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rrdtool/rrdtool.spec) | `bindings/python/COPYING` | L1 license-in-doc |
| 77 | [rtkit](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rtkit/rtkit.spec) | `LICENSE` | L1 license-in-doc |
| 78 | [sgml-common](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sgml-common/sgml-common.spec) | `COPYING` | L1 license-in-doc |
| 79 | [sgml-common](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sgml-common/sgml-common.spec) | `COPYING` | L1 license-in-doc |
| 80 | [softhsm](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/softhsm/softhsm.spec) | `LICENSE` | L1 license-in-doc |
| 81 | [sshpass](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sshpass/sshpass.spec) | `COPYING` | L1 license-in-doc |
| 82 | [tcl](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tcl/tcl.spec) | `license.terms` | L1 license-in-doc |
| 83 | [tuned](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tuned/tuned.spec) | `COPYING` | L1 license-in-doc |
| 84 | [tuned](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tuned/tuned.spec) | `COPYING` | L1 license-in-doc |
| 85 | [utf8proc](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/utf8proc/utf8proc.spec) | `LICENSE.md` | L1 license-in-doc |
| 86 | [volume_key](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/volume_key/volume_key.spec) | `COPYING` | L1 license-in-doc |
| 87 | [xfsdump](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xfsdump/xfsdump.spec) | `doc/COPYING` | L1 license-in-doc |
| 88 | [xkeyboard-config](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xkeyboard-config/xkeyboard-config.spec) | `COPYING` | L1 license-in-doc |
| 89 | [ypserv](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ypserv/ypserv.spec) | `COPYING` | L1 license-in-doc |
| 90 | [zfs](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zfs/zfs.spec) | `LICENSE` | L1 license-in-doc |
| 91 | [zsh](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/zsh/zsh.spec) | `LICENCE` | L1 license-in-doc |

### `%files` 中直接通配 `%{_datadir}/locale/*`（14 条）

| # | spec 文件 | 字段值 | 问题类型 |
| --- | --- | --- | --- |
| 1 | [kf6-kconfig](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kconfig/kf6-kconfig.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kconfig6_qt.qm` | L5 locale-glob |
| 2 | [kf6-kcoreaddons](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kcoreaddons/kf6-kcoreaddons.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kcoreaddons6_qt.qm` | L5 locale-glob |
| 3 | [kf6-kdbusaddons](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kdbusaddons/kf6-kdbusaddons.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kdbusaddons6_qt.qm` | L5 locale-glob |
| 4 | [kf6-kjobwidgets](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kjobwidgets/kf6-kjobwidgets.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kjobwidgets6_qt.qm` | L5 locale-glob |
| 5 | [kf6-knotifications](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-knotifications/kf6-knotifications.spec) | `%{_datadir}/locale/*/LC_MESSAGES/knotifications6_qt.qm` | L5 locale-glob |
| 6 | [kf6-kwindowsystem](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kf6-kwindowsystem/kf6-kwindowsystem.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kwindowsystem6_qt.qm` | L5 locale-glob |
| 7 | [kpmcore](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kpmcore/kpmcore.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kpmcore.mo` | L5 locale-glob |
| 8 | [kpmcore](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kpmcore/kpmcore.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kpmcore._policy_.mo` | L5 locale-glob |
| 9 | [krb5](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/krb5/krb5.spec) | `%{_datadir}/locale/*/LC_MESSAGES/mit-krb5.mo` | L5 locale-glob |
| 10 | [kwin](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kwin/kwin.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kwin*.mo` | L5 locale-glob |
| 11 | [kwin](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/kwin/kwin.spec) | `%{_datadir}/locale/*/LC_MESSAGES/kcm*.mo` | L5 locale-glob |
| 12 | [samba](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/samba/samba.spec) | `%{_datadir}/locale/*/LC_MESSAGES/net.mo` | L5 locale-glob |
| 13 | [samba](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/samba/samba.spec) | `%{_datadir}/locale/*/LC_MESSAGES/pam_winbind.mo` | L5 locale-glob |
| 14 | [texinfo](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/texinfo/texinfo.spec) | `%{_datadir}/locale/*` | L5 locale-glob |

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
