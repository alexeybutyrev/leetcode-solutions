# Problem: Concatenate Non-Zero Digits and Multiply by Sum I
# Language: python3
# Runtime: 4 ms
# Memory: 17.7 MB

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        a = ''
        s = 0
        for x in str(n):
            if x != '0':
                a += x
                s += int(x)
        if not a: return 0
        return int(a) * s