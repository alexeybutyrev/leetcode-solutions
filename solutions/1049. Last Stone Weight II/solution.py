# Problem: Last Stone Weight II
# Language: python3
# Runtime: 44 ms
# Memory: 14.6 MB

from heapq import *
class Solution:
    def lastStoneWeightII(self, A: List[int]) -> int:
        
        dp = {0}
        for a in A:
            dp = {a + x for x in dp} | {a - x for x in dp}
        return min(abs(x) for x in dp)