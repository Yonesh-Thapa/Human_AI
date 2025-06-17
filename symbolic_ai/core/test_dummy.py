# symbolic_ai/core/test_dummy.py

import unittest
from .brain_controller import BrainController
from .memory_manager import MemoryManager


class TestCore(unittest.TestCase):
    def test_brain_memory_cycle(self):
        mem = MemoryManager()
        brain = BrainController(mem)
        result = brain.run("c")
        self.assertIn(result, mem.patterns)

if __name__ == '__main__':
    unittest.main()
