# Problem: Largest Substring Between Two Equal Characters
# Language: python3
# Runtime: 24 ms
# Memory: 14.2 MB

from collections import Counter
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        c = Counter(s)
        
        max_ln = -1
        for k,v in c.items():
            if v > 1:
                i1 = s.find(k)
                i2 = s.rfind(k)
                max_ln = max(i2-i1-1, max_ln)
        
        return max_ln