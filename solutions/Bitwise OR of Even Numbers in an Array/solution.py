# Problem: Bitwise OR of Even Numbers in an Array
# Language: python3
# Runtime: 0 ms
# Memory: 18 MB

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        ans = 0
        for i,x in enumerate(nums):
            if x % 2 == 0:
                ans |= x
        return ans