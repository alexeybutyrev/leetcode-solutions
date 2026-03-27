# Problem: Maximum Score Using Exactly K Pairs
# Language: python3
# Runtime: 12068 ms
# Memory: 267.8 MB

class Solution:
    def maxScore(self, A: List[int], B: List[int], k: int) -> int:
        N = len(A)
        M = len(B)
        DP = [[[None] * (k + 1) for _ in range(M)] for x in range(N)]
        
        def dp(i,j,k):
            if k == 0: return 0
            if i == N or j == M: return -inf
            if DP[i][j][k] is None:
                ans = A[i] * B[j] + dp(i+1,j+1, k-1)
                DP[i][j][k] = max(ans, dp(i,j+1,k), dp(i+1,j,k))
            return DP[i][j][k]
        return dp(0,0,k)