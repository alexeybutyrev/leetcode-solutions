# Problem: Search a 2D Matrix II
# Language: python3
# Runtime: 160 ms
# Memory: 20.5 MB

from bisect import bisect_left
class Solution:
    def searchMatrix(self, A: List[List[int]], target: int) -> bool:
        
        
        N, M = len(A), len(A[0])
        
        # find col
        
        for col in range(M):
            i = 0
            j = N - 1
            while i <= j:
                mid = i + (j - i) //2
                if A[mid][col] == target:
                    return True

                if A[mid][col] > target:
                    j = mid - 1
                else:
                    i = mid + 1

        return False
        
        