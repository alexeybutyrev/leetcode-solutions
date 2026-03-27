# Problem: Number of Enclaves
# Language: python3
# Runtime: 599 ms
# Memory: 75.9 MB

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        N = len(A)
        M = len(A[0])
        
        def dfs(i,j):
            if 0 <= i < N and 0 <= j < M and A[i][j]:
                A[i][j] = 0
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
        
        for i in range(N):
            for j in [0,M-1]:
                dfs(i,j)
        
        for j in range(M-1):
            for i in [0,N-1]:
                dfs(i,j)
        
        return sum(A[i][j] for i in range(N) for j in range(M))