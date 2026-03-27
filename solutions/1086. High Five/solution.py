# Problem: High Five
# Language: python3
# Runtime: 68 ms
# Memory: 14.5 MB

from heapq import *
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort()
        n = len(items)
        
        h = []
        j = 0
        res = []
        while j < n:
            cid = items[j][0]
            h = []
            while j < n and items[j][0] == cid:
                heappush(h, items[j][1])
                if len(h) > 5:
                    v = heappop(h)
                j += 1
            res.append([cid, int(sum(h) / len(h))])
            
                
        return res