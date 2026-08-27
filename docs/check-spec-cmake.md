# check-spec-cmake

> 规则 ID：`check-spec-cmake`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-cmake-results.md](../openruyi-scan-results/check-spec-cmake-results.md)

## 原始需求

来源：[openRuyi 打包指南 · 构建系统 · cmake](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems/cmake)

> 如需要使用 `cmake` 构建系统，那么需要添加这些 `BuildRequires`，
> 因为 `gcc` 在构建环境预装，可不显式声明。
>
> ```spec
> BuildRequires:  cmake
> ```

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 声明必需依赖 | `BuildSystem: cmake` 的 spec 必须在 `BuildRequires` 中声明 `cmake` | 头部区域 `BuildRequires` 缺失 `cmake`，即失败 |

**说明**：

- `gcc` 是唯一豁免项：文档明确说明 `gcc` 在构建环境预装，可不显式声明；
  `cmake` 为构建系统必需组件，不随构建环境预装。
- 检查点只要求**存在声明**，不限制声明顺序、是否带版本约束；
  "一行一个依赖包"的书写格式由 `check-spec-buildrequires` 规则覆盖。

**跳过**（无法静态判定 / 由其它规则覆盖）：

- `BuildSystem` 字段缺失：为必填字段，由 `check-spec-structure` 规则覆盖；
- 非 `cmake` 构建系统的 spec：本规则不适用，不检查；
- `%package` 子包段落内的 `BuildRequires`：该字段声明的是子包构建依赖，
  不代表主包构建依赖，不判定；
- `%conf` 阶段预置的 `cmake` 相关宏（如 `%cmake`、`%cmake_build`）：
  描述构建环境平台行为，无法静态判定，不在本规则范围内；
- 是否应将 `%build`/`%install` 指令迁移为 `BuildOption`/`%build -p`/
  `%install -a`：由 `check-spec-buildoption` 规则覆盖与指南示例说明，
  不在本规则范围内。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-cmake
```

也可独立运行：`check-spec-cmake path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
BuildSystem:    cmake
BuildRequires:  cmake
```

```spec
BuildSystem:    cmake
BuildRequires:  cmake >= 3.20
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(zlib)
```

（`ninja-build`、`pkgconfig(zlib)` 等额外依赖不影响判定）

### 不通过 ❌

```spec
BuildSystem:    cmake
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(zlib)
```

→ `BuildSystem is cmake; BuildRequires must declare cmake`

```spec
BuildSystem:    cmake
```

→ `BuildSystem is cmake; BuildRequires must declare cmake`
