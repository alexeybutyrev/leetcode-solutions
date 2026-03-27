# Problem: Remove One Element to Make the Array Strictly Increasing
# Language: python3
# Runtime: 336 ms
# Memory: 14.4 MB

class Solution:
    def canBeIncreasing(self, A: List[int]) -> bool:
        N = len(A)
        for i in range(N):
            B = A[:i] + A[i+1:]
            if B == sorted(B) and max(Counter(B).values()) == 1:
                return True

        return False
    