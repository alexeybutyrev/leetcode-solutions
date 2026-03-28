# Problem: N-th Tribonacci Number
# Language: python3
# Runtime: 28 ms
# Memory: 14.3 MB

class Solution:
    def tribonacci(self, n: int) -> int:
        if n in {0,1,2}: return min(n,1)
        
        a,b,c = 0,1,1
        
        for _ in range(2,n):
            a,b,c = b,c,a+b+c
        
        return c