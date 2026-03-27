# Problem: Minimum Common Value
# Language: python3
# Runtime: 340 ms
# Memory: 42.8 MB

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1)& set(nums2)) if set(nums1)& set(nums2) else -1