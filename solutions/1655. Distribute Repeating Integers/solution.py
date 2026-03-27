# Problem: Distribute Repeating Integers
# Language: python3
# Runtime: 4164 ms
# Memory: 25.8 MB

from collections import Counter
from heapq import *
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        c = collections.Counter(nums)

        n = len(quantity)
        quantity.sort(reverse=True)
        
        left = sorted(c.values())[-n:]
        def backtrack(i,left):
            if i == n:
                return True
            
            
            res = False
            val = quantity[i]
            for j in range(len(left)):
                if left[j] >= val:
                    left[j] -= val
                    if backtrack(i+1,left):
                        return True
                    left[j] += val
            
            return res
        
        return backtrack(0,left)
    