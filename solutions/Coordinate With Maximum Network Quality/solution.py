# Problem: Coordinate With Maximum Network Quality
# Language: python3
# Runtime: 5524 ms
# Memory: 14.1 MB

from math import floor
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        
        x = list(map(lambda x: x[0], towers))
        y = list(map(lambda x: x[1], towers))
        minx, maxx = min(x) - radius, max(x) + radius
        miny, maxy = min(y) - radius, max(y) + radius
        
        max_signal = 0
        rx, ry = 0, 0
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy +1):
                s = 0
                for xc,yc,q in towers:
                    if (xc - x) * (xc - x) + (yc - y) * (yc - y) <= radius * radius:
                        s += floor(q / (1 + sqrt( (x-xc)*(x-xc) +  (y-yc)*(y-yc))))
                if max_signal < s:
                    rx, ry = x, y
                    max_signal = s
        return rx, ry