from symbolic_ai.ai_autopilot import AutonomousAI


def main() -> None:
    print("Where should I learn from? (camera / voice / web)")
    source = input("> ").strip().lower()
    if source not in {"camera", "voice", "web"}:
        print("Unknown source, defaulting to camera")
        source = "camera"
    ai = AutonomousAI(source)
    ai.run()


if __name__ == "__main__":
    main()
