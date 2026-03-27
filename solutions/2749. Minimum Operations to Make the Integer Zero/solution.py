# Problem: Minimum Operations to Make the Integer Zero
# Language: python3
# Runtime: 43 ms
# Memory: 16.2 MB

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(60):
            x = num1 - k * num2
            if x.bit_count() <= k <= x:
                return k
        return -1