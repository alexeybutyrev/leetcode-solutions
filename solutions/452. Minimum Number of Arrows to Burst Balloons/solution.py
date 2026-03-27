# Problem: Minimum Number of Arrows to Burst Balloons
# Language: python3
# Runtime: 392 ms
# Memory: 19.3 MB

from math import inf
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0
        
        # sort by x_end
        points.sort(key = lambda x : x[1])
        
        arrows = 1
        first_end = points[0][1]
        for x_start, x_end in points:
            # if the current balloon starts after the end of another one,
            # one needs one more arrow
            if first_end < x_start:
                arrows += 1
                first_end = x_end
        
        return arrows
    