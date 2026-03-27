# Problem: Ant on the Boundary
# Language: python3
# Runtime: 35 ms
# Memory: 16.7 MB

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = s = 0
        for x in nums:
            s += x
            if s == 0:
                ans += 1
        return ans