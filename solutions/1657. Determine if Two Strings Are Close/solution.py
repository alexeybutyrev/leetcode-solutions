# Problem: Determine if Two Strings Are Close
# Language: python3
# Runtime: 124 ms
# Memory: 15 MB

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n = len(word1)
        if len(word2) != n:
            return False
        
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        return sorted(c1.values()) == sorted(c2.values()) and set(c1.keys()) == set(c2.keys())

        