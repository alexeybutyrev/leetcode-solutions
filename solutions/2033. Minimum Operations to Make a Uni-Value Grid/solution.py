# Problem: Minimum Operations to Make a Uni-Value Grid
# Language: python3
# Runtime: 189 ms
# Memory: 39.2 MB

class Solution:
    def minOperations(self, A: List[List[int]], x: int) -> int:
        A = [A[i][j] for j in range(len(A[0])) for i in range(len(A))]
        A.sort()
        N = len(A)
        c = A[N//2]
        ans=0
        for y in A:
            if abs(y - c) % x != 0: return -1
            ans += abs(y - c) // x
        return ans