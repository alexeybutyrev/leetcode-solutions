# Problem: Flood Fill
# Language: python3
# Runtime: 104 ms
# Memory: 14.3 MB

class Solution:
    def floodFill(self, A: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        N, M = len(A), len(A[0])
        COLOR = A[sr][sc]
        if COLOR == newColor:
            return A
        seen = set()
        def dfs(i,j):
            if (i >= 0 and i <N and
                j >= 0 and j <M and
                A[i][j] == COLOR
               ):
                A[i][j] = newColor
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i,j-1)
                dfs(i-1,j)
            
        dfs(sr,sc)
        return A
            