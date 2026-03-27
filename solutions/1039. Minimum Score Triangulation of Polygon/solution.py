# Problem: Minimum Score Triangulation of Polygon
# Language: python3
# Runtime: 59 ms
# Memory: 18.8 MB

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        N = len(A)
        @cache
        def dp(i,j):
            if i + 2 > j: return 0
            if i + 2 == j: return A[i] * A[i+1] * A[i+2]
            ans = inf
            for k in range(i+1,j):
                ans = min(ans, A[i] * A[k] * A[j] + dp(i,k) + dp(k,j))
            return ans
        return dp(0, N-1)