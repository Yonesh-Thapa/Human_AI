class HandwritingDecoder:
    """Very small decoder that checks if any pixels are present."""

    def decode(self, image) -> str:
        if image is None:
            return "?"
        return "#" if sum(image) > 0 else "?"
