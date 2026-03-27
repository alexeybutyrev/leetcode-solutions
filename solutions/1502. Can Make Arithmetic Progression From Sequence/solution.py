# Problem: Can Make Arithmetic Progression From Sequence
# Language: python3
# Runtime: 1 ms
# Memory: 19.3 MB

class Solution:
    def canMakeArithmeticProgression(self, A: List[int]) -> bool:
        A.sort()
        dx = A[0] - A[1]

        return all(A[i-1] - A[i] == dx for i in range(1,len(A)))