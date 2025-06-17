class CameraHandler:
    """Handles webcam capture (returns 1x1 pixel matrix)."""

    def capture(self) -> list[list[int]]:
        """Return a single white pixel represented as nested list."""
        return [[255]]
