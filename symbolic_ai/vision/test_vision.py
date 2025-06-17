from .character_shape_trainer import CharacterShapeTrainer
from .shape_identifier import ShapeIdentifier
from .handwriting_decoder import HandwritingDecoder
from .live_character_reader import LiveCharacterReader


def test_train():
    trainer = CharacterShapeTrainer()
    assert trainer.train(None)

def test_identify():
    identifier = ShapeIdentifier()
    assert identifier.identify(None) == "?"

def test_decode():
    decoder = HandwritingDecoder()
    assert decoder.decode(None) == "?"

def test_live_reader():
    reader = LiveCharacterReader()
    assert reader.read() is None
