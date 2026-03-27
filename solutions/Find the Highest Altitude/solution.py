# Problem: Find the Highest Altitude
# Language: python3
# Runtime: 44 ms
# Memory: 16.4 MB

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial = 0))