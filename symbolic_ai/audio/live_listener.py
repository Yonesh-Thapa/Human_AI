from symbolic_ai.audio.speech_letter_linker import SpeechLetterLinker


class VoiceListener:
    """Listen for spoken letters via standard input."""

    def __init__(self):
        self.linker = SpeechLetterLinker()

    def listen(self) -> list[str]:
        """Prompt the user and return a list of letters."""
        audio = input("\U0001F3A4 Say letters: ")
        return self.linker.link(audio)
