try:  # optional speech_recognition import
    import speech_recognition as sr
except Exception:  # pragma: no cover - library may be missing
    sr = None


class SpeechTranscriber:
    """Transcribe audio or live microphone input into text."""

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

    def transcribe(self, audio: bytes | str) -> str:
        if isinstance(audio, bytes):
            try:
                return audio.decode("utf-8")
            except Exception:
                return ""
        return str(audio or "")

    def listen_live(self) -> list[str]:
        """Capture speech from the microphone and return tokens."""
        if self.rec and self.mic:
            with self.mic as source:
                audio = self.rec.listen(source)
            try:
                text = self.rec.recognize_google(audio)
            except Exception:  # pragma: no cover - recognition may fail
                text = ""
        else:
            text = input("\U0001F399 Speak words: ")
        return [t for t in text.split() if t]
