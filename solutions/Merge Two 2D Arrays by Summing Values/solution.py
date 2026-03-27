# Problem: Merge Two 2D Arrays by Summing Values
# Language: python3
# Runtime: 0 ms
# Memory: 17.9 MB

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        c = Counter()
        for a,b in nums1 + nums2: c[a] += b
        return sorted([x,y] for x,y in c.items())
        