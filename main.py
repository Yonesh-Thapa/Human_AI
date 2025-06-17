from symbolic_ai.core.brain_controller import BrainController
from symbolic_ai.core.memory_manager import MemoryManager


def main():
    memory = MemoryManager()
    brain = BrainController(memory)

    for char in "abcABC123":
        output = brain.run(char)
        print(f"{char} => {output}")

    print("\U0001F4E6 Stored patterns:", memory.all_symbols())




if __name__ == "__main__":
    main()
