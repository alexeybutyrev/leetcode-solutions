# Problem: Smallest Index With Equal Value
# Language: python3
# Runtime: 76 ms
# Memory: 14.4 MB

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i,x in enumerate(nums):
            if i % 10 == x:
                return i
        return -1