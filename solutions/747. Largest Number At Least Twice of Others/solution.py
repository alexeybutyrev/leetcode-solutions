# Problem: Largest Number At Least Twice of Others
# Language: python
# Runtime: 28 ms
# Memory: 11.9 MB

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = max(nums)
        mx_ind = nums.index(mx)
        
        for v in nums:
            if v != mx:
                if v > mx / 2:
                    return -1
        
        return mx_ind