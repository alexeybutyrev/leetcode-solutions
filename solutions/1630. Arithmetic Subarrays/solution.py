# Problem: Arithmetic Subarrays
# Language: python3
# Runtime: 476 ms
# Memory: 14.4 MB

from copy import deepcopy
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(nums)        
        
        k = len(l)
        result = [True] * k
        for i in range(k):
            #print(r[i],l[i], nums[l[i]:r[i]+1])
            size = r[i] - l[i] + 1
            if size > 1:
                sa = deepcopy(nums[l[i]:r[i]+1])
                sa.sort()
                delta = sa[1] - sa[0]
                
                for j in range(1,size):
                    if sa[j] - sa[j-1] != delta:
                        #print(delta,"here", sa)
                        result[i] = False
                        break
                #print(delta,"here", sa, result[i], i)
        return result
                