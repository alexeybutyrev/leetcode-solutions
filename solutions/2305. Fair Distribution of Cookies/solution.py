# Problem: Fair Distribution of Cookies
# Language: python3
# Runtime: 267 ms
# Memory: 22 MB

class Solution:
    def distributeCookies(self, A: List[int], k: int) -> int:
        
        
        N = len(A)
        
        mask = 0
        T = (1 << N)  - 1
        
        @cache
        def dp(mask, k, s):
            if k == 1:
                ans = s
                for i in range(N):
                    if mask & (1<<i) == 0:
                        ans += A[i]
                return ans
            
            ans = max(s, dp(mask, k-1,0))
            for i in range(N):
                if mask & (1 << i) == 0:
                    ans = min(ans, dp(mask | (1<<i), k, s + A[i]))
                    
            return ans
            
        
        return dp(0,k,0)