# Problem: Largest Submatrix With Rearrangements
# Language: python3
# Runtime: 123 ms
# Memory: 36.4 MB

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        N, M = len(matrix), len(matrix[0])
        
        for j in range(M):
            s  = 0
            for i in range(N):
                s = 0 if matrix[i][j] == 0 else s + 1
                matrix[i][j] = s
        
        ans = 0
        for row in map(sorted, matrix):
            for col in range(M):
                ans = max(ans, ( M - col ) * row[col])
        
        return ans