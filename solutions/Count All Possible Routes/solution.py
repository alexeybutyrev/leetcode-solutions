# Problem: Count All Possible Routes
# Language: python3
# Runtime: 2329 ms
# Memory: 41.1 MB

class Solution:
    def countRoutes(self, A: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        N = len(A)
        @cache
        def dp(i,f):
            if f < 0:
                return 0
            ans = 0
            if i == finish:
                ans += 1
            for j in range(N):
                if i !=j:
                    ans += dp(j, f - abs(A[i]-A[j]))
                    ans %=MOD
            return ans
        return dp(start, fuel)