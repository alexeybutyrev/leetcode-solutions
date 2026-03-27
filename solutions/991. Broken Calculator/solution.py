# Problem: Broken Calculator
# Language: python3
# Runtime: 50 ms
# Memory: 13.9 MB

class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        ans = 0
        while y > x:
            if y & 1:
                y += 1
            else:
                y >>= 1
            ans += 1
        return ans + x-y
            