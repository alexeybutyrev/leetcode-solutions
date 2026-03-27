# Problem: Find Nearest Point That Has the Same X or Y Coordinate
# Language: python3
# Runtime: 784 ms
# Memory: 19.2 MB

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def dist(a,b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        P = [x,y]
        
        d = inf
        ind = -1
        for i,p in enumerate(points):
            if p[0] == P[0] or p[1] == P[1]:
                if d > dist(p, P):
                    ind = i
                    d = dist(p, P)
        
        return ind