# Problem: Two Out of Three
# Language: python3
# Runtime: 75 ms
# Memory: 14.2 MB

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return set(nums1) & set(nums2) | set(nums1) & set(nums3) | set(nums2) & set(nums3)