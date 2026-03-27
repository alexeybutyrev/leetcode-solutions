# Problem: Dungeon Game
# Language: python3
# Runtime: 64 ms
# Memory: 15.2 MB

class Solution:
    def calculateMinimumHP(self, A: List[List[int]]) -> int:
        N,M = len(A), len(A[0])
        dp = [inf] * M
        dp[M-1] = 1 - min(A[N-1][M-1],0)
        
        for j in range(M-2,-1,-1):
            dp[j] = max(1,dp[j+1] - A[N-1][j])
        
        for i in range(N -2,-1,-1):
            new_dp = dp[:]
            new_dp[M-1] = max(1,dp[M-1] - A[i][M-1])
            for j in range(M-2,-1,-1):
                new_dp[j] = min(max(1,dp[j] - A[i][j]),max(1,new_dp[j+1] - A[i][j]))
            dp = new_dp[:]
            
        
        return dp[0]
        