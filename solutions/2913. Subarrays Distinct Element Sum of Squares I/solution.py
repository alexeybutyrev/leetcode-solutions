# Problem: Subarrays Distinct Element Sum of Squares I
# Language: python3
# Runtime: 192 ms
# Memory: 16.2 MB

class Solution:
    def sumCounts(self, A: List[int]) -> int:
        N = len(A)
        ans = 0
        for i in range(N):
            for j in range(i+1,N+1):
                ans += len(set(A[i:j]))**2
        return ans