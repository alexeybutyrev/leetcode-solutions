# Problem: Steps to Make Array Non-decreasing
# Language: python3
# Runtime: 1428 ms
# Memory: 28.5 MB

class Solution:
    def totalSteps(self, A: List[int]) -> int:
        
        stack = []
        N = len(A)
        dp = [0] * N
        ans = 0
        for i in range(N-1,-1,-1):
            while stack and A[i] > A[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
                ans = max(ans,dp[i])
            stack.append(i)
        
        return ans