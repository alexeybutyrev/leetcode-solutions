# Problem: Find First and Last Position of Element in Sorted Array
# Language: python3
# Runtime: 72 ms
# Memory: 15.5 MB


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        l = bisect_left(nums, target)
        r = bisect_right(nums, target)
        if l > len(nums) - 1:
            return [-1,-1]
        if r == 0 and nums[r] != target:
            return [-1,-1]

        if nums[l] == target and (r > len(nums) - 1 or nums[r] != target):
            r -= 1
        
        if nums[r] == target and nums[l] != target:
            l = r
        
        return [l if nums[l] == target else -1, r if nums[r] == target else -1]