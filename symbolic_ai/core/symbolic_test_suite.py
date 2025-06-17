from .brain_controller import BrainController
from .memory_manager import MemoryManager


def self_check():
    mem = MemoryManager()
    brain = BrainController(mem)
    result = brain.run("b")
    return mem.patterns and mem.patterns[-1] == result
