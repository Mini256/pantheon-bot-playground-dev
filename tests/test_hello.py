import os
import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class HelloScriptTests(unittest.TestCase):
    def test_normal_usage_prints_greeting(self):
        result = subprocess.run(
            [sys.executable, "hello.py", "Alice"],
            cwd=REPO_ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Hello, Alice\n")
        self.assertEqual(result.stderr, "")

    def test_broken_pipe_exits_zero_without_traceback(self):
        read_fd, write_fd = os.pipe()
        os.close(read_fd)  # ensure no readers exist for the pipe
        try:
            result = subprocess.run(
                [sys.executable, "hello.py", "Alice"],
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

