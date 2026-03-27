# Problem: Single Number III
# Language: python3
# Runtime: 56 ms
# Memory: 15.7 MB

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0
        
        for n in nums:
            mask^=n
        

        m = mask & (-mask)
        x = 0
        for n in nums:
            if n & m:
                x ^= n
        
        return [x,x^mask]

        