# Problem: Knight Probability in Chessboard
# Language: python3
# Runtime: 173 ms
# Memory: 25.9 MB

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def is_legal(i,j):
            if i < 0 or j < 0 or i >= n or j >= n:
                return False
            return True
        
        @cache
        def next_move(i,j):
            ans = []
            for dx,dy in [(1,2),(2,1),(-1,2),(2,-1),(-2,1),(-2,-1),(1,-2),(-1,-2)]:
                x = i + dx
                y = j + dy
                if is_legal(x,y):
                    ans.append((x,y))
            return ans
    
        @cache
        def dfs(i,j,k):
            if k == 0:
                return 1
            ans = 0
            for x,y in next_move(i,j):
                ans += dfs(x,y,k-1)
            return ans
        
        return dfs(row,column,k) / 8 ** k
            