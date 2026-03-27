# Problem: New 21 Game
# Language: python3
# Runtime: 76 ms
# Memory: 14.7 MB

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if N > K - 1 + W or K == 0:
            return 1
        if N < K:
            return 0
        dp = [1.0] + [0.0] * N
        ws = 1
        for i in range(1, N+1):
            dp[i] = ws / W
            if i < K:
                ws += dp[i]
            if i - W >= 0:
                ws -= dp[i-W]
            
        
        return sum(dp[K:])
    
            
        