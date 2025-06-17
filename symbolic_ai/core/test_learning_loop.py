import unittest

from .learning_loop import LearningLoop
from .memory_manager import MemoryManager


class TestLearningLoop(unittest.TestCase):
    def test_learn_voice(self):
        mem = MemoryManager()
        loop = LearningLoop(mem)
        loop.learn_from_voice(b"a")
        self.assertIn("A", mem.all_symbols())

    def test_learn_camera(self):
        mem = MemoryManager()
        loop = LearningLoop(mem)
        loop.learn_from_camera()
        self.assertTrue(len(mem.all_symbols()) > 0)


if __name__ == "__main__":
    unittest.main()
