import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO_ROOT))

import hello


class HelloTests(unittest.TestCase):
    def test_greet_to_user_returns_expected_message(self):
        self.assertEqual(hello.greet_to_user("Alice"), "Hello, Alice")

    def test_greet_compat_alias_exists(self):
        self.assertTrue(hasattr(hello, "greet"))
        self.assertEqual(hello.greet("Alice"), hello.greet_to_user("Alice"))

    def test_cli_prints_greeting_and_exits_zero(self):
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "hello.py"), "Alice"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertEqual(result.stdout.strip(), "Hello, Alice")


if __name__ == "__main__":
    unittest.main()
