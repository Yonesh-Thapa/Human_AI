class ShapeIdentifier:
    """Matches patterns for unknown letters based on pixel counts."""

    def __init__(self, patterns: dict[str, int]):
        self.patterns = patterns

    def identify(self, image: list[int]) -> str:
        pixels = sum(image)
        closest = min(self.patterns.items(), key=lambda kv: abs(kv[1] - pixels), default=("?", None))
        return closest[0]
