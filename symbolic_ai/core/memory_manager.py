class MemoryManager:
    """Manage symbolic memory with compression and pruning."""

    def __init__(self):
        self.patterns = []

    def add_pattern(self, pattern):
        self.patterns.append(pattern)

    def prune(self):
        if self.patterns:
            self.patterns.pop(0)
