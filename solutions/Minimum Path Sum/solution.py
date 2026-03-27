# Problem: Minimum Path Sum
# Language: python3
# Runtime: 96 ms
# Memory: 15.7 MB

class Solution:
    def minPathSum(self, A: List[List[int]]) -> int:
        N, M = len(A), len(A[0])
        for j in range(1,M):
            A[0][j] += A[0][j-1]
        
        for i in range(1,N):
            A[i][0] += A[i-1][0]
        
        for i in range(1,N):
            for j in range(1,M):
                A[i][j] = min(A[i][j] + A[i-1][j],A[i][j] + A[i][j-1])
        
        return A[N-1][M-1]
        
            