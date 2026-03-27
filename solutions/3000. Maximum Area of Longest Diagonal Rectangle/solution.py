# Problem: Maximum Area of Longest Diagonal Rectangle
# Language: python3
# Runtime: 70 ms
# Memory: 17.4 MB

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        l = 0
        ans = 0
        for x in dimensions:
            l0 = sqrt(x[0] * x[0] + x[1] * x[1])
            if l0 == l:
                l = l0
                ans = max(ans, x[0] * x[1])
            elif l0 > l:
                l = l0
                ans = x[0] * x[1]
        return ans