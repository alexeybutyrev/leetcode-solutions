# Problem: Partition Array for Maximum Sum
# Language: python3
# Runtime: 723 ms
# Memory: 165.5 MB

class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        @cache
        def dp(i,j,k):
            if i == N: return 0
            if k == K: return K * max(A[i],A[j]) + dp(i+1,i+1,1)
            
            s1 = dp(i+1,i if A[i] > A[j] else j, k+1)
            s2 = k * max(A[i],A[j]) + dp(i+1,i+1,1)
            return max(s1, s2)
        return dp(0,0,1)