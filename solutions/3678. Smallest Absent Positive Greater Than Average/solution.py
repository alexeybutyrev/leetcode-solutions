# Problem: Smallest Absent Positive Greater Than Average
# Language: python3
# Runtime: 41 ms
# Memory: 17.9 MB

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        a = mean(nums)
        s = set(nums)
        for x in range(1,102,1):
            if x > a and x not in s: return x
            
        