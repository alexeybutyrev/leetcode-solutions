# Problem: Two Sum II - Input Array Is Sorted
# Language: python
# Runtime: 48 ms
# Memory: 11.9 MB

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            
            s = numbers[left] + numbers[right] 
            
            if s == target:
                return [left+1, right+1]
            
            if s < target:
                left +=1
            else:
                right -=1
                
        
        return []
        