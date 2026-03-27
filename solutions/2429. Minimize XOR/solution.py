# Problem: Minimize XOR
# Language: python3
# Runtime: 0 ms
# Memory: 17.7 MB

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n = (bin(num2)[2:]).count('1')
        ans = 0
        for i in range(33,-1,-1):
            if (1<<i) & num1 != 0:
                n -= 1
                ans |= (1 <<i)
            if 0 == n:
                return ans
        for i in range(33):
            if ans & (1<<i) != 0:
                continue
            ans |= (1<<i)
            n -= 1
            if n == 0:
                return ans
        return ans