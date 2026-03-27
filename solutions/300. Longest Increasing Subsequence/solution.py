# Problem: Longest Increasing Subsequence
# Language: python3
# Runtime: 52 ms
# Memory: 14.7 MB

from collections import deque
from bisect import bisect 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [-10**5]
        l = 0
        for n in nums:
            ind = bisect_left(dp, n)
            
            if ind >= len(dp):
                dp.append(-1)
                
            dp[ind] = n
        return len(dp) - 1