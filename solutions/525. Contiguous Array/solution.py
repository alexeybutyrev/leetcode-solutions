# Problem: Contiguous Array
# Language: python3
# Runtime: 888 ms
# Memory: 18.5 MB

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums) 
        if  n == 0 : return 0
        if  n == 1 : return 0
        
        hm = {0:-1}
        
        mx_ = 0
        v = 0
        
        for i in range(n):
            if nums[i] == 0:
                v -= 1 
            else: 
                v += 1
            if v in hm:
                mx_ = max(mx_, i - hm[v])
            else:
                hm[v]=i
                    
        return mx_