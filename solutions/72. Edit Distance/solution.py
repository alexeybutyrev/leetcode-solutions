# Problem: Edit Distance
# Language: python3
# Runtime: 35 ms
# Memory: 20.2 MB

class Solution:
    def minDistance(self, A: str, B: str) -> int:
        NA, NB = len(A), len(B)
        @cache
        def dp(i,j):
            if i == NA: return NB - j
            if j == NB: return NA - i
            if A[i] == B[j]:
                return dp(i+1, j+1)
            return min(1 + dp(i+1,j), 1 + dp(i,j+1), 1 + dp(i+1,j+1))
        
        return dp(0,0)