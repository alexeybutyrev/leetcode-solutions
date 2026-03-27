# Problem: Maximize Score of Numbers in Ranges
# Language: python3
# Runtime: 2457 ms
# Memory: 32.6 MB

class Solution:
    def maxPossibleScore(self, A: List[int], d: int) -> int:
        lo, hi = 0, 10**10
        A.sort()
        N = len(A)
        def f(x):
            curr = A[0]
            for i in range(1,N):
                if A[i] + d - curr <x:
                    return False
                curr = max(A[i],curr + x)
            return True
                
            
        
        while lo<hi:
            mid = lo + hi >> 1
            if f(mid):
                lo = mid + 1
            else:
                hi = mid
        
        return lo if f(lo) else lo-1