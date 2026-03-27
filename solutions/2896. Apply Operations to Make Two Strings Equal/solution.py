# Problem: Apply Operations to Make Two Strings Equal
# Language: python3
# Runtime: 51 ms
# Memory: 17.1 MB

class Solution:
    def minOperations(self, s1: str, s2: str, X: int) -> int:

        A = []
        for i,(x,y) in enumerate(zip(s1,s2)):
            if x != y:
                A.append(i)
        N = len(A)
        
        if N & 1: return -1
        
        @cache
        def dp(i):
            if i == N-1: return X/2
            if i >= N: return 0
            
            c1 = dp(i+1) + X/2
            c2 = inf
            if i < N-1:
                c2 = dp(i+2) + A[i+1] - A[i]
            return min(c1,c2)
        return int(dp(0))
            
            
            