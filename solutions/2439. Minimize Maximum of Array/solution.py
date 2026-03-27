# Problem: Minimize Maximum of Array
# Language: python3
# Runtime: 1833 ms
# Memory: 26.9 MB

class Solution:
    def minimizeArrayValue(self, A: List[int]) -> int:
        
        def possible(x):
            left = 0
            for a in A:
                if a > x:
                    if left >= 0:
                        left -= a-x
                    if left < 0: return False
                else:
                    left += x-a
            return True
        
        
        lo = 0
        hi = sum(A)
        
        while lo < hi:
            mid = lo + hi >> 1
            if not possible(mid):
                lo = mid+1
            else:
                hi = mid
        
        return lo
                