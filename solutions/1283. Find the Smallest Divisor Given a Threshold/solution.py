# Problem: Find the Smallest Divisor Given a Threshold
# Language: python3
# Runtime: 556 ms
# Memory: 19.9 MB

from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def devide(d):
            s = 0
            for n in nums:
                s+= ceil(n/d)
            return s
        
        nums.sort()
        
        left, right = 1, 2
        while devide(right) > threshold:
            left = right
            right <<= 1
        
        while left <= right:

            mid = (right + left) // 2
            
            d = devide(mid)
            
            if d > threshold:
                left = mid+1
            else:
                right = mid-1
        
        
        #print(left, right, threshold)
        
        return left