# Problem: Make Array Strictly Increasing
# Language: python3
# Runtime: 4063 ms
# Memory: 253.4 MB

class Solution:
    def makeArrayIncreasing(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        if N == 1: return 0
        
        B.sort()
        @cache
        def dp(i,j,s):
            if i == N: return 0
            
            x = B[j] if s else A[i-1]
            c1 = inf
            if x < A[i]:
                c1 = dp(i+1,j,False)
            
            ind = bisect_right(B[j:],x)

            if ind == len(B[j:]):
                c2 = inf
            else:
                c2 = 1 + dp(i+1,j+ind,True)
                
            return min(c1,c2)
        
        
        ans = min(dp(1,0,False), 1 + dp(1,0,True))
        return -1 if ans == inf else ans
                