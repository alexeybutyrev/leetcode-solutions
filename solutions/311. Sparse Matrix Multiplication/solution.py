# Problem: Sparse Matrix Multiplication
# Language: python3
# Runtime: 100 ms
# Memory: 13.8 MB

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n, m, r  = len(A), len(B[0]), len(A[0])
        
        C = []
        
        for i in range(n):
            C.append([0] * m)
            for j in range(m):
                for k in range(r):
                    if A[i][k] and B[k][j]:
                        C[i][j] += A[i][k] * B[k][j]
        
        return C