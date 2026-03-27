# Problem: Merge Two 2D Arrays by Summing Values
# Language: python3
# Runtime: 59 ms
# Memory: 14.2 MB

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        c1 = Counter()
        c2 = Counter()
        s = set()
        for i,x in nums1:
            c1[i] = x
            s.add(i)
        
        for i,x in nums2:
            c2[i] = x
            s.add(i)
        
        ans = []
        for i in sorted(s):
            ans.append([i,c1[i] + c2[i]])
        return ans
        
        