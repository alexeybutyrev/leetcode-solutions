# Problem: Champagne Tower
# Language: python3
# Runtime: 99 ms
# Memory: 14 MB

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        A = [[0] * i for i in range(1,102)]
        
        A[0][0] = poured
        
        for i in range(query_row+1):
            for j in range(i + 1):
                q = (A[i][j] - 1.0) / 2.0
                if q > 0:
                    A[i+1][j] += q
                    A[i+1][j+1] += q
        return min(1, A[query_row][query_glass])