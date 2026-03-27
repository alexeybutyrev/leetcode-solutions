# Problem: Maximum Strong Pair XOR I
# Language: python3
# Runtime: 123 ms
# Memory: 16.2 MB

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(len(nums)):
            x = nums[i]
            for j in range(i+1,len(nums)):
                y = nums[j]
                if abs(x-y) <= min(x,y):
                    ans = max(ans, x^y)
        return ans