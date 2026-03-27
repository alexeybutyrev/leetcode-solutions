# Problem: Minimum Bit Flips to Convert Number
# Language: python3
# Runtime: 30 ms
# Memory: 16.6 MB

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal)[2:].count("1")