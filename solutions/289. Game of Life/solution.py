# Problem: Game of Life
# Language: python3
# Runtime: 28 ms
# Memory: 14.2 MB

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m = len(board), len(board[0])
        stack = []
        
        for i in range(n):
            for j in range(m):
                count = 0
                for sx in [-1,0,1]:
                    for sy in [-1,0,1]:
                        if sx == 0 and sy == 0 or i + sx > n -1 or j + sy > m -1 or i + sx < 0 or j + sy < 0:
                            continue
                        if board[i+sx][j+sy] in [1,-1]:
                            count += 1
                if board[i][j]:
                    if count < 2 or count > 3:
                        board[i][j] = -1
                else:
                    if count == 3:
                        board[i][j] = 2
                        
        for i in range(n):
            for j in range(m):
                if board[i][j] in [2,-1]:
                    board[i][j] = 1 if board[i][j] == 2 else 0
        
        