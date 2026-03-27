# Problem: Reorganize String
# Language: python3
# Runtime: 24 ms
# Memory: 14.2 MB

from collections import Counter
from heapq import *
class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        
        max_v = -1
        h = []
        for k,v in c.items():
            max_v = max(v, max_v)
            heappush(h,(-v,k))
        
        #if max_v > len(c) + 1:
        #    return ""
        
        #print(h)
        res = ""
        while h:
            
            v1,l1 = heappop(h)
            
            if h and h[0][0] > v1:
                while h and h[0][0] > v1:
                    v1  += 1
                    res += l1

                    v2,l2 = heappop(h)
                    v2  += 1
                    res += l2

                    if v2 != 0:
                        heappush(h,(v2,l2))

            else:
                v1  += 1
                res += l1
            if v1 != 0:
                heappush(h,(v1,l1))
                
                
             
            if len(h) == 1 and h[0][0] != -1:
                return ""
        return res
                