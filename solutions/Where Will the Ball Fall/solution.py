# Problem: Where Will the Ball Fall
# Language: python3
# Runtime: 201 ms
# Memory: 14.4 MB

from collections import deque
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n,m = len(grid), len(grid[0])
        q = deque()
        for j in range(m):
            q.append((j,(0,j)))
        
        res = [-1] * m
        while q:
            l = len(q)
            for _ in range(l):
                ind, (x,y) = q.popleft()
                if x == n:
                    res[ind] = y
                    continue
                if grid[x][y] == 1 and y < m - 1 and grid[x][y+1] != -1:
                    q.append((ind, (x+1, y + 1)))
                if grid[x][y] == -1 and y > 0 and grid[x][y-1] != 1:
                    q.append((ind, (x+1, y - 1)))
        
        return res