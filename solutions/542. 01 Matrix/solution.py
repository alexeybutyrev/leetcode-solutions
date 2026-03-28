# Problem: 01 Matrix
# Language: python3
# Runtime: 676 ms
# Memory: 17.4 MB

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        N, M = len(mat), len(mat[0])
        dp = [[inf] * M for _ in range(N)]
        q = deque()
        for i in range(N):
            for j in range(M):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                    q.append((i,j))
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while q:
            i,j = q.popleft()
            for dx,dy in directions:
                x = i + dx
                y = j + dy
                if x>=0 and x < N and y >= 0 and y < M and dp[x][y] == inf:
                    dp[x][y] = 1 + dp[i][j]
                    q.append((x,y))

        return dp