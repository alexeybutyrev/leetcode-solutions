# Problem: House Robber II
# Language: python3
# Runtime: 24 ms
# Memory: 14.5 MB

class Solution:
    def rob(self, A: List[int]) -> int:
        N = len(A)
        
        @cache
        def dp(i, mask):
            if i >= N:
                return 0
            if i == N-1:
                return 0 if mask else A[N-1]
            
            s1 = dp(i+1,mask)
            if i == 0:
                s2 = A[i] + dp(i+2,1)
            else:
                s2 = A[i] + dp(i+2,mask)
            return max(s1, s2)
        
        return dp(0,0)
            