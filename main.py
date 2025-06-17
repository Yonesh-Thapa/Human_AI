from symbolic_ai.ai_autopilot import AutonomousAI


def main() -> None:
    print("Where should I learn from? (camera / voice / web)")
    source = input("> ").strip().lower()
    ai = AutonomousAI(source)
    ai.run()


if __name__ == "__main__":
    main()
