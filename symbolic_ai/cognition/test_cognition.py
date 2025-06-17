import unittest

from .letter_meaning_engine import LetterMeaningEngine
from .symbolic_pattern_discoverer import SymbolicPatternDiscoverer
from .emotional_letter_mapper import EmotionalLetterMapper


class TestCognition(unittest.TestCase):
    def test_meaning(self):
        engine = LetterMeaningEngine()
        self.assertEqual(engine.meaning("a"), "start")

    def test_discover(self):
        discoverer = SymbolicPatternDiscoverer()
        self.assertEqual(discoverer.discover("abca"), {"a": 2, "b": 1, "c": 1})

    def test_emotion(self):
        mapper = EmotionalLetterMapper()
        self.assertEqual(mapper.emotion("z"), "sleepy")


if __name__ == "__main__":
    unittest.main()
