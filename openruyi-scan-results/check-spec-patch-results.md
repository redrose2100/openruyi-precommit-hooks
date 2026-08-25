# check-spec-patch 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-patch` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 含 `Patch`/`%patchlist` | 通过 | 违规 |
| --- | ---: | ---: | ---: |
| 5267 | 462 | 258 | 204 |

> 说明：违规数按 spec 文件去重统计（一个文件可能命中多条规则）。

## 问题类型分布

| 问题类型 | 数量 |
| --- | ---: |
| `Patch` 字段上方缺少注释行 | 333 |
| 补丁文件名未以四位数字开头 | 121 |
| `Patch` 字段放置顺序错误 | 26 |
| 补丁数量 > 3 未使用 `%patchlist` | 25 |
| 补丁文件名前缀不在 `0001-2999` 范围内 | 4 |
| `%patchlist` 位于 `%description` 之下 | 4 |

## 问题清单

### 1. `Patch` 字段上方缺少注释行（333 条，涉及 168 个 spec）

规则要求每个 `Patch:` 字段上方必须有一行注释（以 `#` 开头）说明补丁
用途。以下 spec 存在至少一处 `Patch` 字段上方无注释：

`angelscript`, `arrow`, `aspell`, `attr`, `audiofile`, `autoconf`,
`autofs`, `bash`, `bdfresize`, `bison`, `cgctl`, `cloud-init`,
`console-setup`, `crash`, `cunit`, `cups`, `cyrus-sasl`, `dbus-broker`,
`dejagnu`, `desktop-file-utils`, `docbook-dtds`, `dosfstools`,
`doxygen`, `dpdk`, `duktape`, `dwz`, `eigen3`, `ethtool`, `expect`,
`f2fs-tools`, `fakeroot`, `fcoe-utils`, `firefox`, `freetype`,
`fscryptctl`, `gcc15`, `gcc16`, `gdbm`, `gflags`, `giflib`, `glib`,
`go-github-envoyproxy-protoc-gen-validate`, `go-gopkg-tomb.v1`, `gpm`,
`gpsd`, `gptfdisk`, `grpc`, `guile`, `gzip`, `hipfft`, `hipify`,
`i2c-tools`, `icu4c`, `isa-l_crypto`, `itstool`, `kf6-ksvg`, `kiwi`,
`libburn`, `libdwarf`, `libfaketime`, `libjpeg-turbo`, `liblc3`,
`liblognorm`, `libmodulemd`, `libosinfo`, `libseccomp`, `libselinux`,
`libsquish`, `libtiff`, `libunwind`, `libutempter`, `libvdpau`,
`libwebp`, `libyuv`, `llvm22`, `llvm-snapshot`, `lsof`, `lua`,
`lua-json`, `lz4`, `mariadb`, `mergerfs`, `miopen`, `mkosi`, `msgpack`,
`nghttp3`, `nodejs`, `nss`, `numad`, `openldap`, `openzl`, `orbit2`,
`otf2bdf`, `perl-Log-Any`, `perl-rpm-packaging`, `pesign`, `pinfo`,
`plasma-desktop`, `popt`, `postgresql`, `powertop`, `python-cart`,
`python-cppheaderparser`, `python-gcloud-aio-auth`, `python-optimum`,
`python-optimum-benchmark`, `python-propcache`, `python-pytest-xdist`,
`python-tensile`, `python-tokenizers`, `python-torchvision`,
`qt6-qtwebengine`, `quota`, `readline`, `recutils`, `rocblas`,
`rocclr`, `rocfft`, `rocksdb`, `rocminfo`, `rocr-runtime`, `rpm`,
`rrdtool`, `rust-async-std-1`, `rust-dlib-0.5`, `rust-generator-0.8`,
`rust-hyper-util-0.1`, `rust-malloc-buf-0.0.6`, `rust-nom-locate-5`,
`rust-objc-0.2`, `rust-pyo3-introspection-0.28`,
`rust-python-pkginfo-0.6`, `rust-reflink-copy-0.1`,
`rust-shellexpand-3`, `rust-signal-hook-registry-1`,
`rust-system-deps-7`, `rust-tracy-client-0.18`, `rust-v-frame-0.3`,
`rust-wasite-1`, `scap-security-guide`, `sddm`, `shadow`, `sharutils`,
`soxr`, `srt`, `startup-notification`, `symlinks`, `tcsh`, `texlive`,
`unzip`, `xdg-utils`, `xevd`, `xeve`, `xinetd`, `xtrans`, `yaml-cpp`,
`zimg`, `zip`

### 2. 补丁文件名未以四位数字开头（121 条，涉及 59 个 spec）

规则要求补丁文件名必须以四位数字开头（如 `0001-xxx.patch`）。以下
spec 存在文件名不符合要求：

`autoconf`, `autofs`, `bdfresize`, `bison`, `blake3`, `busybox`,
`compsize`, `crash`, `dblatex`, `dbus-broker`, `dejagnu`, `dotnet10.0`,
`doxygen`, `dwz`, `efivar`, `eigen3`, `fakeroot`, `findutils`,
`freetype`, `gcc15`, `gdbm`, `glib`, `glibc`, `glmark2`, `grub`,
`gtk-doc`, `guile`, `gzip`, `keybinder`, `krb5`, `libaio`, `libdwarf`,
`libselinux`, `libsemanage`, `libtiff`, `libxcrypt`, `libxkbcommon`,
`lz4`, `mariadb`, `mdevd`, `mesa`, `mesa-demos`, `multipath-tools`,
`nmap`, `nodejs`, `otf2bdf`, `patch`, `policycoreutils`, `postgresql`,
`powertop`, `quota`, `rpm`, `rrdtool`, `utf8cpp`, `util-linux`, `uuid`,
`valkey`, `xtrans`, `xxhash`, `zlib-ng`

### 3. `Patch` 字段放置顺序错误（26 条，涉及 26 个 spec）

规则要求 `Patch` 字段位于 `BuildSystem` 与 `BuildOption`（或
`BuildRequires`）之间。以下 spec 的 `Patch` 字段位置不符合要求：

`aom`, `aspell`, `cgctl`, `compsize`, `crash`, `dbus-broker`, `eigen3`,
`giflib`, `guile`, `hipfft`, `hipify`, `hipsparselt`, `keybinder`,
`libaio`, `libdwarf`, `libjpeg-turbo`, `libunwind`, `lua-json`,
`msgpack`, `powertop`, `python-python-dateutil`, `qhull`, `rocblas`,
`rocsolver`, `soxr`, `vdo`

### 4. 补丁数量 > 3 未使用 `%patchlist`（25 条，涉及 25 个 spec）

规则要求补丁数量超过 3 个时应使用 `%patchlist` 统一管理。以下 spec
存在 4 个及以上 `Patch` 字段但未使用 `%patchlist`：

`audiofile`(11), `binutils`(5), `cyrus-sasl`(4), `expect`(7),
`gcc15`(40), `gpm`(4), `grub`(4), `icu4c`(4), `indent`(4),
`libselinux`(4), `lua`(4), `ncurses`(4), `nodejs`(4), `openjade`(4),
`openldap`(4), `orbit2`(4), `otf2bdf`(4), `pesign`(4), `pinfo`(4),
`procmail`(4), `qt6-qtbase`(4), `qt6-qtwebengine`(4), `readline`(4),
`rpm`(4), `zip`(4)

> 括号内为 `Patch` 字段数量。

### 5. 补丁文件名前缀不在 `0001-2999` 范围内（4 条，涉及 3 个 spec）

| # | spec 文件 | 补丁文件名 |
| --- | --- | --- |
| 1 | `libunwind/libunwind.spec` | `3000-libunwind-no-dl-iterate-phdr.patch` |
| 2 | `nodejs/nodejs.spec` | `60588.diff` |
| 3 | `nodejs/nodejs.spec` | `60591.diff` |
| 4 | `rpm/rpm.spec` | `6464-auto-config-update.diff` |

### 6. `%patchlist` 位于 `%description` 之下（4 条，涉及 4 个 spec）

规则要求 `%patchlist` 必须位于 `%description` 之上。以下 spec 的
`%patchlist` 位置不符合要求：

`cdparanoia`, `openssl`, `python-torch`, `spdk`

## 说明

- 注释要求：规则要求每个 `Patch:` 字段上方必须有一行以 `#` 开头的
  注释，用于说明补丁用途。openRuyi 仓库中大量 spec 未遵循此约定。
- 命名要求：补丁文件名应以四位数字开头（`0001-0999`、`1000-1999`、
  `2000-2999` 三个区间），用于控制补丁应用顺序。仓库中部分 spec 使用
  了 `60588.diff`、`3000-xxx.patch` 等不符合约定的命名。
- `%patchlist`：当补丁数量超过 3 个时，建议使用 `%patchlist` 统一
  管理，避免逐个 `%patch` 应用。仓库中 `gcc15`（40 个补丁）、
  `audiofile`（11 个补丁）等 spec 未使用 `%patchlist`。
- 放置顺序：`Patch` 字段应位于 `BuildSystem` 与 `BuildOption`（或
  `BuildRequires`）之间，与 `Source` 字段类似。
- 本规则仅扫描 spec 头部区域（`%description`/`%package` 等段落之前），
  `%patchlist` 位置检查除外（在整个文件中查找）。

> 规则说明：[docs/check-spec-patch.md](../docs/check-spec-patch.md)
