# Problem: Keep Multiplying Found Values by Two
# Language: python3
# Runtime: 0 ms
# Memory: 18 MB

class Solution:
    def findFinalValue(self, nums: List[int], x: int) -> int:
        s = set(nums)

        while x in s:
            x *= 2
        return x