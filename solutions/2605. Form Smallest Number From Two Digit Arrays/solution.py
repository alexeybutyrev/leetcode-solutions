# Problem: Form Smallest Number From Two Digit Arrays
# Language: python3
# Runtime: 37 ms
# Memory: 13.9 MB

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        s = set(nums1) & set(nums2)
        if s:
            return min(s)
        

        return min(nums1[0] * 10 + nums2[0],nums2[0] * 10 + nums1[0])