# Problem: Valid Sudoku
# Language: python3
# Runtime: 96 ms
# Memory: 14.3 MB

class Solution:
    def isValidSudoku(self, A: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                if A[i][j] != ".":
                    if A[i][j] in s:
                        return False
                    s.add(A[i][j])
        
        for i in range(9):
            s = set()
            for j in range(9):
                if A[j][i] != ".":
                    if A[j][i] in s:
                        return False
                    s.add(A[j][i])
        
        for k in range(3):
            for l in range(3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        if A[i + 3*k][j + 3*l] != ".":
                            if A[i + 3*k][j + 3*l] in s:
                                return False
                            s.add(A[i + 3*k][j + 3*l])
                    
        return True