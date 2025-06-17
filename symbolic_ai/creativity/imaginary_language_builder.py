class ImaginaryLanguageBuilder:
    """Generate a small imaginary alphabet from shifted ASCII letters."""

    def invent(self, count: int = 3) -> list[str]:
        base = ord('α')  # greek alpha as start
        return [chr(base + i) for i in range(count)]
