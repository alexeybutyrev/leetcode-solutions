# Problem: Minimum Distance to the Target Element
# Language: python3
# Runtime: 84 ms
# Memory: 14.5 MB

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        ans = inf
        for i in range(len(nums)):
            if nums[i] == target:
                ans = min(ans, abs(i - start))
                
        return ans