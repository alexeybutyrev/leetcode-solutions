# Problem: Largest Perimeter Triangle
# Language: python3
# Runtime: 15 ms
# Memory: 18.6 MB

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        N = len(A)
        for i in range(N-3,-1,-1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0