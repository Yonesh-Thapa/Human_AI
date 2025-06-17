class BrainController:
    """Main symbolic brain controller handling pattern creation."""

    def __init__(self, memory_manager: "MemoryManager"):
        self.memory = memory_manager

    def run(self, input_letter: str) -> dict:
        """Generate a basic pattern for ``input_letter`` and store it."""
        shape = ord(input_letter)
        pattern = {
            "symbol": input_letter,
            "ascii": shape,
            "vector": [shape % 3, shape % 5, shape % 7],
        }
        self.memory.store(input_letter, pattern)
        return pattern
