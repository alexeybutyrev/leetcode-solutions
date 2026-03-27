# Problem: Count Number of Special Subsequences
# Language: python3
# Runtime: 2984 ms
# Memory: 18.1 MB

class Solution:
    def countSpecialSubsequences(self, A: List[int]) -> int:
        N = len(A)
        
        dp = [1, 0, 0, 0]
        MOD = 10 ** 9 + 7
        for x in A:
            dp[x+1] += dp[x] + dp[x+1]
        
        return dp[-1] % MOD
        