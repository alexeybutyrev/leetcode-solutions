# Problem: Find the Difference of Two Arrays
# Language: python3
# Runtime: 189 ms
# Memory: 16.8 MB

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        return [set(nums1)-set(nums2),set(nums2)-set(nums1)]