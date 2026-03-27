# Problem: Bitwise AND of Numbers Range
# Language: python3
# Runtime: 46 ms
# Memory: 16.7 MB

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # turn off rightmost 1-bit
            n = n & (n - 1)
        return m & n
                