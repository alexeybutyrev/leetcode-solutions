# Problem: Final Element After Subarray Deletions
# Language: python3
# Runtime: 0 ms
# Memory: 34.3 MB

class Solution:
    def finalElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(nums[0], nums[-1])