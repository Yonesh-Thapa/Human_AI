class SymbolicArtGenerator:
    """Create a mini ASCII art representation of a letter."""

    def create(self, letter: str) -> str:
        top = f" /{letter}\ "
        mid = f"| {letter} |"
        bot = f" \_{letter}_/"
        return "\n".join([top, mid, bot])
