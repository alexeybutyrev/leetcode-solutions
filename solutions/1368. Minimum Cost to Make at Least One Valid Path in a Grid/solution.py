# Problem: Minimum Cost to Make at Least One Valid Path in a Grid
# Language: python3
# Runtime: 199 ms
# Memory: 19.9 MB

class Solution:
    def minCost(self, A: List[List[int]]) -> int:
        N, M = len(A), len(A[0])
        mapping = {1: (0,1), 2: (0,-1), 3: (1,0), 4: (-1,0)}
        
        dp = defaultdict(lambda : inf)
        
        heappush( h := [], (0,0,0))
        while h:
            c,i,j = heappop(h)
            
            if i == N -1 and j == M - 1: return c
            
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                dc = int(mapping[A[i][j]] != (dx,dy))
                x = i + dx
                y = j + dy
                if N > x >= 0 and M > y >= 0 and dp[(x,y)] > c + dc:
                    dp[(x,y)] = c + dc
                    heappush(h,(dp[(x,y)],x,y))
        
        