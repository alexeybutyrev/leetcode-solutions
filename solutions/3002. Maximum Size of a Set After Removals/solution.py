# Problem: Maximum Size of a Set After Removals
# Language: python3
# Runtime: 531 ms
# Memory: 27.7 MB

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1) // 2
        
        s1 = set(nums1)
        s2 = set(nums2)
        
        if len(s1) <= n and len(s2) <= n:
            return len(s1 | s2)
        
        o = s1 & s2
        leno = len(o)
        
        
        l1 = len(s1-o)
        if l1 > n:
            l1 = n
        x = n - l1
        
        l2 = len(s2-o)
        if l2 > n:
            l2 = n
        
        y = n - l2
        

        
        return min(leno,x + y) + l1 + l2
        