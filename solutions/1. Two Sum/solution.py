# Problem: Two Sum
# Language: python3
# Runtime: 60 ms
# Memory: 15.3 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i,x in enumerate(nums):
            if target - x in hm:
                return [i,hm[target-x]]
            hm[x] = i
            
        return []