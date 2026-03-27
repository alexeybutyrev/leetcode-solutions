# Problem: Minimum Knight Moves
# Language: python3
# Runtime: 121 ms
# Memory: 15.5 MB

class Solution:
    def minKnightMoves(self, X: int, Y: int) -> int:
        
        @cache
        def dfs(x,y):
            if x + y == 0:
                return 0
            if x + y == 2:
                return 2
            
            return min(dfs(abs(x-1),abs(y-2)),dfs(abs(x-2),abs(y-1))) + 1
        
        return dfs(abs(X),abs(Y))