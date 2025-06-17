from symbolic_ai.web.deepseek_ai_connector import DeepSeekAIConnector


class DeepSeekConnector:
    """Wrapper around ``DeepSeekAIConnector`` used by the autonomous AI."""

    def __init__(self):
        self.client = DeepSeekAIConnector()

    def ask(self, text: str) -> str:
        return self.client.query(text)
