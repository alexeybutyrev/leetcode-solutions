# Problem: Smallest Integer Divisible by K
# Language: python3
# Runtime: 2703 ms
# Memory: 18.1 MB

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        x = 0
        for i in range(k+1):
            x = x * 10 + 1
            if x %k == 0: return i+1
        return -1