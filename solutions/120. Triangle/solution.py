# Problem: Triangle
# Language: python3
# Runtime: 91 ms
# Memory: 17.5 MB

class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        N = len(A)
        
        @cache
        def dp(i,j):
            if i == N:
                return 0
            else:

                s2 = dp(i+1,j)
                s3 = dp(i+1,j+1)
                return A[i][j] + min(s2,s3) 
        
        return dp(0,0)