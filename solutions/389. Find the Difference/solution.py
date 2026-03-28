# Problem: Find the Difference
# Language: python3
# Runtime: 60 ms
# Memory: 14 MB

from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return next(iter((Counter(t) - Counter(s))))
        