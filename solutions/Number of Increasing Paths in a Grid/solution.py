# Problem: Number of Increasing Paths in a Grid
# Language: python3
# Runtime: 2154 ms
# Memory: 142.5 MB

class Solution:
    def countPaths(self, A: List[List[int]]) -> int:
        N, M = len(A),len(A[0])
        MOD = 10 ** 9 + 7
        
        DP = [[-1] * M for _ in range(N)]
        def dp(i,j):
            if DP[i][j] != -1: return DP[i][j]
            
            ans = 0
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x = i + dx
                y = j + dy
                if x >= 0 and x < N and y >= 0 and y < M and A[i][j] < A[x][y]:

                    ans +=  1 + dp(x,y)
                    ans %= MOD
            DP[i][j] = ans % MOD
            return DP[i][j]
        
        ans = N * M
        for i in range(N):
            for j in range(M):
                if DP[i][j] == -1:
                    dp(i,j)
                ans += DP[i][j]
                ans %= MOD

        return ans