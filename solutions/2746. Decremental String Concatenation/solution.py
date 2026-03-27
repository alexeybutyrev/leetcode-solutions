# Problem: Decremental String Concatenation
# Language: python3
# Runtime: 451 ms
# Memory: 48.6 MB

class Solution:
    def minimizeConcatenatedLength(self, A: List[str]) -> int:
        S = 0
        for x in A:
            S += len(x)
        
        N = len(A)
        
        @cache
        def dp(s,e, i):
            if i == N:
                return S
            
            l1 = (dp(A[i][0],e, i + 1) - 1) if s == A[i][-1] else dp(A[i][0],e,  i + 1)
            
            l2 = (dp(s,A[i][-1], i + 1) - 1) if e == A[i][0] else dp(s,A[i][-1],  i + 1)
            return min(l1,l2)
        
        return dp(A[0][0],A[0][-1],1)
            
            
        