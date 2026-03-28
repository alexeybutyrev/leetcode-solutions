# Problem: Binary Number with Alternating Bits
# Language: python3
# Runtime: 24 ms
# Memory: 14.2 MB

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        
        cur = n %2
        n >>=1
        while n:
            if cur == n %2:
                return False
            cur = n % 2
            n >>= 1
            
        return True