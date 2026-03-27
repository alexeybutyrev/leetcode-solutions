# Problem: Maximum Product of Three Numbers
# Language: python3
# Runtime: 260 ms
# Memory: 15.5 MB

class Solution:
    def maximumProduct(self, A: List[int]) -> int:
        A.sort()
        return max(A[0] * A[1] * A[2], A[-3] * A[-2] * A[-1], A[1] * A[0] * A[-1])