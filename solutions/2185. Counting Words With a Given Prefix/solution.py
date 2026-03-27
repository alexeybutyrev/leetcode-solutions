# Problem: Counting Words With a Given Prefix
# Language: python3
# Runtime: 0 ms
# Memory: 18 MB

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w.startswith(pref) for w in words)