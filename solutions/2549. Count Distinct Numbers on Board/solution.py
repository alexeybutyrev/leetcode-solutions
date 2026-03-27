# Problem: Count Distinct Numbers on Board
# Language: python3
# Runtime: 38 ms
# Memory: 13.8 MB

class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n == 1:
            return 1
        return n-1