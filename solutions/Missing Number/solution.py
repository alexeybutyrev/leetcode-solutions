# Problem: Missing Number
# Language: python3
# Runtime: 109 ms
# Memory: 17.8 MB

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums)*(len(nums)+1)//2 -sum(nums)