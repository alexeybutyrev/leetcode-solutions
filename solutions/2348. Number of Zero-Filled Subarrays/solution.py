# Problem: Number of Zero-Filled Subarrays
# Language: python3
# Runtime: 1102 ms
# Memory: 24.7 MB

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        for x,l in groupby(nums):
            if x == 0:
                c = len(list(l))
                ans += c * (c + 1) // 2
        return ans