# Problem: Number of 1 Bits
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans