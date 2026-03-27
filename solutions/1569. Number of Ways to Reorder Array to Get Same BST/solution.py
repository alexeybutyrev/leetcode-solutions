# Problem: Number of Ways to Reorder Array to Get Same BST
# Language: python3
# Runtime: 178 ms
# Memory: 21.9 MB

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        
        def dfs(nums):
            m = len(nums)
            if m < 3: 
                return 1
            left_nodes = [a for a in nums if a < nums[0]]
            right_nodes = [a for a in nums if a > nums[0]]
            return dfs(left_nodes) * dfs(right_nodes) * comb(m - 1, len(left_nodes)) % mod
        
        return (dfs(nums) - 1) % mod