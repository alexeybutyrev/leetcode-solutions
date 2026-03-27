# Problem: Unique Paths
# Language: python3
# Runtime: 16 ms
# Memory: 14.1 MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        #print(dp)
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        #print(dp)
        return dp[m-1][n-1]