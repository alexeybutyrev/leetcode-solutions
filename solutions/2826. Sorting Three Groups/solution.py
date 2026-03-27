# Problem: Sorting Three Groups
# Language: python3
# Runtime: 213 ms
# Memory: 17.1 MB

class Solution:
    def minimumOperations(self, A: List[int]) -> int:
        N = len(A)
        G = list(sorted(set(A)))
        NG = len(G)
        if NG == 1: return 0
        
        @cache
        def dp(i,g):
            if i == N: return 0
            if A[i] == g: return dp(i+1,g)
            if A[i] < g:
                return 1 + dp(i+1,g)
            return min(1 + dp(i+1,g), dp(i+1,A[i]))
        
        return dp(0, G[0])