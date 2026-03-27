# Problem: Minimum Score by Changing Two Elements
# Language: python3
# Runtime: 353 ms
# Memory: 26.7 MB

class Solution:
    def minimizeSum(self, A: List[int]) -> int:
        A.sort()
        N = len(A)
        return min(A[N-3] - A[0], A[N-2] - A[1], A[N-1] - A[2])