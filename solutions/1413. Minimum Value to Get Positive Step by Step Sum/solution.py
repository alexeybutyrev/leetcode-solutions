# Problem: Minimum Value to Get Positive Step by Step Sum
# Language: python3
# Runtime: 24 ms
# Memory: 13.7 MB

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # calculate running sum
        n = len(nums)
        for i in range(1,n):
            nums[i] = nums[i] + nums[i-1]
        
        #print(nums)
        m = min(nums)
        
        return max(1,1 - m)