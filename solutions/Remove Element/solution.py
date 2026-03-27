# Problem: Remove Element
# Language: python3
# Runtime: 32 ms
# Memory: 14 MB

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        
                