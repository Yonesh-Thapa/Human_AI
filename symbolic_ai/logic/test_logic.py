import unittest

from .pattern_discoverer import PatternDiscoverer
from .symbol_recognizer import SymbolRecognizer
from .logic_chain import LogicChain
from symbolic_ai.core.memory_manager import MemoryManager


class TestLogic(unittest.TestCase):
    def test_cluster(self):
        pats = [
            {"vector": [1, 2]},
            {"vector": [1, 2]},
            {"vector": [3]}
        ]
        clusters = PatternDiscoverer().cluster(pats)
        self.assertEqual(len(clusters[(1, 2)]), 2)

    def test_recognizer(self):
        mem = MemoryManager()
        mem.memory = {"a": [{"ascii": 97, "vector": [1]}]}
        recog = SymbolRecognizer(mem)
        self.assertEqual(recog.recognize("a"), "a")
        self.assertEqual(recog.recognize("b"), "a")

    def test_logic_chain(self):
        chain = LogicChain()
        chain.add_link("1", "2")
        chain.add_link("2", "3")
        self.assertTrue(chain.infer("1", "3"))


if __name__ == "__main__":
    unittest.main()
