# check-spec-vcs 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行
`check-spec-vcs` 规则的扫描结果。

## 结果概览

| 扫描 spec 文件数 | 通过 | 问题 |
| --- | ---: | ---: |
| 5267 | 5244 | 23 |

## 问题类型分布

| 问题类型 | 数量 |
| --- | --- |
| `# VCS:` 注释内容不是精确的 `No VCS link available` | 13 |
| `VCS` 不是可克隆的源码仓库链接（非 `git:` 前缀） | 10 |

## 问题清单（23 条）

| # | spec 文件 | `VCS` 值 | 问题所在行数 | 问题类型 |
| --- | --- | --- | ---: | --- |
| 1 | [busybox/busybox.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/busybox/busybox.spec) | `# VCS: No reliable VCS link available` | 15 | `# VCS:` 注释不精确 |
| 2 | [checkpolicy/checkpolicy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/checkpolicy/checkpolicy.spec) | `# VCS: TODO: Multiple tags in one repo` | 16 | `# VCS:` 注释不精确 |
| 3 | [db/db.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/db/db.spec) | `# VCS: This package does not have a VCS link` | 17 | `# VCS:` 注释不精确 |
| 4 | [dblatex/dblatex.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/dblatex/dblatex.spec) | `hg:http://hg.code.sf.net/p/dblatex/dblatex` | 13 | 非 `git:` 可克隆链接 |
| 5 | [ebook-tools/ebook-tools.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ebook-tools/ebook-tools.spec) | `svn:https://svn.code.sf.net/p/ebook-tools` | 13 | 非 `git:` 可克隆链接 |
| 6 | [ed/ed.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/ed/ed.spec) | `# VCS: TODO: How to write https://savannah.gnu.org/cvs/?group=ed` | 14 | `# VCS:` 注释不精确 |
| 7 | [expect/expect.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/expect/expect.spec) | `# VCS: TODO: Protentially cvs https://sourceforge.net/p/expect/c...` | 17 | `# VCS:` 注释不精确 |
| 8 | [gmp/gmp.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/gmp/gmp.spec) | `hg:https://gmplib.org/repo/gmp` | 14 | 非 `git:` 可克隆链接 |
| 9 | [intltool/intltool.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/intltool/intltool.spec) | `# VCS: Bazzar upstream will be deprecated so no upstream?? - 251` | 15 | `# VCS:` 注释不精确 |
| 10 | [jbigkit/jbigkit.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/jbigkit/jbigkit.spec) | `# VCS: No git repo found.` | 14 | `# VCS:` 注释不精确 |
| 11 | [judy/judy.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/judy/judy.spec) | `svn:https://svn.code.sf.net/p/judy/code/trunk` | 13 | 非 `git:` 可克隆链接 |
| 12 | [lame/lame.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lame/lame.spec) | `svn:https://svn.code.sf.net/p/lame/svn/trunk/lame` | 14 | 非 `git:` 可克隆链接 |
| 13 | [libdaemon/libdaemon.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libdaemon/libdaemon.spec) | `# VCS: Upstream git dead` | 15 | `# VCS:` 注释不精确 |
| 14 | [libev/libev.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libev/libev.spec) | `# VCS: TODO: Add cvs link here` | 15 | `# VCS:` 注释不精确 |
| 15 | [libotf/libotf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/libotf/libotf.spec) | `# VCS: TODO: cvs -d :pserver:anonymous@cvs.m17n.org:/cvs/root co...` | 14 | `# VCS:` 注释不精确 |
| 16 | [lzip/lzip.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/lzip/lzip.spec) | `# VCS: TODO: cvs -z3 -d:pserver:anonymous@cvs.savannah.nongnu.or...` | 14 | `# VCS:` 注释不精确 |
| 17 | [mandoc/mandoc.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/mandoc/mandoc.spec) | `# VCS: TODO: This project use CVS` | 18 | `# VCS:` 注释不精确 |
| 18 | [nspr/nspr.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nspr/nspr.spec) | `hg:https://hg.mozilla.org/projects/nspr` | 15 | 非 `git:` 可克隆链接 |
| 19 | [nss/nss.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/nss/nss.spec) | `hg:https://hg.mozilla.org/projects/nss` | 22 | 非 `git:` 可克隆链接 |
| 20 | [sshpass/sshpass.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/sshpass/sshpass.spec) | `svn:https://svn.code.sf.net/p/sshpass/code/trunk` | 15 | 非 `git:` 可克隆链接 |
| 21 | [texlive-texmf/texlive-texmf.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/texlive-texmf/texlive-texmf.spec) | `svn:https://tug.org/svn/texlive/trunk` | 63 | 非 `git:` 可克隆链接 |
| 22 | [tunctl/tunctl.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/tunctl/tunctl.spec) | `# VCS: TODO: This is CVS` | 14 | `# VCS:` 注释不精确 |
| 23 | [uuid/uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/uuid/uuid.spec) | `# VCS: TODO: http://cvs.ossp.org/pkg/lib/uuid/` | 14 | `# VCS:` 注释不精确 |

## 说明

- `# VCS:` 注释不精确：规则要求不存在可用源码仓库链接时，必须在
  `VCS` 字段位置写入精确的 `# VCS: No VCS link available`（`# VCS:`
  前缀必须保留）。`No reliable VCS link available`、`TODO: ...` 等
  其它写法均不合规，应统一改为 `# VCS: No VCS link available`。
- 非 `git:` 可克隆链接：规则要求当源代码托管于 Git 仓库时，`VCS`
  应当使用可克隆链接（`git:` 前缀，或指向已知源码托管平台的
  http(s) 链接）。`hg:`、`svn:` 等其它 VCS 前缀的链接不合规，应改写
  为 `git:` 可克隆链接；若确实不存在可用的 Git 仓库链接，则应使用
  `# VCS: No VCS link available` 注释。
- 字段缺失（5267 个 spec 中缺 `VCS` 字段的文件）由
  `check-spec-structure` 规则覆盖（`URL` 已为源码仓库链接时 `VCS`
  可省略），本规则不重复报告。

> 规则说明：[docs/check-spec-vcs.md](../docs/check-spec-vcs.md)
