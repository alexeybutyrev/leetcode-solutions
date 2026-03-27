# Problem: Count Total Number of Colored Cells
# Language: python3
# Runtime: 1 ms
# Memory: 17.9 MB

class Solution:
    def coloredCells(self, n: int) -> int:
        n-=1
        return 1 + 2 *n*(n+1)