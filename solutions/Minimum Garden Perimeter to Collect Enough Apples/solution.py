# Problem: Minimum Garden Perimeter to Collect Enough Apples
# Language: python3
# Runtime: 2092 ms
# Memory: 14.1 MB

class Solution:
    def minimumPerimeter(self, x: int) -> int:

        
        apples = i = 0
        while apples < x:
            i += 1
            corner, other = 2 * i, 3 * i * (i - 1)
            apples += 4 * (corner + i + other)
        return 8 * i