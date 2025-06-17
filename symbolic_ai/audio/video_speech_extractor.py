class VideoSpeechExtractor:
    """Dummy extractor that returns raw bytes from provided content."""

    def extract(self, data: bytes | str) -> bytes:
        """Return ``data`` as bytes, simulating extraction."""
        if isinstance(data, bytes):
            return data
        if isinstance(data, str):
            return data.encode("utf-8")
        return b""
