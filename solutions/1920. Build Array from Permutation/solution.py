# Problem: Build Array from Permutation
# Language: python3
# Runtime: 164 ms
# Memory: 14.4 MB

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        A = []
        for n in nums:
            A.append(nums[n])
        return A