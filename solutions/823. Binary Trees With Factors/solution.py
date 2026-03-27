# Problem: Binary Trees With Factors
# Language: python3
# Runtime: 410 ms
# Memory: 17.2 MB

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        A = set(arr)
        MOD = 10**9 + 7
        @cache
        def dp(a):
            ans = 1
            for x in A:
                if a % x == 0 and a//x in A:
                    ans += dp(x) * dp(a//x)
                    ans %= MOD
            return ans
        
        ans = 0
        for a in A:
            ans += dp(a)
            ans %= MOD
        return ans