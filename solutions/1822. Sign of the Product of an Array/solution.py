# Problem: Sign of the Product of an Array
# Language: python3
# Runtime: 78 ms
# Memory: 16.4 MB

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        a = 1
        for x in nums:
            if x == 0: return 0
            a *= 1 if x > 0 else -1
        return a