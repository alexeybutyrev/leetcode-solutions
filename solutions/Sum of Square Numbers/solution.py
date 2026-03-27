# Problem: Sum of Square Numbers
# Language: python3
# Runtime: 149 ms
# Memory: 16.3 MB

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def is_sq(x):
            b = int(sqrt(c - x * x) )
            return b*b == c - x * x
        
        return any(is_sq(a) for a in range(int(sqrt(c)) + 1))