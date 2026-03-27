# Problem: Semi-Ordered Permutation
# Language: python3
# Runtime: 85 ms
# Memory: 16.3 MB

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        i1 = nums.index(1)
        iN = nums.index(len(nums))
        N = len(nums)
        if i1 == 0 and iN == N - 1:
            return 0
        
        if i1 > iN:
            return i1 + N - iN - 2
        return i1 + N - iN - 1