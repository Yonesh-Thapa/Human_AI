class YouTubeLetterLearner:
    """Pretend to learn letters from a YouTube URL."""

    def learn(self, url: str) -> bool:
        return url.startswith("http")
