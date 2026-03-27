# Problem: Maximum Number of Moves in a Grid
# Language: python3
# Runtime: 102 ms
# Memory: 37 MB

class Solution:
    def maxMoves(self, A: List[List[int]]) -> int:
        N, M = len(A),len(A[0])
        seen = set()
        q = deque()
        for j in range(N):
            q.append((j,0))
            seen.add((j,0))
        l = 0
        
        while q:
            L = len(q)
            for _ in range(L):
                x,y = q.popleft()
                for dx,dy in [(-1,1),(0,1),(1,1)]:
                    i = x + dx
                    j = y + dy
                    if 0 <= i  < N and 0 <= j < M and A[x][y] < A[i][j] and (i,j) not in seen:
                        seen.add((i,j))
                        q.append((i,j))
            if q:
                l += 1
            
        return l