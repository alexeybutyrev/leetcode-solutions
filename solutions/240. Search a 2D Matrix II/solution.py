# Problem: Search a 2D Matrix II
# Language: python3
# Runtime: 274 ms
# Memory: 20.5 MB

class Solution:
    def searchMatrix(self, A: List[List[int]], target: int) -> bool:
        #A = list(zip(*A))
        N,M = len(A), len(A[0])
        
        for B in A:
            row = bisect_right(B,target)
            if B[row-1] == target:
                return True
        return False
        
            
            
            
        