# Problem: Intersection of Two Arrays II
# Language: python3
# Runtime: 46 ms
# Memory: 16.4 MB

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        ans = []
        for k in c1:
            ans += ([k] * min(c1[k], c2[k]))
        
        return ans