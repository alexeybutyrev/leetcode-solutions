# Problem: Non-decreasing Array
# Language: python3
# Runtime: 184 ms
# Memory: 15.3 MB

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        N = len(nums)
        pr = False
        for i in range(1, N):
            if nums[i] < nums[i-1]:
                if pr: return False
                
                if i < 2 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                pr = True
        return True