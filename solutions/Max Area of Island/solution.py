# Problem: Max Area of Island
# Language: python3
# Runtime: 116 ms
# Memory: 16.8 MB

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        
        
        def dfs(i,j):
            if i >= 0 and j >= 0 and i < N and j < M and grid[i][j]:
                grid[i][j] = 0
                s1 = dfs(i+1,j)
                s2 = dfs(i-1,j)
                s3 = dfs(i,j+1)
                s4 = dfs(i,j-1)
                return 1 + s1 + s2 + s3 + s4
            else:
                return 0
            
        ans = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j]:
                    ans = max(ans, dfs(i,j))
        
        return ans
        
        