# Problem: Bomb Enemy
# Language: python3
# Runtime: 2268 ms
# Memory: 180.4 MB

class Solution:
    def maxKilledEnemies(self, A: List[List[str]]) -> int:
        N,M = len(A), len(A[0])
        @cache
        def dp(i,j,d):
            if i < 0 or i == N or j < 0 or j == M or A[i][j] == "W":
                return 0
            
            c = +(A[i][j] == 'E')
            
            if d == 'l':
                return c + dp(i-1,j,d)
            elif d == 'r':
                return c + dp(i+1,j,d)
            elif d == 'd':
                return c + dp(i,j-1,d)
            else:
                return c + dp(i,j+1,d)
        
        ans = 0
        for i in range(N):
            for j in range(M):
                if A[i][j] == '0':
                    ans = max(ans, dp(i,j,'l') + dp(i,j,'r') + dp(i,j,'d') + dp(i,j,'u'))
        return ans
    