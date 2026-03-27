# Problem: Complement of Base 10 Integer
# Language: python3
# Runtime: 0 ms
# Memory: 19.5 MB

class Solution:
    def bitwiseComplement(self, x: int) -> int:
        if x ==0: return 1
        mask = (1 << x.bit_length() ) - 1
        return x ^ mask