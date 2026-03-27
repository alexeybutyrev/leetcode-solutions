# Problem: Minimum Array Sum
# Language: python3
# Runtime: 1723 ms
# Memory: 242.6 MB

class Solution:
    def minArraySum(self, A: List[int], K: int, O1: int, O2: int) -> int:
        
        N = len(A)
        @cache
        def dp(i,o1,o2):
            if i == N: return 0
            a1 = A[i] + dp(i+1,o1, o2)
            a2 = inf
            a3 = inf
            if o1:
                x = ceil(A[i]/ 2)
                a2 = x + dp(i+1,o1-1, o2)
                if o2 and x >= K:
                    a2 = min(a2, x-K + dp(i+1,o1-1, o2-1))
                
            
            if o2 and A[i] >= K:
                a3 = A[i] - K + dp(i+1,o1, o2-1)
                if o1:
                    a3 = min(a3, ceil((A[i] - K)/2) + dp(i+1,o1-1, o2-1))
            return min(a1,a2,a3)

        return dp(0,O1,O2)