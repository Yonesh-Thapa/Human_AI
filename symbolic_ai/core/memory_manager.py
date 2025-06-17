import json
from pathlib import Path


class MemoryManager:
    """Manage symbolic memory as a small JSON based store."""

    MEMORY_FILE = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "memory"
        / "memory.json"
    )

    def __init__(self):
        self.patterns = []
        if self.MEMORY_FILE.exists():
            try:
                self.patterns = json.loads(self.MEMORY_FILE.read_text())
            except Exception:
                self.patterns = []

    def add_pattern(self, pattern: str) -> None:
        """Add a new symbolic pattern and persist it."""
        self.patterns.append(pattern)
        self._save()

    def prune(self, max_size: int = 10) -> None:
        """Remove oldest patterns if memory exceeds ``max_size``."""
        while len(self.patterns) > max_size:
            self.patterns.pop(0)
        self._save()

    def _save(self) -> None:
        self.MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        self.MEMORY_FILE.write_text(json.dumps(self.patterns))
