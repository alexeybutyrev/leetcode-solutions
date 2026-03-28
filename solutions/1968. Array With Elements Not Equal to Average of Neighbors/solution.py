# Problem: Array With Elements Not Equal to Average of Neighbors
# Language: python3
# Runtime: 1448 ms
# Memory: 29.3 MB

class Solution:
    def rearrangeArray(self, A: List[int]) -> List[int]:
        N = len(A)
        
        i = 0
        
        
        while i < N-1:
            if i >= 1 and A[i] - A[i-1] == A[i+1] - A[i]:
                A[i],A[i+1] = A[i+1],A[i]
                i-=1
            else:
                i+=1
                
        return A