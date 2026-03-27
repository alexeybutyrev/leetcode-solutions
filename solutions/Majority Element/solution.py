# Problem: Majority Element
# Language: python3
# Runtime: 131 ms
# Memory: 17.9 MB

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ans = nums[0]
        count = 0
        for x in nums:
            if count == 0:
                ans = x
                
            if ans == x:
                count += 1
            else:
                count -= 1
        
        return ans