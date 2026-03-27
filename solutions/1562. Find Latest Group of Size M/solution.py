# Problem: Find Latest Group of Size M
# Language: python3
# Runtime: 960 ms
# Memory: 28.2 MB

from itertools import groupby
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        N = len(arr)
        if N == m:
            return m
        size = [0] + [0] * N + [0]
        
        ans = -1
        for k,a in enumerate(arr):
            
            size[a] += 1
            
            left = size[a-1]
            right = size[a+1]
            
            if left == m or right == m:
                ans = k
                
            size[a-left] = size[a+right] = left + right + 1
                
        return ans