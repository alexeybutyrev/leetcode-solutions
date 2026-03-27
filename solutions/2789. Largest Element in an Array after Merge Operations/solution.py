# Problem: Largest Element in an Array after Merge Operations
# Language: python3
# Runtime: 1013 ms
# Memory: 27.3 MB

class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        ans = 0
        
        while nums:
            x = nums.pop()
            ans = max(ans, x)
            if nums and nums[-1] <= x:
                nums[-1] += x
        
        return ans
                