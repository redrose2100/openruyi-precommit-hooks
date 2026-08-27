# check-spec-perl

> 规则 ID：`check-spec-perl`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-perl-results.md](../openruyi-scan-results/check-spec-perl-results.md)

## 原始需求

来源：[openRuyi 打包指南 · 构建系统 · Perl](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems/perl)

> 如需要使用 Perl 声明式构建系统，通常需要添加以下 `BuildRequires`。
>
> ```spec
> BuildRequires:  perl-rpm-packaging
> BuildRequires:  perl-rpm-macros
> BuildRequires:  perl-macros
> ```

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 声明必需依赖 | `BuildSystem: perlbuild` 或 `BuildSystem: perlmaker` 的 spec 必须在 `BuildRequires` 中声明 `perl-rpm-packaging`、`perl-rpm-macros`、`perl-macros` | 头部区域 `BuildRequires` 缺失其中任意一项，即失败 |

**说明**：

- 本规则同时覆盖 `perlbuild` 与 `perlmaker` 两个构建系统值；
- 与 cmake/autotools 指南不同，perl 页面**未提及** `gcc` 等
  预装工具豁免，因此三项均为必需声明；
- 检查点只要求**存在声明**，不限制声明顺序、是否带版本约束；
  "一行一个依赖包"的书写格式由 `check-spec-buildrequires` 规则覆盖。

**跳过**（无法静态判定 / 由其它规则覆盖 / 建议性要求）：

- `BuildSystem` 字段缺失：为必填字段，由 `check-spec-structure` 规则覆盖；
- 非 `perlbuild` / `perlmaker` 构建系统的 spec：本规则不适用，不检查；
- `perl(Module::Build)` / `perl(ExtUtils::MakeMaker)` /
  `perl(Test::More)` 等虚拟依赖：文档措辞为「通常需要」，且取决于
  上游构建脚本（`Build.PL` → `perlbuild`、`Makefile.PL` → `perlmaker`），
  未纳入强检查点；
- 选择构建系统（`Build.PL` / `Makefile.PL`）：基于上游源码树，
  spec 内无法静态判定；
- `BuildOption(build)` / `BuildOption(install)` / `BuildOption(check)`
  示例：由 `check-spec-buildoption` 规则覆盖；
- `%files -f %{name}.files` 文件列表：文档措辞为「通常使用」，
  属建议性要求，未纳入强检查点。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.1.0   # 使用最新 tag
    hooks:
    -   id: check-spec-perl
```

也可独立运行：`check-spec-perl path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
BuildSystem:    perlbuild
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
```

```spec
BuildSystem:    perlmaker
BuildRequires:  perl-rpm-packaging >= 1
BuildRequires:  perl-rpm-macros >= 2
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
```

（`perl(...)` 虚拟依赖等额外声明不影响判定）

### 不通过 ❌

```spec
BuildSystem:    perlbuild
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
```

→ `BuildSystem is perlbuild; BuildRequires must declare perl-macros`

```spec
BuildSystem:    perlmaker
BuildRequires:  zlib-devel
```

→ `BuildSystem is perlmaker; BuildRequires must declare perl-macros, perl-rpm-macros, perl-rpm-packaging`
