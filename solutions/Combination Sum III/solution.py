# Problem: Combination Sum III
# Language: python3
# Runtime: 32 ms
# Memory: 13.8 MB

from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        for c in combinations(range(1,10),k):
            if sum(c) == n:
                res.append(c)
        return res