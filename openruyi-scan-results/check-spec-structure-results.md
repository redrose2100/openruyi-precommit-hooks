# check-spec-structure 扫描结果

> 扫描仓库：[openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) `main` 分支
> 扫描时间：2026-08-21
> 扫描文件数：5337 个 `.spec` 文件
> 不合规：**61 个**（头部字段乱序 51 个 + 段落前缺少空行 11 个，其中 `lzo` 同时涉及两类）

## 检查点 1：头部字段顺序

主包头部（第一个 `%description` 之前）中，字段若出现则必须按
`Name → Version → Release → Summary → License → URL → VCS → Source → BuildSystem → BuildRequires → Requires`
的顺序排列。

共 **51 个**文件违规：

| openRuyi 仓库文件链接 | 问题原因简述 |
| --- | --- |
| [aardvark-dns/aardvark-dns.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/aardvark-dns/aardvark-dns.spec) | `Summary` 出现在 `License` 之后 |
| [acl/acl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/acl/acl.spec) | `Version` 出现在 `Summary` 之后 |
| [binutils/binutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/binutils/binutils.spec) | `Version` 出现在 `Summary` 之后 |
| [boost/boost.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/boost/boost.spec) | `Version` 出现在 `Summary` 之后 |
| [chkconfig/chkconfig.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/chkconfig/chkconfig.spec) | `Version` 出现在 `Summary` 之后 |
| [clang-wrap/clang-wrap.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/clang-wrap/clang-wrap.spec) | `Summary` 出现在 `License` 之后 |
| [cloud-hypervisor/cloud-hypervisor.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cloud-hypervisor/cloud-hypervisor.spec) | `Version` 出现在 `Summary` 之后 |
| [coreutils/coreutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/coreutils/coreutils.spec) | `Name` 出现在 `Summary` 之后 |
| [dkms/dkms.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dkms/dkms.spec) | `Name` 出现在 `Summary` 之后 |
| [gcc/gcc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc/gcc.spec) | `Version` 出现在 `URL` 之后 |
| [gcc16/gcc16.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gcc16/gcc16.spec) | `Version` 出现在 `URL` 之后 |
| [glibc/glibc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glibc/glibc.spec) | `Version` 出现在 `Summary` 之后 |
| [gmp/gmp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gmp/gmp.spec) | `License` 出现在 `URL` 之后 |
| [graphviz/graphviz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/graphviz/graphviz.spec) | `Version` 出现在 `Summary` 之后 |
| [hipfft/hipfft.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hipfft/hipfft.spec) | `License` 出现在 `URL` 之后 |
| [hwloc/hwloc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/hwloc/hwloc.spec) | `Version` 出现在 `Summary` 之后 |
| [iptstate/iptstate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iptstate/iptstate.spec) | `Version` 出现在 `Summary` 之后 |
| [ipvsadm/ipvsadm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ipvsadm/ipvsadm.spec) | `Version` 出现在 `Summary` 之后 |
| [libcroco/libcroco.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libcroco/libcroco.spec) | `Version` 出现在 `Summary` 之后 |
| [libdrm/libdrm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdrm/libdrm.spec) | `Summary` 出现在 `License` 之后 |
| [libiscsi/libiscsi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libiscsi/libiscsi.spec) | `Version` 出现在 `Summary` 之后 |
| [libplacebo/libplacebo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libplacebo/libplacebo.spec) | `Release` 出现在 `License` 之后 |
| [libyuv/libyuv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libyuv/libyuv.spec) | `Version` 出现在 `Summary` 之后 |
| [lua/lua.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lua/lua.spec) | `Summary` 出现在 `License` 之后 |
| [lzo/lzo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lzo/lzo.spec) | `Summary` 出现在 `License` 之后 |
| [mesa/mesa.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mesa/mesa.spec) | `Version` 出现在 `Summary` 之后 |
| [minicom/minicom.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/minicom/minicom.spec) | `Version` 出现在 `Summary` 之后 |
| [mlocate/mlocate.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mlocate/mlocate.spec) | `Name` 出现在 `Summary` 之后 |
| [mtools/mtools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mtools/mtools.spec) | `Version` 出现在 `Summary` 之后 |
| [netavark/netavark.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/netavark/netavark.spec) | `Summary` 出现在 `License` 之后 |
| [pigz/pigz.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pigz/pigz.spec) | `Summary` 出现在 `License` 之后 |
| [popt/popt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/popt/popt.spec) | `Summary` 出现在 `License` 之后 |
| [procmail/procmail.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/procmail/procmail.spec) | `Version` 出现在 `Summary` 之后 |
| [pulseaudio-qt/pulseaudio-qt.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pulseaudio-qt/pulseaudio-qt.spec) | `Version` 出现在 `Summary` 之后 |
| [pulseaudio/pulseaudio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/pulseaudio/pulseaudio.spec) | `Version` 出现在 `Summary` 之后 |
| [python-meson-python/python-meson-python.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-meson-python/python-meson-python.spec) | `Summary` 出现在 `License` 之后 |
| [python-pdm-backend/python-pdm-backend.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pdm-backend/python-pdm-backend.spec) | `Summary` 出现在 `License` 之后 |
| [python-pynacl/python-pynacl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pynacl/python-pynacl.spec) | `Summary` 出现在 `License` 之后 |
| [python-pytest-asyncio/python-pytest-asyncio.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-pytest-asyncio/python-pytest-asyncio.spec) | `Summary` 出现在 `License` 之后 |
| [python-python-dotenv/python-python-dotenv.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-python-dotenv/python-python-dotenv.spec) | `Summary` 出现在 `License` 之后 |
| [python-torch/python-torch.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-torch/python-torch.spec) | `Summary` 出现在 `License` 之后 |
| [qca/qca.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/qca/qca.spec) | `Version` 出现在 `Summary` 之后 |
| [range-v3/range-v3.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/range-v3/range-v3.spec) | `Version` 出现在 `Summary` 之后 |
| [re2c/re2c.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/re2c/re2c.spec) | `Name` 出现在 `Summary` 之后 |
| [rocblas/rocblas.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocblas/rocblas.spec) | `Version` 出现在 `Summary` 之后 |
| [rocthrust/rocthrust.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rocthrust/rocthrust.spec) | `License` 出现在 `URL` 之后 |
| [rpm/rpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/rpm/rpm.spec) | `Version` 出现在 `Summary` 之后 |
| [smartmontools/smartmontools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/smartmontools/smartmontools.spec) | `Name` 出现在 `Summary` 之后 |
| [taglib/taglib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/taglib/taglib.spec) | `Version` 出现在 `Summary` 之后 |
| [tbb/tbb.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tbb/tbb.spec) | `Version` 出现在 `Summary` 之后 |
| [vdo/vdo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/vdo/vdo.spec) | `Name` 出现在 `Summary` 之后 |

## 检查点 2：段落之间的空行

`%description`、`%files`、`%changelog`、`%package`、`%prep`、`%build`、`%install`、`%check`
段落之间必须以空行分隔。

共 **11 个**文件违规：

| openRuyi 仓库文件链接 | 问题原因简述 |
| --- | --- |
| [NetworkManager/NetworkManager.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/NetworkManager/NetworkManager.spec) | 段落 `%files tui` 前缺少空行分隔 |
| [bluez/bluez.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/bluez/bluez.spec) | 段落 `%files hid2hci` 前缺少空行分隔 |
| [cloud-utils/cloud-utils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/cloud-utils/cloud-utils.spec) | 段落 `%description    vcs-run` 前缺少空行分隔 |
| [drpm/drpm.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/drpm/drpm.spec) | 段落 `%changelog` 前缺少空行分隔 |
| [glib/glib.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/glib/glib.spec) | 段落 `%description    tests` 前缺少空行分隔 |
| [htop/htop.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/htop/htop.spec) | 段落 `%description` 前缺少空行分隔 |
| [iprutils/iprutils.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/iprutils/iprutils.spec) | 段落 `%changelog` 前缺少空行分隔 |
| [lzo/lzo.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lzo/lzo.spec) | 段落 `%description` 前缺少空行分隔 |
| [mkosi/mkosi.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mkosi/mkosi.spec) | 段落 `%description   addon` 前缺少空行分隔 |
| [python-qemu-qmp/python-qemu-qmp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/python-qemu-qmp/python-qemu-qmp.spec) | 段落 `%description    doc` 前缺少空行分隔 |
| [xfsprogs/xfsprogs.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/xfsprogs/xfsprogs.spec) | 段落 `%check` 前缺少空行分隔 |

## 说明

- 本次扫描基于 [check-spec-structure](../docs/check-spec-structure.md) 规则的校验逻辑。
- 扫描脚本与本仓库 hook 使用同一套判定逻辑（`_check_spec_structure`），无额外过滤。
- `%if`/`%endif` 条件块后紧跟段落属于 RPM 合法写法，不判违规。
- `VCS` 缺少 4363 个（82%）与 `Requires` 缺少 1923 个（36%）属于正常情况，本规则不判违规。
