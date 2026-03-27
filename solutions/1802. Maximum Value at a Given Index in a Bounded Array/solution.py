# Problem: Maximum Value at a Given Index in a Bounded Array
# Language: python3
# Runtime: 28 ms
# Memory: 14.3 MB

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def asum(a,b):
            return (a + b) * (b - a + 1) // 2
        
        def S(a):
            left  = asum(max(0, a - index),a)
            right = asum(max(0, a - (n - 1 - index)),a)
            return left + right -a
        
        maxSum -= n
        
        lo, hi = 0, maxSum
        
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if S(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1