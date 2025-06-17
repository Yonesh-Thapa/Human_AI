class LetterToSoundMapper:
    """Maps letters to simple English phonetic representations."""

    _table = {
        "a": "ay",
        "b": "bee",
        "c": "cee",
        "d": "dee",
        "e": "ee",
        "f": "ef",
        "g": "gee",
        "h": "aitch",
        "i": "eye",
        "j": "jay",
        "k": "kay",
        "l": "el",
        "m": "em",
        "n": "en",
        "o": "oh",
        "p": "pee",
        "q": "cue",
        "r": "ar",
        "s": "ess",
        "t": "tee",
        "u": "you",
        "v": "vee",
        "w": "double you",
        "x": "ex",
        "y": "why",
        "z": "zee",
    }

    def map(self, letter: str) -> str:
        """Return the phonetic sound for a given letter."""
        return self._table.get(letter.lower(), "")
