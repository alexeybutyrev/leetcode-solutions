# Problem: Sum of Digits in Base K
# Language: python3
# Runtime: 36 ms
# Memory: 14.2 MB

import string
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        digs = string.digits + string.ascii_letters


        def int2base(x, base):
            if x < 0:
                sign = -1
            elif x == 0:
                return digs[0]
            else:
                sign = 1

            x *= sign
            digits = []

            while x:
                digits.append(digs[int(x % base)])
                x = int(x / base)

            if sign < 0:
                digits.append('-')

            digits.reverse()

            return ''.join(digits)
        
        ans = 0
        for d in int2base(n, k):
            ans += int(d)
        return ans