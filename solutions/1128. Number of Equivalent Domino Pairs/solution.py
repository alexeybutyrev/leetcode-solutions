# Problem: Number of Equivalent Domino Pairs
# Language: python3
# Runtime: 265 ms
# Memory: 23.6 MB

from math import comb
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:        
        return sum(v * (v - 1)//2 for v in Counter([(a,b) if a < b else (b,a) for a,b in dominoes]).values())