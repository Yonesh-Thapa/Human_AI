from urllib.parse import urlparse


class WebLetterCrawler:
    """Extract words from a fake URL."""

    def crawl(self, url: str) -> str:
        path = urlparse(url).path
        return path.strip("/")
