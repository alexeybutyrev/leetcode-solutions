# Problem: Alternating Digit Sum
# Language: python3
# Runtime: 35 ms
# Memory: 13.8 MB

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        x = 1
        s = 0
        for d in str(n):
            s += x * int(d)
            x *= (-1)
        return s
    