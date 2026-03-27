# Problem: Minimum Swaps to Arrange a Binary Grid
# Language: python3
# Runtime: 8 ms
# Memory: 20.8 MB

from math import inf
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0]) 
        
        zeros = []
        for r in grid:
            count = 0
            for c in range(M-1,-1,-1):
                if r[c] == 1:
                    break
                else:
                    count += 1
            zeros.append(count)
        
        count = 0
        for k in range(M-1,-1,-1):
            for i, v in enumerate(zeros):
                if v >= k:
                    zeros.pop(i)
                    count += i
                    break
            else:
                return -1
        return count