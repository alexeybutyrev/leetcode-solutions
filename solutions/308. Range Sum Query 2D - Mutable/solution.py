# Problem: Range Sum Query 2D - Mutable
# Language: python3
# Runtime: 115 ms
# Memory: 19.1 MB

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.A = []
        for m in matrix:
            F = [0]
            for x in m:
                F.append(F[-1] + x)
            self.A.append(F)

    def update(self, row: int, col: int, val: int) -> None:
        before = self.A[row][col+1] - self.A[row][col]
        for c in range(col+1, len(self.A[0])):
            self.A[row][c] = self.A[row][c] - before + val
        
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for r in range(row1, row2+1):
            s += self.A[r][col2+1] - self.A[r][col1]
        return s
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)