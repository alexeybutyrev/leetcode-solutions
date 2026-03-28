# Problem: Single Number III
# Language: python3
# Runtime: 1868 ms
# Memory: 15.6 MB

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = 0
        for e in nums:
            s ^= e
        
        for e in nums:
            if s^e in nums:
                break
        
        return [e,s^e]
        
        