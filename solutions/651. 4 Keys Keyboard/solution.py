# Problem: 4 Keys Keyboard
# Language: python3
# Runtime: 0 ms
# Memory: 19.5 MB

class Solution:
    def maxA(self, n: int) -> int:
        # best[k] = max(best[k-1] + 1, best[k-2] * 1, best[])
        
        dp = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            dp[i] = max(dp[i], i)
            s = 2 * dp[i]
            for j in range(i+3,n+1):
                dp[j] = max(dp[j],s)
                s += dp[i]
        
        return dp[-1]