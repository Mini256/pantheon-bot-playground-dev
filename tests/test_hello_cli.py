import subprocess
import sys
import unittest
from pathlib import Path


class TestHelloCli(unittest.TestCase):
    def setUp(self):
        self.project_root = Path(__file__).resolve().parents[1]
        self.script_path = self.project_root / "hello.py"

    def test_no_args_prints_usage_and_exits_2(self):
        result = subprocess.run(
            [sys.executable, str(self.script_path)],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("Usage:", result.stderr)
        self.assertIn("hello.py", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_with_name_prints_greeting(self):
        result = subprocess.run(
            [sys.executable, str(self.script_path), "Alice"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Hello, Alice\n")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()

