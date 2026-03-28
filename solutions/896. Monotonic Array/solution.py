# Problem: Monotonic Array
# Language: python
# Runtime: 464 ms
# Memory: 18.1 MB

class Solution(object):
    
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        def copmare(a,b,is_increasing=True):
            return b >= a if is_increasing else b<=a
        n = len(A)
        if n <= 2:
            return True
        
        is_increasing = copmare(A[0], A[n-1])
        
        for i in range(n-1):
            if not copmare(A[i], A[i+1],is_increasing):
                return False
        return True
        