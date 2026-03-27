# Problem: Construct the Minimum Bitwise Array II
# Language: python3
# Runtime: 3 ms
# Memory: 19.3 MB

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            res = -1
            d = 1
            while (nums[i] & d) != 0:
                res = nums[i] - d
                d <<= 1
            nums[i] = res
        return nums