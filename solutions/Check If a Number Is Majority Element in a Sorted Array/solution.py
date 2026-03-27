# Problem: Check If a Number Is Majority Element in a Sorted Array
# Language: python3
# Runtime: 32 ms
# Memory: 14.6 MB

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        c = Counter(nums)
        
        return c[target] > len(nums) // 2