# Problem: Range Sum Query 2D - Immutable
# Language: python3
# Runtime: 100 ms
# Memory: 17.4 MB

from itertools import accumulate
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        N, M = len(matrix), len(matrix[0])
        for i,r in enumerate(matrix):
            r = list(accumulate([0] + r))
            matrix[i] = r
        
        matrix = [[0] * (M + 1)] + matrix
        for i in range(1,N+1):
            for j in range(M+1):
                matrix[i][j] += matrix[i-1][j]
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2+1][col2+1] + self.matrix[row1][col1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)