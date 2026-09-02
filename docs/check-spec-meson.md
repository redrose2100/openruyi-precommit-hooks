# check-spec-meson

> 规则 ID：`check-spec-meson`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-meson-results.md](../openruyi-scan-results/check-spec-meson-results.md)

## 原始需求

来源：[openRuyi 打包指南 · 构建系统 · Meson](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems/meson)

> 如需要使用 `meson` 构建系统，那么需要添加这些 `BuildRequires`。
>
> ```spec
> BuildRequires:  meson
> ```

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 声明必需依赖 | `BuildSystem: meson` 的 spec 必须在 `BuildRequires` 中声明 `meson` | 头部区域 `BuildRequires` 缺失 `meson`，即失败 |

**说明**：

- 与 cmake/autotools 指南不同，meson 页面**未提及** `gcc` 等
  预装工具豁免，因此 `meson` 为必需声明；
- 检查点只要求**存在声明**，不限制声明顺序、是否带版本约束；
  "一行一个依赖包"的书写格式由 `check-spec-buildrequires` 规则覆盖。

**跳过**（无法静态判定 / 由其它规则覆盖 / 建议性要求）：

- `BuildSystem` 字段缺失：为必填字段，由 `check-spec-structure` 规则覆盖；
- 非 `meson` 构建系统的 spec：本规则不适用，不检查；
- `BuildOption(conf)` / `BuildOption(build)` 示例
  （`-Dman=enabled` 等）以及 `%build` → `%conf`、`%install -a`
  区段迁移：属配置迁移语义，由 `check-spec-buildoption` 规则覆盖，
  且无法静态判定，不在本规则范围内；
- `ninja-build`：meson 的构建后端，指南未要求 spec 声明，
  不纳入本规则。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.2.0   # 使用最新 tag
    hooks:
    -   id: check-spec-meson
```

也可独立运行：`check-spec-meson path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
BuildSystem:    meson
BuildRequires:  meson
```

```spec
BuildSystem:    meson
BuildRequires:  meson >= 0.60
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(glib-2.0)
```

（`ninja-build`、`pkgconfig(...)` 等额外声明不影响判定）

### 不通过 ❌

```spec
BuildSystem:    meson
BuildRequires:  ninja-build
```

→ `BuildSystem is meson; BuildRequires must declare meson`
