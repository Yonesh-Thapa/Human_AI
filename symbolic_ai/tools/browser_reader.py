import re


class BrowserReader:
    """Parses provided HTML text and returns plain text."""

    def read(self, html: str) -> str:
        cleaned = re.sub(r"<[^>]+>", "", html or "")
        return cleaned.strip()
