from symbolic_ai.audio.speech_to_letter import SpeechToLetter


class VoiceListener:
    """Listen for spoken letters via standard input."""

    def __init__(self):
        self.speech = SpeechToLetter()

    def listen(self) -> list[str]:
        """Prompt the user and return a list of letters."""
        return self.speech.listen()
