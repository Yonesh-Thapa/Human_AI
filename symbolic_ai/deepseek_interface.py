from symbolic_ai.web.deepseek_connector import DeepSeekConnector

class DeepSeekInterface:
    """Simple helper that queries DeepSeek when clarification is needed."""

    def __init__(self) -> None:
        self.connector = DeepSeekConnector()

    def clarify(self, question: str) -> str:
        """Return the answer from DeepSeek or an empty string on failure."""
        try:
            return self.connector.ask(question)
        except Exception:
            return ""
