# Problem: Power of Two
# Language: python3
# Runtime: 23 ms
# Memory: 16.5 MB

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and bin(n)[2:].count("1") == 1