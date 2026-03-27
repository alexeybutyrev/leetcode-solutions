# Problem: Painting the Walls
# Language: python3
# Runtime: 1009 ms
# Memory: 16.3 MB

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        N = len(cost)
        dp = [0] + [inf] * N
        
        for i in range(N):
            t = time[i]
            c = cost[i]
            for j in range(N,0,-1):
                dp[j] = min(dp[j], dp[max(j-t-1,0)] + c)
        
        return dp[-1]