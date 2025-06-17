class SymbolicPatternDiscoverer:
    """Recognizes simple frequency patterns in sequences."""

    def discover(self, sequence: str) -> dict:
        freq = {}
        for ch in sequence:
            freq[ch] = freq.get(ch, 0) + 1
        return freq
