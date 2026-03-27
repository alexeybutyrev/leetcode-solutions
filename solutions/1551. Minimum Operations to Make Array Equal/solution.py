# Problem: Minimum Operations to Make Array Equal
# Language: python3
# Runtime: 28 ms
# Memory: 14.1 MB

class Solution:
    def minOperations(self, n: int) -> int:
        return n//2 * (n//2 + 1) - n//2 * (n % 2 == 0)
        