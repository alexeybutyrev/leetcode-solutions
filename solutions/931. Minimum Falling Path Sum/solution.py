# Problem: Minimum Falling Path Sum
# Language: python3
# Runtime: 102 ms
# Memory: 18.2 MB

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        A = matrix[0]
        M = len(A)
        for r in matrix[1:]:
            B = r[:]
            
            for i in range(M):
                if i == 0:
                    B[i] += min(A[0], A[min(1,M-1)])
                elif i == M - 1:
                    B[i] += min(A[M-1], A[min(M-1,max(0,M-2))])
                else:
                    B[i] += min(A[i], A[i-1],A[i+1])
            A = B[:]
            
        return min(A)