# Problem: Number of Good Ways to Split a String
# Language: python3
# Runtime: 392 ms
# Memory: 14.3 MB

from collections import Counter

class Solution:
    def numSplits(self, s: str) -> int:
        
        
        n = len(s)
        if n < 2:
            return 0
        
        
        
        cr = Counter(s)
        cl = Counter()
        
        count = 0
        for i in range(n):
            cl[s[i]] += 1
            cr[s[i]] -= 1
            if cr[s[i]] == 0:
                del cr[s[i]]
                
            #print(cl,cr)
            if len(cl) == len(cr):
                count += 1
        return count