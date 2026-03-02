import os
import subprocess
import sys
import unittest

import hello


class TestHello(unittest.TestCase):
    def test_greet_to_user(self):
        self.assertEqual(hello.greet_to_user("Alice"), "Hello, Alice")

    def test_greet_backward_compat_alias(self):
        self.assertIs(hello.greet, hello.greet_to_user)
        self.assertEqual(hello.greet("Bob"), "Hello, Bob")

    def test_cli_prints_greeting(self):
        script_path = os.path.join(os.path.dirname(__file__), "hello.py")
        result = subprocess.run(
            [sys.executable, script_path, "Alice"],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.stdout.strip(), "Hello, Alice")


if __name__ == "__main__":
    unittest.main()

