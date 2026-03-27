# Problem: Count Equal and Divisible Pairs in an Array
# Language: python
# Runtime: 123 ms
# Memory: 13.4 MB

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c = Counter(nums)
        ans = 0
        for i, a in enumerate(nums):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j] and (i * j)% k == 0:
                    ans +=1
        return ans
                