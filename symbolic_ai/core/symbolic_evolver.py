class SymbolicEvolver:
    """Very small symbolic evolution engine."""

    def evolve(self, symbol: str) -> str:
        """Return a transformed version of ``symbol`` used as a toy evolution."""
        if not isinstance(symbol, str):
            raise TypeError("symbol must be a string")
        return symbol[::-1].upper()
