# Problem: Bulb Switcher
# Language: python3
# Runtime: 38 ms
# Memory: 16.4 MB

class Solution:
    def bulbSwitch(self, n: int) -> int:
        i = 0
        while n > 0:
            i += 1
            n -= (2 * i + 1)
        return i