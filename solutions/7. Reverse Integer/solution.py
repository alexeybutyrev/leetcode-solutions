# Problem: Reverse Integer
# Language: python3
# Runtime: 32 ms
# Memory: 14.1 MB

class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) > 2**31 -1:
            return 0
        
        if x < 0:
            c = -int(str(x)[1:][::-1])
            
        else:
            c = int(str(x)[::-1])
        
        return c if abs(c) <= 2**31 -1 else 0