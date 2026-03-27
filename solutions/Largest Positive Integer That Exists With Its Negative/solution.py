# Problem: Largest Positive Integer That Exists With Its Negative
# Language: python3
# Runtime: 311 ms
# Memory: 14.2 MB

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        ans = -1
        for a in s:
            if a in s and -a in s:
                ans = max(ans, abs(a))
        return ans