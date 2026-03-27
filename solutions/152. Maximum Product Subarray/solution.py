# Problem: Maximum Product Subarray
# Language: python3
# Runtime: 52 ms
# Memory: 15.1 MB

class Solution:
    def maxProduct(self, A: List[int]) -> int:
        B = A[::-1]
        
        for i in range(1,len(A)):
            A[i] *= 1 if A[i-1] == 0 else A[i-1]
            B[i] *= 1 if B[i-1] == 0 else B[i-1]
        
        return max(A+B)