# Problem: Find Minimum in Rotated Sorted Array
# Language: python3
# Runtime: 36 ms
# Memory: 14.4 MB

class Solution:
    def findMin(self, A: List[int]) -> int:
        
        lo = 0
        hi = len(A)-1
        
        while lo < hi:
            mid = hi + lo >> 1
            
            if A[mid] < A[hi]:
                hi = mid
            else:
                lo = mid + 1
                
        return A[lo]