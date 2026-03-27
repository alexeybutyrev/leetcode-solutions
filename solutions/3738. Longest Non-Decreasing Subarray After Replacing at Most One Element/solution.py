# Problem: Longest Non-Decreasing Subarray After Replacing at Most One Element
# Language: python3
# Runtime: 383 ms
# Memory: 33.1 MB

class Solution:
    def longestSubarray(self, A: List[int]) -> int:
        
        N = len(A)
        
        L, R = [1] * N, [1] * N

        for i in range(1,N):
            if A[i-1] <= A[i]:
                L[i] = L[i-1] + 1
        for i in range(N-2,-1,-1):
            if A[i] <= A[i+1]:
                R[i] = R[i+1] + 1
        
        ans = min(N, max(L) + 1)
        for i in range(1,N-1):
            if A[i-1] <= A[i+1]:
                ans = max(ans, L[i-1] + 1 + R[i+1])
        return ans