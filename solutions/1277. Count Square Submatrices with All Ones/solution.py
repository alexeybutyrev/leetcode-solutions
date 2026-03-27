# Problem: Count Square Submatrices with All Ones
# Language: python3
# Runtime: 81 ms
# Memory: 19.2 MB

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        
            
        n,m = len(matrix), len(matrix[0])

        for i in range(1,n):
            for j in range(1,m):
                matrix[i][j] *= min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
        return sum(map(sum, matrix))