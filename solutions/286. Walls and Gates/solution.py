# Problem: Walls and Gates
# Language: python3
# Runtime: 580 ms
# Memory: 16.8 MB

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if [] == rooms: return rooms
        n, m = len(rooms), len(rooms[0])
        inf, wall = 2147483647, -1
        directions = [(-1,0),(1,0), (0,-1), (0,1)]
        
        # find 0s
        q = []
        for i in range(n):
            for j in range(m):
                if 0 == rooms[i][j]:
                    q.append((i,j))
        
        while q:
            v = q.pop(0)
            for d in directions:
                r = [0,0]
                r[0] = v[0] + d[0]
                r[1] = v[1] + d[1]
                
                if (r[0] > n-1 or r[1] > m -1 or r[0] < 0 or r[1] < 0 or rooms[r[0]][r[1]] != inf):
                    continue
                
                rooms[r[0]][r[1]] = rooms[v[0]][v[1]] + 1
                q.append([r[0],r[1]])

                
        
        return rooms
                            