# Problem: Nim Game
# Language: python3
# Runtime: 32 ms
# Memory: 14.2 MB

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0