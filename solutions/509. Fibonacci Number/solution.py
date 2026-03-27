# Problem: Fibonacci Number
# Language: python3
# Runtime: 23 ms
# Memory: 13.8 MB

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n in {1,2}:
            return 1
        
        a,b = 1,1
        
        for i in range(n-1):
            a,b = b, a+b
        
        return a