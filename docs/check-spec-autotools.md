# check-spec-autotools

> 规则 ID：`check-spec-autotools`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-autotools-results.md](../openruyi-scan-results/check-spec-autotools-results.md)

## 原始需求

来源：[openRuyi 打包指南 · 构建系统 · autotools](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems/autotools)

> 如需要使用 `autotools` 构建系统，那么需要添加这些 `BuildRequires`，
> 因为 `gcc` 在构建环境预装，可不显式声明。
>
> ```spec
> BuildRequires:  autoconf
> BuildRequires:  automake
> BuildRequires:  libtool
> BuildRequires:  make
> ```

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 声明必需依赖 | `BuildSystem: autotools` 的 spec 必须在 `BuildRequires` 中声明 `autoconf`、`automake`、`libtool`、`make` | 头部区域 `BuildRequires` 缺失其中任意一项，即失败 |

**说明**：

- `gcc` 是唯一豁免项：文档明确说明 `gcc` 在构建环境预装，可不显式声明；
  其余四项均为 autotools 工具链的必需组件，不随构建环境预装。
- 检查点只要求**存在声明**，不限制声明顺序、是否带版本约束；
  "一行一个依赖包"的书写格式由 `check-spec-buildrequires` 规则覆盖。

**跳过**（无法静态判定 / 由其它规则覆盖）：

- `BuildSystem` 字段缺失：为必填字段，由 `check-spec-structure` 规则覆盖；
- 非 `autotools` 构建系统的 spec：本规则不适用，不检查；
- `%package` 子包段落内的 `BuildRequires`：该字段声明的是子包构建依赖，
  不代表主包构建依赖，不判定；
- 是否应在 `%conf` 前置运行 `autoreconf -fiv`、源码无 `configure` 脚本时
  是否应使用空 `%conf` 并注释说明：依赖源码树内容，无法静态判定，
  不在本规则范围内。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-autotools
```

也可独立运行：`check-spec-autotools path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
BuildSystem:    autotools
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
```

```spec
BuildSystem:    autotools
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(zlib)
```

```spec
BuildSystem:    cmake
BuildRequires:  cmake >= 3.20
```

（非 `autotools` 构建系统不适用本规则）

### 不通过 ❌

```spec
BuildSystem:    autotools
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
```

→ `BuildSystem is autotools; BuildRequires must declare make`

```spec
BuildSystem:    autotools
BuildRequires:  zlib-devel
BuildRequires:  gettext-devel
```

→ `BuildSystem is autotools; BuildRequires must declare autoconf, automake, libtool, make`