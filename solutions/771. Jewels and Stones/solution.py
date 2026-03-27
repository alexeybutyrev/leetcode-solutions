# Problem: Jewels and Stones
# Language: python3
# Runtime: 24 ms
# Memory: 13.7 MB

from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J:
            return 0
        c = Counter(S)
        res = 0
        for k in J:
            if k in c:
               res += c[k]
        
        return res