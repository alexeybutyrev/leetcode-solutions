# Problem: Sum of Values at Indices With K Set Bits
# Language: python3
# Runtime: 79 ms
# Memory: 16.5 MB

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i,x in enumerate(nums):
            c = bin(i)[2:].count('1')
            if c == k:
                ans += x
        return ans