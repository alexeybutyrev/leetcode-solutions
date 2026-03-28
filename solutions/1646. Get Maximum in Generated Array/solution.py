# Problem: Get Maximum in Generated Array
# Language: python3
# Runtime: 40 ms
# Memory: 14 MB

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        def f(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i % 2 == 0:
                return f(i // 2)
            else:
                j = (i - 1) // 2
                return f(j) + f(j+1)
        
        
        return max([f(i) for i in range(n+1)])