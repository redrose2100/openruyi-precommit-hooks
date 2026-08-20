from __future__ import annotations

import subprocess
from typing import Any


class CalledProcessError(RuntimeError):
    """Raised when a subprocess exits with an unexpected return code."""

    def __init__(
            self,
            cmd: tuple[str, ...],
            expected_retcode: int | None,
            retcode: int,
            stdout: str,
            stderr: str,
    ) -> None:
        super().__init__(cmd, expected_retcode, retcode, stdout, stderr)
        self.cmd = cmd
        self.expected_retcode = expected_retcode
        self.retcode = retcode
        self.stdout = stdout
        self.stderr = stderr


def cmd_output(
        *cmd: str,
        retcode: int | None = 0,
        **kwargs: Any,
) -> str:
    """Run a command and return its stdout, checking the return code."""
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


def added_files() -> set[str]:
    """Return the set of files staged for addition in git."""
    cmd = ('git', 'diff', '--staged', '--name-only', '--diff-filter=A')
    return set(cmd_output(*cmd).splitlines())


def zsplit(s: str) -> list[str]:
    """Split a NUL-separated string, ignoring a trailing NUL."""
    s = s.strip('\0')
    if s:
        return s.split('\0')
    else:
        return []
