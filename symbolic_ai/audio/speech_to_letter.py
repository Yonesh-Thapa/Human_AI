class SpeechToLetter:
    """Convert microphone bytes to a single uppercase letter."""

    def convert(self, data: bytes) -> str:
        try:
            text = data.decode("utf-8").strip()
        except Exception:
            text = ""
        return text[:1].upper() if text else ""
