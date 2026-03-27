# Problem: Split the Array
# Language: python3
# Runtime: 54 ms
# Memory: 16.5 MB

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        c = Counter(nums)
        return all(x <= 2 for x in c.values())