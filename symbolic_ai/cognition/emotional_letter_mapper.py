class EmotionalLetterMapper:
    """Associate letters with basic emotions."""

    _emotion = {
        "z": "sleepy",
    }

    def emotion(self, letter: str) -> str:
        """Return the emotion linked to ``letter``."""
        return self._emotion.get(letter.lower(), "neutral")
