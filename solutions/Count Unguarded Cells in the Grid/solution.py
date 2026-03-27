# Problem: Count Unguarded Cells in the Grid
# Language: python3
# Runtime: 1192 ms
# Memory: 74.8 MB

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        A = [[0] * n for _ in range(m)]
        N,M = len(A), len(A[0])
        W = set()
        for w in walls:
            W.add((w[0],w[1]))
            
        seen = set()
        def walk_left(i,j):
            if i >= 0 and i < N and j >= 0 and j < M and (i,j) not in W and (i,j,'l') not in seen:
                seen.add((i,j,'l'))
                A[i][j] = 1
                walk_left(i-1,j)
        
        def walk_up(i,j):
            if i >= 0 and i < N and j >= 0 and j < M and (i,j) not in W and (i,j,'u') not in seen:
                seen.add((i,j,'u'))
                A[i][j] = 1
                walk_up(i,j+1)
        
        def walk_down(i,j):
            if i >= 0 and i < N and j >= 0 and j < M and (i,j) not in W and (i,j,'d') not in seen:
                seen.add((i,j,'d'))
                A[i][j] = 1
                walk_down(i,j-1)
                
        
        def walk_right(i,j):
            if i >= 0 and i < N and j >= 0 and j < M and (i,j) not in W and (i,j,'r') not in seen:
                seen.add((i,j,'r'))
                A[i][j] = 1
                walk_right(i+1,j)
                
                
            
        
        for i,j in guards:
            walk_left(i,j)
            walk_up(i,j)
            walk_down(i,j)
            walk_right(i,j)
        
        s = 0
        for i in range(N):
            for j in range(M):
                if (i,j) not in W:
                    s += (A[i][j] == 0)
        return s
    