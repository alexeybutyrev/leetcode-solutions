# Problem: Climbing Stairs II
# Language: python3
# Runtime: 963 ms
# Memory: 276.8 MB

class Solution:
    def climbStairs(self, n: int, A: List[int]) -> int:
        A = A
        N = len(A)
        @cache
        def dp(i):
            if i == N: return 0
            # i = 0
            x1 = A[i+1 -1] + 1 * 1 + dp(i+1) if i + 1 <= N else inf
            x2 = A[i+2 -1] + 2 * 2 + dp(i+2) if i + 2 <= N else inf
            x3 = A[i+3 -1] + 3 * 3 + dp(i+3) if i + 3 <= N else inf
            return min(x1,x2,x3)
            
        return dp(0)
            