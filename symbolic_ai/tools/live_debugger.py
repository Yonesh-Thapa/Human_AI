class LiveDebugger:
    """Print a summary of learned symbols and pattern counts."""

    def __init__(self, memory_manager: "MemoryManager"):
        self.memory = memory_manager

    def display(self) -> None:
        for symbol, patterns in self.memory.memory.items():
            print(f"{symbol}: {len(patterns)} patterns")
