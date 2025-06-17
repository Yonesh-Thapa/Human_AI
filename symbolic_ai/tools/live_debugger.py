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

    def show_status(self, memory: "MemoryManager", next_goal: str | None = None) -> None:
        """Display memory usage and upcoming goal."""
        total = sum(len(p) for p in memory.memory.values())
        print(f"[MEM] stored patterns: {total}")
        if next_goal:
            print(f"[NEXT] {next_goal}")
