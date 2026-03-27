# Problem: House Robber IV
# Language: python3
# Runtime: 5272 ms
# Memory: 25 MB

class Solution:
    def minCapability(self, A: List[int], k: int) -> int:
        
        N = len(A)        
        if N <= 2:
            return min(A)
        
        def f(x):
            a = int(A[0] <= x)
            b = int(A[1] <= x)
            for i in range(2,N):
                a,b = max(b,a), int(A[i] <= x) + a
                if b >= k or a >= k:
                    return True
            return False
        
        lo = 0
        hi = sum(A)
        while lo < hi:
            mid = lo + hi >> 1
            
            if not f(mid):
                lo = mid + 1
            else:
                hi = mid 
        return lo
    