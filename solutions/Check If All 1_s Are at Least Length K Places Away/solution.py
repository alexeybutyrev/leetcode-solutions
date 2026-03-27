# Problem: Check If All 1's Are at Least Length K Places Away
# Language: python3
# Runtime: 8 ms
# Memory: 20.8 MB

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 0 == k: return True
        while nums and nums[-1] == 0:
            nums.pop()
        while nums and nums[0] == 0:
            nums.pop(0)
        if not nums: return True
        for key,v in groupby(nums):
            if key == 1 and len(list(v)) > 1: return False
            if key == 0 and len(list(v)) < k: return False
        return True