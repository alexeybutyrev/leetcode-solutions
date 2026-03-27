# Problem: Bitwise XOR of All Pairings
# Language: python3
# Runtime: 118 ms
# Memory: 44.1 MB

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        #nums1 = set(nums1)
        #nums2 = set(nums2)
        N1 = len(nums1)
        N2 = len(nums2)
        
        c1 = Counter(nums1) 
        c2 = Counter(nums2)
        c = Counter()
        for k,v in c1.items():
            c1[k] = v * N2
        
        for k,v in c2.items():
            c2[k] = v * N1
        
        c = c1 + c2
        a = 0
        for k,v in c.items():
            if v % 2 != 0:
                a ^= k
        return a
        
       