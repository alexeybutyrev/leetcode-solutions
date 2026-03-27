# Problem: Max Dot Product of Two Subsequences
# Language: python3
# Runtime: 405 ms
# Memory: 112.5 MB

class Solution:
    def maxDotProduct(self, A: List[int], B: List[int]) -> int:
        N, M = len(A), len(B)
        @cache
        def dp(i,j):
            if i == N or j == M: return -inf
            s1 = A[i] * B[j] + max(0,dp(i+1,j+1))
            s2 = dp(i+1,j)
            s3 = dp(i,j+1)
            return max(s1,s2,s3)
        
        return dp(0,0)