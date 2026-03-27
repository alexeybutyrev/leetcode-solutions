# Problem: Find Xor-Beauty of Array
# Language: python3
# Runtime: 356 ms
# Memory: 28 MB

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        x = 0
        for a in nums:
            x ^= a
        return x