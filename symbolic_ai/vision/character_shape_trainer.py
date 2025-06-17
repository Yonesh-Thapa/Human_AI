class CharacterShapeTrainer:
    """Stores simple numeric patterns for letters."""

    def __init__(self):
        self.patterns: dict[str, int] = {}

    def render_letter(self, letter: str) -> list[int]:
        return [ord(letter)]

    def train(self, image: list[int], letter: str = "?") -> bool:
        pixels = sum(image)
        self.patterns[letter] = pixels
        return True
