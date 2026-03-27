# Problem: Minimum Difference Between Largest and Smallest Value in Three Moves
# Language: python3
# Runtime: 294 ms
# Memory: 31.8 MB

class Solution:
    def minDifference(self, A: List[int]) -> int:
        A.sort()
        N = len(A)
        if N<4: return 0
        
        @cache
        def dp(i,j,k):
            if i >=j: return 0
            if not k: return A[j]-A[i]
            return min(dp(i+1,j,k-1),dp(i,j-1,k -1))
        
        return dp(0,N-1,3)