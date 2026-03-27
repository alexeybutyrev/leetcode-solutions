# Problem: Increment Submatrices by One
# Language: python3
# Runtime: 2963 ms
# Memory: 35.3 MB

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        A = [[0] * n for _ in range(n)]
        
        c = defaultdict(Counter)
        
        for r1,c1,r2,c2 in queries:
            for r in range(r1,r2 + 1):
                A[r][c1] += 1
                if c2 + 1<n:
                    A[r][c2+1] -= 1
        
        for i in range(n):
            for j in range(1,n):
                A[i][j] += A[i][j-1]
        return A