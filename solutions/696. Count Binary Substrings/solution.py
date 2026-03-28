# Problem: Count Binary Substrings
# Language: python3
# Runtime: 148 ms
# Memory: 14.5 MB

from itertools import groupby
class Solution:
    def countBinarySubstrings(self, S: str) -> int:
        c = 0
        n1 = 0
        n0 = 0
        for k, v in groupby(S):
            n1 = len(list(v))
            c+= min(n1, n0)
            n0 = n1
        return c
        