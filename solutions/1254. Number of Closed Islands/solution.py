# Problem: Number of Closed Islands
# Language: python3
# Runtime: 121 ms
# Memory: 14.4 MB

class Solution:
    def closedIsland(self, A: List[List[int]]) -> int:
        N, M  = len(A), len(A[0])
        
            
        ans = 0
        def dfs(i,j):
            nonlocal closed
            if i >= 0 and j >=0 and i < N and j < M and A[i][j] == 0:
                A[i][j] = 1
                if i == 0 or j == 0 or i == N - 1 or j == M - 1:
                    closed = False
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
                dfs(i-1,j)
            
        for i in range(N):
            for j in range(M):
                if A[i][j] == 0:
                    closed = True
                    dfs(i,j)
                    ans += +(closed)
        
        return ans
                    
        