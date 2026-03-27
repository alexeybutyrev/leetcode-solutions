# Problem: Rotting Oranges
# Language: python3
# Runtime: 44 ms
# Memory: 14 MB

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        n,m = len(grid), len(grid[0])
        
        
        def dimentions(i,j):
            return [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]
        
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:            
                    q.append((i,j))
                
        count = 0
        while q:
            l = len(q)
            for _ in range(l):
                ci,cj = q.popleft()
                for i,j in dimentions(ci,cj):
                    if i<0 or j<0 or i>n-1 or j>m-1 or grid[i][j] != 1:
                        continue
                    
                    grid[i][j] = 2
                    q.append((i,j))
                    
            count +=1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
                    
        return count -1 if count else 0
                
                    