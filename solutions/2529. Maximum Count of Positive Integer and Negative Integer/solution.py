# Problem: Maximum Count of Positive Integer and Negative Integer
# Language: python3
# Runtime: 8 ms
# Memory: 18 MB

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p,n = 0,0
        for x in nums:
            p += (x > 0)
            n += (x < 0)
        return max(p,n)
            