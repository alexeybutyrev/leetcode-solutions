# Problem: Permutations II
# Language: python3
# Runtime: 163 ms
# Memory: 14.2 MB

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        s = set()
        for p in permutations(nums):
            s.add(tuple(p))
        return s