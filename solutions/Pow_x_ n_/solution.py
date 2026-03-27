# Problem: Pow(x, n)
# Language: python
# Runtime: 20 ms
# Memory: 11.8 MB

class Solution(object):
    
    def _pow(self, x, n):
        if 1 == n: return x
        
        if 0 == n % 2:
            mid = n / 2
            C = self._pow(x,mid)
            return C * C
        else:
            mid = (n-1) / 2
            C = self._pow(x,mid)
            return C * C * x
        
        return x * self._pow(x, n-1)
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
            
        return self._pow(x,n)

        