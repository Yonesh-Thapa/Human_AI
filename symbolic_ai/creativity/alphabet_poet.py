class AlphabetPoet:
    """Generates a tiny two-line poem about a letter."""

    def compose(self, letter: str) -> str:
        line1 = f"{letter.upper()} stands strong."
        line2 = f"{letter.lower()} whispers along."
        return "\n".join([line1, line2])
