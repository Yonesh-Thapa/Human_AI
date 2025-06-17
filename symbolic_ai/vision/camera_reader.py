from symbolic_ai.tools.camera_handler import CameraHandler
from .character_shape_trainer import CharacterShapeTrainer
from .shape_identifier import ShapeIdentifier


class CameraReader:
    """Read letters from a webcam using very simple pattern matching."""

    def __init__(self):
        self.camera = CameraHandler()
        self.trainer = CharacterShapeTrainer()
        for ch in "ABC":
            img = self.trainer.render_letter(ch)
            self.trainer.train(img, ch)
        self.identifier = ShapeIdentifier(self.trainer.patterns)

    def read_letter(self) -> str:
        frame = self.camera.capture()
        pixels = sum(sum(row) for row in frame)
        return self.identifier.identify([pixels])
