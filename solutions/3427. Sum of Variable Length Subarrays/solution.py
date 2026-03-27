# Problem: Sum of Variable Length Subarrays
# Language: python3
# Runtime: 3 ms
# Memory: 18 MB

class Solution:
    def subarraySum(self, A: List[int]) -> int:
        N = len(A)
        ans = 0
        for i in range(N):
            start = max(0, i - A[i])
            ans += sum(A[start:i+1])
        return ans
                