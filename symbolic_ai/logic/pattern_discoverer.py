class PatternDiscoverer:
    """Cluster similar vector patterns by their tuple representation."""

    def cluster(self, patterns: list[dict]) -> dict[tuple, list[dict]]:
        clusters: dict[tuple, list[dict]] = {}
        for pat in patterns:
            vect = tuple(pat.get("vector", []))
            clusters.setdefault(vect, []).append(pat)
        return clusters
