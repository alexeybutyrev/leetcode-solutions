# Problem: The Maze
# Language: python3
# Runtime: 291 ms
# Memory: 14.7 MB

from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        n, m = len(maze), len(maze[0])

        def directions(i,j):
            return (1,0), (-1,0), (0,1), (0,-1)
        q = deque()
        q.append(start)
        visited = set()
        visited.add((start[0],start[1]))
        while q:
            l = len(q)
            for _ in range(l):
                i0,j0 = q.popleft()
                if [i0,j0] == destination:
                    return True
                for sx,sy in directions(i0,j0):
                    i = i0 + sx
                    j = j0 + sy
                    while i >= 0 and i < n and j >= 0 and j < m and maze[i][j] == 0:
                        i+=sx
                        j+=sy
                    
                    if (i-sx,j-sy) not in visited:
                        q.append([i-sx,j-sy])
                        visited.add((i-sx,j-sy))
                        
                        
        return False