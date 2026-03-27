# Problem: Search Insert Position
# Language: python3
# Runtime: 67 ms
# Memory: 17.1 MB

class Solution:
    def searchInsert(self, A: List[int], T: int) -> int:
        lo = 0 
        hi = len(A)
        
        while lo < hi:
            mid = lo + hi >> 1
            
            if A[mid] < T:
                lo = mid + 1
            else:
                hi = mid
        return lo
