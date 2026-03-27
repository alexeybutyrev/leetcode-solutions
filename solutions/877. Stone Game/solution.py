# Problem: Stone Game
# Language: python3
# Runtime: 460 ms
# Memory: 126.7 MB

class Solution:
    def stoneGame(self, A: List[int]) -> bool:
        N = len(A)
        @lru_cache(None)
        def dfs(i,j):
            if i == j:
                return 0
            
            return max(A[i] + dfs(i+1, j), A[j] + dfs(i,j-1))
        
        a = dfs(0,N-1)
        return a > sum(A) - a