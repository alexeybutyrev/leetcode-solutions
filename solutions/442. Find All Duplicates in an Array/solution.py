# Problem: Find All Duplicates in an Array
# Language: python3
# Runtime: 332 ms
# Memory: 23.2 MB

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [k for k,v in Counter(nums).items() if v == 2]