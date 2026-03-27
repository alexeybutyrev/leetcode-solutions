# Problem: Maximum Product of Two Elements in an Array
# Language: python3
# Runtime: 52 ms
# Memory: 14.2 MB

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        return (nums[0] - 1)  * (nums[1] - 1)