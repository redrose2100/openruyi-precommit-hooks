# check-spec-subpackage

> 规则 ID：`check-spec-subpackage`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-subpackage-results.md](../openruyi-scan-results/check-spec-subpackage-results.md)

## 原始需求

来源：[openRuyi 打包指南 · 软件包拆分（SplitPackage）](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/SplitPackage)

指南开篇即列出「以下是编写 RPM Spec 时必须要遵守的规则」，其中关于
子包依赖主包的要求（意译）：

> 需要主包的子包必须严格指定版本地依赖主包，这可以避免头文件/链接文件
> 与运行时库之间版本不同步的问题：
>
> ```spec
> Requires: %{name}%{?_isa} = %{version}-%{release}
> ```
>
> 同时建议在主包名后追加 `%{?_isa}`，使依赖成为架构特定的。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 子包依赖主包必须严格版本 | `%package` 子包块内，若 `Requires` 引用了主包（`%{name}` 或主包字面名），必须携带版本比较符（`=`、`>=`、`<=`、`>`、`<`） | 子包块内出现裸主包引用（`Requires: %{name}` 或 `Requires: <主包名>`）且无版本比较符，即失败 |

**说明**：

- 本检查点适用于**所有 spec 文件**（不限构建系统），只要是
  `%package` 子包块内的 `Requires` 引用了主包即检查；
- 主包自身的块（顶层）不适用：子包依赖主包才需要严格版本，主包
  依赖自己的子包不受此规则约束；
- 版本比较符只要出现即视为已约束版本（如 `= %{version}`、
  `>= %{version}`、以及指南推荐的
  `%{name}%{?_isa} = %{version}-%{release}` 均可通过）。

**豁免**（不判定为引用主包）：

- 引用**其它子包**：`%{name}-devel`、`%{name}-client`、`<主包名>-devel`
  等带连字符后缀的写法是对子包的依赖，不是对主包的依赖；
- **虚拟能力**：`go(...)`、`pkgconfig(...)`、`perl(...)`、
  `python3dist(...)`、`cmake(...)` 等整值虚拟依赖不引用主包
  （即使主包名恰为能力名的子串，如 `moby` 与
  `go(github.com/moby/...)`、`perl` 与 `perl(Devel::PPPort)`）；
- **宏续接**：`gcc%{gcc_version}-c++` 这类主包名后紧跟 `%` 再接宏的
  写法展开后是*另一个*包名（如 `gcc16-c++`），不是对主包 `gcc` 的
  裸引用；
- **scriptlet 变体**：`Requires(pre):`、`Requires(post):`、
  `Requires(preun):`、`Requires(postun):` 等声明的是脚本段依赖角色，
  不属于 `Requires` 运行期依赖（与 `check-spec-requires` 一致）；
- **宏展开的主包名**：`Name: %{base_name}` 之类无法静态解析，
  跳过不判。

**跳过**（无法静态判定 / 由其它规则覆盖）：

- `Requires` 字段缺失：由 `check-spec-structure` 规则覆盖；
- `Name` 字段缺失：由 `check-spec-structure` 规则覆盖；
- 「一行一个依赖」的书写格式：由 `check-spec-requires` 规则覆盖。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.2.0   # 使用最新 tag
    hooks:
    -   id: check-spec-subpackage
```

也可独立运行：`check-spec-subpackage path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
```

```spec
%package        -n myapp-plugins
Summary:        Plugins for myapp
Requires:       myapp-libs >= 1.0
```

```spec
%package        -n go-github-moby-moby-api
Summary:        API package
Requires:       go(github.com/moby/docker-image-spec)
```

### 不通过 ❌

```spec
%package        -n e2fsprogs-scrub
Summary:        Scrub tool
Requires:       e2fsprogs
```
→ `foo.spec:10: subpackage "e2fsprogs-scrub" depends on the main package "e2fsprogs" without a strict version; add a version comparison such as "Requires: %{name}%{?_isa} = %{version}-%{release}" (found "e2fsprogs")`
（`foo.spec:10` 中 `10` 为违规 `Requires` 行所在行号）
