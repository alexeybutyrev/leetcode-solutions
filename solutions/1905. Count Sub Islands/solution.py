# Problem: Count Sub Islands
# Language: python3
# Runtime: 3100 ms
# Memory: 96.7 MB

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        N, M = len(grid1), len(grid1[0])
        def dfs(i,j):
            if i >= 0 and i < N and j >=0 and j < M and grid2[i][j]:
                grid2[i][j] = 0
                seen.add((i,j))
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
        
        count = 0
        for i in range(N):
            for j in range(M):
                if grid2[i][j]:
                    seen = set()
                    dfs(i,j)
                    for (l,m) in seen:
                        if not grid1[l][m]:
                            break
                    else:
                        count +=1
        return count   