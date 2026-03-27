# Problem: Find Valid Matrix Given Row and Column Sums
# Language: python3
# Runtime: 550 ms
# Memory: 22.1 MB

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N, M = len(rowSum), len(colSum)
        A = [[0] * M for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
                A[i][j] = min(rowSum[i], colSum[j])
                rowSum[i], colSum[j] = rowSum[i] - A[i][j], colSum[j] - A[i][j]
        return A
                