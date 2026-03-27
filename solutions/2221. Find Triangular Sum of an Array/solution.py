# Problem: Find Triangular Sum of an Array
# Language: python3
# Runtime: 3236 ms
# Memory: 14.2 MB

class Solution:
    def triangularSum(self, A: List[int]) -> int:
        
        while len(A) > 1:
            B = []
            for i in range(1,len(A)):
                B.append((A[i-1] + A[i])% 10)
            A = B[:]
        
        return A[0]