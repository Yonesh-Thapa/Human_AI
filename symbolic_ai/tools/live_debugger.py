class LiveDebugger:
    """Print a summary of learned symbols and pattern counts."""

    def __init__(self, memory_manager: "MemoryManager"):
        self.memory = memory_manager

    def display(self) -> None:
        for symbol, patterns in self.memory.memory.items():
            print(f"{symbol}: {len(patterns)} patterns")


class Debugger:
    """Lightweight logger for the autonomous AI."""

    def update(self, msg: str) -> None:
        print(f"[UPDATE] {msg}")

    def log(self, msg: str) -> None:
        print(msg)
