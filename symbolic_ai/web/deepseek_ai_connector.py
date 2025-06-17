class DeepSeekAIConnector:
    """Mock connector returning uppercase responses."""

    def query(self, text: str) -> str:
        return text.upper()
