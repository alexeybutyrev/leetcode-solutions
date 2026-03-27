# Problem: Number of Ways of Cutting a Pizza
# Language: python3
# Runtime: 204 ms
# Memory: 16 MB

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m,n = len(pizza),len(pizza[0])
        mod = 10**9 + 7
        apple = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                apple[i][j] = apple[i+1][j] + apple[i][j+1] - apple[i+1][j+1] + (pizza[i][j] == 'A')
        @lru_cache(None)
        def dp(i,j,k):
            if  k==1:
                return 1 if apple[i][j]>0 else 0
            c = 0
            for row in range(i+1,m):
                if apple[i][j]-apple[row][j]>0:
                    c+=dp(row,j,k-1)%mod
            for col in range(j+1,n):
                if apple[i][j]-apple[i][col]>0:
                    c+=dp(i,col,k-1)%mod
            return c
        return dp(0,0,k)%mod