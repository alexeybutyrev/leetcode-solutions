# Problem: First Unique Character in a String
# Language: python3
# Runtime: 76 ms
# Memory: 13.8 MB

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = Counter(s)
        
        for i in range(len(s)):
            if 1 == hm[s[i]]:
                return i
        return -1