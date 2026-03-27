# Problem: Binary Search
# Language: python
# Runtime: 278 ms
# Memory: 14.5 MB

class Solution(object):
    def search(self, A, x):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(A)
        
        while lo < hi:
            m = lo + hi >> 1
            
            if A[m] < x:
                lo = m + 1
            else:
                hi = m
                
        
        return lo if (lo < len(A) and A[lo] == x) else -1