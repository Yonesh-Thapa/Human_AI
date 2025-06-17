import re


class ContentScraper:
    """Extract alphabetical characters from HTML content."""

    def scrape(self, html: str) -> list[str]:
        text = re.sub(r"<[^>]+>", "", html or "")
        return [ch for ch in text if ch.isalpha()]
