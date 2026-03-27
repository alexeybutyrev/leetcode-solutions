# Problem: Single Number
# Language: python
# Runtime: 72 ms
# Memory: 15 MB

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)