class LetterMeaningEngine:
    """Provide a very small mapping of letters to symbolic meaning."""

    _meaning = {
        "a": "start",
        "z": "end",
    }

    def meaning(self, letter: str) -> str:
        """Return a symbolic meaning for ``letter`` if known."""
        return self._meaning.get(letter.lower(), "unknown")
