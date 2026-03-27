# Problem: Find Peak Element
# Language: python3
# Runtime: 54 ms
# Memory: 14 MB

class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        if len(A) == 1: return 0
        if len(A) == 2: 
            return max( (a,i) for i,a in enumerate(A))[1]
        
        lo = 0
        hi = len(A)-1
        
        while lo < hi:
            mid = lo + hi >> 1
            
            if A[mid + 1] < A[mid] > A[mid-1] :
                return mid
            
            if A[mid-1] <= A[mid] <= A[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo