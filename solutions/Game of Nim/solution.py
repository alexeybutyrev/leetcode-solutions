# Problem: Game of Nim
# Language: python3
# Runtime: 1154 ms
# Memory: 31.5 MB

class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        N = len(piles)
        
        @cache
        def dp(piles):
            if sum(piles) == 0: return False
            A = list(piles)
            for i in range(N):
                # no stones in this pile do nothing
                if not A[i]: continue
                
                # try removing different number of stones
                for s in range(1,A[i]+1):
                    before = A[i]
                    A[i] = A[i] - s
                    if not dp(tuple(A)): return True
                    A[i] = before
            return False
        
        return dp(tuple(piles))