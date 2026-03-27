# Problem: Leftmost Column with at Least a One
# Language: python3
# Runtime: 101 ms
# Memory: 14 MB

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, M: 'BinaryMatrix') -> int:
        n,m = M.dimensions()
        j = m - 1
        ans = inf
        for i in range(n-1,-1,-1):
            
            while j >=0 and M.get(i,j):
                ans = min(ans, j)
                j -= 1
                
        return -1 if ans == inf else ans