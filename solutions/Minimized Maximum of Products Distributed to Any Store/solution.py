# Problem: Minimized Maximum of Products Distributed to Any Store
# Language: python3
# Runtime: 1047 ms
# Memory: 28.5 MB

class Solution:
    def minimizedMaximum(self, K: int, A: List[int]) -> int:
        N = len(A)
        lo = 1
        hi = sum(A)
        
        while lo < hi:
            
            mid = lo + hi >> 1
            
            if sum( (a-1)//mid+1 for a in A) > K:
                lo = mid + 1
            else:
                hi = mid
        return lo