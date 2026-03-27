# Problem: Minimum Difference Between Highest and Lowest of K Scores
# Language: python3
# Runtime: 3 ms
# Memory: 19.5 MB

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        ans = inf
        k-=1
        for i in range(len(nums) - k):
            ans = min(ans, nums[i + k] - nums[i])
            
        return ans