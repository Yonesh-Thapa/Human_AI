class FontDownloader:
    """Pretend to download fonts by validating the name."""

    def download(self, name: str) -> bool:
        return bool(name)
