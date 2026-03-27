# Problem: Maximize Win From Two Segments
# Language: python3
# Runtime: 705 ms
# Memory: 25.1 MB

class Solution:
    def maximizeWin(self, A: List[int], k: int) -> int:
        N = len(A)
        dp = [0] *(N+1)
        j = ans = 0
        for i in range(N):
            while A[j]< A[i] -k:
                j+=1
            
            dp[i+1] = max(dp[i], i-j+1)
            ans = max(ans,dp[j]+i-j+1)
        return ans