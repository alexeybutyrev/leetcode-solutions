# Problem: Product of Array Except Self
# Language: python3
# Runtime: 367 ms
# Memory: 22.4 MB

class Solution:
    def productExceptSelf(self, A: List[int]) -> List[int]:
        N = len(A)
        L = [1] * N
        
        R = [1] * N
        
        for i in range(1,N):
            L[i] = L[i-1] * A[i-1]
        
        for j in range(N-2,-1,-1):
            R[j] = R[j+1] * A[j+1]
        
        return [L[i] * R[i] for i in range(N)]
            
        