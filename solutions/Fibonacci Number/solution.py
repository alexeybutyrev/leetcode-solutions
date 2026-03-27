# Problem: Fibonacci Number
# Language: python
# Runtime: 20 ms
# Memory: 11.8 MB

class Solution(object):
    def _fib(self, memo, n):
        if n == 1:
            return 1
        if 0 == n:
            return 0
        
        if n not in memo.keys():
            memo[n] = self._fib(memo, n-1) + self._fib(memo, n-2)
        
        return memo[n]
        
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        return self._fib(dict(),N)
    