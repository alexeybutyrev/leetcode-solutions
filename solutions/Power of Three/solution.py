# Problem: Power of Three
# Language: python3
# Runtime: 72 ms
# Memory: 14.3 MB

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 %n == 0