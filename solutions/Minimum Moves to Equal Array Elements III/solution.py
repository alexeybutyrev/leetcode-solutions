# Problem: Minimum Moves to Equal Array Elements III
# Language: python3
# Runtime: 0 ms
# Memory: 17.7 MB

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)

        return sum(mx - x for x in nums)