# Problem: Rearrange String k Distance Apart
# Language: python3
# Runtime: 124 ms
# Memory: 14.7 MB

from heapq import *
from collections import Counter
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        c = Counter(s)
        
        h = []
        for key,v in c.items():
            heappush(h, (-v, key))
        
        # "aabbcc" 2a2b2c
        res = ""
        
        while h:
            count = 0 
            h2 = set()
            while h:
                count += 1
                v,l = heappop(h)
                res += l
                v = -v
                v -= 1
                
                if v > 0:
                    h2.add((-v,l))
                
                if count == k:
                    break
            
            if h2 and count < k:
                return ""
            
            for e in h2:
                heappush(h, e)
        
        return res
                