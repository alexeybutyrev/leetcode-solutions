# Problem: Find the Sum of the Power of All Subsequences
# Language: python3
# Runtime: 391 ms
# Memory: 123.6 MB

class Solution:
    def sumOfPower(self, A: List[int], k: int) -> int:
        
        MOD = 10**9 + 7
        N = len(A)
        
        @cache
        def dp(i,n,s):
            
            if s == 0: return 2 ** n
            if i >= N: return 0
            
            
            ans = dp(i+1, n, s)
            if A[i] <= s:
                ans += dp(i+1, n - 1, s - A[i])
                ans %= MOD
            
            
            return ans % MOD
        
        
        return dp(0, N, k)