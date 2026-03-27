# Problem: Determine if a Cell Is Reachable at a Given Time
# Language: python3
# Runtime: 39 ms
# Memory: 16.2 MB

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False
        dx = abs(sx-fx)
        dy = abs(sy-fy)
        m = max(dx,dy)
        if t < m: return False
        return True