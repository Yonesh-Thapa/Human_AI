import re

try:  # optional requests import
    import requests
except Exception:  # pragma: no cover - requests may be missing
    requests = None
from html import unescape
from urllib.request import urlopen


class BrowserReader:
    """Fetch web pages and extract readable text."""

    def read(self, html: str) -> str:
        cleaned = re.sub(r"<[^>]+>", "", html or "")
        return unescape(cleaned.strip())

    def fetch_text(self, url: str) -> str:
        """Download ``url`` using requests if available."""
        html = ""
        if requests:
            try:
                html = requests.get(url, timeout=5).text
            except Exception:
                html = ""
        else:
            try:
                with urlopen(url, timeout=5) as resp:
                    html = resp.read().decode("utf-8", errors="ignore")
            except Exception:
                html = ""
        return self.extract(html)

    def extract(self, html: str) -> str:
        """Return text from bold/headline/link/paragraph tags."""
        matches = re.findall(r"<(b|strong|h[1-6]|a|p)[^>]*>(.*?)</[^>]+>", html, re.I | re.S)
        text = " ".join(unescape(m[1]).strip() for m in matches)
        return self.read(text)
