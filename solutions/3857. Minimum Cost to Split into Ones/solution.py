# Problem: Minimum Cost to Split into Ones
# Language: python3
# Runtime: 3053 ms
# Memory: 29.7 MB

class Solution:
    def minCost(self, n: int) -> int:
        @cache
        def dp(x):
            if x == 1: 
                return 0
            ans = inf
            for a in range(1, x):
                b = x - a
                ans = min(ans, a * b + dp(a) + dp(b))
            return ans
        return dp(n)