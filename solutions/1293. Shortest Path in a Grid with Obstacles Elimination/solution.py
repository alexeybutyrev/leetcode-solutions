# Problem: Shortest Path in a Grid with Obstacles Elimination
# Language: python3
# Runtime: 652 ms
# Memory: 22.2 MB

class Solution:
    def shortestPath(self, A: List[List[int]], k: int) -> int:
        N = len(A)
        M = len(A[0])
        
        q = deque([(0,0,k)])
        seen = [[inf] * M for _ in range(N)]
        seen = {(0,0,k)}
        step = 0
        while q:
            L = len(q)
            for _ in range(L):
                i,j,o = q.popleft()
                if i == N - 1 and j == M - 1:
                    return step
                
                for dx,dy in {(1,0),(-1,0),(0,1),(0,-1)}:
                    x = i + dx
                    y = j + dy
                    if x >= 0 and x < N and y >= 0 and y < M:
                        if A[x][y]:
                            if o and (x,y,o-1) not in seen:
                                seen.add((x,y,o-1))
                                q.append((x,y,o-1))
                        else:
                            if (x,y,o) not in seen:
                                seen.add((x,y,o))
                                q.append((x,y,o))
            step += 1
        
        return -1
        
        