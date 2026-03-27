# Problem: Handshakes That Don't Cross
# Language: python3
# Runtime: 844 ms
# Memory: 15.2 MB

class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dp(n):
            if n == 0:
                return 1
            
            ans = 0
            for i in range(0,n,2):
                ans += dp(i) * dp(n-2-i)
            return ans % MOD
        return dp(numPeople)