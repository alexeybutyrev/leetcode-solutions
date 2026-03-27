# Problem: Complement of Base 10 Integer
# Language: python3
# Runtime: 37 ms
# Memory: 14.3 MB

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        x = 0
        i = 0
        while n:
            x += (1 << i) *((n - 1) & 1)
            i += 1
            n >>= 1
        return x