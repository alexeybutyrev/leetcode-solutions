# Problem: Check if Point Is Reachable
# Language: python3
# Runtime: 36 ms
# Memory: 13.8 MB

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        g = gcd(targetX,targetY)
        return g & (g-1) == 0