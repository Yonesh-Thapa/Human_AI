from symbolic_ai.vision.camera_reader import CameraReader


class VisionReader:
    """Simple wrapper that returns a letter from the camera."""

    def __init__(self):
        self.camera = CameraReader()

    def scan(self) -> list[str]:
        """Capture a single letter from the camera."""
        return [self.camera.read_letter()]
