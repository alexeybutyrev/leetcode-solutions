# Problem: Minimum Obstacle Removal to Reach Corner
# Language: python3
# Runtime: 6752 ms
# Memory: 51 MB


class Solution:
    def minimumObstacles(self, A: List[List[int]]) -> int:
        N,M = len(A), len(A[0])
        
        
        """
        seen = set()
        #@cache
        def dfs(i,j, seen):
            #print(i,j)
            if i == N - 1 and j == M - 1:
                #print("here")
                return 0
            
            ans = inf
            if i >= 0 and j >= 0 and i < N and j < M and (i,j) not in seen:
                ans = min(ans, A[i][j] + dfs(i+1,j, seen | {(i,j)}))
                ans = min(ans, A[i][j] + dfs(i-1,j, seen | {(i,j)}))
                ans = min(ans, A[i][j] + dfs(i,j+1, seen | {(i,j)}))
                ans = min(ans, A[i][j] + dfs(i,j-1, seen | {(i,j)}))
            return ans
        
        """
        q = []
        heappush(q, (0,0,0,0))
        
        D = [[inf] * M for _ in range(N)]
        steps = [[inf] * M for _ in range(N)]
        D[0][0] = 0
        steps[0][0] = 0
        while q:
            d, s, i, j = heappop(q)
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x = i + dx
                y = j + dy
                if x >= 0 and y >= 0 and x < N and y < M:
                    if D[x][y] < d + A[x][y]:
                        continue
                    elif D[x][y] == d + A[x][y]:
                        if steps[x][y] <= s + 1:
                            continue
                        steps[x][y]= s + 1
                        heappush(q,(d + A[x][y], s + 1, x,y))
                    else:
                        D[x][y] = d + A[x][y]
                        steps[x][y] = s + 1
                        heappush(q,(d + A[x][y], s + 1, x,y))
            
        return D[-1][-1]
    
    
    