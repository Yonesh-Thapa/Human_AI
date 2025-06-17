class SymbolRecognizer:
    """Recognize known symbols or return best approximate match."""

    def __init__(self, memory_manager: "MemoryManager"):
        self.memory = memory_manager

    def recognize(self, symbol: str) -> str:
        if symbol in self.memory.memory:
            return symbol
        ascii_val = ord(symbol)
        best = None
        best_diff = float("inf")
        for sym, patterns in self.memory.memory.items():
            diff = abs(patterns[0]["ascii"] - ascii_val)
            if diff < best_diff:
                best = sym
                best_diff = diff
        return best if best is not None else ""
