# Problem: Sum of Unique Elements
# Language: python3
# Runtime: 36 ms
# Memory: 14.2 MB

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        return sum([k for k, v in c.items() if v == 1])
            
        