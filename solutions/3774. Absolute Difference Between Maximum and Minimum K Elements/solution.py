# Problem: Absolute Difference Between Maximum and Minimum K Elements
# Language: python3
# Runtime: 7 ms
# Memory: 18 MB

class Solution:
    def absDifference(self, A: List[int], k: int) -> int:
        A.sort()

        return abs(sum(A[-k:]) - sum(A[:k]))