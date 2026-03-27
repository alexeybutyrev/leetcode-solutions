# Problem: Range Sum Query 2D - Immutable
# Language: python3
# Runtime: 2722 ms
# Memory: 26.5 MB

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.A = [list(accumulate(r,initial = 0)) for r in matrix]
        self.A = [list(accumulate(r,initial = 0)) for r in zip(*self.A)]
        self.A = list(zip(*self.A))
        #print(self.A)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row2 += 1
        col2 += 1
        S11 = self.A[row1][col1]
        S12 = self.A[row1][col2]
        S21 = self.A[row2][col1]
        S22 = self.A[row2][col2]
        return S22 + S11 - S12 - S21


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)