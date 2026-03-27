# Problem: Maximum Subarray Sum After One Operation
# Language: python3
# Runtime: 1136 ms
# Memory: 45.7 MB

from itertools import accumulate
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        N = len(nums)
        # find running sum
        s = list(accumulate([0] + nums))
        
        # for each element in the array find Smax to the right of it
        mx = s[-1]
        Smax = {}
        for i in range(len(s) -1,0,-1):
            mx = max(mx,s[i])
            Smax[i-1] = mx
        
        # for each element in the array find Smin to the left of it
        Smin = {}
        mn = s[0]
        for i in range(1,len(s)):
            Smin[i-1] = mn
            mn = min(mn,s[i])
        
        # loop by each element maximum sub array of each element 
        # S(left,right) = Smax[i] - Smin[i]
        # repace there nums[i] to nums[i] * nums[i]. S*(left,right) = Smax[i] - Smin[i] - nums[i] + nums[i]* nums[i]
        # find max
        ans = 0 
        for i in range(N):
            ans = max(ans, Smax[i] - Smin[i] - nums[i] + nums[i] * nums[i])
        
        return ans