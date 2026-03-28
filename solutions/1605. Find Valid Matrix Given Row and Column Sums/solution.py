# Problem: Find Valid Matrix Given Row and Column Sums
# Language: python3
# Runtime: 1192 ms
# Memory: 18.6 MB

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

    
        m, n = len(rowSum), len(colSum)
        A = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                A[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= A[i][j]
                colSum[j] -= A[i][j]
        return A