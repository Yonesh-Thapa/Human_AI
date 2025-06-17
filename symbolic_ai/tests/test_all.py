# symbolic_ai/tests/test_all.py

import unittest
import os
import sys

print("🔍 Running all symbolic AI tests...\n")

# Ensure project root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

def discover_and_run_tests():
    """Auto-discover and run all test_*.py files in symbolic_ai/."""
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="symbolic_ai", pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        exit(1)

if __name__ == "__main__":
    discover_and_run_tests()
