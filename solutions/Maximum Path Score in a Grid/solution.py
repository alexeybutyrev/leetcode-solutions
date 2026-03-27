# Problem: Maximum Path Score in a Grid
# Language: python3
# Runtime: 9395 ms
# Memory: 630.7 MB

class Solution:
    def maxPathScore(self, A: List[List[int]], k: int) -> int:
        N,M = len(A), len(A[0])

        @cache
        def dp(i,j,c):
            if i == N-1 and j == M-1:
                c += int(A[i][j] > 0)
                return A[i][j] if c <= k else -inf
            if i == N or j == M or c > k:
                return -inf
            c += int(A[i][j] > 0)
            ans = A[i][j] + max(dp(i+1,j,c), dp(i,j+1,c))
            return ans

        ans = dp(0,0,int(A[0][0] > 1))
        return -1 if ans == -inf else ans