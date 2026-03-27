# Problem: Number of Distinct Islands
# Language: python3
# Runtime: 216 ms
# Memory: 18.1 MB

from collections import deque
class Solution:
    def numDistinctIslands(self, M: List[List[int]]) -> int:
        n, m = len(M), len(M[0])
        
        seen = set()
        path = ""
        def dfs(i,j, d):
            nonlocal path
            if i < n and j < m and i >= 0 and j >= 0 and (i,j) not in seen and M[i][j]:
                seen.add((i,j))
                path += d
                dfs(i+1, j, "D")
                dfs(i-1, j, "U")
                dfs(i, j+1, "L")
                dfs(i, j-1, "R")
                path += "0"
            return ""
        
        count = 0
        islands = set()
        for i in range(n):
            for j in range(m):
                if (i,j) not in seen and M[i][j]:
                    count += 1
                    
                    path = ""
                    dfs(i,j,"0")
                    islands.add(path)
                    
        return len(islands)
                        
                    