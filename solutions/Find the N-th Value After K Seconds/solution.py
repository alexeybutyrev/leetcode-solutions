# Problem: Find the N-th Value After K Seconds
# Language: python3
# Runtime: 5751 ms
# Memory: 16.3 MB

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        A = [1] * n
        MOD = 10**9 + 7
        for _ in range(k):
            for j in range(1,n):
                A[j] += A[j-1]
                A[j] %= MOD
        return A[-1]