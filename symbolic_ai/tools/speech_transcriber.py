class SpeechTranscriber:
    """Converts raw bytes to a UTF-8 string (mock transcription)."""

    def transcribe(self, audio: bytes | str) -> str:
        if isinstance(audio, bytes):
            try:
                return audio.decode("utf-8")
            except Exception:
                return ""
        return str(audio or "")
