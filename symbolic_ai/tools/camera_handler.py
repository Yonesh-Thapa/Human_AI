try:  # optional OpenCV import
    import cv2
except Exception:  # pragma: no cover - OpenCV may be missing
    cv2 = None


class CameraHandler:
    """Handles webcam capture using OpenCV when available."""

    def __init__(self) -> None:
        self.cap = cv2.VideoCapture(0) if cv2 else None

    def capture(self) -> list[list[int]]:
        """Capture a small grayscale matrix from the webcam."""
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                small = cv2.resize(gray, (5, 5))
                return small.tolist()
        return [[255]]
