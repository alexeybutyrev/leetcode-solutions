# Problem: Maximum Number of Consecutive Values You Can Make
# Language: python3
# Runtime: 916 ms
# Memory: 19.7 MB

from heapq import *
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        
        coins.sort()
        k = 1
        
        
        for c in coins:
            if c <= k:
                k += c
            else:
                break

        return k
            