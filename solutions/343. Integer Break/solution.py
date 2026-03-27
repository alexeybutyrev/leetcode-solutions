# Problem: Integer Break
# Language: python3
# Runtime: 65 ms
# Memory: 14.1 MB

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [1] * (n + 2)
        dp[1] = 1
        for i in range(1,n+2):
            for j in range(i-1,0,-1):
                dp[i] = max( dp[j] * (i-j), dp[i])
            
        return dp[-1]