# Problem: First Missing Positive
# Language: python3
# Runtime: 32 ms
# Memory: 14.2 MB

from math import inf
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if not nums:
            return 1
        nums = list(set(nums))        
        n = len(nums)
        count = 0
        left,right = 0,n-1
        while left <= right:
            if nums[left] <= 0:
                nums[left],nums[right] = nums[right],nums[left]
                count +=1
                right -= 1
            else:
                left += 1


        left, right = 0, n - count - 1
        number = 1
        while left < right:
            if nums[right] == number:
                nums[left],nums[right] = nums[right],nums[left]
                right = n - count - 1
            
            if nums[left] > nums[right]:
                nums[left],nums[right] = nums[right],nums[left]
                
                    
            if nums[left] == number:
                left += 1
                number += 1
                continue
            right -= 1
        
        #print(nums)
        for i in range(n - count):
            if nums[i] != i + 1:
                return i + 1
        
        return n - count + 1
        