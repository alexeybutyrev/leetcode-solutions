# Problem: Best Position for a Service Centre
# Language: python3
# Runtime: 140 ms
# Memory: 14.1 MB

from math import sqrt
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        n = len(positions)
        if n <= 1:
            return 0
        
        x = list(map(lambda x: x[0],positions))
        y = list(map(lambda x: x[1],positions))
        
        def norm(x1,x2):
            return sqrt((x1[0] - x2[0]) * (x1[0] - x2[0]) + (x1[1] - x2[1]) * (x1[1] - x2[1]))
        
        def dist(x):
            d = 0
            for p in positions:
                d += norm(x, p)
            return d
        
        xc = sum(x) / n
        yc = sum(y) / n
        ans = dist( [xc, yc])
        chg = 100 #change since 0 <= positions[i][0], positions[i][1] <= 100
        while chg > 1e-6: #accuracy within 1e-5
            zoom = True
            for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0):
                xx = xc + chg * dx
                yy = yc + chg * dy
                dd = dist( [xx, yy])
                if dd < ans: 
                    ans = dd 
                    xc, yc = xx, yy
                    zoom = False 
                    break 
            if zoom: chg /= 2
        return ans 
            
            
        
        
        