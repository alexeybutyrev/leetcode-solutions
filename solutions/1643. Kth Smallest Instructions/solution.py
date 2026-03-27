# Problem: Kth Smallest Instructions
# Language: python3
# Runtime: 52 ms
# Memory: 14.2 MB

from collections import deque
from math import factorial
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        def choose(n, k):
            if n < k:
                return 0
            return factorial(n) / (factorial(k) * factorial(n - k))
        
        def combination(n, k, m):
            result = []
            a      = n
            b      = k
            x      = (choose(n, k) - 1) - m
            for i in range(0, k):
                a = a - 1
                while choose(a, b) > x:
                    a = a - 1
                result.append(n - 1 - a)
                x = x - choose(a, b)
                b = b - 1
            return result
        
        c = combination(destination[0]  + destination[1], destination[1], k-1)
        #print(c)
        res = ["V"] * (destination[0]  + destination[1])
        
        for i in c:
            res[i] = "H"
        return "".join(res)