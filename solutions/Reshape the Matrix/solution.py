# Problem: Reshape the Matrix
# Language: python3
# Runtime: 80 ms
# Memory: 15.2 MB

class Solution:
    def matrixReshape(self, A: List[List[int]], r: int, c: int) -> List[List[int]]:
        N, M = len(A), len(A[0])
        if r * c != N * M:
            return A
        
        k=0
        
        ANS = [[-1] * c for _ in range(r)]
        row = 0
        col = 0
        for i in range(N):
            for j in range(M):
                ANS[row][col] = A[i][j]
                col += 1
                if col == c:
                    col = 0
                    row += 1
        
        return ANS