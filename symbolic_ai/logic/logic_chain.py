from typing import Optional


class LogicChain:
    """Simple symbolic deduction chain."""

    def __init__(self, memory: Optional["MemoryManager"] = None):
        self.links: dict[str, set[str]] = {}
        self.memory = memory

    def add_link(self, a: str, b: str) -> None:
        self.links.setdefault(a, set()).add(b)

    def infer(self, start: str, end: str) -> bool:
        visited: set[str] = set()

        def dfs(symbol: str) -> bool:
            if symbol == end:
                return True
            if symbol in visited:
                return False
            visited.add(symbol)
            for nxt in self.links.get(symbol, set()):
                if dfs(nxt):
                    return True
            return False

        return dfs(start)

    def process(self, sequence: list[str]) -> None:
        """Add links between each consecutive symbol in ``sequence``."""
        for a, b in zip(sequence, sequence[1:]):
            self.add_link(a, b)

    def explain(self, start: str, depth: int = 3) -> list[str]:
        """Return a reasoning chain starting from ``start`` up to ``depth`` steps."""
        path = [start]
        current = start
        for _ in range(depth):
            next_set = self.links.get(current)
            if not next_set:
                break
            current = sorted(next_set)[0]
            path.append(current)
        return path
