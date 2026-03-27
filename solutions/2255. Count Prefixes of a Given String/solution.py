# Problem: Count Prefixes of a Given String
# Language: python3
# Runtime: 68 ms
# Memory: 14.2 MB

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(s.startswith(w) for w in words)