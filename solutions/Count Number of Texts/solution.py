# Problem: Count Number of Texts
# Language: python3
# Runtime: 1692 ms
# Memory: 21.1 MB

from itertools import groupby
class Solution:
    def countTexts(self, S: str) -> int:
        MOD = 10**9 + 7
        N = len(S)
        dp = [0] * (N+1)
        dp[0] = 1
        for i in range(1,len(S)+1):
            #l = S[i]
            dp[i] = dp[i-1]
            if i >= 2 and S[i-1] == S[i-2]:
                dp[i] += dp[i-2]
            
            if i >= 3 and S[i-1] == S[i-2] == S[i-3]:
                dp[i] += dp[i-3]
            
            if i >= 4 and S[i-1] in {'7','9'} and  S[i-1] == S[i-2] == S[i-3] == S[i-4]:
                dp[i] += dp[i-4]
            
            dp[i] %= MOD
        print(dp)
        return dp[-1]