# Problem: Generate Random Point in a Circle
# Language: python3
# Runtime: 136 ms
# Memory: 24.4 MB

from math import sin, cos, pi, sqrt
from random import uniform
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.xc = x_center
        self.yc = y_center
        self.R = radius

    def randPoint(self) -> List[float]:
        R =   self.R * sqrt(uniform(0, 1.0))
        phi = uniform(0,2*pi)
        return [self.xc +  R * cos(phi), self.yc + R * sin(phi)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()