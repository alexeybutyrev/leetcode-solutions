# Problem: Minimum Impossible OR
# Language: python3
# Runtime: 455 ms
# Memory: 29.1 MB

class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(100):
            if 2 ** i not in s:
                return 2**i
        return 1
        
        