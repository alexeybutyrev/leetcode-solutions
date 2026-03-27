# Problem: 01 Matrix
# Language: python3
# Runtime: 553 ms
# Memory: 19.7 MB

class Solution:
    def updateMatrix(self, A: List[List[int]]) -> List[List[int]]:
        N,M = len(A), len(A[0])
        seen = set()
        q = deque()
        for i in range(N):
            for j in range(M):
                if A[i][j]== 0:
                    q.append((i,j))
                    seen.add((i,j))
        l = 0
        while q:
            L = len(q)
            for _ in range(L):
                i,j = q.popleft()
                A[i][j] = l
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    
                    x = i + dx
                    y = j + dy
                    if 0<=x<N and 0<=y<M and (x,y) not in seen:
                        seen.add((x,y))
                        q.append((x,y))
            l+=1
        return A
    