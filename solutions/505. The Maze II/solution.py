# Problem: The Maze II
# Language: python3
# Runtime: 436 ms
# Memory: 15 MB

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        N,M = len(maze), len(maze[0])
        q = []
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        heappush(q, (0, start[0], start[1]))
        
        visited = {(start[0], start[1]): 0}
        while q:
            d, i, j = heappop(q)
            for dx, dy in directions:
                x = i
                y = j
                step = 0
                while x >= 0 and x < N and y >= 0 and y < M and maze[x][y] == 0:
                    x += dx
                    y += dy
                    step += 1
                x-=dx
                y-=dy
                step -= 1
                if (x,y) not in visited or d + step < visited[(x,y)]:
                    visited[(x,y)] = d + step
                    heappush(q, (d+step, x, y) )
                step += 1
                      
        dest = (destination[0],destination[1])            
        return -1 if dest not in visited else visited[dest]