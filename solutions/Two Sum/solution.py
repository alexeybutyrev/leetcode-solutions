# Problem: Two Sum
# Language: python3
# Runtime: 1 ms
# Memory: 19.1 MB

class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        c = {}
        for i,x in enumerate(nums):
            if t - x in c:
                return [c[t-x],i]
            c[x] =i
        return []
