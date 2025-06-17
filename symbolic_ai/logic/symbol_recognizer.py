class SymbolRecognizer:
    """Recognize known symbols and return their stored pattern."""

    def __init__(self, memory_manager: "MemoryManager"):
        self.memory = memory_manager

    def recognize(self, symbol: str) -> dict:
        """Return pattern dict for ``symbol`` or closest match."""
        if symbol in self.memory.memory:
            return self.memory.memory[symbol][0]
        ascii_val = ord(symbol)
        best = None
        best_diff = float("inf")
        for sym, patterns in self.memory.memory.items():
            diff = abs(patterns[0]["ascii"] - ascii_val)
            if diff < best_diff:
                best = sym
                best_diff = diff
        if best is not None:
            return self.memory.memory[best][0]
        return {}
