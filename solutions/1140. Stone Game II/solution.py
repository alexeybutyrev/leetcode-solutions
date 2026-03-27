# Problem: Stone Game II
# Language: python3
# Runtime: 175 ms
# Memory: 17.9 MB

class Solution:
    def stoneGameII(self, A: List[int]) -> int:
        A = list(accumulate(A[::-1]))[::-1]
        N = len(A)
        @cache
        def dp(i,m):
            if i+2*m>=N: return A[i]
            ans = A[i]
            p = inf
            for j in range(1, 2*m +1):
                p = min(p,dp(i+j,max(j,m)))
                
            return ans-p
        
        return dp(0,1)