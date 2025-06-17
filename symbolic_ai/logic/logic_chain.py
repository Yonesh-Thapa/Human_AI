class LogicChain:
    """Simple symbolic deduction chain."""

    def __init__(self):
        self.links: dict[str, set[str]] = {}

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
