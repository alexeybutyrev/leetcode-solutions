# Problem: Egg Drop With 2 Eggs and N Floors
# Language: python3
# Runtime: 4435 ms
# Memory: 15.7 MB

class Solution:
    def twoEggDrop(self, n: int) -> int:
        @cache
        def dp(m):
            if m <= 1:
                return m
            
            ans = inf
            for i in range(1,m+1):
                ans = min(ans, 1 + max(i-1, dp(m-i)))
            
            return ans
        return dp(n)