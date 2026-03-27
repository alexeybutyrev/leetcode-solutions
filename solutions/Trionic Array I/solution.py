# Problem: Trionic Array I
# Language: python3
# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def isTrionic(self, A: List[int]) -> bool:
        if A[0] >= A[1]: return False
        N = len(A)
        c = 1
        for i in range(2,N):
            if A[i-1] == A[i]: return False
            if (A[i-2] - A[i-1]) * (A[i-1]- A[i]) < 0:
                c += 1
        return c == 3
