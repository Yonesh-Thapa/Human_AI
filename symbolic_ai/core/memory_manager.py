import json
import os

MEMORY_PATH = "symbolic_ai/data/memory/memory.json"


class MemoryManager:
    """Store patterns for each symbol without duplication."""

    def __init__(self):
        self.memory = self.load()

    def load(self) -> dict:
        if os.path.exists(MEMORY_PATH):
            with open(MEMORY_PATH, "r") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data
        return {}

    def store(self, symbol: str, pattern: dict) -> None:
        if symbol not in self.memory:
            self.memory[symbol] = []
        if pattern not in self.memory[symbol]:
            self.memory[symbol].append(pattern)
        self.save()

    def save(self) -> None:
        os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
        with open(MEMORY_PATH, "w") as f:
            json.dump(self.memory, f, indent=2)

    def all_symbols(self) -> list:
        return list(self.memory.keys())
