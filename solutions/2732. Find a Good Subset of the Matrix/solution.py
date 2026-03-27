# Problem: Find a Good Subset of the Matrix
# Language: python3
# Runtime: 2036 ms
# Memory: 21.2 MB

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        if len(grid) == 1:
            return [0] if sum(grid[0]) == 0 else []
        A = []
        for x in grid:
            A.append(int("".join(str(s) for s in x),2))
        d = {}
        for x,a in enumerate(A):
            for i in range(32):
                if (i & a) == 0 and i in d:
                    return [d[i], x]
            d.setdefault(a,x)
        return []