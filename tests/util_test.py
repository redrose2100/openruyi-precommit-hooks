from __future__ import annotations

import sys

import pytest

from openruyi_precommit_hooks.util import CalledProcessError
from openruyi_precommit_hooks.util import cmd_output
from openruyi_precommit_hooks.util import zsplit


def test_zsplit_empty() -> None:
    assert zsplit('') == []


def test_zsplit_trailing_nul() -> None:
    assert zsplit('a\0b\0') == ['a', 'b']


def test_cmd_output_ok() -> None:
    assert cmd_output(sys.executable, '-c', 'print(1)').strip() == '1'


def test_cmd_output_bad_retcode() -> None:
    with pytest.raises(CalledProcessError):
        cmd_output(sys.executable, '-c', 'import sys; sys.exit(1)')


def test_cmd_output_retcode_none() -> None:
    out = cmd_output(sys.executable, '-c', 'import sys; sys.exit(3)', retcode=None)
    assert out == ''


def test_called_process_error_attributes() -> None:
    err = CalledProcessError(('cmd',), None, 1, 'out', 'err')
    assert err.cmd == ('cmd',)
    assert err.expected_retcode is None
    assert err.retcode == 1
    assert err.stdout == 'out'
    assert err.stderr == 'err'
