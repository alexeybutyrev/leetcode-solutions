# Problem: House Robber
# Language: python3
# Runtime: 24 ms
# Memory: 14.2 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a,b = nums[0], max(nums[1], nums[0])
        
        for i in range(2,len(nums)):
            a,b = b, max(a+nums[i],b)
        
        return max(a,b)