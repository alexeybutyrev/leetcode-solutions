# Problem: Reverse Bits
# Language: python3
# Runtime: 64 ms
# Memory: 13.7 MB

class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        s = '0' * (32 - len(s)) + s
        
        return int(s[::-1],2)