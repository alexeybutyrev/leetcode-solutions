# Problem: Make Array Strictly Increasing
# Language: python3
# Runtime: 826 ms
# Memory: 139.3 MB

class Solution:
    def makeArrayIncreasing(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        if N == 1: return 0
        B.sort()
        @cache
        def dp(i,x):
            if i == N: return 0
            
            c1 = dp(i+1,A[i]) if x < A[i] else inf
            c2 = inf
            
            ind = bisect_right(B,x)
            if ind < len(B): 
                c2 = 1 + dp(i+1,B[ind])
                
            return min(c1,c2)
        
        ans = min(dp(1,A[0]), 1 + dp(1,B[0]))
        return -1 if ans == inf else ans    