import unittest

from .character_shape_trainer import CharacterShapeTrainer
from .shape_identifier import ShapeIdentifier
from .handwriting_decoder import HandwritingDecoder
from .live_character_reader import LiveCharacterReader


class TestVision(unittest.TestCase):
    def test_train(self):
        trainer = CharacterShapeTrainer()
        img = trainer.render_letter("a")
        self.assertTrue(trainer.train(img, "a"))

    def test_identify(self):
        trainer = CharacterShapeTrainer()
        img = trainer.render_letter("b")
        trainer.train(img, "b")
        identifier = ShapeIdentifier(trainer.patterns)
        self.assertEqual(identifier.identify(img), "b")

    def test_decode(self):
        decoder = HandwritingDecoder()
        self.assertEqual(decoder.decode(None), "?")

    def test_live_reader(self):
        reader = LiveCharacterReader()
        self.assertIsNotNone(reader.read())


if __name__ == "__main__":
    unittest.main()
