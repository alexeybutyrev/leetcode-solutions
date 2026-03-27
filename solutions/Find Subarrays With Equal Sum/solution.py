# Problem: Find Subarrays With Equal Sum
# Language: python3
# Runtime: 47 ms
# Memory: 13.9 MB

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s = set()
        for i in range(1,len(nums)):
            if nums[i] + nums[i-1] in s:
                return True
            s.add(nums[i] + nums[i-1])
        return False