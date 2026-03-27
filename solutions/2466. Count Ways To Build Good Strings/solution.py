# Problem: Count Ways To Build Good Strings
# Language: python3
# Runtime: 1028 ms
# Memory: 17.9 MB

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1]
        MOD = 10**9 + 7
        ans = 0
        for i in range(1, high + 1):
            dp.append(0)
            if i - zero >= 0:
                dp[i] += dp[i-zero]
            
            if i - one >= 0:
                dp[i] += dp[i-one]
            dp[i] %= MOD
            if  high >= i >= low:
                ans += dp[i]
                ans %= MOD
        return ans