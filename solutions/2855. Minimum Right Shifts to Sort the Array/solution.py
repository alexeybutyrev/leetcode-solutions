# Problem: Minimum Right Shifts to Sort the Array
# Language: python3
# Runtime: 48 ms
# Memory: 16.2 MB

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        A = nums[:]
        A.sort()
        if A == nums:
            return 0
        for _ in range(len(A)):
            nums = [nums.pop()] + nums
            if nums == A:
                return _ + 1
        return -1