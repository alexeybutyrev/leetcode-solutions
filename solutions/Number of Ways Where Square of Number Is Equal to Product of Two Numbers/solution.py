# Problem: Number of Ways Where Square of Number Is Equal to Product of Two Numbers
# Language: python3
# Runtime: 480 ms
# Memory: 24.2 MB

from collections import defaultdict
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1,n2 = len(nums1), len(nums2)
        hm1 = defaultdict(lambda :0)
        d1  = defaultdict(lambda :0)
        for i in range(n1):
            for j in range(i, n1):
                v = nums1[i] * nums1[j] 
                if i == j:
                    d1[v] += 1
                else:
                    hm1[v] += 1
        
        #print(hm1)
        #print(d1)
        count = 0
        for i in range(n2):
            for j in range(i, n2):
                v = nums2[i] * nums2[j] 
                if i == j:
                    if v in hm1:
                        count += hm1[v]
                    
                else:
                    if v in d1:
                        count += d1[v]
        
                
        return count