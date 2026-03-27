# Problem: Convert a Number to Hexadecimal
# Language: python3
# Runtime: 30 ms
# Memory: 16.1 MB

class Solution:
    def toHex(self, n: int) -> str:
        if n == 0: return "0"
        m = '0123456789abcdef'
        ans = ''
        for i in range(8):
            d = n % 16
            c = m[d]
            ans = c + ans
            n //= 16
        
        return ans.lstrip('0')