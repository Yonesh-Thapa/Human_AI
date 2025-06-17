from .symbolic_evolver import SymbolicEvolver


class BrainController:
    """Main symbolic brain loop controller."""

    def __init__(self, memory_manager: "MemoryManager"):
        self.memory = memory_manager
        self.evolver = SymbolicEvolver()

    def run(self, symbol: str = "a") -> str:
        """Process ``symbol`` through the evolution pipeline and store it."""
        evolved = self.evolver.evolve(symbol)
        self.memory.add_pattern(evolved)
        self.memory.prune()
        return evolved
