# Problem: Power of Four
# Language: python3
# Runtime: 30 ms
# Memory: 16.1 MB

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and any(0 == n ^ (1<<i) for i in range(0,32,2))