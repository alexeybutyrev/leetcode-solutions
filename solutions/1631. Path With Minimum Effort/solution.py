# Problem: Path With Minimum Effort
# Language: python3
# Runtime: 696 ms
# Memory: 15.1 MB

from collections import deque
from math import inf
from copy import deepcopy
from heapq import *
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n,m = len(heights), len(heights[0])
        
        if n == 1 and m == 1:
            return 0
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        dist = [[inf] * m for _ in range(n)]
        
        
        h = [(0,0,0)]
        while h:            
            
            d, x, y = heappop(h) 
            if x == n - 1 and y == m - 1:
                return d
            
            for sx,sy in directions:
                xc = x + sx
                yc = y + sy
                if xc >= 0 and xc < n and yc >= 0 and yc < m:
                    cost2 = max(d, abs(heights[xc][yc] - heights[x][y]))
                    if dist[xc][yc] > cost2:
                        dist[xc][yc] = cost2
                        heappush(h,(cost2,xc,yc))
                    
        return min_cost
            