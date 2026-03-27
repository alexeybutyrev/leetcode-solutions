# Problem: Running Sum of 1d Array
# Language: python3
# Runtime: 51 ms
# Memory: 14.2 MB

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))