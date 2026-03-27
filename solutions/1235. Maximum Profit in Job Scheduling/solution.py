# Problem: Maximum Profit in Job Scheduling
# Language: python3
# Runtime: 510 ms
# Memory: 26.5 MB

class Solution:
    def jobScheduling(self, S: List[int], E: List[int], profit: List[int]) -> int:
        A = sorted(list(zip(S, E, profit)))
        N = len(A)
        S = list(map(lambda x: x[0], A))
        dp = [0] * (N + 1)
        for i in range(N -1, -1, -1):
            ind = bisect_left(S, A[i][1])
            dp[i] = max(dp[i+1], A[i][2] + dp[ind])
            
        return dp[0]
        