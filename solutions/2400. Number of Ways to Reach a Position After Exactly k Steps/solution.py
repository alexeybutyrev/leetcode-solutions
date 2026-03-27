# Problem: Number of Ways to Reach a Position After Exactly k Steps
# Language: python3
# Runtime: 5417 ms
# Memory: 647.3 MB

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dp(x, k):
            if x == endPos and k == 0:
                return 1
            if k == 0:
                return 0
            
            return (dp(x-1,k-1) + dp(x+1,k-1)) % MOD
            
        return dp(startPos,k)