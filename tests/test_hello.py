import os
import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
HELLO_PY = REPO_ROOT / "hello.py"


class HelloScriptTests(unittest.TestCase):
    def test_normal_usage_prints_greeting(self) -> None:
        result = subprocess.run(
            [sys.executable, str(HELLO_PY), "Alice"],
            cwd=REPO_ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Hello, Alice\n")
        self.assertEqual(result.stderr, "")

    def test_broken_pipe_exits_zero_without_traceback(self) -> None:
        read_fd, write_fd = os.pipe()
        os.close(read_fd)

        try:
            if hasattr(os, "set_inheritable"):
                os.set_inheritable(write_fd, True)

            result = subprocess.run(
                [sys.executable, str(HELLO_PY), "Alice"],
                cwd=REPO_ROOT,
                stdout=write_fd,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
            )
        finally:
            os.close(write_fd)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
