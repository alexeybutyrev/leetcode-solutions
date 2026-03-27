# Problem: Perfect Squares
# Language: python3
# Runtime: 178 ms
# Memory: 16.7 MB



A = [i*i for i in range(100+1)]
dp = [inf] * (10001)
dp[0] = 0

# 1,2,3..
for i in range(1,10001):
    for a in A:
        if i - a >= 0:
            dp[i] = min(dp[i - a] + 1, dp[i])
        else:
            break
            
class Solution:
    def numSquares(self, n: int) -> int:
        return dp[n]
        