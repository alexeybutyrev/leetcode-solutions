# Problem: Maximum Value of K Coins From Piles
# Language: python3
# Runtime: 4133 ms
# Memory: 141.2 MB

class Solution:
    def maxValueOfCoins(self, A: List[List[int]], k: int) -> int:
        
        A = [list(accumulate(a)) for a in A]
        
        N = len(A)
        @cache
        def dp(i,k):
            if i == N: return 0
            if k == 0:return 0
            
            ans = dp(i+1,k)
            for j in range(min(len(A[i]),k)):
                ans = max(ans, A[i][j] + dp(i+1,k-j-1))
            return ans
        return dp(0,k)