# Problem: Number of Strings Which Can Be Rearranged to Contain Substring
# Language: python3
# Runtime: 2146 ms
# Memory: 412.7 MB

class Solution:
    def stringCount(self, n: int) -> int:
        N = 4
        T = (1 << N) - 1
        MOD = 10**9 + 7
        # 1111
        # 
        @cache
        def dp(i,mask):
            if i == n: return int(mask == T)
            
            ans = dp(i+1, mask | 1) + dp(i+1, mask | 8)
            ans %= MOD
            
            if mask & 2:
                ans += dp(i+1, mask | 4)
                ans %= MOD
            else:
                ans += dp(i+1, mask | 2)
                ans %= MOD
            
            ans += 23 * dp(i+1, mask)
            
            return ans % MOD
            
            
            
        
        return dp(0,0)