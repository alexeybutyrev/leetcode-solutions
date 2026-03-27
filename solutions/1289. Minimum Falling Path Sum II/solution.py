# Problem: Minimum Falling Path Sum II
# Language: python3
# Runtime: 9872 ms
# Memory: 32.3 MB

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N = len(A)
        @cache
        def dp(i, j):
            if i == N:
                return 0
            c = inf
            for k in range(N):
                if k != j:
                    c = min(c, A[i][k] + dp(i+1,k))
            return c
        
        return dp(0,-1)