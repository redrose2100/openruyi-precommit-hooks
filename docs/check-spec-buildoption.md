# check-spec-buildoption

> 规则 ID：`check-spec-buildoption`

## 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi) 仓库 spec 文件的扫描结果见：

- [openruyi-scan-results/check-spec-buildoption-results.md](../openruyi-scan-results/check-spec-buildoption-results.md)

## 原始需求

来源：[openRuyi 打包指南 · BuildOption (可选)](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines#buildoption-%E5%8F%AF%E9%80%89)
与 [声明式构建系统 · 传递额外参数](https://www.openruyi.cn/zh-Hans/docs/guide/packaging-guidelines/BuildSystems#%E4%BC%A0%E9%80%92%E9%A2%9D%E5%A4%96%E5%8F%82%E6%95%B0)

> 1. 当需要为特定构建阶段声明额外参数时，Spec 可以使用 `BuildOption(<stage>):` 字段。
> 2. `BuildOption(<stage>):` 与参数之间必须以两个空格分隔。
> 3. 多个参数必须按行分别声明。
> 4. 若使用 `BuildOption`，其位置应当位于 `BuildSystem` 与 `BuildRequires` 之间。
> 5. `BuildOption` 的书写顺序，应当与 RPM 的构建过程保持一致，即 `%build` → `%install` → `%check`。

补充文档（声明式构建系统）：

> 该标签的语法为：`BuildOption(<section>): <option string>`。
> 该标签可以在 spec 文件中针对每个部分出现任意多次。
> 请注意，冒号 (`:`) 与后面的选项参数之间需要有两个空格。
> 虽然语法上可以省略 BuildOption 后的构建阶段名称，但我们需要打包者写明。

## 检查点

| 序号 | 检查点 | 要求 | 违规判定 |
| --- | --- | --- | --- |
| 1 | 阶段名称 | `BuildOption` 后必须写明构建阶段名称（`BuildOption(<stage>):`），不得省略 | 写成 `BuildOption:` 或 `BuildOption():` 即失败 |
| 2 | 双空格分隔 | `BuildOption(<stage>):` 与参数之间必须以两个空格分隔 | 冒号后为单个空格或无空格即失败 |
| 3 | 字段位置 | `BuildOption` 应当位于 `BuildSystem` 与 `BuildRequires` 之间 | 位于 `BuildSystem` 之前、或位于 `BuildRequires` 之后即失败 |
| 4 | 书写顺序 | `BuildOption` 的书写顺序应当与 RPM 构建过程一致（`build` → `install` → `check`） | `build`/`install`/`check` 三个阶段的相对顺序不符合即失败 |

**跳过**（无法静态判定）：

- 字段缺失：`BuildOption` 为可选字段，缺失由 `check-spec-structure` 规则覆盖，本规则不重复报告；
- 多个参数按行分别声明：参数本身可能含空格（如 `--disable-option-checking MAKEINFO=true`），无法可靠区分"一个参数含空格"与"多个参数同行"，不判定；
- 参数是否真的为对应构建阶段所需：需人工核对，不判定；
- `%package` 子包段落内的 `BuildOption`：该字段声明的是子包构建选项，不属于本规则范围，不判定；
- 缺少 `BuildSystem` 或 `BuildRequires` 锚点时：位置无法判定，仅校验其它检查点；
- 阶段名称取值：`stage` 为开放集合（不同构建系统有不同阶段，如 `conf`/`prep`/`generate_buildrequires`），仅要求非空，不做白名单校验。

**注意**：检查点 1、2 为「必须」级要求（阶段名称必须写明、双空格分隔），
检查点 3、4 为「应当」级要求（位置在 `BuildSystem` 与 `BuildRequires`
之间、顺序为 `build` → `install` → `check`）。任一违反即报告。顺序检查
仅判定 `build`/`install`/`check` 三个阶段的相对顺序，其它阶段（如
`conf`/`prep`/`generate_buildrequires`）不参与顺序判定。

## 用法

在 `.pre-commit-config.yaml` 中添加：

```yaml
-   repo: https://github.com/redrose2100/openruyi-precommit-hooks
    rev: v0.2.0   # 使用最新 tag
    hooks:
    -   id: check-spec-buildoption
```

也可独立运行：`check-spec-buildoption path/to/foo.spec`。
返回码 0 表示通过，1 表示有违规。

## 示例

### 通过 ✅

```spec
BuildSystem:    autotools
BuildOption(conf):  --enable-foo
BuildOption(build):  all info html
BuildOption(install):  install.info
BuildOption(check):  run-tests
BuildRequires:  gcc
```

```spec
BuildSystem:    meson
BuildOption(conf):  -Dadmin_group=wheel
BuildOption(conf):  -Dgtk_doc=true
BuildRequires:  gcc
```

### 不通过 ❌

```spec
BuildSystem:    autotools
BuildOption(conf): --enable-foo
BuildRequires:  gcc
```
→ `BuildOption(conf) must be separated from its arguments by two spaces (found "--enable-foo")`

```spec
BuildSystem:    autotools
BuildOption:  --enable-foo
BuildRequires:  gcc
```
→ `BuildOption must carry a build stage name (found "BuildOption: ..." without "(<stage>)")`

```spec
BuildOption(conf):  --enable-foo
BuildSystem:    autotools
BuildRequires:  gcc
```
→ `BuildOption must be located between BuildSystem and BuildRequires`

```spec
BuildSystem:    autotools
BuildOption(install):  install.info
BuildOption(build):  all
BuildRequires:  gcc
```
→ `BuildOption stages should be written in the order build, install, check (found install, build)`
