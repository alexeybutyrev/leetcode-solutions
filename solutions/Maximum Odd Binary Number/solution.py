# Problem: Maximum Odd Binary Number
# Language: python3
# Runtime: 37 ms
# Memory: 16.7 MB

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        z,o = s.count("0"),s.count("1")
        return "1"*(o-1)+"0"*z + "1"