import urllib.request
from .content_scraper import ContentScraper


class WebDownloader:
    """Fetch a URL and extract alphabetical symbols from its contents."""

    def __init__(self) -> None:
        self.scraper = ContentScraper()

    def fetch(self, url: str) -> list[str]:
        try:
            with urllib.request.urlopen(url, timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
        except Exception:
            html = ""
        letters = self.scraper.scrape(html)
        return [ch.upper() for ch in letters]
