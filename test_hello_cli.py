import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent


class TestHelloCli(unittest.TestCase):
    def test_no_args_prints_usage_and_exits_2(self) -> None:
        completed = subprocess.run(
            [sys.executable, "hello.py"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(completed.stdout, "")
        self.assertIn("Usage:", completed.stderr)

    def test_name_arg_prints_greeting_and_exits_0(self) -> None:
        completed = subprocess.run(
            [sys.executable, "hello.py", "Ada"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0)
        self.assertEqual(completed.stdout, "Hello, Ada\n")
        self.assertEqual(completed.stderr, "")


if __name__ == "__main__":
    unittest.main()

