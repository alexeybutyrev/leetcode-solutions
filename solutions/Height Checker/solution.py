# Problem: Height Checker
# Language: python3
# Runtime: 36 ms
# Memory: 14.2 MB

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum( a!= b for a,b in zip(heights, sorted(heights)))
            