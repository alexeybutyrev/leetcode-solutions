# Problem: Make Array Zero by Subtracting Equal Amounts
# Language: python3
# Runtime: 62 ms
# Memory: 13.8 MB

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        while sum(nums) > 0:
            #print(nums)
            s = min(x for x in nums if x > 0)
            nums = [x - s for x in nums if x]
            ans += 1
        return ans