# Problem: Map of Highest Peak
# Language: python3
# Runtime: 5064 ms
# Memory: 221.8 MB

from collections import deque
class Solution:
    def highestPeak(self, A: List[List[int]]) -> List[List[int]]:
        N, M = len(A), len(A[0])
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        q = deque()
        seen = set()
        for i in range(N):
            for j in range(M):
                if A[i][j]:
                    A[i][j] = 0
                    seen.add((i,j))
                    q.append((i,j))
                else:
                    A[i][j] = inf
                    
        while q:
            l = len(q)
            for _ in range(l):
                i,j = q.popleft()
                
                val = A[i][j]
                
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if x >= 0 and x < N and y >= 0 and y < M: 
                        val = min(val, A[x][y])
                        if (x,y) not in seen:
                            seen.add((x,y))
                            q.append((x,y))
                        
                
                if A[i][j] !=0:
                    A[i][j] = val + 1
                    
                
        return A