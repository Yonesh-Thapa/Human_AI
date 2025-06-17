class SpeechLetterLinker:
    """Links simple spoken letter strings to symbols."""

    def link(self, audio: str) -> list[str]:
        """Convert a string of spoken letters into a list of uppercase letters."""
        if not audio:
            return []
        return [part.strip().upper()[:1] for part in audio.split() if part.strip()]
