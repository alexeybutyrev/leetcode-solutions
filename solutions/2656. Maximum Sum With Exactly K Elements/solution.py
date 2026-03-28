# Problem: Maximum Sum With Exactly K Elements 
# Language: python3
# Runtime: 185 ms
# Memory: 16.3 MB

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        s = m
        x = m
        for i in range(k-1):
            x += 1
            s += x
        return s