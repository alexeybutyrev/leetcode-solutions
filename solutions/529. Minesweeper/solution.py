# Problem: Minesweeper
# Language: python3
# Runtime: 172 ms
# Memory: 19.2 MB

class Solution:
    def updateBoard(self, A: List[List[str]], C: List[int], seen = False) -> List[List[str]]:

        N, M = len(A), len(A[0])
        
        r,c = C
        if 0 <= r < N and 0 <= c < M:
            directions = ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))

            if A[r][c] == 'M':
                if not seen:
                    A[r][c] = 'X'
            elif A[r][c] == 'E':
                s = 0
                for dx,dy in directions:
                    x = r + dx
                    y = c + dy
                    if 0 <= x < N and 0 <= y < M and A[x][y] in {'M','X'}:
                        s += 1
                
                
                A[r][c] = str(s) if s else 'B'
                if s == 0:
                    for dx,dy in directions:
                        x = r + dx
                        y = c + dy
                        self.updateBoard(A, [x,y], True)
                
        return A
                
                
        