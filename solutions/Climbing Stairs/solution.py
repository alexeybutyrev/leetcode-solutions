# Problem: Climbing Stairs
# Language: python
# Runtime: 16 ms
# Memory: 11.9 MB

class Solution(object):
    def _cst(self,d, l,n):
        if l > n:
            return 0
        if l == n:
            return 1
        if l not in d:
            d[l] = self._cst(d, l+1, n) + self._cst(d, l+2, n)
        return d[l]
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self._cst(dict(), 0,n)