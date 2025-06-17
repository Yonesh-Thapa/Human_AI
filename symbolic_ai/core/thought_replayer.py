class ThoughtReplayer:
    """Replay stored patterns from memory for analysis."""

    def replay(self, memory: "MemoryManager") -> list[dict]:
        patterns: list[dict] = []
        for symbol in memory.all_symbols():
            patterns.extend(memory.memory.get(symbol, []))
        return patterns
