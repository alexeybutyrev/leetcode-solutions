# Problem: Count Number of Ways to Place Houses
# Language: python3
# Runtime: 235 ms
# Memory: 14.2 MB

class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7

        dp = [1] + [0] * (n+1)
        dp[1] = 1
        for i in range(2,n+2):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        
        x = dp[-1]
        return (x * x) % MOD