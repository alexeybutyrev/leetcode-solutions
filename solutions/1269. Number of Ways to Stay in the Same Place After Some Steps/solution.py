# Problem: Number of Ways to Stay in the Same Place After Some Steps
# Language: python3
# Runtime: 339 ms
# Memory: 106.9 MB

class Solution:
    def numWays(self, NS: int, L: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dp(x,s):
            if s == 0: return x == 0
            if x < 0 or x >= L: return 0
            return (dp(x-1,s-1) + dp(x+1,s-1) + dp(x,s-1)) % MOD
        
        return dp(0,NS)