from symbolic_ai.tools.camera_handler import CameraHandler
from .character_shape_trainer import CharacterShapeTrainer
from .shape_identifier import ShapeIdentifier

try:  # optional OpenCV import
    import cv2
except Exception:  # pragma: no cover - OpenCV may not be installed
    cv2 = None


class CameraReader:
    """Read letters from a webcam using very simple pattern matching."""

    def __init__(self):
        self.camera = CameraHandler()
        self.cap = cv2.VideoCapture(0) if cv2 else None
        self.trainer = CharacterShapeTrainer()
        for ch in "ABC":
            img = self.trainer.render_letter(ch)
            self.trainer.train(img, ch)
        self.identifier = ShapeIdentifier(self.trainer.patterns)

    def read_letter(self) -> str:
        if self.cap:
            ret, frame = self.cap.read()
            if not ret:
                frame = [[0]]
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            pixels = int(gray.sum())
        else:
            frame = self.camera.capture()
            pixels = sum(sum(row) for row in frame)
        return self.identifier.identify([pixels])
