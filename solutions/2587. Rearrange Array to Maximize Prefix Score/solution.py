# Problem: Rearrange Array to Maximize Prefix Score
# Language: python3
# Runtime: 725 ms
# Memory: 29.5 MB

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        s = 0
        a = 0
        for x in nums:
            s += x
            if s <= 0:
                return a
            a += 1
        return a