# Problem: Increasing Triplet Subsequence
# Language: python3
# Runtime: 56 ms
# Memory: 14.7 MB

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 3:
            return False
        
        mid  = inf
        left = inf
        
        for n in nums:
            if n > mid:
                return True
            
            if n < left:
                left = n
            
            if n > left and n < mid:
                mid = n
        
        return False
    