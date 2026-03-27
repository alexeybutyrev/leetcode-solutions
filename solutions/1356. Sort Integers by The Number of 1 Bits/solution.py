# Problem: Sort Integers by The Number of 1 Bits
# Language: python3
# Runtime: 7 ms
# Memory: 19.7 MB

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x: (bin(x)[2:].count('1'),x))