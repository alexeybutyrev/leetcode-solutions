# Problem: Jump Game
# Language: python3
# Runtime: 76 ms
# Memory: 16.1 MB

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if not nums:
            return False
        n = len(nums)
        
        i = 0
        last_pos = n - 1
        for i in range(n-1,-1,-1):
            if i + nums[i] >= last_pos:
                last_pos = i
        
        return last_pos == 0
        
        