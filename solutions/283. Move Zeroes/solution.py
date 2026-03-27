# Problem: Move Zeroes
# Language: python3
# Runtime: 52 ms
# Memory: 15.3 MB

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[ind] = nums[ind], nums[i]
                ind += 1
        
        