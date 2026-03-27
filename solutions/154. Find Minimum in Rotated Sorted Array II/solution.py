# Problem: Find Minimum in Rotated Sorted Array II
# Language: python3
# Runtime: 48 ms
# Memory: 14.7 MB

class Solution:
    def findMin(self, A: List[int]) -> int:
        lo = 0
        hi = len(A)-1
        
        while lo < hi:
            mid = hi + lo >> 1
            
                
            if A[mid] < A[hi]:
                hi = mid
            elif A[mid] > A[hi]:
                lo = mid + 1
            else:
                hi -= 1
                
                
        return A[lo]