# Problem: Find Missing and Repeated Values
# Language: python3
# Runtime: 145 ms
# Memory: 16.9 MB

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        c = Counter()
        for x in grid:
            for y in x:
                c[y] += 1
        ans = [0,0]
        for x in range(1, len(grid[0]) * len(grid[0]) + 1):
            if x not in c:
                ans[1] = x
            if c[x] > 1:
                ans[0] = x
        return ans
            