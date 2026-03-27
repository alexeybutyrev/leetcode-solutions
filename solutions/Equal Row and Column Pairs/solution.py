# Problem: Equal Row and Column Pairs
# Language: python3
# Runtime: 482 ms
# Memory: 21.3 MB

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c = Counter()
        for r in grid:
            c[tuple(r)] += 1
        
        ans = 0
        for col in zip(*grid):
            ans += c[tuple(col)]
        return ans