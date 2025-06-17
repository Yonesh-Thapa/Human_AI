try:  # optional speech_recognition import
    import speech_recognition as sr
except Exception:  # pragma: no cover - library may be missing
    sr = None


class SpeechToLetter:
    """Convert microphone bytes to letters and support continuous listening."""

    def __init__(self) -> None:
        if sr:
            try:
                self.rec = sr.Recognizer()
                self.mic = sr.Microphone()
            except Exception:  # pragma: no cover - microphone not available
                self.rec = None
                self.mic = None
        else:
            self.rec = None
            self.mic = None

    def convert(self, data: bytes) -> str:
        try:
            text = data.decode("utf-8").strip()
        except Exception:
            text = ""
        return text[:1].upper() if text else ""

    def listen(self) -> list[str]:
        """Continuously capture speech and return recognized letters."""
        if self.rec and self.mic:
            with self.mic as source:
                audio = self.rec.listen(source)
            try:
                text = self.rec.recognize_google(audio)
            except Exception:  # pragma: no cover - speech recognition may fail
                text = ""
        else:
            text = input("\U0001F3A4 Say letters: ")
        return [part.strip().upper()[:1] for part in text.split() if part.strip()]
