# Problem: Rotate Array
# Language: python3
# Runtime: 56 ms
# Memory: 15.6 MB

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        nums[0:k] = reversed(nums[0:k])
        nums[k:] = reversed(nums[k:])
        
        return nums