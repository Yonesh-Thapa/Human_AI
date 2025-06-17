from .alphabet_poet import AlphabetPoet
from .symbolic_art_generator import SymbolicArtGenerator
from .imaginary_language_builder import ImaginaryLanguageBuilder


def test_poet():
    poet = AlphabetPoet()
    assert "poem" in poet.compose('a')

def test_art():
    art = SymbolicArtGenerator()
    assert art.create('b') == 'art_b'

def test_language():
    builder = ImaginaryLanguageBuilder()
    assert builder.invent() == []
