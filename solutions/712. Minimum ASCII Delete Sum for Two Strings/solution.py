# Problem: Minimum ASCII Delete Sum for Two Strings
# Language: python3
# Runtime: 711 ms
# Memory: 222.1 MB

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        A = [ord(x) for x in s1]
        B = [ord(x) for x in s2]
        SA = list(accumulate(A, initial =0))
        SB = list(accumulate(B, initial =0))
        
        NA = len(A)
        NB = len(B)
        @cache
        def dp(i,j):
            if i == NA: return SB[-1] - SB[j]
            if j == NB: return SA[-1] - SA[i]
            if A[i] == B[j]: return dp(i+1,j+1)
            return min(A[i] + dp(i+1,j), B[j] + dp(i,j+1))
            
        return dp(0,0)