# Problem: Transformed Array
# Language: python3
# Runtime: 63 ms
# Memory: 19.5 MB

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        A = []
        N = len(nums)
        for i,x in enumerate(nums):
            if x > 0:
                 i += x 
                 i %= N
                
            elif x < 0:
                i += N
                i += x
                i %= N
            A.append(nums[i])
        return A