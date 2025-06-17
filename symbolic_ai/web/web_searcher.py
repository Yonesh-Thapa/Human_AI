from symbolic_ai.tools.browser_reader import BrowserReader


class WebSearcher:
    """Extract letters from provided HTML text via standard input."""

    def __init__(self):
        self.browser = BrowserReader()

    def extract_symbols(self) -> list[str]:
        html = input("\U0001F310 Enter HTML: ")
        text = self.browser.read(html)
        return [ch.upper() for ch in text if ch.isalpha()]
