# Problem: Rotate Image
# Language: python3
# Runtime: 24 ms
# Memory: 14.3 MB

class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(A)
        
        for i in range(N):
            for j in range(i+1,N):
                A[i][j],A[j][i] = A[j][i], A[i][j]
        
        for i in range(N):
            A[i] = A[i][::-1]