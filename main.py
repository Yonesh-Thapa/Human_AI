from symbolic_ai.core.brain_controller import BrainController
from symbolic_ai.core.memory_manager import MemoryManager


def main():
    memory = MemoryManager()
    brain = BrainController(memory)
    print(brain.run("a"))


if __name__ == "__main__":
    main()
