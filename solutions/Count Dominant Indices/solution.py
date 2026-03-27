# Problem: Count Dominant Indices
# Language: python3
# Runtime: 7 ms
# Memory: 19.4 MB

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-1):
            if nums[i] > sum(nums[i+1:]) / len(nums[i+1:]):
                ans += 1
        return ans