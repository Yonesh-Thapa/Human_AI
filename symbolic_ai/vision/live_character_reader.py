from symbolic_ai.tools.camera_handler import CameraHandler


class LiveCharacterReader:
    """Camera-based real-time recognition (mocked)."""

    def __init__(self):
        self.camera = CameraHandler()

    def read(self):
        return self.camera.capture()
