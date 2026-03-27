# Problem: Minimum Number of Coins for Fruits
# Language: python3
# Runtime: 1051 ms
# Memory: 18.8 MB

class Solution:
    def minimumCoins(self, A: List[int]) -> int:
        
        N = len(A)
        @cache
        def dp(i):
            if i >= N: return 0
            
            ans = inf
            for x in range(1,i+3):
                ans =  min(ans, A[i] + dp(i+x))
            return ans
        
        return dp(0)