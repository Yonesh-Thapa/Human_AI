import unittest
from .symbolic_art_generator import SymbolicArtGenerator


class TestCreativity(unittest.TestCase):
    def test_art(self):
        art = SymbolicArtGenerator().create("Z")
        self.assertIn("Z", art)


if __name__ == "__main__":
    unittest.main()
