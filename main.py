from symbolic_ai.core.brain_controller import BrainController
from symbolic_ai.core.memory_manager import MemoryManager


def main():
    """Run a simple demo processing a few letters."""
    memory = MemoryManager()
    brain = BrainController(memory)

    for letter in "abc":
        evolved = brain.run(letter)
        print(f"{letter} -> {evolved}")

    print("Stored patterns:", memory.patterns)


if __name__ == "__main__":
    main()
