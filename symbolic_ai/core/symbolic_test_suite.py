from .brain_controller import BrainController
from .memory_manager import MemoryManager


def self_check():
    mem = MemoryManager()
    brain = BrainController(mem)
    result = brain.run("b")
    return "b" in mem.memory and result in mem.memory["b"]
