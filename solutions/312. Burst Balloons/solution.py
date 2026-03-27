# Problem: Burst Balloons
# Language: python3
# Runtime: 428 ms
# Memory: 15 MB

from collections import deque
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        N = len(nums)
                
        dp = [[0] * N for _ in range(N)]
        
        for i in range(N-2,-1,-1):
            for j in range(i+2, N):
                for k in range(i+1,j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        
        return dp[0][N-1]