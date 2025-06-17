class PatternDiscoverer:
    """Cluster patterns by the sum of their vectors."""

    def cluster(self, patterns: list[dict]) -> dict[int, list[dict]]:
        clusters: dict[int, list[dict]] = {}
        for pat in patterns:
            key = sum(pat.get("vector", []))
            clusters.setdefault(key, []).append(pat)
        return clusters
