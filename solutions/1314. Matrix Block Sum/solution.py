# Problem: Matrix Block Sum
# Language: python3
# Runtime: 92 ms
# Memory: 15.3 MB

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = []
        N = len(matrix)
        M = len(matrix[0])
        
        for r in matrix:
            self.matrix.append(list(accumulate([0] + r)))
        
        self.matrix = [[0] * (M + 1)] +  self.matrix
        for j in range(1,M+1):
            for i in range(1,N+1):
                self.matrix[i][j] += self.matrix[i-1][j]
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2+1][col2+1] + self.matrix[row1][col1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1]
    

class Solution:
    def matrixBlockSum(self, A: List[List[int]], k: int) -> List[List[int]]:
        num_matrix = NumMatrix(A)
        
        N, M = len(A), len(A[0])
        
        for i in range(N):
            for j in range(M):
                rl = max(i - k, 0)
                rr = min(i + k, N - 1)
                
                cl = max(j - k, 0)
                cr = min(j + k, M - 1)
                
                A[i][j] = num_matrix.sumRegion(rl,cl,rr,cr)
        
        return A
                
                
                
        