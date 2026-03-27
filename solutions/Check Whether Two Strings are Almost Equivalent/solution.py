# Problem: Check Whether Two Strings are Almost Equivalent
# Language: python3
# Runtime: 28 ms
# Memory: 14.3 MB

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        for k in c1:
            if abs(c1[k] - c2[k]) > 3:
                return False
        
        for k in c2:
            if abs(c1[k] - c2[k]) > 3:
                return False
        
        return True
        