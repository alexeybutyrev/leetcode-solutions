# Problem: Solving Questions With Brainpower
# Language: python3
# Runtime: 2612 ms
# Memory: 208.6 MB

class Solution:
    def mostPoints(self, A: List[List[int]]) -> int:
        N = len(A)
        @cache
        def dp(i):
            if i >= N:
                return 0
            s1 = A[i][0] + dp(i + A[i][1]+1)
            s2 = dp(i + 1)
            return max(s1,s2)
        return dp(0)