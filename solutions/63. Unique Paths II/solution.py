# Problem: Unique Paths II
# Language: python3
# Runtime: 32 ms
# Memory: 14.3 MB

class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        N, M = len(A), len(A[0])
        if A[0][0]:
            return 0
        dp = [[0] * M for _ in range(N)]
        
        dp[0][0] = 1
        for i in range(N):
            for j in range(M):
                if not A[i][j]:
                    if j > 0:
                        
                        dp[i][j] += dp[i][j-1]
                        
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
        
        return dp[N-1][M-1]