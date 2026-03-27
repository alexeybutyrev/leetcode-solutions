# Problem: Letter Tile Possibilities
# Language: python3
# Runtime: 184 ms
# Memory: 22.9 MB

class Solution:
    def numTilePossibilities(self, A: str) -> int:
        N = len(A)
        T = (1 << N) - 1
        ans = set()
        def backtrack(mask, s):
            if s:
                ans.add(s)
                
            if mask != T:
                for j in range(N):
                    if mask & (1 << j) == 0:
                        backtrack(mask | (1<<j), s + A[j])
        
        backtrack(0,"")
        return len(ans)