"""Regenerate openruyi-scan-results/check-spec-structure-results.md.

Uses the same validation logic as the check-spec-structure hook.
"""
from __future__ import annotations

import os
import re
import sys
from collections import Counter
from collections import defaultdict

sys.path.insert(0, r'e:\code\ai_agent\openruyi-precommit-hooks')
from openruyi_precommit_hooks.check_spec_structure import (  # noqa: E402
    _HEADER_FIELDS,
    _check_header_order,
    _check_section_spacing,
)

SPECS_DIR = os.path.join(os.environ.get('TEMP', ''), 'openruyi-scan', 'SPECS')
OUT = os.path.join(
    r'e:\code\ai_agent\openruyi-precommit-hooks',
    'openruyi-scan-results',
    'check-spec-structure-results.md',
)
BASE = 'https://github.com/openRuyi-Project/openRuyi/blob/main/SPECS/'


def link(rel: str) -> str:
    return f'[{rel}]({BASE}{rel})'


def main() -> None:
    missing_combos: Counter[tuple[str, ...]] = Counter()
    missing_files: dict[tuple[str, ...], list[str]] = defaultdict(list)
    order_errors: list[tuple[str, str]] = []
    spacing_errors: list[tuple[str, str]] = []
    total = 0

    for root, _dirs, files in os.walk(SPECS_DIR):
        for fn in sorted(files):
            if not fn.endswith('.spec'):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, SPECS_DIR).replace('\\', '/')
            total += 1
            with open(path, encoding='utf-8', errors='replace') as fh:
                content = fh.read().splitlines()
            for err in _check_header_order(content, rel):
                if 'missing required header field' in err:
                    m = re.search(
                        r'missing required header field\(s\): (.+)$', err,
                    )
                    fields = tuple(m.group(1).split(', ')) if m else ()
                    missing_combos[fields] += 1
                    missing_files[fields].append(rel)
                else:
                    order_errors.append((rel, err))
            for err in _check_section_spacing(content, rel):
                spacing_errors.append((rel, err))

    missing_total = sum(missing_combos.values())
    order_total = len(order_errors)
    spacing_total = len(spacing_errors)
    all_bad = set()
    for files in missing_files.values():
        all_bad.update(files)
    all_bad.update(rel for rel, _ in order_errors)
    all_bad.update(rel for rel, _ in spacing_errors)
    non_compliant = len(all_bad)

    lines: list[str] = []
    lines.append('# check-spec-structure 扫描结果')
    lines.append('')
    lines.append(
        '对 [openRuyi-Project/openRuyi]'
        '(https://github.com/openRuyi-Project/openRuyi)',
    )
    lines.append('仓库的 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `main`）执行')
    lines.append('`check-spec-structure` 规则的扫描结果。')
    lines.append('')
    lines.append('## 结果概览')
    lines.append('')
    lines.append('| 项目 | 数量 |')
    lines.append('| --- | --- |')
    lines.append(f'| 扫描 spec 文件数 | {total} |')
    lines.append(f'| 通过 | {total - non_compliant} |')
    lines.append(f'| 违规 | {non_compliant} |')
    lines.append('')
    lines.append('## 问题类型分布')
    lines.append('')
    lines.append('| 问题类型 | 数量 |')
    lines.append('| --- | --- |')
    lines.append(f'| 缺少必填字段 | {missing_total} |')
    lines.append(f'| 头部字段乱序 | {order_total} |')
    lines.append(f'| 段落前缺少空行 | {spacing_total} |')
    lines.append('')
    lines.append('## 问题清单')
    lines.append('')
    lines.append('### 1. 缺少必填字段')
    lines.append('')
    lines.append(
        '主包头部（第一个 `%description` 之前）**必须**包含以下全部字段，'
        '且按顺序出现：',
    )
    lines.append('')
    lines.append('```spec')
    for f in _HEADER_FIELDS:
        lines.append(f'{f}:')
    lines.append('```')
    lines.append('')
    lines.append(
        '> **`VCS` 豁免**：若 `URL` 已为源代码仓库链接'
        '（如 `github.com`、`gitlab.*`、`git.*`、`codeberg.org`、'
        '`bitbucket.org` 等源码托管平台，或以 `git:` 开头、'
        '以 `.git` 结尾），则 `VCS` 可以省略。',
    )
    lines.append('')
    lines.append('各字段缺失文件数：')
    lines.append('')
    lines.append('| 字段 | 缺失文件数 |')
    lines.append('| --- | --- |')
    missing_counter: Counter[str] = Counter()
    for combo, cnt in missing_combos.items():
        for f in combo:
            missing_counter[f] += cnt
    for f in _HEADER_FIELDS:
        lines.append(f'| `{f}` | {missing_counter[f]} |')
    lines.append('')
    lines.append('按缺失字段组合统计：')
    lines.append('')
    lines.append('| 缺失字段组合 | 文件数 |')
    lines.append('| --- | --- |')
    for combo, cnt in sorted(
        missing_combos.items(), key=lambda x: (-x[1], x[0]),
    ):
        lines.append(f'| `{", ".join(combo)}` | {cnt} |')
    lines.append('')
    lines.append('缺失文件清单（按缺失组合分组，链接指向 openRuyi 仓库 `main` 分支）：')
    lines.append('')
    for combo, files in sorted(
        missing_files.items(), key=lambda x: (-missing_combos[x[0]], x[0]),
    ):
        lines.append(f'#### 缺失 `{", ".join(combo)}`（{len(files)} 个）')
        lines.append('')
        for rel in files:
            lines.append(f'- {link(rel)}')
        lines.append('')
    lines.append('### 2. 头部字段乱序')
    lines.append('')
    lines.append('| # | spec 文件 | 问题原因简述 |')
    lines.append('| --- | --- | --- |')
    for i, (rel, err) in enumerate(order_errors, 1):
        # ``header fields out of order: "Summary" appears after "License"
        # (expected 4 < 5)`` -> ``Summary`` 出现在 ``License`` 之后
        m = re.search(
            r'header fields out of order: "(\w+)" appears after "(\w+)"',
            err,
        )
        if m:
            reason = f'`{m.group(1)}` 出现在 `{m.group(2)}` 之后'
        else:
            reason = err
        lines.append(f'| {i} | {link(rel)} | {reason} |')
    lines.append('')
    lines.append('### 3. 段落前缺少空行')
    lines.append('')
    lines.append(
        '`%description`、`%files`、`%changelog`、`%package`、'
        '`%prep`、`%build`、`%install`、`%check`',
    )
    lines.append('段落之间必须以空行分隔。')
    lines.append('')
    lines.append('| # | spec 文件 | 问题原因简述 |')
    lines.append('| --- | --- | --- |')
    for i, (rel, err) in enumerate(spacing_errors, 1):
        # ``section "%files tui" must be preceded by a blank line``
        # -> 段落 `"%files tui"` 前缺少空行分隔
        m = re.search(
            r'section "([^"]+)" must be preceded by a blank line', err,
        )
        if m:
            reason = f'段落 `"{m.group(1)}"` 前缺少空行分隔'
        else:
            reason = err
        lines.append(f'| {i} | {link(rel)} | {reason} |')
    lines.append('')
    lines.append('## 说明')
    lines.append('')
    lines.append(
        '- 本次扫描基于 [check-spec-structure]'
        '(../docs/check-spec-structure.md) 规则的校验逻辑。',
    )
    lines.append(
        '- 扫描脚本与本仓库 hook 使用同一套判定逻辑'
        '（`_check_spec_structure`），无额外过滤。',
    )
    lines.append('- `%if`/`%endif` 条件块后紧跟段落属于 RPM 合法写法，不判违规。')
    lines.append('- `Source` 匹配 `Source`/`Source0`/`Source1` 等所有变体。')
    lines.append('- 当 `URL` 为源代码仓库链接时，`VCS` 缺失不判违规。')
    lines.append('')

    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(lines))

    print(f'written {OUT}')
    print(
        f'total={total} missing={missing_total} order={order_total} '
        f'spacing={spacing_total} non_compliant={non_compliant}',
    )


if __name__ == '__main__':
    main()
