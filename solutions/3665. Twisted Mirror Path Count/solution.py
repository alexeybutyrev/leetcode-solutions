# Problem: Twisted Mirror Path Count
# Language: python3
# Runtime: 2659 ms
# Memory: 311.5 MB

class Solution:
    def uniquePaths(self, A: List[List[int]]) -> int:
        N,M = len(A), len(A[0])
        MOD = 10**9+7
        @cache
        def dp(i,j,r):
            if i == N - 1 and j == M - 1: return 1
            if i == N or j == M: return 0

            ans = 0
            if A[i][j] == 0:
                return (dp(i+1,j,True) + dp(i,j+1,False))%MOD
            if r:
                return dp(i,j+1,False)
            return dp(i+1,j,True)
        return (dp(0,1,False) + dp(1,0,True)) % MOD