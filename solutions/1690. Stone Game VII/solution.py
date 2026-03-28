# Problem: Stone Game VII
# Language: python3
# Runtime: 6052 ms
# Memory: 121.1 MB

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        N = len(stones)
        S = list(accumulate([0] + stones))

        dp = [[-1] * N for _ in range(N)]
        def dfs(i, j):
            if i == j:
                return 0
            if dp[i][j] < 0:
                dS = S[j+1] - S[i]
                dp[i][j] = max(-dfs(i+1, j) + dS - stones[i], -dfs(i, j-1) + dS - stones[j])
            return dp[i][j]
            

        
        return dfs(0,N-1)