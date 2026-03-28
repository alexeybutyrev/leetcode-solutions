# Problem: Contains Duplicate
# Language: python
# Runtime: 108 ms
# Memory: 17.1 MB

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))