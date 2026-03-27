# Problem: Disconnect Path in a Binary Matrix by at Most One Flip
# Language: python3
# Runtime: 913 ms
# Memory: 19.2 MB

class Solution:
    def isPossibleToCutPath(self, A: List[List[int]]) -> bool:
        N, M = len(A), len(A[0])
        def dfs(i,j):
            if i == N-1 and j == M-1:
                return True
            if i > N-1 or j > M-1 or A[i][j]==0:
                return False
            A[i][j] = 0
            return dfs(i+1,j) or dfs(i,j+1)
        if not dfs(0,0):
            return True
        A[0][0] = 1
        return not dfs(0,0)
        