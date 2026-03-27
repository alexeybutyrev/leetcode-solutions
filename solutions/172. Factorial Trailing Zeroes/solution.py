# Problem: Factorial Trailing Zeroes
# Language: python3
# Runtime: 32 ms
# Memory: 14.3 MB

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0 
        while n > 0:
            n //= 5
            ans += n
        return ans
            