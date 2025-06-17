import unittest

from .alphabet_poet import AlphabetPoet
from .symbolic_art_generator import SymbolicArtGenerator
from .imaginary_language_builder import ImaginaryLanguageBuilder


class TestCreativity(unittest.TestCase):
    def test_poet(self):
        poet = AlphabetPoet()
        self.assertIn("stands", poet.compose("a"))

    def test_art(self):
        art = SymbolicArtGenerator()
        self.assertIn("b", art.create("b"))

    def test_language(self):
        builder = ImaginaryLanguageBuilder()
        self.assertIsInstance(builder.invent(), list)


if __name__ == "__main__":
    unittest.main()
