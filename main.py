from symbolic_ai.core.memory_manager import MemoryManager
from symbolic_ai.core.learning_loop import LearningLoop


def main() -> None:
    print("Where should I learn from? (camera / voice / web)")
    source = input("> ").strip().lower()
    if source not in {"camera", "voice", "web"}:
        print("Unknown source, defaulting to camera")
        source = "camera"
    memory = MemoryManager()
    loop = LearningLoop(memory)
    loop.run_autonomous(source)


if __name__ == "__main__":
    main()
