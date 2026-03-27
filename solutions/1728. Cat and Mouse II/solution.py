# Problem: Cat and Mouse II
# Language: python3
# Runtime: 3950 ms
# Memory: 408.2 MB

class Solution:
    def canMouseWin(self, A: List[str], CJ: int, MJ: int) -> bool:
        
        N,M = len(A), len(A[0])
        FX,FY = None, None
        for i in range(N):
            for j in range(M):
                if A[i][j] == 'F':
                    FX,FY = i,j
                if A[i][j] == 'M':
                    MX,MY = i,j
                if A[i][j] == 'C':
                    CX,CY = i,j

        
        @cache    
        def get_moves(x, y, jump):
            moves = [(x, y)]  # include staying
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                for step in range(1, jump+1):
                    nx, ny = x + dx*step, y + dy*step
                    if not (0 <= nx < N and 0 <= ny < M) or A[nx][ny] == '#': 
                        break
                    moves.append((nx, ny))
            return moves
        
        @cache
        def dp(mx,my,cx,cy,c):
            if mx == FX and my == FY: return True
            if (mx == cx and my == cy) or (cx == FX and cy == FY): return False
            if c >= 200: return False
            
            # mouse
            if c & 1 == 0:
                moves = get_moves(mx,my,MJ)
                for x,y in moves:
                    if dp(x,y,cx,cy, c + 1): return True
                return False
            else:
                moves = get_moves(cx,cy,CJ)
                for x,y in moves:
                    if not dp(mx,my,x,y, c + 1): return False
                return True
                

        return dp(MX,MY,CX,CY,0)