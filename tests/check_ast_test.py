from __future__ import annotations

import pytest

from openruyi_precommit_hooks.check_ast import main
from testing.util import get_resource_path


@pytest.mark.parametrize(
    ('filename', 'expected_retval'), (
        ('cannot_parse_ast.notpy', 1),
        ('ok_python.py', 0),
    ),
)
def test_main(filename, expected_retval):
    ret = main([get_resource_path(filename)])
    assert ret == expected_retval


def test_main_ok_python(tmpdir):
    f = tmpdir.join('test.py')
    f.write('x = 1\n')
    assert main([str(f)]) == 0


def test_main_bad_python(tmpdir):
    f = tmpdir.join('test.py')
    f.write('this is not valid python\n')
    assert main([str(f)]) == 1
