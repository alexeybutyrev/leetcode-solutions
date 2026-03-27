# Problem: Increment Submatrices by One
# Language: python3
# Runtime: 203 ms
# Memory: 39.8 MB

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        A = [[0] * n for _ in range(n)]
        D = [[0] * (n+1) for _ in range(n+1)]

        for r1,c1,r2,c2 in queries:
            D[r1][c1] += 1

            D[r2 + 1][c1] -= 1
            D[r1][c2+1]   -= 1
            
            D[r2 + 1][c2 + 1] += 1


        for i in range(n):
            for j in range(n):
                x1 = 0 if i == 0 else A[i-1][j]
                x2 = 0 if j == 0 else A[i][j-1]
                x3 = 0 if i == 0 or j == 0 else A[i-1][j-1]
                A[i][j] = D[i][j] + x1 + x2 - x3
        return A