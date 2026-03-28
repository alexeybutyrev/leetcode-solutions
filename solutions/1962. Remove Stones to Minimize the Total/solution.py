# Problem: Remove Stones to Minimize the Total
# Language: python3
# Runtime: 2585 ms
# Memory: 28.3 MB

from math import ceil
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = []
        for p in piles:
            heappush(h,-p)
        
        for _ in range(k):
            
            p = heappop(h)
            p = -p
            p = ceil(p/2)
            heappush(h,-p)
            if not h:
                return 0
        
        return -sum(h)