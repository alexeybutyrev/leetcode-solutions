# Problem: Paths in Matrix Whose Sum Is Divisible by K
# Language: python3
# Runtime: 1095 ms
# Memory: 148.3 MB

class Solution:
    def numberOfPaths(self, A: List[List[int]], k: int) -> int:
        N, M = len(A),len(A[0])
        
        if N == M == 1:
            return 1 if A[0][0] % k == 0 else 0
        
        MOD = 10 ** 9 + 7
        
        dp = [[[0] * k for _ in range(M)] for i in range(N)]
        
        s = 0
        for i in range(N):
            s += A[i][0]
            dp[i][0][s%k] += 1
        
        s = 0
        for j in range(M):
            s += A[0][j]
            dp[0][j][s%k] += 1
        
        for i in range(1,N):
            for j in range(1,M):
                for x in range(k):
                    y = (A[i][j] + x) % k
                    dp[i][j][y] += dp[i-1][j][x] + dp[i][j-1][x]

                    
        return dp[-1][-1][0] % MOD