# Problem: Shift 2D Grid
# Language: python3
# Runtime: 192 ms
# Memory: 14.7 MB

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        A = deepcopy(grid)
        N, M = len(A), len(A[0])
        k %= N *M
        
        for i in range(N):
            for j in range(M):
                j1 = (j + k) % M
                i1 = (i + (j + k) // M) % N
                A[i1][j1] = grid[i][j]
        return A