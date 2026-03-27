# Problem: Solving Questions With Brainpower
# Language: python3
# Runtime: 174 ms
# Memory: 139.1 MB

class Solution:
    def mostPoints(self, A: List[List[int]]) -> int:
        N = len(A)
        @cache
        def dp(i):
            if i >= N: return 0
            return max(A[i][0] + dp(i + A[i][1]+1), dp(i+1))
        return dp(0)