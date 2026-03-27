# Problem: Find Maximum Value in a Constrained Sequence
# Language: python3
# Runtime: 191 ms
# Memory: 57.1 MB

class Solution:
    def findMaxVal(self, n: int, R: List[List[int]], D: List[int]) -> int:
        N = n
        A = [inf] * N
        A[0] = 0

        for i,x in R:
            A[i] = x

        for i in range(N-1):
            if A[i+1] > A[i] + D[i]:
                A[i+1] = A[i] + D[i]

        for i in range(N-2,-1,-1):
            if A[i] > A[i+1] + D[i]:
                A[i] = A[i+1] + D[i]

        return max(A)