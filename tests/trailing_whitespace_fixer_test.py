from __future__ import annotations

import pytest

from openruyi_precommit_hooks.trailing_whitespace_fixer import main


def test_fixes_trailing_whitespace(tmpdir):
    f = tmpdir.join('test.txt')
    f.write_binary(b'a b c  \nfoo \nbar\n')

    assert main([str(f)]) == 1

    assert f.read_binary() == b'a b c\nfoo\nbar\n'


def test_no_change(tmpdir):
    f = tmpdir.join('test.txt')
    f.write_binary(b'a b c\nfoo\nbar\n')

    assert main([str(f)]) == 0

    assert f.read_binary() == b'a b c\nfoo\nbar\n'