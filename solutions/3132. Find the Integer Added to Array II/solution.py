# Problem: Find the Integer Added to Array II
# Language: python3
# Runtime: 137 ms
# Memory: 16.6 MB

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        for x in range(-1005,1005):
            valid = True
            for a in c2:
                if c1[a-x] < c2[a]:
                    valid = False
                    break
            if valid:
                return x
                