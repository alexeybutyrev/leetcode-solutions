# Problem: Path With Minimum Effort
# Language: python3
# Runtime: 502 ms
# Memory: 17.6 MB

class Solution:
    def minimumEffortPath(self, A: List[List[int]]) -> int:
        N = len(A)
        M = len(A[0])
        
        D = [[inf] * M for _ in range(N)]
        
        h = []
        
        heappush(h, (0,0,0))
        
        while h:
            d,i,j = heappop(h)
            if i == N - 1 and j == M - 1:
                return d
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                x = i + dx
                y = j + dy
                
                if x >= 0 and x < N and y >= 0 and y < M:
                    dd = max(d,abs(A[i][j] - A[x][y]))
                    if D[x][y] > dd:
                        D[x][y] = dd
                        heappush(h,(dd,x,y))
        
        return D[-1][-1]
        
        